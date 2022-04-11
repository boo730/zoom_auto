import os, datetime, time, pyautogui
import schedule

def job():
    now = datetime.datetime.now()
    print("현재 시간 출력")
    print(now)
    print("--------------")

    #os.system("taskkill.exe /f /im zoom.exe")
    #time.sleep(2)
    #os.chdir("C:\\Users\\KKB win7\\AppData\\Roaming\\Zoom\\bin")
    #os.startfile("Zoom.exe")
    #time.sleep(30)
    #pyautogui.click(515,393,button='left', clicks=1, interval=1)
    #pyautogui.hotkey('alt','f4')

    pyautogui.click(444,22,button='left', clicks=1, interval=1)
    time.sleep(1)
    pyautogui.click(337,64,button='left', clicks=1, interval=1)


schedule.every().day.at("12:00").do(job)


while True:
    schedule.run_pending()
