def parse_number(s):
    s = s.strip()
    if not s:
        print("Not a number error")
        return
    s = s.replace(',','')
    return float(s)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("division by zero error")
        return
    return a/b
def accept_numbers():
    x = parse_number(input("Enter the first number: "))
    y = parse_number(input("Enter the second number: "))
    return x,y
def main():
    menu = """
    Simple Calculator:
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    5.Exit
    Plese select a menu: 
    """
    while True:
        choice = int(input(menu).strip())
        if choice == 1:
            a,b = accept_numbers()
            ans = add(a,b)
            print(ans)
        elif choice == 2:
            a,b = accept_numbers()
            ans = sub(a,b)
            print(ans)
        elif choice == 3:
            a,b = accept_numbers()
            ans = mul(a,b)
            print(ans)
        elif choice == 4:
            a,b = accept_numbers()
            ans = div(a,b)
            print(ans)
        elif choice == 5:
            print("Bye")
            break
        else:
            print("Please choose the menu between 1-5")
main()