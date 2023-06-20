s = input("Введите строку до 1000 символов:")
if len(s) > 1000:
    print("До 1000!")
else:
    while "  " in s:
        s = s.replace("  ", " ")
    print(s)
