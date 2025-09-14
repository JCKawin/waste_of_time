u=int(input("Initial velocity(in m/s):"))
planet=str(input("In which planet you through the object ( also moon , pluto , titan ):"))
if (planet=="earth"):
    R=(u*u)/9.8
elif(planet=="mars"):
    R=(u*u)/3.7
elif(planet=="mercury"):
    R=(u*u)/3.7
elif(planet=="venus"):
    R=(u*u)/8.8
elif(planet=="jupiter"):
    R=(u*u)/24.7
elif(planet=="saturn"):
    R=(u*u)/10.5
elif(planet=="neptune"):
    R=(u*u)/11.7
elif(planet=="uranus"):
    R=(u*u)/9.0
elif(planet=="moon"):
    R=(u*u)/1.7
elif(planet=="pluto"):
    R=(u*u)/0.49
elif(planet=="titan"):
    R=(u*u)/1.353
else:
    R=0
print("The maximum range of the object that it can travel in",planet,"=",R,"m")
