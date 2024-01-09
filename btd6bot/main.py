import pyautogui
import time
import keyboard
import threading
from ace import test_colors_and_positions_ace
from tackshooterfire import test_colors_and_positions_tack
from spikefactory import test_colors_and_positions_spike
from perma import test_colors_and_positions_permaspike
from speed import false
from speed import true

mouse_speed = 0.1

tagshooter = [
    ((79, 213, 0), (280, 490), "1"),
    ((79, 213, 0), (1500, 490), "1"),
]

aceandspike = [
    ((79, 213, 0), (280, 790), "3"),
    ((79, 213, 0), (1500, 790), "3"),
]

#Defeat still in development
def defeat():
    global restart_main_loop
    left, top, width, height = 682, 244, 537, 171
    region = (left, top, width, height)
    
    try:
        img = pyautogui.locateOnScreen('images/defeat.PNG', confidence=0.9, grayscale=True, region=region)
        if img is not None:
            print('Lag spikes caused an unstable run')
            time.sleep(1)
            print('Script will fix itself')
            time.sleep(3)
            print("Restarting main Loop ")
            pyautogui.moveTo(x=621, y=807, duration=mouse_speed)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            restart_main_loop = True
    except pyautogui.ImageNotFoundException:
        pass

def loadgame():
    print('starting script')
    time.sleep(1)
    pyautogui.moveTo(x=821, y=947, duration=mouse_speed)
    time.sleep(0.1)
    print('Pressing play button')
    pyautogui.click()

    print('Navigate to map')
    pyautogui.moveTo(x=277, y=435, duration=mouse_speed)
    time.sleep(0.1)
    pyautogui.click()

    print('Selecting Dark castle')
    pyautogui.moveTo(x=527, y=573, duration=mouse_speed)
    time.sleep(0.1)
    pyautogui.click()

    print('choosing hard impobbable')
    pyautogui.moveTo(x=1300, y=531, duration=mouse_speed)
    time.sleep(0.1)
    pyautogui.click()

    print('choosing hard impobbable')
    pyautogui.moveTo(x=1300, y=741, duration=mouse_speed)
    time.sleep(0.1)
    pyautogui.click()

    print('Waiting for game to load')
    while True: 
        try:
            left, top, width, height = 760,660,407,166
            region = (left, top, width, height)
            img = pyautogui.locateOnScreen('images/play.PNG', confidence=0.9, grayscale=True, region=region)
            if img is not None:
                time.sleep(1)
                pyautogui.moveTo(x=950, y=756, duration=mouse_speed)
                time.sleep(0.1)
                print('Pressing Ok')
                pyautogui.click()
                time.sleep(0.1)
                break
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.1) 


def starttowers():
    a = 33
    b = 33
    if b == a:
        pyautogui.moveTo(x=587, y=614, duration=mouse_speed)
        time.sleep(2)

        print('Placing hero')
        keyboard.press_and_release('u')
        time.sleep(0.1)
        pyautogui.click()
        
        print('Placing tackshooter')
        pyautogui.moveTo(x=573, y=492, duration=mouse_speed)
        time.sleep(0.1)
        time.sleep(0.1)
        keyboard.press_and_release('r')
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)

        print('Upgrading tackshooter')
        keyboard.press_and_release('1')
        time.sleep(0.1)
        keyboard.press_and_release('3')
        time.sleep(0.1)
        keyboard.press_and_release('3')
       
        time.sleep(0.1)
        print('pressed play')
        keyboard.press_and_release('space')
        true()



def round16stop():
    #Detecting round 16
    left, top, width, height = 1006,0,671,123
    region = (left, top, width, height)
    while True: 
        try:
            img = pyautogui.locateOnScreen('images/16.PNG', confidence=0.9, grayscale=True, region=region)
            if img is not None:
                print('Round 16')
                true()
                time.sleep(0.1)
            #place spike
                print('Spike Factory 2/0/3')
                pyautogui.moveTo(x=1522, y=535, duration=mouse_speed)
                time.sleep(0.1)
                keyboard.press_and_release('j')
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
            #upgrade spike
                print('Upgrading spike factory')
                keyboard.press_and_release('1')
                time.sleep(0.1)
                keyboard.press_and_release('1')
                time.sleep(0.1)  
                keyboard.press_and_release('3')
                time.sleep(0.1)
                keyboard.press_and_release('3')
                time.sleep(0.1)
                keyboard.press_and_release('3')
                keyboard.press_and_release('3')
                time.sleep(0.1)
                false()
                break
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.1) 

def round32stop():
    #regionArea to check image in
    left, top, width, height = 1006,0,671,123
    region = (left, top, width, height)
    while True: 
        try:
            img = pyautogui.locateOnScreen('images/32.PNG', confidence=0.9, grayscale=True, region=region)
            if img is not None:
                print('Round 32')
                true()
                time.sleep(1)
                print('Tack Shooter 4/0/2')
                pyautogui.moveTo(x=555, y=474, duration=mouse_speed)
                time.sleep(1)
                pyautogui.click()
                keyboard.press_and_release('1')
                time.sleep(0.1)
                pyautogui.moveTo(x=1522, y=535, duration=mouse_speed)
                time.sleep(0.1)
                pyautogui.click()
                false()
                break
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.1)  


def round47stop():
    left, top, width, height = 1006,0,671,123
    region = (left, top, width, height)
    while True: 
        try:
            img = pyautogui.locateOnScreen('images/47.PNG', confidence=0.9, grayscale=True, region=region)
            if img is not None:
                print('Round 47')
                break
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.1)  

def round58stop():
    left, top, width, height = 1006,0,671,123
    region = (left, top, width, height)
    while True: 
        try:
            img = pyautogui.locateOnScreen('images/58.PNG', confidence=0.9, grayscale=True, region=region)
            if img is not None:
            #Detecting round 58
                print('Round 58')
                true()
                time.sleep(1)
                pyautogui.moveTo(x=1412, y=202, duration=mouse_speed)
                time.sleep(0.1)
            #Placing ace monkey
                print('Ace monkey 2/0/4')
                pyautogui.click()
                pyautogui.click()
                keyboard.press_and_release('v')
                time.sleep(0.1)
                pyautogui.click()
                pyautogui.click()
            #Upgrading ace
                keyboard.press_and_release('3')
                time.sleep(0.1)
                keyboard.press_and_release('3')
                time.sleep(0.1)
                keyboard.press_and_release('3')
                time.sleep(0.1)
                keyboard.press_and_release('3')
                time.sleep(0.1)
                keyboard.press_and_release('1')
                time.sleep(0.1)
                keyboard.press_and_release('1')
                time.sleep(0.1)
                false()
                break
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.1)

def gamefinished():
    while True: 
        try:
            img = pyautogui.locateOnScreen('images/instamonkey.PNG', confidence=0.9, grayscale=True)
            if img is not None:
                print('Collecting round 100 insta monkey')
                pyautogui.moveTo(x=962, y=532, duration=mouse_speed)
                time.sleep(1)
                pyautogui.click()
             #Next button
                while True: 
                    try:
                        img = pyautogui.locateOnScreen('images/next.PNG', confidence=0.9, grayscale=True)
                        if img is not None:
                            print('press next')
                            time.sleep(1)
                            pyautogui.moveTo(x=960,  y=906, duration=mouse_speed)
                            time.sleep(0.1)
                            pyautogui.click()
                            break
                    except pyautogui.ImageNotFoundException:
                        pass
                    time.sleep(0.1)
             #Pressing Victory home button
                while True: 
                    try:
                        img = pyautogui.locateOnScreen('images/home2.PNG', confidence=0.9, grayscale=True)
                        if img is not None:
                            print('press home')
                            time.sleep(1)
                            pyautogui.moveTo(x=716,  y=842, duration=mouse_speed)
                            time.sleep(0.1)
                            pyautogui.click()
                            break
                    except pyautogui.ImageNotFoundException:
                        pass
                    time.sleep(0.1)
                break
        except pyautogui.ImageNotFoundException:
            pass


def collect():
    left, top, width, height = 835, 630, 249, 92
    region = (left, top, width, height)
    try:
        img = pyautogui.locateOnScreen('images/collect.PNG', confidence=0.9, grayscale=True, region=region)
        if img is not None:
            print('Can collect event monkeys')
            time.sleep(2)
            pyautogui.moveTo(x=958, y=673, duration=mouse_speed)
            time.sleep(1)
            pyautogui.click()
            print('Collecting')
            # insta monkey event collecting 1,2 and 3
            pyautogui.moveTo(x=764, y=541, duration=mouse_speed)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            pyautogui.moveTo(x=1157, y=534, duration=mouse_speed)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            pyautogui.moveTo(x=952, y=539, duration=mouse_speed)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            # continue
            pyautogui.moveTo(x=965, y=996, duration=mouse_speed)
            time.sleep(1)
            pyautogui.click()
            pyautogui.moveTo(x=75, y=52, duration=mouse_speed)
            time.sleep(1)
            pyautogui.click()
        else:
            print('Nothing to collect.')
    except pyautogui.ImageNotFoundException:
        pass
        time.sleep(0.1)

def levelup():
    while True: 
        try:
            img = pyautogui.locateOnScreen('images/levelup.PNG', confidence=0.9, grayscale=True)
            if img is not None:
                print('level up')
                pyautogui.moveTo(x=971,  y=525, duration=mouse_speed)
                time.sleep(0.1)
                pyautogui.click()
                break
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.1)

def mainloop():
    global restart_main_loop
    while True:
        time.sleep(1)
        loadgame()
        starttowers()
        defeat() 
        test_colors_and_positions_tack(tagshooter)
        round16stop()
        test_colors_and_positions_spike(aceandspike)
        round32stop()
        round47stop()
        test_colors_and_positions_permaspike(aceandspike)
        round58stop() 
        test_colors_and_positions_ace(aceandspike)
        gamefinished()
        print('ready in homescreen')
        while True: 
            try:
                left, top, width, height = 0,95,261,223
                region = (left, top, width, height)
                img = pyautogui.locateOnScreen('images/home.PNG', confidence=0.9, grayscale=True, region=region)
                if img is not None:
                    print('ready to restart')
                    time.sleep(0.1)
                    break
            except pyautogui.ImageNotFoundException:
                pass
            time.sleep(0.1) 
        collect()
        print('End script')
        time.sleep(1)
        if keyboard.is_pressed('F6'):
            print('Loop terminated by user.')
            break


#Running 2 loops at the same time (Checking if level up and the main)
def run_levelup():
    while True:
        levelup()

def run_mainloop():
    while True:
        mainloop()

thread_levelup = threading.Thread(target=run_levelup)
thread_mainloop = threading.Thread(target=run_mainloop)

thread_levelup.start()
thread_mainloop.start()

thread_levelup.join()
thread_mainloop.join()


