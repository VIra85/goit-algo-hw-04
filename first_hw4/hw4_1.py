from pathlib import Path

def total_salary(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            total = 0
            count = 0
            for line in lines:
                name, salary = line.strip().split(',')
                salary = float(salary)
                total += salary
                count += 1
            if count == 0:
                return 0, 0
            else:
                average = total / count
                return total, average
    except FileNotFoundError:
        return "Файл не знайдено"

file_path = "first_hw4/salary_file.txt"
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {'%d'%total}, Середня заробітна плата: {'%d'%average}")



