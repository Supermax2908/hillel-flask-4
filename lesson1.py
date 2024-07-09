from datetime import datetime
import platform


def hello():
    print('Initialization')
    print('Hello world!')
    print((datetime.now()))
    print(platform.platform())
    print('Goodbye')


if __name__ == '__main__':
    hello()
