import cv2
import numpy as np
import os
import time
import pyautogui
from pynput.mouse import Button, Controller
from Naked.toolshed.shell import execute_js, muterun_js
import easygui
from selenium import webdriver

time.sleep(2)
screenSize = pyautogui.size()

def findSmallImage(small_image, large_image):
    method = cv2.TM_SQDIFF_NORMED

    result = cv2.matchTemplate(small_image, large_image, method)

    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    MPx,MPy = mnLoc

    trows,tcols = small_image.shape[:2]

    boundingRect = cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    #cv2.imshow("largeim", large_image)
    #cv2.waitKey(0)
    return (MPx, MPy)

def checkIfImageExists(small_image, large_image):
    res = cv2.matchTemplate(small_image, large_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    threshold = 0.8
    flag = False
    if np.amax(res) > threshold:
        flag = True
        return True
    else:
        return False

def getPixelsFromPercent(percentX, percentY):
    return (screenSize[0] * percentX, screenSize[1] * percentY)

def getPixelsXPercent(percentX):
    return screenSize[0] * percentX
def getPixelsYPercent(percentY):
    return screenSize[1] * percentY

def main():
    os.popen("open -a Roblox")
    time.sleep(1)
    pyautogui.press('e')
    time.sleep(1)
    pyautogui.press('e')
    time.sleep(1)

    firstScreenPy = pyautogui.screenshot()
    firstScreen = cv2.cvtColor(np.array(firstScreenPy), cv2.COLOR_RGB2BGR)
    addSauceButtonPosition = findSmallImage(cv2.imread("./Buttons/TomatoSauceButton.png"), firstScreen)
    pyautogui.click(addSauceButtonPosition[0] + cv2.imread("./Buttons/TomatoSauceButton.png").shape[1]/2, addSauceButtonPosition[1])
    time.sleep(1)
    os.popen("open -a Terminal")

    secondScreenPy = pyautogui.screenshot()
    secondScreen = cv2.cvtColor(np.array(secondScreenPy), cv2.COLOR_RGB2BGR)
    addCheeseButtonPosition = findSmallImage(cv2.imread("./Buttons/CheeseButton.png"), secondScreen)
    pyautogui.click(addCheeseButtonPosition[0] + cv2.imread("./Buttons/CheeseButton.png").shape[1]/2, addCheeseButtonPosition[1])
    time.sleep(1)
    os.popen("open -a Terminal")

    thirdScreenPy = pyautogui.screenshot()
    thirdScreen = cv2.cvtColor(np.array(thirdScreenPy), cv2.COLOR_RGB2BGR)

    def addPepperoni():
        addPepperoniButtonPosition = findSmallImage(cv2.imread("./Buttons/PepperoniButton.png"), thirdScreen)
        pyautogui.click(addPepperoniButtonPosition[0] + cv2.imread("./Buttons/PepperoniButton.png").shape[1]/2, addPepperoniButtonPosition[1])
    def addHam():
        addHamButtonPosition = findSmallImage(cv2.imread("./Buttons/HamButton.png"), thirdScreen)
        pyautogui.click(addHamButtonPosition[0] + cv2.imread("./Buttons/HamButton.png").shape[1]/2, addHamButtonPosition[1])
    def addVeggies():
        addVeggiesButtonPosition = findSmallImage(cv2.imread("./Buttons/VegetablesButton.png"), thirdScreen)
        pyautogui.click(addVeggiesButtonPosition[0] + cv2.imread("./Buttons/VegetablesButton.png").shape[1]/2, addVeggiesButtonPosition[1])

    def submitPizza():
        doneButtonPosition = findSmallImage(cv2.imread("./Buttons/DoneButton.png"), thirdScreen)
        pyautogui.click(doneButtonPosition[0] + cv2.imread("./Buttons/DoneButton.png").shape[1]/2, doneButtonPosition[1])
        time.sleep(0.25)
        pyautogui.click(doneButtonPosition[0] + cv2.imread("./Buttons/DoneButton.png").shape[1]/2, doneButtonPosition[1] + cv2.imread("./Buttons/DoneButton.png").shape[0]/2)
        time.sleep(0.25)
        pyautogui.click(doneButtonPosition[0] + cv2.imread("./Buttons/DoneButton.png").shape[1]/2, doneButtonPosition[1] + cv2.imread("./Buttons/DoneButton.png").shape[0]/2)
        time.sleep(0.25)
        pyautogui.click(doneButtonPosition[0] + cv2.imread("./Buttons/DoneButton.png").shape[1]/2, doneButtonPosition[1] + cv2.imread("./Buttons/DoneButton.png").shape[0]/2)
        time.sleep(0.25)
        pyautogui.click(doneButtonPosition[0] + cv2.imread("./Buttons/DoneButton.png").shape[1]/2, doneButtonPosition[1] + cv2.imread("./Buttons/DoneButton.png").shape[0]/2)
        time.sleep(0.25)
        pyautogui.click(doneButtonPosition[0] + cv2.imread("./Buttons/DoneButton.png").shape[1]/2, doneButtonPosition[1] + cv2.imread("./Buttons/DoneButton.png").shape[0]/2)

    def getPizzaType():
        if checkIfImageExists(cv2.imread("./PizzaImages/Cheese.png"), thirdScreen):
            return "Cheese"
        elif checkIfImageExists(cv2.imread("./PizzaImages/Ham.png"), thirdScreen):
            return "Ham"
        elif checkIfImageExists(cv2.imread("./PizzaImages/Pepperoni.png"), thirdScreen):
            return "Pepperoni"
        elif checkIfImageExists(cv2.imread("./PizzaImages/Veggie.png"), thirdScreen):
            return "Veggie"

    def getNewPizzaType():
        greenLower = (0, 68, 0)
        greenUpper = (13, 219, 255)
        mask = cv2.inRange(thirdScreen, greenLower, greenUpper)
        cv2.imshow("mask", mask)
        cv2.imwrite("./mask.png", mask)

    print(getPizzaType())
    getPizzaType()
    pyautogui.moveTo(10, 10)
    time.sleep(1)

    if getPizzaType() == "Ham":
        addHam()
    elif getPizzaType() == "Pepperoni":
        addPepperoni()
    elif getPizzaType() == "Veggie":
        addVeggies()
    else:
        print("Cheese or None")

    time.sleep(1)
    os.popen("open -a Terminal")
    time.sleep(1)
    submitPizza()
    time.sleep(3)
    main()
main()