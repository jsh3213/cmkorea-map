import pyautogui as pag
import time

# print(pag.position())
#
#  pag.screenshot('1.png', region=(1517, 503, 30, 30))
#
#  pag.moveTo(1517, 503)
#
# num1 = pag.locateCenterOnScreen('1.png')
# print(num1)
# pag.moveTo(num1)
# pag.moveRel(100, 100, 2)
#  pag.click(num1)
pag.click(clicks=2, interval=2)
pag.doubleClick()
pag.rightClick()  # 우클릭
pag.doubleClick() # 더블 클릭
pag.dragTo(x=100, y=100, duration=2)
time.sleep(1)
pag.typewrite('Hello', interval=1)
pag.typewrite(['enter'])
pag.press('enter')
pag.keyDown('shift')  # shift 누르고 누른 상태 유지
pag.keyUp('shift')    # shift 떼기
pag.hotkey('ctrl', 'c')  # ctrl+c
pag.hotkey('alt', 'f4')  # alt+F4


btn_1 = pag.alert(text='경고', title='title', button='okay')

print(btn_1)
print(type(btn_1))

btn_2 = pag.confirm(text='테스트', title='TITLE', buttons=['1', '2', '3', '4'])
if btn_2 == '1':
    print("1 입니다.")

btn_3 = pag.prompt(text='TEXT', title="TITLE", default='여기에 쓰세요.')
print(btn_3)

btn_4 = pag.password('password', '비밀번호를 입력하세요.', mask='$')
print(btn_4)