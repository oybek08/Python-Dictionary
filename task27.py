def phonebook_menu(phonebook):
    while True:
        print("\n1. Qoshish\n2. Korish\n3. Qidirish\n4. Chiqish")
        choice = input("Tanlov: ")
        if choice == "1":
            name = input("Ism: ")
            number = input("Telefon: ")
            phonebook[name] = number
        elif choice == "2":
            for name, number in phonebook.items():
                print(f"{name}: {number}")
        elif choice == "3":
            name = input("Qidirilayotgan ism: ")
            print(phonebook.get(name, "Topilmadi"))
        elif choice == "4":
            break