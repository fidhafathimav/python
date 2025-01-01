def exchange_first_last(str):
    if len(str)<=1:
        return str
    return str[-1]+str[1:-1]+str[0]
input_string=input("enter a string:")
result=exchange_first_last(input_string)
print("modified string:",result)