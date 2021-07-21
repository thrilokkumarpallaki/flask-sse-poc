from requests import get
from threading import Thread, Lock
from random import choice
from time import sleep


usernames = ['bob', 'kane']
msgs = {'bob': ['Hey Bob!', 'Bob, what\'s up?', 'Hey Bob, How are you?', 'Hey Bob, How things are going?', 'Hey Bob, reply me man...'],
        'kane': ['Hey Kane!', 'Hey Kane, why didn\'t you come to office yesterday?', 'Hey Kane, Is everything file?', 'Hey Kane, My Task is completed!']}


def trigger_loop(username, msg):
    thread_lock.acquire()
    get(f'http://localhost:5000/event-trigger/{username}/{msg}')
    sleep(0.5)
    thread_lock.release()


if __name__ == '__main__':
    thread_lock = Lock()
    count = 5
    while count != 0:
        _username = choice(usernames)
        msg = choice(msgs[_username])
        t = Thread(target=trigger_loop, args=(_username, msg))
        t.start()
        count -= 1

