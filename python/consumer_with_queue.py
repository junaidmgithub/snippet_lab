import queue
import threading
import time

# Create a queue object
queue = queue.Queue()

def add_to_queue(data):
    queue.put(data)

def consumer():
    while True:
        time.sleep(2)
        data = queue.get()
        answer = data['number_1'] + data['number_2']
        print('consumer got => ', data, 'answer => ', answer)


t = threading.Thread(target=consumer)
t.daemon = True # allow the main thread to exit
t.start()

# Adding Data to queue
add_to_queue({'number_1': 1, 'number_2': 1, 'uid': 1})
add_to_queue({'number_1': 2, 'number_2': 2, 'uid': 2})
add_to_queue({'number_1': 3, 'number_2': 3, 'uid': 3})
add_to_queue({'number_1': 4, 'number_2': 4, 'uid': 4})
