import os

direct = os.getcwd() + '/'

def bust_script(direct):

  if (os.listdir(direct)):
    for obj in os.listdir(direct):
      strings = int(0)

      if (os.path.isdir(direct + '/' + obj) == True):
        newdir = direct + '/' + obj + '/'
        bust_script(newdir)
      elif (os.path.isfile(direct + obj) == True):
        try:
          with open(obj, 'r', encoding = 'utf-8') as file:
            for line in file:
              strings += 1
        except:
          pass

        print('Имя:', obj, '\nКоличество строк:', strings)
        print('-------------------')
  else:
    print('Директория:',direct,'\nСтатус: Пуста')
    print('-------------------')

bust_script(direct)
