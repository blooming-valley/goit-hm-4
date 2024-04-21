def get_cats_info(path):
    cats_list = []
    try:   
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:    
                id, name, age = line.split(',')
                
                cats_info = {
                    'id' : id,
                    'name' : name,
                    'age' : age,
                    }
                
                cats_list.append(cats_info)
    
    except FileNotFoundError:
        print(f'File {path} not found')
        return None
    
    except Exception as e:
        print(f' Error {e}')
        return None
    
    if not cats_list:
        print(f'File "{path}" is empty')
        return None

    return cats_list

general_info = get_cats_info('pets_info.txt')
if general_info is not None:
    print(general_info) 
    

            
            