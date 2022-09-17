#This function is used to calculate Greatest common divisor of two numbers using recursion
class GCD:
    def gcd(self, num1, num2):
        if num2==0:
            return num1
        else:
            return self.gcd(num2,num1%num2)

number1=int(input("Enter 1st number ="))
number2=int(input("Enter 2nd number ="))

g=GCD()

print("Greatest Common Divisor ==",g.gcd(number1, number2))
    
    