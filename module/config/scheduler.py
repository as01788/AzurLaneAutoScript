import time

from cached_property import cached_property

from module.config.config import AzurLaneConfig, TaskEnd
from module.device.device import Device
from module.exception import *
from module.handler.login import LoginHandler
from module.logger import logger
from module.research.research import RewardResearch


class AzurLaneAutoScript:
    def __init__(self, config_name='alas'):
        self.config_name = config_name

    @cached_property
    def config(self):
        config = AzurLaneConfig(config_name=self.config_name)
        config.bind(config.get_next())
        return config

    @cached_property
    def device(self):
        device = Device(config=self.config)
        return device

    def run(self, command):
        logger.attr('Command', command)
        while 1:
            try:
                self.__getattribute__(command)()
                return True
            except TaskEnd as e:
                return True
            except GameNotRunningError as e:
                logger.warning(e)
                az = LoginHandler(self.config, device=self.device)
                az.app_restart()
                az.ensure_no_unfinished_campaign()
                continue
            except GameTooManyClickError as e:
                logger.warning(e)
                self.save_error_log()
                az = LoginHandler(self.config, device=self.device)
                az.handle_game_stuck()
                continue
            except GameStuckError as e:
                logger.warning(e)
                self.save_error_log()
                az = LoginHandler(self.config, device=self.device)
                az.handle_game_stuck()
                continue
            except LogisticsRefreshBugHandler as e:
                logger.warning(e)
                self.save_error_log()
                az = LoginHandler(self.config, device=self.device)
                az.device.app_stop()
                time.sleep(600)
                az.app_ensure_start()
                continue
            except Exception as e:
                logger.exception(e)
                self.save_error_log()
                return False

    def save_error_log(self):
        """
        Save last 60 screenshots in ./log/error/<timestamp>
        Save logs to ./log/error/<timestamp>/log.txt
        """
        pass

    def research(self):
        RewardResearch(config=self.config, device=self.device).run()

    def loop(self):
        while 1:
            success = self.run(self.config.task)
            del self.__dict__['config']

            if not success:
                break


scheduler = AzurLaneAutoScript()
scheduler.loop()