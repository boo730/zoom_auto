import pyautogui, time, datetime, schedule, webbrowser, os

#os.system("net user administrator /active:yes")

#창세팅
winDowAll = pyautogui.getAllWindows()

for w in winDowAll:
    
    if w.title == "C:\Windows\py.exe" or w.title == "taskeng.exe" or w.title == "C:\WINDOWS\py.exe":
        w.top=0
        w.left=652
        w.width=200
        w.height=700


def start_check():
    now_h = datetime.datetime.now()
    now_wday = datetime.datetime.now().weekday()

    id = "id번호"
    pw = "비밀번호"

    url = "zoommtg://zoom.us/join?action=join&confno={}&pwd={}".format(id,pw)

    dayList = ['월','화','수','목','금','토','일']
    stored_day = dayList[now_wday]

    if now_wday == 2 or now_wday == 6: #수,일 요일만 접속
        print(now_h)
        webbrowser.open(url)
        print(stored_day + "요일 접속시도")
        print("-"*30)

    else:
        print(now_h)
        print(stored_day + "요일은 안함")
        print("-"*30)
        time.sleep(2)

def zoomkill_upgrade():
    now = datetime.datetime.now()
    print(now)
    winDowAll = pyautogui.getAllWindows()

    for w in winDowAll:
        s = w.title
        word = "Zoom"
        zoomCon = s.startswith(word)
        
        if zoomCon == True:
            w.activate()
            time.sleep(1)
            pyautogui.hotkey('alt','q')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press("enter")
            print(f"'{w.title}' 창을 종료합니다")
            print("-"*30)
        elif w.title == "호스트를 기다리는 중":
            print("아무일도 없었다")
            w.close()
            print("-"*30)

def ntp_sync():
    os.system("w32tm /resync > nul")

def close_task():
    print("접속기를 종료합니다")
    time.sleep(3)
    quit()


schedule.every().day.at("11:50").do(start_check)
schedule.every().day.at("13:30").do(zoomkill_upgrade)
schedule.every().monday.at("16:50").do(close_task)
schedule.every().minute.at(":30").do(ntp_sync)


while True:
    schedule.run_pending()
    winDowAll = pyautogui.getAllWindows()
    time.sleep(7)
    time.sleep(5)
    for w in winDowAll:
        if w.title == "이 회의는 호스트 또는 참가자가 기록 중입니다":
            w.close()
            print("기록중 확인 완료")
            print("-"*30)
        elif w.title == "소회의실":
            w.activate()
            pyautogui.press("enter")
            print("소회의실 입장완료")
            print("-"*30)

