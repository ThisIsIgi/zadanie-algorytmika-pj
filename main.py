import random
import time

#-----------------------------------------------------------------------------------------------------------------------
#                                               LISTA JEDNOKIERUNKOWA
#-----------------------------------------------------------------------------------------------------------------------

# Lista jednokierunkowa

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def appendl(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def remove(self, value):
        if self.head is None:
            print("Lista jest pusta")
            return

        current = self.head
        if current.data == value:
            self.head = current.next
            return

        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            else:
                print("Wartość", value, "nie została znaleziona w liście")

            current = current.next

    def pop(self, index=None, value=None):
        if not self.head:
            print("tablica jest pusta")
            return None

        if value is not None:
            current = self.head
            previous = None
            while current:
                if current.data == value:
                    if previous:
                        previous.next = current.next
                    else:
                        self.head = current.next
                    return current.data
                previous = current
                current = current.next
            print("Wartość", value, "nie została znaleziona")
            return None

        if index is None:
            if not self.head.next:
                data = self.head.data
                self.head = None
                return data

            current = self.head
            while current.next.next:
                current = current.next
            data = current.next.data
            current.next = None
            return data

        elif index == 0:
            data = self.head.data
            self.head = self.head.next
            return data

        else:
            current = self.head
            for _ in range(index - 1):
                if current.next:
                    current = current.next
                else:
                    print("Indeks poza zakresem")
                    return None
            if not current.next:
                print("Indeks poza zakresem")
                return None
            data = current.next.data
            current.next = current.next.next
            return data



    def show_list(self):
        current = self.head
        print("Lista:")
        while current:
            print(current.data, end="; ")
            current = current.next
        print(" ")

    def src(self, value):
        current = self.head
        while current:
            if current.data == value:
                print("Liczba znajduje się w liście")
                return
            current = current.next
        print("Liczba nie znajduje się w liście")


#-----------------------------------------------------------------------------------------------------------------------
#                                               OPERACJE NA TABLICY I LISCIE
#-----------------------------------------------------------------------------------------------------------------------

# Dodawanie elementów

def add_rand(tab, lista, amount):
    start = time.time()
    for i in range(amount):
        value = random.randint(1, 9999)
        tab.append(value)
        lista.appendl(value)
    end = time.time()
    print("Czas wykonania operacji: ", round((end - start), 7), " sekund")


def add_specific_element(tab, list, index, value):
    start = time.time()
    current = list.head
    current_index = 0
    while current and current_index < index - 1:
        current = current.next
        current_index += 1
    if current:
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
    tab.insert(index, value)

    end = time.time()
    print("Czas wykonania operacji: ", round(end - start, 7), " sekund")


# Usuwanie elementów

def del_a_thing_from_tab(tab, list, value):
    start = time.time()
    try:
        tab.pop(value)
    except ValueError:
        print("Wartość", value, "nie została znaleziona w tablicy")

    list.remove(value)

    end = time.time()
    print("Czas wykonania operacji: ", round(end - start, 7), " sekund")



def del_fst_ele(tab, list):
    start = time.time()
    if not tab:
        print("Tablica jest pusta")
    else:
        tab.pop(0)

    if list.head:
        list.head = list.head.next
    else:
        print("Lista jest pusta")

    end = time.time()
    print("Czas wykonania operacji: ", round(end - start, 7), " sekund")


def del_lst_ele(tab, list):
    start = time.time()
    if not tab:
        print("Tablica jest pusta")
    else:
        tab.pop()

    current = list.head
    if not current:
        return
    if not current.next:
        list.head = None
        return
    while current.next.next:
        current = current.next
    current.next = None
    end = time.time()
    print("Czas wykonania operacji: ", round(end - start, 7), " sekund")


def del_rand(tab, list):
    start = time.time()
    if not tab:
        print("Tablica jest pusta")
        return

    try:
        random_index = random.randint(0, len(tab) - 1)
        tab.pop(random_index)
    except IndexError:
        print("Nie można usunąć elementu z pustej tablicy")

    current = list.head
    if not current:
        return
    if not current.next:
        list.head = None
        return
    previous = None
    length = 0
    while current:
        current = current.next
        length += 1
    random_index = random.randint(1, length)
    current = list.head
    index = 1
    while current and index < random_index:
        previous = current
        current = current.next
        index += 1
    if not previous:
        list.head = current.next
    else:
        previous.next = current.next
    end = time.time()
    print("Czas wykonania operacji: ", round(end - start, 7), " sekund")


# Szukanie elementu

def src(tab, value):
    start = time.time()
    if value in tab:
        print("Liczba znajduje się w tablicy")
    else:
        print("Brak takiej liczby")
    end = time.time()
    print("Czas wykonania operacji: ", round(end - start, 7), " sekund")


# Wczytywanie danych z pliku

def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = [int(num) for line in file for num in line.strip().split(',') if num]
        return data
    except FileNotFoundError:
        print("Plik nie istnieje")
        return []

#-----------------------------------------------------------------------------------------------------------------------
#                                                           TESTY I MENU
#-----------------------------------------------------------------------------------------------------------------------

mytab = []
mylist = List()

print("----------------------------------------------------------------------------------------------------------")
print("Badanie efektywności operacji dodawania, usuwania oraz wyszukiwania elementów w różnych strukturach danych")
print("----------------------------------------------------------------------------------------------------------")
print("Jesli checesz wczytac z pliku wpisz jeden jesli chcesz wygenerowac wpisz 2")
zpliku = int(input("- "))
if(zpliku==1):
    filename = input("wpisz nazwe pliku: ")
    data = load_data_from_file(filename)
    if data:
        mytab.extend(data)
        for item in data:
            mylist.appendl(item)

    print(mytab)
    print("Wybierz numer operacji: ")
    print("1. Dodaj liczbę")
    print("2. Usuń specyficzną liczbę")
    print("3. Usuń pierwszą liczbę")
    print("4. Usuń ostatnią liczbę")
    print("5. Usuń losową liczbę")
    print("6. Wyszukaj liczbę")
    print("7. Wykonaj wszystkie powyższe operacje")
    menu_number = int(input("Wybierz numer: "))
    if menu_number == 1:
        index = int(input("Podaj indeks: "))
        number = int(input("Podaj liczbę: "))
        add_specific_element(mytab, mylist, index, number)
        print("Twoja tablica: ", mytab)
        mylist.show_list()
    elif menu_number == 2:
        print("Twoja tablica: ", mytab)
        mylist.show_list()
        number = int(input("Podaj liczbę: "))
        del_a_thing_from_tab(mytab, mylist, number)
        print("Twoja tablica:")
        print(mytab)
        mylist.show_list()
    elif menu_number == 3:
        del_fst_ele(mytab, mylist)
        print("Twoja tablica: ")
        print(mytab)
        mylist.show_list()

    elif menu_number == 4:
        del_lst_ele(mytab, mylist)
        print("Twoja tablica: ")
        print(mytab)
        mylist.show_list()

    elif menu_number == 5:
        del_rand(mytab, mylist)
        print("Twoja tablica: ")
        print(mytab)
        mylist.show_list()
    elif menu_number == 6:
        number = int(input("wpisz liczbe: "))
        src(mytab, number)
        mylist.src(number)
    elif menu_number == 7:
        start = time.time()
        how_many = int(input("podaj ilosc powtorzen testu: "))
        index = int(input("wpisz indeks: "))
        number = int(input("wpisz liczbe: "))
        for i in range(how_many):
            print(mytab)
            print(mylist)
            index = 5
            add_specific_element(mytab, mylist, index, number)
            del_a_thing_from_tab(mytab, mylist, number)
            del_fst_ele(mytab, mylist)
            del_lst_ele(mytab, mylist)
            del_rand(mytab, mylist)
            src(mytab, number)
            mylist.src(number)

        end = time.time()
        print("Czas wykonywania wszytkich operacji: ", round(end - start, 4), " sekundy")

else:
    print("Ile liczb ma znajdować się w liście i tablicy?")
    how_many_numbers = int(input("- "))
    add_rand(mytab,mylist,how_many_numbers)
    print("Wybierz numer operacji: ")
    print("1. Dodaj liczbę")
    print("2. Usuń specyficzną liczbę")
    print("3. Usuń pierwszą liczbę")
    print("4. Usuń ostatnią liczbę")
    print("5. Usuń losową liczbę")
    print("6. Wyszukaj liczbę")
    print("7. Wykonaj wszystkie powyższe operacje")
    menu_number = int(input("Wybierz numer: "))
    if menu_number == 1:
        index = int(input("Podaj indeks: "))
        number = int(input("Podaj liczbę: "))
        add_specific_element(mytab, mylist, index, number)
        print("Twoja tablica: ", mytab)
        mylist.show_list()
    elif menu_number == 2:
        print("Twoja tablica: ", mytab)
        mylist.show_list()
        number = int(input("Podaj liczbę: "))
        del_a_thing_from_tab(mytab, mylist, number)
        print("Twoja tablica:")
        print(mytab)
        mylist.show_list()
    elif menu_number == 3:
        del_fst_ele(mytab, mylist)
        print("Twoja tablica: ")
        print(mytab)
        mylist.show_list()

    elif menu_number == 4:
        del_lst_ele(mytab,mylist)
        print("Twoja tablica: ")
        print(mytab)
        mylist.show_list()

    elif menu_number == 5:
        del_rand(mytab, mylist)
        print("Twoja tablica: ")
        print(mytab)
        mylist.show_list()
    elif menu_number == 6:
        number = int(input("wpisz liczbe: "))
        src(mytab,number)
        mylist.src(number)
    elif menu_number == 7:
        start = time.time()
        how_many = int(input("podaj ilosc powtorzen testu: "))
        index = int(input("wpisz indeks: "))
        number = int(input("wpisz liczbe: "))
        for i in range(how_many):
            mytab = []
            mylist = List()
            add_rand(mytab, mylist, how_many_numbers)
            print(mytab)
            print(mylist)
            index = 5
            add_specific_element(mytab, mylist, index, number)
            del_a_thing_from_tab(mytab, mylist, number)
            del_fst_ele(mytab, mylist)
            del_lst_ele(mytab, mylist)
            del_rand(mytab, mylist)
            src(mytab, number)
            mylist.src(number)

        end = time.time()
        print("Czas wykonywania wszytkich operacji: ", round(end - start, 4), " sekundy")









