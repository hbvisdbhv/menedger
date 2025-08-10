import setup
from timetab.models import*



def menu():
    print('1.Додати придмет. 2.Додати вчителя. 3.Додати клас. 4.Додати учня. 5.Додати розклад. 6.додати оцінку. 0.Вийти.')
    return num
def subject():
    name = input('Введіть опис предмету:')
    description = input('Ввудіть опис предмету:')
    Subject.objects.create(name=name, description=description)

def teacher_add():
    first_name = input('Введфть ім*я вчителя:')
    last_name = input('Введіть прізвище вчителя:')
    id = int(input('Введіть ID вчителя'))

    sub = Subject.objects.get(id=id)
    print(Subject.objects.all())
    if sub:
        Teacher.objects.create(first_name=first_name, last_name=last_name, subject=sub)
    else:
        print('Такого ID немає')

while True:
    num = menu()
    if num == 0:
        break
    elif num == 1:
        subject()
    elif num == 2:
        teacher_add()