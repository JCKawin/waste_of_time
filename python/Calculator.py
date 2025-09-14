class calculator():
    def __init__(self,a,b):
        self.h = a 
        self.g = b
    def add(self):
        print(self.h+self.g)
    def sub(self):
        print(self.h-self.g)
    def mul(self):
        print(self.h*self.g)
    def div(self):
        print(self.h/self.g)

if __name__ == "__main__":
    while True:
        print("enter two nos:")
        a=int(input())
        b=int(input())
        val = calculator(a,b)
        opt=input("Enter your option:")
        if opt=="+":
            val.add()
        elif opt=="-":
            val.sub()
        elif opt=="*":
            val.mul()
        elif opt=="/":
            val.div()
        elif opt=="Exit":
            break
        else:
            print("invalid option")
