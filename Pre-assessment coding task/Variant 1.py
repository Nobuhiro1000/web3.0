def multiplication_table():
    for i in range(1, 13):
        for j in range(1, 13):
            print(f"{i * j:3}", end=" ")
        print()

multiplication_table()
