import pyautogui
import mouse
import keyboard
import time
def CS():
    Image = "Data/csgodata/Nuke.png"
    Image2 = "Data/csgodata/Shortdust.png"
    Image3 = "Data/csgodata/Lake.png"
    Image4 = "Data/csgodata/CobbleStone.png"
    Image5 = "Data/csgodata/Train.png"
    Image6 = "Data/csgodata/Overpass.png"
    Image7 = "Data/csgodata/Vertigo.png"
    Image8 = "Data/csgodata/Inferno.png"
    Image9 = "Data/csgodata/HumanMap1.png"
    Image10 = "Data/csgodata/HumanMap2.png"
    start = True
    while start:
        Start = pyautogui.locateCenterOnScreen(Image, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
        Start1 = pyautogui.locateCenterOnScreen(Image2, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
        Start2 = pyautogui.locateCenterOnScreen(Image3, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
        Start3 = pyautogui.locateCenterOnScreen(Image4, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
        Start4 = pyautogui.locateCenterOnScreen(Image5, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
        Start5 = pyautogui.locateCenterOnScreen(Image6, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
        Start6 = pyautogui.locateCenterOnScreen(Image7, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
        Start7 = pyautogui.locateCenterOnScreen(Image8, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
        Start8 = pyautogui.locateCenterOnScreen(Image9, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
        Start9 = pyautogui.locateCenterOnScreen(Image10, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
        print("None")
        if keyboard.is_pressed("f10"):
            Infer()
        if Start != None:
            pyautogui.moveTo(Start)
            mouse.click("left")
            start = False
            Infer()
        if Start1 != None:
            pyautogui.moveTo(Start1)
            mouse.click("left")
            start = False
            Infer()
        if Start2 != None:
            pyautogui.moveTo(Start2)
            mouse.click("left")
            start = False
            Infer()
        if Start3 != None:
            pyautogui.moveTo(Start3)
            mouse.click("left")
            start = False
            Infer()
        if Start4 != None:
            pyautogui.moveTo(Start4)
            mouse.click("left")
            start = False
            Infer()
        if Start5 != None:
            pyautogui.moveTo(Start5)
            mouse.click("left")
            start = False
            Infer()
        if Start6 != None:
            pyautogui.moveTo(Start6)
            mouse.click("left")
            start = False
            Infer()
        if Start7 != None:
            pyautogui.moveTo(Start7)
            mouse.click("left")
            start = False
            Infer()
        if Start8 != None:
            pyautogui.moveTo(Start8)
            mouse.click("left")
            start = False
            Infer()
        if Start9 != None:
            pyautogui.moveTo(Start9)
            mouse.click("left")
            start = False
            Infer()
def MyPack():
    print("Your, Pack name.")
    PackName = input("Data/")
    pnm = ["Data/", PackName, "/Images"]
    pns = ["Data/", PackName, "/Settings"]
    imgpnm = "".join(pnm)
    imgpns = "".join(pns)
    print("Working not alivebel")
    time.sleep(10)
    exit()
def myimage():
    imagename = input("Data/FOR YOU IMAGE!!!/")
    s = ["Data/FOR YOU IMAGE!!!/", imagename]
    imgn = "".join(s)
    print("")
    print("1) left click")
    print("2) right click")
    print("3) double left click")
    print("4) double right click")
    whyclick = int(input("why click?:"))
    print("")
    start = True
    while start:
        myimage = pyautogui.locateOnScreen(imgn)
        print(myimage)
        if myimage != None:
            pyautogui.moveTo(myimage)
            if whyclick == 1:
                mouse.click("left")
            if whyclick == 2:
                mouse.right_click()
            if whyclick == 3:
                mouse.double_click("left")
            if whyclick == 4:
                mouse.double_click("right")
            start = False
            Infer()
def Infer():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("         ___           _ _              __ _             _ _             ")
    print("        / __\_ _ _ __ (_) | __ ___  __ / _\ |_ _   _  __| (_) ___        ")
    print(" _____ / _\/ _` | '_ \| | |/ _` \ \/ / \ \| __| | | |/ _` | |/ _ \ _____ ")
    print("|_____/ / | (_| | | | | | | (_| |>  <  _\ \ |_| |_| | (_| | | (_) |_____|")
    print("      \/   \__,_|_| |_|_|_|\__,_/_/\_\ \__/\__|\__,_|\__,_|_|\___/       ")
    print("")
    print("  _____                                ___ _           _           ")
    print("  \_   \_ __ ___   __ _  __ _  ___    / __(_)_ __   __| | ___ _ __ ")
    print("   / /\/ '_ ` _ \ / _` |/ _` |/ _ \  / _\ | | '_ \ / _` |/ _ \ '__|")
    print("/\/ /_ | | | | | | (_| | (_| |  __/ / /   | | | | | (_| |  __/ |   ")
    print("\____/ |_| |_| |_|\__,_|\__, |\___| \/    |_|_| |_|\__,_|\___|_|   ")
    print("                        |___/                                    ")
    print("1) CS:GO,CS2")
    print("2) My Image")
    print("3) Ethernet Pack")
    print("")
    con = int(input("Send number:"))
    if con == 1:
        print("CS:GO/CS2")
        print("Press f10 to Cs open window")
        start = True
        while start:
            if keyboard.is_pressed("f10"):
                CS()
    if con == 2:
        print("You Image name.png/jpg/")
        myimage()
    if con == 3:
        MyPack()
Infer()