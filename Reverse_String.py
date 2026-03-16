# A python program on Reverse a string using recursion

def reverse_string(data):
    if len(data) <= 1:
        return data
    else:
        return reverse_string(data[1:]) + data[0]
    
ip_string = input("Enter a String:")
print("Reverse of String is:", reverse_string(ip_string))
