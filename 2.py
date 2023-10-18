with open("employees.txt", "w") as file:
    file.write("Иванов 23543.12\n")
    file.write("Колючкин 13749.32\n")
    file.write("Пупкин 20000.00\n")
    file.write("Тумбочкин 19500.50\n")
    file.write("Кружечкин 21000.75\n")
    file.write("Ковришкин 18000.25\n")
    file.write("Киселев 22000.45\n")
    file.write("Проворов 19500.80\n")
    file.write("Варюшкин 19000.00\n")
    file.write("Тапочкин 20500.15\n")

total_income = 0.0
count = 0
low_income_employees = []

with open("employees.txt", "r") as file:
    for line in file:
        parts = line.split()
        if len(parts) == 2:
            surname = parts[0]
            income = float(parts[1])
            total_income += income
            count += 1
            if income < 20000:
                low_income_employees.append(surname) #добавление в список

print("Сотрудники с окладом менее 20 тысяч:")
for employee in low_income_employees:
    print(employee)

average_income = total_income / count
print("Средний доход сотрудников:", average_income)
