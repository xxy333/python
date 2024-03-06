# #age = int(input("Zadejte vás věk\n"))
# #if age >= 18:
# #    print("Jste dospělý")
# #else:
# #    print("nejste dospělý")


# print("Vítejte na horské dráze")
# height = int(input("Jaká je vaše výška? (v cm): "))
# price = 0
# if height >= 90:
#     print("Můžete jet na horské dráze")
#     age = int(input("Zadejte váš věk: "))
#     if age < 12:
#         price = 50
#         print("Cena za dítě je 50 Kč")
#     elif age < 18 :
#         price = 100
#         print("Cena za studenta je 100 Kč")
#     else:
#         price = 150
#         print("Cena za dospělého je 150 Kč")

#     photo = input("Chcete během jízdy na dráze pořídit fotky? Odpovězte Ano nebo Ne\n")

#     if photo == "Ano":
#         price = price + 40

#         print(f"Vaše cena celková cena je {price} Kč")


# else:
#     print("Nemůžete jet na horské dráze")


print ("Vítejte v apliakci na objednání pizzy")
size = str(input("Jakou velikost pizzy chcete? S, M nebo L?. "))
pizza = 0
chees = 0
feferony = 15

if size == "S":
     pizza = 100
     chees = 20
     print(f"Objednal jste si malou pizzu, cena je {pizza}")
     plus_chees = input("Chcete na pizzu navíc sýr ? Odpovězte Ano nebo Ne\n")
     if plus_chees == "Ano":
         pizza = pizza + chees
         plus_feferony = input("Chcete na pizzu navíc ještě feferonky? Odpovězte Ano nebo Ne\n")
         if plus_feferony == "Ano":
             pizza = pizza + feferony
             print (f"Celková cena je {pizza}")
         else:
             print(f"Celková cena je {pizza}")
     else:
         plus_feferony = input("Chcete na pizzu navíc ještě feferonky? Odpovězte Ano nebo Ne\n")
         if plus_feferony == "Ano":
             pizza = pizza + feferony
             print(f"Celková cena pouze s feferonky je {pizza}")
        


elif size == "M":
     pizza = 150
     chees = 30
     print(f"Objednal jste si střední pizzu, cena je {pizza}")
     plus_chees = input("Chcete na pizzu navíc sýr ? Odpovězte Ano nebo Ne\n")
     if plus_chees == "Ano":
         pizza = pizza + chees
         plus_feferony = input("Chcete na pizzu navíc ještě feferonky? Odpovězte Ano nebo Ne\n")
         if plus_feferony == "Ano":
             pizza = pizza + feferony
             print (f"Celková cena je {pizza}")
         else:
             print(f"Celková cena je {pizza}")
     else:
         plus_feferony = input("Chcete na pizzu navíc ještě feferonky? Odpovězte Ano nebo Ne\n")
         if plus_feferony == "Ano":
             pizza = pizza + feferony
             print(f"Celková cena pouze s feferonky je {pizza}")


else:
     pizza = 200
     chees = 30
     print (f"Objednal jste si velkou pizzu, cena je {pizza}")
     plus_chees = input("Chcete na pizzu navíc sýr ? Odpovězte Ano nebo Ne\n")
     if plus_chees == "Ano":
         pizza = pizza + chees
         plus_feferony = input("Chcete na pizzu navíc ještě feferonky? Odpovězte Ano nebo Ne\n")
         if plus_feferony == "Ano":
             pizza = pizza + feferony
             print (f"Celková cena je {pizza}")
         else:
             print(f"Celková cena je {pizza}")
     else:
         plus_feferony = input("Chcete na pizzu navíc ještě feferonky? Odpovězte Ano nebo Ne\n")
         if plus_feferony == "Ano":
             pizza = pizza + feferony
             print(f"Celková cena pouze s feferonky je {pizza}")









