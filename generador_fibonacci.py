# fibinacci
# 0 1 1 2 3 5 8 13 21

def fibonacci(limite):
    a, b = 0, 1
    while a< limite:
        yield a 
        a, b = b, a+b

for num in fibonacci(10):
    print(num)


print("--------------------")

def num_par(limite):
    a=1
    while a< limite+1:
        yield a
        a= a+2
for num in num_par(11):
    print(num) 