import covid_data as cd
import time
import os
import multiprocessing
import notifiy_mgr

notification_queue = multiprocessing.Queue()

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

if __name__ == "__main__":
    background_process = multiprocessing.Process(target=notifiy_mgr.notify_from_queue)
    background_process.start()
    covid = cd.CovidData()
    while True:
        covid.retreive()
        time.sleep(10)