

avrage_age_years = 90

while True:
    try:
        user_age = int(input("Zadejte, kolik je Vám let: "))
        left_age_years = avrage_age_years - user_age
        left_age_month = left_age_years * 12
        left_age_weeks = left_age_years * (365 / 7)
        left_age_days = left_age_years * 365
        print(f"Podle průměrného věku Vám zbývá {left_age_years} let což je {left_age_month} měsíců, což je {round(left_age_weeks)} týdnů, což je {left_age_days} dnů.")
        break


    except ValueError:
        print("Nezadal jste platný věk!")



