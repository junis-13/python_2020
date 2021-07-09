durchgang = 1
while durchgang < 11:
    print(durchgang)
print("nach der Schleife")


op = input("welchen operater willst du verwenden")
num1 = input("sage mir eine zahl")
num2 = input("sage noch eine")
num1 = int(num1)
num2 = int(num2)

#plus
if (op == "+"):
    print(num1 + num2)
#minus
elif (op == "-"):
    print(num1 - num2)
#mal
elif (op == "*"):
    print(num1 * num2)

#geteilt
elif (op == "/"):
    print(num1 / num2)