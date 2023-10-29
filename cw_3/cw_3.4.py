while True:
    user_input = input("Podaj liczbę lub 'stop' aby zakończyć ")

    if user_input == 'stop':
        break

    if user_input.isnumeric():
        x = float(user_input)
        print(f"{x}^3 = {x ** 3}")
    else:
        print("Spróbuj ponownie")
