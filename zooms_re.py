import os, pyautogui, time, datetime, schedule

def chrome_kill():
    os.system("taskkill.exe /im chrome.exe")

def start_check():
    now_h = datetime.datetime.now()
    now_wday = datetime.datetime.now().weekday()

    if now_wday == 0: #요일 이름 저장
        stored_day = "월"
    elif now_wday == 1:
        stored_day = "화"
    elif now_wday == 2:
        stored_day = "수"
    elif now_wday == 3:
        stored_day = "목"
    elif now_wday == 4:
        stored_day = "금"
    elif now_wday == 5:
        stored_day = "토"
    elif now_wday == 6:
        stored_day = "일"
    else:
        stored_day = "X"

    if now_wday == 0 or now_wday == 2 or now_wday == 4: #월,수,금 요일만 접속
        print(now_h)
        #os.system("firefox www.naver.com")
        #os.system("start www.naver.com")
        os.system("start zoom입장주소입력")
        print(stored_day,"요일 접속시도")
        print("-"*30)
        #time.sleep(30)
        #os.system("pkill firefox")
        #os.system("taskkill.exe /im chrome.exe")

    else:
        print(now_h)
        print(stored_day,"요일은 안함")
        print("-"*30)
        time.sleep(2)


schedule.every().day.at("10:15").do(start_check)
schedule.every().day.at("10:25").do(chrome_kill)

while True:
        schedule.run_pending()
