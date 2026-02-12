def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            total = 0
            count = 0
            for line in lines:
                line = line.strip()
                if line:
                    name, salary = line.split(",")
                    total += int(salary)
                    count += 1
            if count == 0:
                return 0, 0
            average = total / count
            return total, average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None


total, average = total_salary("salary_file.txt")
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
