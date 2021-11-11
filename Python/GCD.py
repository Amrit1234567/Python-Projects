def gcd(x,y):
         '''Finds the greatest common divisor'''
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
                  
