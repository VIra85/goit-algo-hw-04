from pathlib import Path

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": int(cat_data[2])
                }
                cats_list.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено")
    
    return cats_list

cats_info = get_cats_info("second_hw4/cats_file.txt")
print(cats_info)
