import threading

cv = threading.Condition()
current_value = 1

def thread_function(i, n):
    global cv
    global current_value

    for j in range(n):
        with cv:
            cv.wait_for(lambda: current_value == i)
            print(i, end='')
            current_value = 1 + current_value % 3
            cv.notify_all()

n = int(input())

threads = [
    threading.Thread(target=thread_function, args=(1, n)),
    threading.Thread(target=thread_function, args=(2, n)),
    threading.Thread(target=thread_function, args=(3, n)),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
