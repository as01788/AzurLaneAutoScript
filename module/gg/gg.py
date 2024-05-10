from module.base.base import ModuleBase
from module.gg.assets import *
from module.logger import logger

class GGHandler(ModuleBase):
    def run(self):
        logger.info("Open GG!")
        # self.image_file = GG_MENU_STEP_1.file
        # print(self.appear(GG_MENU_STEP_1))
        screenShot = False
        buttons = [GG_ICON, GG_STEP_1, GG_STEP_2, GG_STEP_3, GG_STEP_4, GG_STEP_5, GG_STEP_6]
        for button in buttons:
            # print("开始点击按钮 > " + button.file)
            if not self.click_button(button, screenShot):
                # print("点击按钮Error > " + button.file)
                break

        # self.device.screenshot()
        # 如果有end，点击end，否则点击step7-8
        while 1:
            self.device.screenshot()
            if self.appear(GG_STEP_END):
                if self.click_button(GG_STEP_END, False):
                    return
            elif self.appear(GG_STEP_7):
                self.click_button(GG_STEP_7, False)
                self.device.sleep(1)
                self.click_button(GG_STEP_8, False)
                return

    def restart(self):
        self.device.sleep(1)
        # self.image_file = GG_MENU2.file
        count = 0
        while 1:
            self.device.screenshot()
            count = count+1
            if count > 30:
                return
            if self.appear(GG_MENU):
                if self.click_button(GG_MENU, False):
                    return

        # if self.appear(GG_MENU):
        #     self.click_button(GG_MENU, False)

    def click_button(self, button, screenshot):
        if not screenshot:
            self.image_file = button.file
        else:
            self.device.screenshot()
        if button.name == "GG_STEP_1" or button.name == "GG_STEP_END":
            self.device.sleep(1)
        while 1:
            if self.appear_then_click(button, screenshot):
                # print("点击按钮完成 > " + button.file)
                self.device.sleep((0.25, 0.5))
                return True
