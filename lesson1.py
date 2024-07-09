from datetime import datetime


def hello():
    print('Initialization')
    print('Hello world!')
    print((datetime.now()))
    print((datetime.now().strftime("%A")))
    print('Goodbye')


if __name__ == '__main__':
    hello()
