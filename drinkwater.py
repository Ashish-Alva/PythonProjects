from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Drink Water",
            message = "askdlf sad flaskdf asdlfkja asdlfsk asdf",
            timeout =  1,
            app_icon = "D:\Projects\python_projects\Projects\glass.ico" 
        )
        time.sleep(60*60)