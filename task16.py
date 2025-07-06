person = {"name": "Ali", "age": 25, "city": "Tashkent"}
key = input("Kalitni kiriting: ")
if key in person:
    del person[key]
    print(f"{key} o`chirildi.")
else:
    print("Bunday kalit yo`q.")