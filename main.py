with open("F1.txt", "w") as f1:
    while True:
        data = input("Введите данные (или оставьте строку пустой для завершения ввода): ")
        if data == "":
            break
        f1.write(data + "\n")

# Копирование четных строк в файл F2
with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    lines = f1.readlines()
    even_lines = [line for i, line in enumerate(lines) if (i + 1) % 2 == 0]
    f2.writelines(even_lines)

import os

f1_size = os.path.getsize("F1.txt")
f2_size = os.path.getsize("F2.txt")

print(f"Размер файла F1: {f1_size} байт")
print(f"Размер файла F2: {f2_size} байт")
