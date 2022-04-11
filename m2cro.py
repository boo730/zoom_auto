import pyautogui,time, datetime
import schedule

print("< ZOOM 메크로 1.0 >")

def sleepjob():
    now = datetime.datetime.now()
    print(now)
    print("일시정지 감지")
    time.sleep(300)
    print("메크로 재가동")
    #schedule.every().day.at("17:18").do(sleepjob)

schedule.every().day.at("10:14").do(sleepjob)
schedule.every().day.at("11:59").do(sleepjob)

while True:
    while True:
        schedule.run_pending()
        time.sleep(7)
        #pyautogui.press('enter')
        time.sleep(5)
        pyautogui.click(515,393,button='left', clicks=1, interval=1)
        time.sleep(2)
        pyautogui.click(497,335,button='left', clicks=1, interval=1)
