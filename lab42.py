from pathlib import Path

def get_cats_info(path):
    listCat = list()
    file_path = Path(path)
    if file_path.exists() == False:
        print(f'Файл {file_path} не існує')
        return listCat
    
    # читаем котов
    with open(path, "r", encoding="UTF-8") as fh:
        lines_salary = [el.strip() for el in fh.readlines()]
    # розбиваемо
    for el in lines_salary:
        sl = el.split(",") # "id", "name", "age"
        listCat.append({"id":sl[0], "name":sl[1], "age":sl[2]})
    return listCat

       
cats_info = get_cats_info("TXTFiles/cats.txt")
print(cats_info)