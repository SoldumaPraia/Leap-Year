# Check to see if a given year is a leap year or not
# Assumes Gregorian calendar leap year rules for ALL years
while True:  # para repetir depois de aparecer erro ou entregar resultado
    print("<<<<<<<<<<<<<<<<<Leap Year Finder>>>>>>>>>>>>>>>>>>>>>\n\n")
    try:  # para checkar se usuário entrar um valor inválido
        n = int(input("Enter a year to be evaluated: "))
    except ValueError:  # tipo de error que acontece se qualquer coisa além de um int for entrado
        print("\n\nInvalid entry. Please enter a positive whole number.\n")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        x = input("press <Enter> to try again or 'x' to exit\t")  # opção de parar ou repetir
        if x == 'x':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Thank you for using this program. Have a nice day!")
            raise SystemExit
        else:
            continue

    # Casos Especiais
    if n == 0:  # não existe o ano "0"
        print("It is commonly accepted that the year \"0\" was never used\n")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
        x = input("Press <Enter> to try again or 'x' to exit\t")  # opção de parar ou repetir
        if x == 'x':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Thank you for using this program. Have a nice day!")
            raise SystemExit
    if n < 0:
        print("Invalid entry. Please enter a positive whole number.\n")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
        x = input("Press <Enter> to try again or 'x' to exit\t")  # opção de parar ou repetir
        if x == 'x':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Thank you for using this program. Have a nice day!")
            raise SystemExit

            # Cálculo
    if n % 4 != 0:
        print("{} is a common year".format(n))
    elif n % 100 == 0 and n % 400 != 0:
        print("{} is a common year".format(n))
    else:
        print("{} is a leap year".format(n))

    if n < 1582: print(
        "(propletic Gregorian Calendar)")  # Anota que o Calendário Gregoriano realmente não existia antes de 1582

    # depois de qualquer resultado vai vir aqui
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")

    x = input("Press <Enter> to try again or 'x' to exit\t")  # opção de parar ou repetir
    if x == 'x':
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Thank you for using this program. Have a nice day!\n")
        raise SystemExit
        # Edited by github.com/MrS4w ;)
