from tkinter import *

import model as m

#Создаём основное окно программы
window = Tk()
window.title('Airports')
window.geometry('1000x800')

main_frame = Frame(window)
main_frame.pack()

top_frame = Frame(main_frame)
top_frame.pack(side=TOP)

bottom_frame = Frame(main_frame)
bottom_frame.pack(side=BOTTOM)


#LATITUDE
Label(top_frame, text="LATITUDE:").grid(row=0, column=0, sticky=W, pady=10, padx=10)

min_lat = Entry(top_frame, width=20)
min_lat.grid(row=0, column=1)
min_lat.delete(0, END)
min_lat.insert(0, '50.0')

Label(top_frame, text="-").grid(row=0, column=2, sticky=W, pady=10, padx=10)

max_lat = Entry(top_frame, width=20)
max_lat.grid(row=0, column=3)
max_lat.delete(0, END)
max_lat.insert(0, '70.0')

#LONGITUDE
Label(top_frame, text="LONGITUDE:").grid(row=2, column=0, sticky=W, pady=10, padx=10)

min_lon = Entry(top_frame, width=20)
min_lon.grid(row=2, column=1)
min_lon.delete(0, END)
min_lon.insert(0, '50.0')

Label(top_frame, text="-").grid(row=2, column=2, sticky=W, pady=10, padx=10)

max_lon = Entry(top_frame, width=20)
max_lon.grid(row=2, column=3)
max_lon.delete(0, END)
max_lon.insert(0, '70.0')

#DEPARTURE AIRPORT
Label(top_frame, text="DEPARTURE AIRPORT:").grid(row=4, column=0, sticky=W, pady=10, padx=10)

departure = Entry(top_frame, width=50)
departure.grid(row=4, column=1, columnspan=3, sticky=EW)
departure.delete(0, END)
departure.insert(0, '')

#ARRIVAL AIRPORT
Label(top_frame, text="ARRIVAL AIRPORT:").grid(row=6, column=0, sticky=W, pady=10, padx=10)

arrival = Entry(top_frame)
arrival.grid(row=6, column=1, columnspan=3, sticky=EW)
arrival.delete(0, END)
arrival.insert(0, '')


#BUTTONS

btn1 = Button(top_frame, text='Find airports', command=m.clicked1)
btn1.grid(column=4, row=0, rowspan=3, padx=10, pady=10, sticky=NSEW)

btn2 = Button(top_frame, text='Find flights', command=m.clicked2)
btn2.grid(column=4, row=4, rowspan=3, padx=10, pady=10, sticky=NSEW)

