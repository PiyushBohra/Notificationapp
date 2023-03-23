import time
from plyer import notification

if __name__=='__main__':
    notification.notify(
        title="PLEASE DRINK WATER",
        message="The human body comprises around 60% water.If you don’t stay hydrated, your physical performance can suffer.",
        app_icon="icon.ico",
        timeout=15

)
time.sleep(60*60)