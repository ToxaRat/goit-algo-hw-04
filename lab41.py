from pathlib import Path

def total_salary(path):
    file_path = Path(path)
    if file_path.exists() == False:
        print(f'Файл {file_path} не існує')
        return 0, 0
    # читаем зарплату
    with open(path, "r", encoding="UTF-8") as fh:
        lines_salary = [el.strip() for el in fh.readlines()]
    
    SumSalary = 0
    for el in lines_salary:
        sl = el.split(",") # ПІБ, ЗП
        SumSalary += int(sl[1]) # загальну суму заробітної плати

    AveSalary = int(SumSalary / len(lines_salary)) # середню суму заробітної плати
    return {SumSalary, AveSalary}
        
SumSalary, AveSalary = total_salary("TXTFiles/salary.txt")
print(f"Загальгна: {SumSalary}, Середня: {AveSalary}")
