from time import time , sleep

def timer(func):
    start = time.time()
    def wrappper():
        timer(func)
    end = time.time()
    print(f"{start - end :.3f}")
    return

@wrapper
def cal():
    time.sleep(3)
    print(90)

if __name__=='__main__':
    cal()
