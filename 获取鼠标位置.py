import pyautogui
print('按CTRL+c退出')
while True:
    x,y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
    print(positionStr,end='')
    print('\b' * len(positionStr),end='',flush=True)