


class calculator:
    def __init__(self):
        self.line : str = ''
        self.lst : list =[]
        self.aug : list[int] = []
        self.oper : list[str] = []
        self.runner = True

        

    def run(self):
        while True:
            self.line = input(">>>")
            if self.line.lower() != 'quit':
                self.lst = self.line.split()
                self._separator()
            else: 
                break
            self._calculate()

    
    def _separator(self):
        for i in self.lst:
            try:
                self.aug.append(int(i))

            except ValueError:
                self.oper.append(i)

    def _calculate(self):
        self.result = self.aug[0]
        for i in range(1,len(self.oper)+1):
            match self.oper[i-1]:
                case '+':
                    self.result += self.aug[i]
                case '-':
                    self.result -= self.aug[i]
                case '*':
                    self.result *= self.aug[i]
                case '/':
                    self.result /= self.aug[i]

        print(self.result)


a : calculator = calculator()
a.run()
        
