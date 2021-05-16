# ping-app
# Michał Czubat

Program sprawdzający ping (python)

Na samym początku należy zainstalować moduł pythonping do systemu.

pip install pythonping

PythonPing to prosty sposób na pingowanie w Pythonie. Dzięki niemu możesz wysyłać sondy ICMP do zdalnych urządzeń, tak jak robisz to z terminala. PythonPing jest modułowy, dzięki czemu można go uruchomić w skrypcie jako samodzielną funkcję lub zintegrować jego komponenty w pełnoprawnej aplikacji.
Najprostsze użycie PythonPing jest w skrypcie. Możesz użyć funkcji ping do pingowania celu. Jeśli chcesz natychmiast zobaczyć wyjście, emulując to, co dzieje się na terminalu, użyj flagi verbose

Niezależnie od trybu pełnego, funkcja ping zawsze zwróci obiekt ResponseList. Jest to specjalny iterowalny obiekt, zawierający listę elementów Response. W każdej odpowiedzi możesz znaleźć otrzymany pakiet i niektóre metainformacje, takie jak czas potrzebny na otrzymanie odpowiedzi i wszelkie komunikaty o błędach.

Możesz także dostroić swój ping, używając niektórych z jego dodatkowych parametrów:

 - size to liczba całkowita, która pozwala określić żądany rozmiar ładunku ICMP
 - timeout to liczba sekund, przez które chcesz czekać na odpowiedź, zanim założymy, że cel jest nieosiągalny
 - payload pozwala na użycie określonego ładunku (bajtów)
 - count określająca pozwala określić, ile pakietów ICMP ma zostać wysłanych
 - sweep_start i sweep_end pozwalają na wykonanie testu ping, zaczynając od rozmiaru ładunku zdefiniowanego w sweep_start i rosnącego do rozmiaru zdefiniowanego w sweep_end. Tutaj powtarzamy podany przez Ciebie ładunek, aby dopasować go do żądanego rozmiaru, lub generujemy losowy, jeśli nie podano ładunku. Zauważ, że jeśli zdefiniowałeś rozmiar, te dwa pola zostaną zignorowane
 - df to flaga, która, jeśli zostanie ustawiona na True, włączy flagę Don't Fragment w nagłówku IP
 - verbose włącza tryb gadatliwy, drukuje dane wyjściowe do strumienia 
 - out jest docelowym strumieniem trybu pełnego. Jeśli włączysz tryb szczegółowy i nie podasz out, szczegółowe dane wyjściowe zostaną wysłane do strumienia sys.stdout.
 - match to flaga, która, jeśli jest ustawiona na True, umożliwi dopasowanie ładunku między żądaniem ping a odpowiedzią (domyślne zachowanie jest zgodne z tym z systemu Windows, który liczy pomyślną odpowiedź tylko przez pasujący identyfikator pakietu
 
 #################################################################################################
 Python GUI – tkinter
 
 Python oferuje wiele opcji tworzenia GUI (Graphical User Interface). Spośród wszystkich metod graficznego interfejsu użytkownika tkinter jest najczęściej używaną metodą. Jest to standardowy interfejs Pythona do zestawu narzędzi Tk GUI dostarczanego z Pythonem. Python z tkinter to najszybszy i najłatwiejszy sposób tworzenia aplikacji GUI
 
Aby utworzyć aplikację tkinter:

1.	Zaimportuj moduł tkinter
2.	Utwórz okno główne (kontener)
3.	Dodaj dowolną liczbę widżetów do głównego okna
4.	Zastosuj wyzwalacz zdarzenia w widżetach

Importowanie tkinter jest takie samo, jak importowanie dowolnego innego modułu w kodzie Pythona. Zwróć uwagę, że nazwa modułu w Pythonie 2.x to „Tkinter”, aw Pythonie 3.x to „tkinter”

import tkinter

Istnieją dwie główne metody, o których użytkownik musi pamiętać podczas tworzenia aplikacji w języku Python z graficznym interfejsem użytkownika

1.	Tk (screenName = None, baseName = None, className = 'Tk', useTk = 1): Aby utworzyć okno główne, tkinter oferuje metodę 'Tk (screenName = None, baseName = None, className =' Tk ', useTk = 1) ”. Aby zmienić nazwę okna, możesz zmienić nazwę klasy na żądaną. Podstawowym kodem używanym do stworzenia głównego okna aplikacji jest:

  m=tkinter.Tk() where m is the name of the main window object

2.	mainloop():  Metoda znana pod nazwą mainloop(), która jest używana, gdy aplikacja jest gotowa do uruchomienia. mainloop () to nieskończona pętla używana do uruchamiania aplikacji
 
  import tkinter
  m = tkinter.Tk()
  '''
  widgets are added here
  '''
  m.mainloop()
 
tkinter oferuje również dostęp do geometrycznej konfiguracji widżetów, które mogą organizować widżety w oknach nadrzędnych. Istnieją głównie trzy klasy menedżerów geometrii
 
1.	pack(), metoda: organizuje widżety w bloki przed umieszczeniem ich w widgecie nadrzędnym
2.	grid(), metoda: organizuje widżety w siatkę (struktura tabelaryczna) przed umieszczeniem w widgecie nadrzędnym
3.	place() metoda: Porządkuje widżety, umieszczając je na określonych pozycjach wskazanych przez programistę

Istnieje wiele widżetów, które można umieścić w aplikacji tkinter. Poniżej opisano te które zostały użyte w projekcie

#################################################################################################

Label 

Odnosi się do pola wyświetlania, w którym można umieścić dowolny tekst lub obraz, który można zaktualizować w dowolnym momencie zgodnie z kodem. 

Ogólna składnia to

  w=Label(master, option=value)
  master is the parameter used to represent the parent window.
  
Istnieje wiele opcji służących do zmiany formatu widżetu. Liczba opcji może być przekazana jako parametry oddzielone przecinkami. Niektóre z nich są wymienione poniżej

 - bg: aby ustawić normalny kolor tła
 - comand: wywołanie funkcji
 - font: ustawienie czcionki na etykiecie przycisku
 - image: ustawienie obrazu na przycisku
 - width: aby ustawić szerokość przycisku
 - height” aby ustawić wysokość przycisku
 
Przykład:

  from tkinter import *
  root = Tk()
  w = Label(root, text="Przykładowy tekst!")
  w.pack()
  root.mainloop()
  
#################################################################################################
 
Entry
 
Służy do wprowadzania jednowierszowego tekstu od użytkownika. Do wprowadzania tekstu w wielu wierszach używany jest widżet Tekst

  w=Entry(master, option=value)

master to parametr używany do reprezentowania okna nadrzędnego. Istnieje wiele opcji służących do zmiany formatu widżetu. Liczba opcji może być przekazana jako parametry oddzielone przecinkami. Niektóre z nich są wymienione poniżej:

 - bd: aby ustawić szerokość obramowania w pikselach
 - bg: ustawienie koloru tła
 - cursor: ustawienie używanego kursora
 - command: wywołanie funkcji 
 - highlightcolor: ustawienie koloru wyświetlanego w podświetleniu fokusa
 - width: ustawienie szerokości przycisku
 - height: ustawienie wysokości przycisku

Przykład:
  
  from tkinter import *
  master = Tk()
  Label(master, text='Imie').grid(row=0)
  Label(master, text='Nazwisko'),grid(row=1)
  e1 = Entry(master)
  e2 = Entry(master)
  e1.grid(row=0,column=1)
  e2.grid(row=1,column=1)
  mainloop()
  
#################################################################################################
Button

Aby dodać przycisk w aplikacji, używany jest ten widżet. Ogólna składnia to:

  w=Button(master, option=value)
  
master to parametr używany do reprezentowania okna nadrzędnego. Istnieje wiele opcji służących do zmiany formatu przycisków. Liczba opcji może być przekazana jako parametry oddzielone przecinkami. Niektóre z nich są wymienione poniżej

 - activebackground: do ustawiania koloru tła, gdy przycisk znajduje się pod kursorem
 - activeforeground: ustawienie koloru pierwszego planu, gdy przycisk znajduje się pod kursorem
 - bg: aby ustawić normalny kolor tła
 - command: wywołanie funkcji
 - font: ustawienie czcionki na etykiecie przycisku
 - image: ustawienie obrazu na przycisku
 - width: ustawienie szerokości przycisku
 - height: ustawienie wysokości przycisku

 Przykład: 
  
  import tkinter as tk
  r = tk.Tk()
  r.title('Licznik sekund')
  button = tk.Button(r, text='Stop',width=25, command=r.destroy)
  button.pack()
  r.mainloop()

#################################################################################################
SpinBox

Jest to wpis widżetu „Wejście”. Tutaj wartość można wprowadzić, wybierając stałą wartość liczb. Ogólna składnia jest następująca:

  w = SpinBox(master, option=value)
 
Istnieje wiele opcji służących do zmiany formatu widżetu. Liczba opcji może być przekazana jako parametry oddzielone przecinkami. Niektóre z nich są wymienione poniżej.

 - highlightcolor: Aby ustawić kolor podświetlenia fokusa, gdy widżet ma być aktywny
 - insertbackground: aby ustawić tło widżetu.
 - bg: aby ustawić normalny kolor tła.
 - font: ustawienie czcionki na etykiecie przycisku.
 - image: ustawienie obrazu w widgecie.
 - width: aby ustawić szerokość widżetu.
 - height: ustawienie wysokości widżetu.

  
  
  


 
