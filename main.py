from Classes import *
from tkinter import *
import random
import csv

root = Tk()
root.title('НЯ НА КИТАЙСКОМ')
root.geometry('555x555')

def save_inp():
	with open('data.csv', 'w', encoding='utf-8') as f:
		print(inp.get(),tem.get(), file=f)
	


inp = StringVar()
tem =StringVar()

text = Label(root, text='Расстояние путешествия (км)->')
text.grid(column=0, row=0)
text_t = Entry(textvariable=inp)
text_t.grid(column=1, row=0)
text_btn = Button(text='save', command=save_inp)
text_btn.grid(column=2, row=2)

text1 = Label(root,text ='Время, в которое необходимо уложиться (дни)->')
text1.grid(column=0, row = 1)
text1_t = Entry(textvariable=tem)
text1_t.grid(column=1, row=1)




with open('data.csv', 'r', encoding='utf-8') as file:  
  data = file.read()
  

#Расстояние и время
range = int(input('Расстояние путешествия (км) '))
req_time = int(input('Время, в которое необходимо уложиться (дни) '))

#Изначальные условия
time = 0  #часы
speed = 0

#Сезон
season = Season(str(input('Выберите сезон(winter, summer, autumn, spring)')))

cycle = Cycle(season)  #Цикла дня и ночи(часы)

speed += season.speed

#Локация
location = Location(
 str(input('Выберите локацию(forest, town, plains, mountains) ')))
speed += location.speed

#Инвентарь
#masinv = MasNesInv()
#speed += self.finalmass

#Путешественники
travelers = Puteshestvenniki(int(input('Количество путешественников ')))
speed += travelers.speed
#Характеристика Путешественников
charact = ChTravelers(int())
for i in range(ctravelers):
			self.chtra.append(random.randint(65,100))

#Привалы
halt = Halt(season, location)
time += halt.time * (req_time - 1)  # Итоговое время, затраченное на привалы
time += cycle.ncycle * (
 req_time)  # Итоговое время с учётом сна. Учитывается каждый день

#итоговое время часы и дни
time += range / speed
time_days = int(time / 24)

#ДОБАВИТЬ ИСПРАВЛЕНИЕ ВЫВОДА ИТОГОВОГО ВРЕМЕНИ. ТО ЕСТЬ ДД/ЧЧ
with open('Names.csv','r', encoding='utf-8')as file:
	file_r = csv.reader(file)
	l_file = list(file_r)
	for i in range(0, ctravelers):
		print(f'{l_file[i][0]}-{charact.chtra[i]}')
    
print('Скорость: ' + str(speed) + '\n Время, затраченное на поход: (ч.): ' +
      str(int(time)) + '\n (Дни): ' + str(time_days) + '\n Светло ' +
      str(cycle.dcycle) + '\n ч. в день, темно ' + str(cycle.ncycle) +
      '\n ч. в день')





root.mainloop()
