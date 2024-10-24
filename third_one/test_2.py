def bonnifaci_methoda(fibo_in, fibo_len):
    for i in range(2, fibo_len):
        if fibo_in[i] != fibo_in[i-1] + fibo_in[i-2]:
            return False
    return True

fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


if bonnifaci_methoda(fibo, len(fibo)):
    print("jedná se o fibonaciho posloupnost")

else:
    print("nejedná se o fibonaciho posloupnost")