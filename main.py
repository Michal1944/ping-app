#importowanie modułów
from tkinter import *
from pythonping import ping

#definicja funkcji

def get_ping():
 domain = inputDomena.get()
 count = int(inputCount.get())
 time = int(inputTime.get())

 try:
    result = ping(domain, verbose=True, count=count, timeout=time)
    res.set(result)
    message.set('')
 except:
    res.set('')
    message.set("Podano złą nazwę domeny!")

# obiekt tkinter
# ustawienie koloru dla tła (jasny szary)
master = Tk(className='Obliczanie pingu')
master.configure(bg='light grey')

#zdefiniowanie zmiennych w klasie tkinter
res = StringVar()
message = StringVar()

#tworzenie label dla każdej informacji
Label(master, text="Enter URL or IP :",
	bg="light grey").grid(row=0, sticky=W)
Label(master, text="Result :", bg="light grey").grid(row=3, sticky=W)

#tworzenie label dla zmiennej klasy
#nazwa widgetu Entry

#wynik
Label(master, text="", textvariable=res, bg="light grey").grid(
	row=3, column=1, sticky=W)

#ilość wyników
Label(master, text="Ilość wyników:",
	bg="light grey").grid(row=1, sticky=W)

#czas oczekiwania na wynik
Label(master, text="Czas oczekiwania:",
	bg="light grey").grid(row=2, sticky=W)

#wiadomość w przypadku wystąpienia błędu
Label(master, text="", textvariable=message, bg="light grey", foreground="red").grid(
	row=3, column=1, sticky=W)

#widgety do wprowadzenia danych
inputDomena = Entry(master)
inputDomena.grid(row=0, column=1,sticky=W)

inputCount = Spinbox(master, from_ = 1, to = 5, width=3)
inputCount.grid(row=1, column=1, sticky=W)

inputTime = Spinbox(master, from_ = 1, to = 20, width=3)
inputTime.grid(row=2, column=1, sticky=W)

#tworzenie przycisku przez użycie Button
#przycisk wywołuje funkcję get_ping
b = Button(master, text="Show", command=get_ping)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()









