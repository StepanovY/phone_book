import random

FILE_CSV = 'Phonebook.csv'
list_organization = ['Один', 'Рога и копыта', 'Телепузики', 'Автопрокат', 'МБСОШ39']


def create_phonebook():
    """ Функция автоматического создания записей телефонного справочника.
    """
    with open(FILE_CSV, 'w', encoding='utf-8') as file:
        file.write(f'Last_name;First_name;Middle_name;Organization;Work_phone;Home_phone\n')

    for i in range(100):
        organization = random.choice(list_organization)
        phone = random.randrange(80000000001, 89999999999)
        with open(FILE_CSV, 'a', encoding='utf-8') as file:
            file.write(f'Last_name{i};First_name{i};Middle_name{i};{organization};{phone};{phone}\n')
