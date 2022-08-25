import json

FILE_PATH = 'data.json'

def listing():
    with open(FILE_PATH)as file:
        return json.load(file)

def retrieve():
    data = listing()
    id = int(input('Enter ID product:'))
    product = list(filter(lambda x: x['id'] == id, data)) 
    if product:
        return product[0]
    else:
        return 'No such product!'


# def get_id():
#     with open('text.txt')as file:
#         id = int(input('Enter ID:'))
#         id += 1
#     with open('text.txt', 'w')as file:
#         file.write(str(id))
id = 0
def create_product(): 
    global id
    id += 1
    data = listing()
    product = {
        'id': id,
        'marka': input('Enter mark:'),
        'model': input('Enter model:'),
        'years': int(input('Enter years:')),
        'price': float(input('Enter price:'))
    }
    
    data.append(product)
    with open(FILE_PATH, 'w')as file:
        json.dump(data, file)
        return 'CREATED'
    
    
def update_product():
    data = listing()
    flag = False
    id = int(input('Enter ID producta to change: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return 'No such product!'
    index_ = data.index(product[0])

    choice = input('Что хотите изменить?: 1 - marka, 2 - model, 3 - years, 4 - price')
    if choice == '1':
        data[index_]['marka'] = input('Enter new mark: ')
        flag = True
    elif choice == '2':
        data[index_]['model'] = input('Enter new model:')
        flag = True
    elif choice == '3':
        data[index_]['years'] = int(input('Enter new years: '))
        flag = True
    elif choice == '4':
        data[index_]['years'] = float(input('Enter new price: '))
        flag = True
    else:
        print('No such pole!')

    with open(FILE_PATH, 'w')as file:
        json.dump(file, data)
    if flag:
        return 'UPDATE'
    else:
        return 'NO CHANGES'


def delete_product():
    data = listing()
    id = int(input('Enter id producta: '))
    delete = list(filter(lambda x: x['id'] == id, data))
    if not delete:
        return 'No such product!'
    index_ = data.index(delete[0])
    data.pop(index_)
    json.dump(data, FILE_PATH, 'w')
    return 'DELETE'









   
    


