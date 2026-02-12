def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats = []
            for line in file:
                line = line.strip()
                if line:
                    cat_id, name, age = line.split(",")
                    cats.append({"id": cat_id, "name": name, "age": age})
            return cats
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return []


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
