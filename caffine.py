import pyautogui,keyboard
pyautogui.FAILSAFE = False
intensity = input("Enter the intensity of caffine (reccomended 2) :")

while True:
    try:
        intensity = float(intensity)
        break
    except:
        intensity = input("Invalid amount of caffine...give some float value : ")
print("Dont sleep, have some caffine...\n press Space Bar to get de-caffinated")
i = 1 
while i>0:
        X,Y = pyautogui.position()
        if i%2==0:
            pyautogui.moveTo(X+intensity ,Y)
        else:
            pyautogui.moveTo(X-intensity ,Y)

        if keyboard.is_pressed("space"):
            print("Space pressed, ending caffinated mode.")
            i=-2
        i+=1


#s   