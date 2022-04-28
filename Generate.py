import csv
import random
from def_function import def_word
import colorama
from GUI import*
import copy
ANSI_GREEN = "\u001B[34m"
ANSI_RESET = "\u001B[0m"


def color_sign(x):
    # c = colorama.Fore.WHITE if x == 0 else colorama.Fore.RED
    if x == 0:
        c = colorama.Fore.BLACK
    if x != 0:
        c = colorama.Fore.GREEN
    if x == 1:
        c = colorama.Fore.RED
    if x == 2:
        c = colorama.Fore.MAGENTA
    return f'{c}{x}'


def empty_col(tab, y, arr_size):
    for c in range(0, arr_size):
        if tab[c][y] != 0:
            return False
    return True


def empty_row_space(x, tab):
    count = 0
    for c in range(0, len(tab)):
        if (tab[c] != x) and (tab[c] != x - 1) and (tab[c] != x + 1):
            count = count + 1
    if count == len(tab):
        return True
    else:
        return False


def space_between_vert(tab, y, arr_size):
    if y == arr_size - 1:
        for c in range(0, arr_size):
            if tab[c][y - 1] != 0:
                return False
        return True
    if y == 0:
        for a in range(0, arr_size):
            if tab[a][y + 1] != 0:
                return False
    else:
        for b in range(0, arr_size):
            if tab[b][y - 1] != 0:
                return False
            if tab[b][y + 1] != 0:
                return False
    return True


def check_if_one(x, arr):  # działa
    for r in range(0, len(arr)):
        if arr[x][r] == 1:
            return False
    return True


def same_row(x, arr):
    for r in range(0, len(arr)):
        if arr[r] == x:
            return False
    return True


def used_words(password, arr):
    count = 0
    for x in range(0, len(arr)):
        if arr[x] == password:
            count = count + 1
    if count == 0:
        return True
    else:
        return False

def same_pos (x,y,tab):
    for a in range(0,len(tab)):
        if tab[a][0] == x and tab[a][1] == y:
            return False
    return True


def insert_horizontal(x, y, password, arr, used_words, arr_size):
    if len(password) + y > arr_size:
        return False

    for data in range(0, len(used_words)):
        if used_words[data] == password:
            return False
    index = 0
    count = 0
    for letter in range(y, y + len(password)):
        if arr[x][letter] != password[index] and arr[x][letter] != 0:
            return False
        if arr[x][letter] != 1 and arr[x][letter] != 0:
            count = count + 1
        index = index + 1
    if count < 2:
        return False
    if (letter + 1) != arr_size:
        if arr[x][letter + 1] != 0:
            return False
    return True


pass_numb = 10  # nieparzyste nie dzialaja?
data = []
used_words_arr = []
arr_size = 15
vertical_numb = pass_numb // 2
horizontal_numb = pass_numb - vertical_numb
tuple = ''
letters = []

with open('Words_final.csv', encoding="utf8") as csvfile:  # encoding error
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        data.append(tuple.join(row))

while len(used_words_arr) != pass_numb - 1:

    hori_row_index = []
    col_index = []
    used_words_arr.clear()
    arr = [[0 for x in range(arr_size)] for y in range(arr_size)]  # col, row
    crossing_points = [[], []]
    row_index = []  # numery wierszy w których są poziome słowa

    for vertical in range(0, vertical_numb):
        while True:
            password = data[random.randint(0, len(data) - 1)]
            if len(password) >= 9 and len(password) < arr_size:
                break
        x = random.randint(0, len(arr) - 1)
        while True:
            y = random.randint(0, len(arr) - 1)  # kolumna
            if empty_col(arr, y, arr_size) == False:  # czy cała kolumna gdzie ma być nowe słowo jest pusta
                pass
            else:
                if space_between_vert(arr, y, arr_size) == True:  # jeżeli są przerwy obok słowa, (żeby dwa nie były obok siebie)
                    break
        if x + len(password) > arr_size:
            if len(password) == arr_size:
                x = arr_size - len(password) - random.randint(0, arr_size - len(password) // 2)
            else:
                x = arr_size - len(password) - random.randint(0, arr_size - len(password))
        if x > 0:
            arr[x - 1][y] = 1

        for z in range(0, len(password)):
            arr[x][y] = password[z]
            x = x + 1

        if x <= arr_size - 1:
            arr[x][y] = 1
        used_words_arr.append(password)
        col_index.append(y)  # kolumny w których są pionowe słowa

    col_index_old = col_index.copy()
    col_index.sort()
    col_index.pop()  # usuń ostatni element bo niepotrzebny

    for horizontal in range(0, horizontal_numb - 1):
        y = col_index[horizontal]
        x = random.randint(0, len(arr) - 1)
        while True:
            if (arr[x][y] != 0) and (arr[x][y] != 1) and (check_if_one(x, arr) == True) and (
                    same_row(x, hori_row_index) == True):
                crossing_points.append([x, y])  # wybierz crossing points
                # arr[x][y] = 2
                hori_row_index.append(x)
                break
            else:
                x = random.randint(0, len(arr) - 1)

    crossing_points = crossing_points[2:]

    for point in crossing_points:
        for a in range(0, len(data)):
            itt = 0
            password = data[a]
            if insert_horizontal(point[0], point[1], password, arr, used_words_arr, arr_size) == True:
                for z in range(point[1], point[1] + len(password)):
                    arr[point[0]][z] = password[itt]
                    itt = itt + 1
                used_words_arr.append(password)
                break

for word in used_words_arr:
    for letter in range(0,len(word)):
        letters.append(word[letter])

hardcopy = copy.deepcopy(arr)
index = 0
coords = [[],[]]

while True:
    while True:
        final_password = data[random.randint(0,len(data)-1)]
        if len(final_password) ==7 and used_words(final_password,used_words_arr):
            break
    coords.clear()
    index = 0
    for c in col_index_old:
        for x in range(0,15):
            if arr[x][c] == final_password[index] and same_pos (x,c,coords):
                coords.append([x,c])
                index = index + 1
                break
    for r in hori_row_index:
        for y in range(0,15):
            if index == 7: # zerowanie indeksu żeby nie przekroczył rozmiaru hasła
                index = 0
            if arr[r][y] == final_password[index] and same_pos(r,y,coords): #poprawic #czy sie nie powtarzaja
                coords.append([r,y])
                index = index + 1
                break

    if len(coords) == len(final_password):
        break

for coord in coords:
    arr[coord[0]][coord[1]] = 2

for x in range(arr_size):
    for y in range(arr_size):
        print(color_sign(arr[x][y]), end='  ')
    print()

