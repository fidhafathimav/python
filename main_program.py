from fib_module import fib
n=int(input("enter the number of fibonacci terms you want:"))
print("fibonacci sequence:")
for i in range(n):
      print(fib(i),end=" ")