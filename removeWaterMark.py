#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui
import time

info ="""
    #用于删除部分水印，操作之前需完成外部软件的操作，主要有，
    #1.设置删除的按键
    #2.设置翻页的滚笼测试
    #3.填写页码
"""

def removeWaterMark():
    print('Press Ctrl-C to quit.')
    print(info)
    #用于删除部分水印，操作之前需完成外部软件的操作，主要有，
    #1.设置删除的按键
    #2.设置翻页的滚笼测试
    #3.填写页码
    page = eval(input("请输入去水印文档的页数，并配置好相关的操作\n"))
    # page = 58
    time.sleep(5)
    while(page >0):
        # cancl = input()
        # if(cancl == "q"):
        #     break
        page = page -1
        pyautogui.click(1800, 400) #点击位置
        time.sleep(0.2)
        pyautogui.hotkey('del')  # 删除按键
        time.sleep(0.2)
        pyautogui.scroll(-300)
        time.sleep(0.2)    # pyautogui.tyerie('delete')   # time.sleep(1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    removeWaterMark()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
