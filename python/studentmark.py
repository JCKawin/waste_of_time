score=int(input("score:"))
if (score<35):
    print("poor student, try you get more")
if(score>3 and score<71):
    print("average student, better luck next time")
if(score>70 and score<101):
    print("good student! keep it up")
else:
    print("invalid mark, feed it again corretly")
