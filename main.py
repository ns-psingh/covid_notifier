import os
import time
from queue import Queue

notification_queue = Queue()
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

#def enqueue(state_name, state, state_new, state_recovered):
#    notification_queue.put({'state_name':state_name, 'state_active': state, 'confirmed': state_new, 'recovered' : state_recovered})



#notify("India {} (+{}) (-{})".format(india_active, india_new, india_recovered,), "{} {} (+{}) (-{})".format(state_name, state, state_new, state_recovered))
#time.sleep(1)
#notify("India {} (+{}) (-{})".format(india_active, india_new, india_recovered,), "{} {} (+{}) (-{})".format(state_name, state, state_new, state_recovered))