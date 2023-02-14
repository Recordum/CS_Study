import threading
import os

def foo():
    print('thread ID', threading.get_native_id())
    print('process ID', os.getpid())


if __name__ == '__main__':
    print('process ID', os.getpid())
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()

# 멀티스레드는 같은 프로세스 ID를 공유하고 각기다른 스레드 ID를 갖는다.