print('gread telling program')
maths=int(input("enter your marks in maths"))
science=int(input("enter your marks in science"))
quantum_physics=int(input("enter your marks in quantum physics"))

if maths>=40 and science>=40 and quantum_physics>=40:
    print("congratilation you are pass")
    marks=(maths+science+quantum_physics)/3
    if marks>=80:
        print("you got A+ grade")
    elif marks>=60:
        print("you got A grade")
    elif marks>=50:
        print("you got B grade")
    else:
        print("you got C grade")

else:
    print("sorry you are fail")