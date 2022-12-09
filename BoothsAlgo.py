
def negate(bits):
    l = ''
    for n in bits:
        if n=="1":
            l+="0"
        if n=="0":
            l+="1"
    return l

def addOne(bits):
    return format(int(bits,2)+1,'08b')

def ShiftRight(bits):
    if bits[0]=="0":
        return "0" + bits[:15]
    if bits[0]=="1":
        return "1" + bits[:15]

def display(Values):
    print(str(Values[0]).center(6) + "|" + str(Values[1]).center(10) + "|" + str(Values[2]).center(10) + "|" + (str(Values[3][:8]+" "+str(Values[3][8:]))).center(19) +"|"+ str(Values[4]).center(3))

AC = '00000000'
BR = ''
NBR = ''
QR = ''
Q1 = '0'

print("Input Multiplicand")
BR = input()
if '-' in BR:
    BR = BR.replace("-","")
    BR = format(int(BR),'08b')
    BR = addOne(negate(BR))
else:
    BR = format(int(BR),'08b')
NBR = negate(BR)

print("Input Multiplier")
QR = input()
if "-" in QR:
    QR = QR.replace("-","")
    QR = format(int(QR),'08b')
    QR = addOne(negate(QR))
else:
    QR = format(int(QR),'08b')

P = AC+QR
print("".ljust(52,"_"))
display(["Step", "Inst", "BR", "Product", "Q"])
print("".ljust(52,"_"))
display([0,"init", BR, P, Q1])
for c in range(1,9):
    inst = "RSh "
    print("".ljust(52,"_"))
    AC = P[:8]
    QR = P[8:]
    if P[-1]=="1" and Q1 == "0":
        AC = format(int(AC,2)+int(NBR,2)+1,'08b')[-8:]
        inst = "Add/"+inst
    if P[-1]=="0" and Q1 == "1":
        AC = format(int(AC,2)+int(BR,2),'08b')[-8:]
        inst = "Sub/"+inst
    Q1 = P[-1]
    P = ShiftRight(AC+QR)
    display([c,inst,BR,P,Q1])
print("".ljust(52,"_"))
if P[0]=="1":
    print("The final Product is: -" + str(int(addOne(negate(P)),2)))
else:
    print("The final Product is: " + str(int(P,2)))