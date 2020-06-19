import time
import multiprocessing
import linux_notify
import traceback

def notify_from_queue():
    proc = multiprocessing.current_process()
    while True:
        try:
            print('started')
            notification = linux_notify.notification_queue.get()
            linux_notify.notify("Total Active cases in {}: {}".format(notification['state_name'], notification['state_active']), "Confirmed: +{} Recovered: -{}".format(notification['confirmed'], notification['recovered']))
            time.sleep(5)
        except Exception:
            print('Error {}'.format(traceback.format_exc()))
            



def enqueue(state_name, state, state_new, state_recovered):
    linux_notify.notification_queue.put({'state_name':state_name, 'state_active': state, 'confirmed': state_new, 'recovered' : state_recovered})


#notify("India {} (+{}) (-{})".format(india_active, india_new, india_recovered,), "{} {} (+{}) (-{})".format(state_name, state, state_new, state_recovered))
#time.sleep(1)
#notify("India {} (+{}) (-{})".format(india_active, india_new, india_recovered,), "{} {} (+{}) (-{})".format(state_name, state, state_new, state_recovered))