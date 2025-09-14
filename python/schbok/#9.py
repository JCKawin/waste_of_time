class convo():
    def __init__(self, name2):
        self.you = name2
    def nalam(self):
        print(f'How are you {self.you}?')
        d = input(">>>")
        d = d.strip()
        if d.lower() != "fine":
            print(f"why what happened {self.you}?")
        else:
            pass
        return
    def eat(self):
        print(f"did you eat? {self.you}")
        d =input(">>>")
        d = d.strip()
        if d.lower() == "yes":
            print("what special?")
        else:
            print("why what happened")
        return

if __name__=="__main__":
    con = convo("kawin")
    con.nalam()
    con.eat()
