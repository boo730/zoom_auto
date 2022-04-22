import pyautogui, time, datetime, schedule, webbrowser

def start_check():
    now_h = datetime.datetime.now()
    now_wday = datetime.datetime.now().weekday()

    id = "회의id"
    pw = "비밀번호"

    url = "zoommtg://zoom.us/join?action=join&confno={}&pwd={}".format(id,pw)

    dayList = ['월','화','수','목','금','토','일']
    stored_day = dayList[now_wday]

    if now_wday == 0 or now_wday == 2 or now_wday == 4: #월,수,금 요일만 접속
        print(now_h)
        webbrowser.open(url)
        print(stored_day + "요일 접속시도")
        print("-"*30)

    else:
        print(now_h)
        print(stored_day + "요일은 안함")
        print("-"*30)
        time.sleep(2)

def zoom_kill():
    now = datetime.datetime.now()
    print("현재 시간 출력")
    print(now)
    print("종료시도")
    print("-"*30)

    pyautogui.click(444,22,button='left', clicks=1, interval=1)
    #time.sleep(1)
    pyautogui.click(337,64,button='left', clicks=1, interval=1)


schedule.every().day.at("10:16").do(start_check)
schedule.every().day.at("12:00").do(zoom_kill)

while True:
    schedule.run_pending()
    time.sleep(7)
    time.sleep(5)
    pyautogui.click(515,393,button='left', clicks=1, interval=1)
    time.sleep(1)
    pyautogui.click(497,335,button='left', clicks=1, interval=1)