
fibo_list = [1, 2, 3, 5, 8, 13]

index_to_remove = -1

while len(fibo_list) >= 3:
    if fibo_list[-1] == fibo_list[-2] + fibo_list[-3]:
        del fibo_list[index_to_remove]
    else:
        print("Nejedná se o fibonaciho")
        break
else:
    if len(fibo_list) < 3:
        print("Přílíš málo prvků k ověřne")

