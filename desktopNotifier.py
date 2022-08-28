from plyer import notification
import time



if __name__ == '__main__' :
    while True:
        notification.notify(
            title= "***Take Rest***",
            message="Rest is vital for better mental health.",
            app_icon="C:/Users/HP/OneDrive/Pictures/Saved Pictures/y1",
            timeout=5)
        time.sleep(10)

