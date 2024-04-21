def total_salary(path):
    total = 0
    developers = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.split(',')
                total += int(salary) 
                developers += 1 
                   
        if developers:
            average = total / developers 
            return total, average 
         
    except FileNotFoundError: 
        print(f'File: {path} not found') 
        return None, None
    except Exception as e:
        print(f'Error:{e}')
        return None, None
    
total, average =  total_salary('salary.txt') 
if total is not None and average is not None:
    print(f"The total amount of salary: {total} \nAverage salary: {average}") 