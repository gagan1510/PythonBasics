def fahrenheit(t):
    return (9.0/5)*t + 32

print(fahrenheit(0))

temp = [0 , 22.5, 40, 100]

temp_f = list(map(fahrenheit, temp))

print(temp_f)

# a map function is used to send a list to the function and receive the result as a list
