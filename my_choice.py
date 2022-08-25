from hakaton import *

while  True:
    chooice = int(input(f'Выберите действие: 1 - LISTING, 2 - RETRIEVE, 3 - CREATE, 4 - UPDATE, 5 - DELETE: '))

    
    if chooice == 1:
        print(listing())
    elif chooice == 2:
        print(retrieve())
    elif chooice == 3:
        print(create_product())
    elif chooice == 4:
        print(update_product())
    elif chooice == 5:
        print(delete_product())
    else:
        'Not find'
        
            












