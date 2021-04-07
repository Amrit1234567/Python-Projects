print("program to find Greatest Common Divisor")
def gcd(x,y):
         if x>y:
                  x = x+y
                  y = x-y
                  x = x-y
         while True:
                  y = y%x
                  if y == 0:
                           return x
                  x = x%y
                  if x == 0:
                           return y

a = int(input("Enter a positive number: "))
b = int(input("Enter another number: "))
c = gcd(a,b)
print("GCD: " + str(c))
