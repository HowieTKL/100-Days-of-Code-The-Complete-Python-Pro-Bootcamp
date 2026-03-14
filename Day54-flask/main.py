import time

print("__name__", __name__)



def delay_decorator(func):
    def wrapper():
        print("Wait...")
        time.sleep(2)
        func()
    return wrapper

@delay_decorator
def say_hello():
    print("hello")


say_hello()