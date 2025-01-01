a=[]
n=int(input("enter the number of elements:"))
for x in range(n):
    num=int(input("enter element{x+1}:"))
    a.append(num)
    odd_numbers=[num for num in a if num%2!=0]
print("original list:",a)
print("list after removing even numbers:",odd_numbers)


