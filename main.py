import threading

cv = threading.Condition()
current_value = 1


def thread_function(expected_val, actions_num):
    global cv
    global current_value

    for j in range(actions_num):
        with cv:
            cv.wait_for(lambda: current_value == expected_val)
            print(expected_val, end='')
            current_value = 1 + current_value % 3
            cv.notify_all()


def main():
    actions_num = int(input())

    threads = [
        threading.Thread(target=thread_function, args=(1, actions_num)),
        threading.Thread(target=thread_function, args=(2, actions_num)),
        threading.Thread(target=thread_function, args=(3, actions_num)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
