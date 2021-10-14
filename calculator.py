## the add function here for john
def add(x, y):
    return x + y
## the sub function here for john
def sub(x, y):
    return (x - y)
## the mul function here for merhwa
def mul2(x,y):
    return x  * y
## the div function here for merhwa
def div(x,y):
    return x / y
def main():
    run = True
    while run:
        n1 = int(input("select the first number you want to use: "))
        n2 = int(input("select the second number you want to use: "))
        op = input("Select the operator you want: ")

        if op == "+":
            result = add(n1, n2)
            run = False
        elif op == "-":
            result = sub(n1, n2)
            run = False
        elif op == "*":
            result = mul(n1, n2)
            run = False
        elif op == "/":
            result = div(n1, n2)
            run = False
        else:
            print("Try again but select a correct operator")

    print(result)

main()