import pyautogui
import subprocess
from datetime import datetime
import time
import pandas as pd 


def log_in(meetingid, password):
    #opens Zoom app
    subprocess.call("C:\\Users\\pudge\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(3)

    #clicks join button
    while True:
        join_button = pyautogui.locateCenterOnScreen('images/zoomjoin1.png')
        if join_button != None:
            pyautogui.moveTo(join_button)
            pyautogui.click()
            time.sleep(1)
            break
        else:
            time.sleep(2)

    while True:
        join_empty = pyautogui.locateCenterOnScreen('images/join_inactive.png')
        if join_empty != None:
            pyautogui.moveTo(join_empty)
            pyautogui.click()
            time.sleep(2)
            break
        else:
            print("Not found")
            time.sleep(1)
    
    #enters meetings id
    while True:
        meeting_id_button = pyautogui.locateCenterOnScreen('images/meeting_id.png')
        if meeting_id_button != None:
            pyautogui.moveTo(meeting_id_button)
            pyautogui.click()
            pyautogui.write(meetingid)
            #pyautogui.press('enter')
            time.sleep(2)
            break
        else:
            print("Meeting bar empty")
            time.sleep(1)
    
    #mutes audio/video
    while True:
        media_button = pyautogui.locateAllOnScreen('images/check_box.png')
        for button in media_button:
            pyautogui.moveTo(button)
            pyautogui.click()
            time.sleep(1)
        break
    
    #joins meeting
    while True:
        join_bttn = pyautogui.locateCenterOnScreen('images/join_button.png')
        if join_bttn != None:
            pyautogui.moveTo(join_bttn)
            pyautogui.click()
            break
        else:
            time.sleep(2)

    #unblocks password bar
    while True:
        join_bttn_blank = pyautogui.locateCenterOnScreen('images/join_meet_blank.png')
        if join_bttn_blank != None:
            pyautogui.moveTo(join_bttn_blank)
            pyautogui.click()
            break
        else:
            time.sleep(2)

    while True:
        passcode_space = pyautogui.locateCenterOnScreen('images/passcode_bar.png')
        if passcode_space != None:
            pyautogui.moveTo(passcode_space)
            pyautogui.click()
            pyautogui.write(password)
            pyautogui.press('enter')
            break
        else:
            time.sleep(2)

    while True:
        join_meet_bttn = pyautogui.locateCenterOnScreen('images/join_meet.png')
        if join_meet_bttn != None:
            pyautogui.moveTo(join_meet_bttn)
            pyautogui.click()
            break
        else:
            time.sleep(2)


df = pd.read_csv('classtimes.csv')


#will check if time from computer matches time in csv and proceed to log into that class
#somewhat glitchy on line 108?//fixed, extra bracket at end
while True: 
    current = datetime.now().strftime("%H:%M")

    if current in str(df['times']):
        row = df.loc[df['times'] == current]
        z_id = str(row.iloc[0, 1])
        z_pass = str(row.iloc[0, 2])

        log_in(z_id, z_pass)
        time.sleep(40)
        print("Logged in to class:")

#log_in("640 028 3291", "123456")