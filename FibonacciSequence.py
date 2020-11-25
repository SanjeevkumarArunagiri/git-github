def Fibonacci(n):
    count = 0
    a = 0
    b = 1
    sum = 0
    result = 0
    for i in range(n):
        while count < n:
            count += 1
            a = b
            b = sum
            sum = a + b
            if sum % 2 == 0:
                print(f"even num is : {sum}")
                result += sum


    print(sum)
    print(f"sum is :{result}")


Fibonacci(4000000)