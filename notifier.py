from win10toast import ToastNotifier
import time
import sys
import pyttsx3
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
times = str(input("Enter time to Notify.: "))
message = input("Enter Message : ")
notify_time = times.split(",")
notify_message = message.split(",")
def notification(notify_time,notify_message):
    test_time = notify_time
    test_message = notify_message
    for i,j in zip(test_time,test_message):

            current_time = time.strftime("%H:%M:%S")
            if current_time == i:
                print(current_time)
                hr = ToastNotifier()
                hr.show_toast("Notification", j,"E:\Python\python work space\webScraping\Practice\Graphicloads-Flat-Finance-Global.ico",3)
                engine = pyttsx3.init()
                engine.setProperty('rate', 125)
                engine.setProperty('voice', en_voice_id)
                engine.say("You have a notification saying" + j)
                engine.runAndWait()
                test_time.remove(i)
                test_message.remove(j)
                if len(test_time)==0:
                    engine.say("tasks completed closing application..")
                    engine.runAndWait()
                    choice = str(input("want to close app.?"))
                    if choice=="yes":

                        sys.exit()
                    elif choice=="no":
                        times = str(input("Enter time to Notify.: "))
                        message = input("Enter Message : ")
                        notify_time2 = times.split(",")
                        notify_message2 = message.split(",")
                        while True:
                            notification(notify_time2,notify_message2)
                else:
                    pass
            else:
                pass
while True:
    notification(notify_time,notify_message)

