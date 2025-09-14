def primechk(no: int) -> bool:
    if no == 1 or no == 2:
        return None
    else:
        a = 2
        while a!=no:
            if no%a == 0:
                return False
            a+=1
        if a == no:
            return True

if __name__ == "__main__":
    
    while True:
        try:
            a = int(input("enter a no.:"))
            break
        except ValueError :
            print("give a proper integer")
                
    print(primechk(a))


