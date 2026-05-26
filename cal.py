num1=int(input("enter num1 number "))
num2=int(input("enter num2 number "))
choose=input("choose operator '+','-' ,'/' ,'//' ,' *' ,'%' : ")
match choose:
    case  '+':
        result=num1+num2
        print("Addition", result)
    case '-':
        result=num1-num2
        print("Subraction",result)
    case '/':
        result=num1/num2
        print("division",result)
    case '//':
        result=num1//num2
        print("floor division",result)
    case '*':
        result=num1*num2
        print("multiplication",result)
    case '%':
        result=num1%num2
        print("modulus",result)

    case default:
        print("Not found")

