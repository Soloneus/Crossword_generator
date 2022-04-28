from Generate import *
from tkinter import *
root = Tk()


def get_row(actual_focus):
    row = actual_focus // 15
    if actual_focus % 15 == 0:  # przypadki brzegowe row
        row = row - 1
    return row


def get_col(actual_focus):
    row = get_row(actual_focus)
    col = actual_focus - 15 * row - 1
    if col == - 1:  # przypadki brzegowe col
        col = 14
    return col


def downKey(event):
    actual_focus = int(str(root.focus_get())[7:])
    row = get_row(actual_focus)
    row = row + 1
    if row == 15:
        row = 14
    col = get_col(actual_focus)
    array2[row][col].focus()


def upKey(event):
    actual_focus = int(str(root.focus_get())[7:])
    row = get_row(actual_focus)
    row = row - 1
    if row == -1:
        row = 0
    col = get_col(actual_focus)
    array2[row][col].focus()


def leftKey(event):
    actual_focus = int(str(root.focus_get())[7:])
    row = get_row(actual_focus)
    col = get_col(actual_focus)
    col = col - 1
    if col == -1:
        col = 0
    array2[row][col].focus()


def rightKey(event):
    actual_focus = int(str(root.focus_get())[7:])
    row = get_row(actual_focus)
    col = get_col(actual_focus)
    col = col + 1
    if col == 15:
        col = 14
    array2[row][col].focus()


def password(event):
    try:
        i = 0
        index = 0
        actual_focus = int(str(root.focus_get())[7:])
        row = get_row(actual_focus)
        col = get_col(actual_focus)
        for coord in coords:  # przenoszenie znaku do hasła
            i = i + 1
            if row == coord[0] and col == coord[1]:
                label0 = Label(root, text=array2[row][col].get(), bg="#fff", height=1, width=2, font='Arial')
                label0.place(x=starting_x + (i - 1) * 50 - 12, y=y0 + 100 - 12)
                break

        if str(array2[row][col].get()) == str(hardcopy[row][col]) and arr[row][col] == 2:
            tablica[i - 1].config(disabledbackground="#0f0")  # tło disabled inputboxu
            label0.config(bg="#0f0")  # tło labelu z literką hasla
            tab_labels_pass[i - 1].config(bg="#0f0")  # tło labelu z numerem (1-7) hasła

        elif str(array2[row][col].get()) != str(hardcopy[row][col]) and arr[row][col] == 2:
            tablica[i - 1].config(disabledbackground="#F00")  # red
            label0.config(bg="#F00")
            tab_labels_pass[i - 1].config(bg="#F00")  # tło labelu z numerem (1-7) hasła

        if array2[row][col].get() == '' and arr[row][col] == 2:
            tablica[i - 1].config(disabledbackground="#fff")  # empty
            label0.config(bg="#fff")  # blank tło jeżeli nic nie ma w inputboxie
            tab_labels_pass[i - 1].config(bg="#fff")  # tło labelu z numerem (1-7) hasła
    except:
        pass


root.bind('<Key>', password)
root.bind('<Down>', downKey)
root.bind('<Up>', upKey)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.attributes('-fullscreen', True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_width = screen_width / 2
center_height = screen_height / 2

x0 = center_width + 7.5 * 50
y0 = center_height + 7.5 * 50
x1 = center_width - 7.5 * 50
y1 = center_height - 7.5 * 50

starting_x = center_width - len(final_password) / 2 * 50 + 25
tablica = [0 for j in range(0, len(final_password))]
tab_labels_pass = [0 for j in range(0, len(final_password))]
array2 = [[0 for j in range(15)] for i in range(15)]
array = ['entry' + str(x + 1) for x in range(len(final_password))]
canvas = Canvas(root, width=screen_width, height=screen_height, bg="#373058")
canvas.pack()
canvas.create_rectangle(x0, y0, x1, y1, width=4, fill="#342e4e")
canvas.create_text(screen_width * 1 / 8 + 50, 250, text='VERTICAL', font='Arial', fill="#fff", anchor=CENTER)
canvas.create_text(screen_width * 7 / 8 - 50, 250, text='HORIZONTAL', font="Arial", fill="#fff", anchor=CENTER)
canvas.create_text(center_width, y0 + 40, text='PASSWORD', font="Arial", fill="#fff")

index_numb = 1
position = 1
count = 1

for col in col_index_old:  # numery kolumn nad kwadratem
    label_pass_numb = Label(root, text=count, bg="#373058", fg="#fff")
    label_pass_numb.place(x=center_width - (7 - col) * 50 - 4, y=120)
    count = count + 1

for row in hori_row_index:  # numery wierszy nad kwadratem,
    label_pass_numb = Label(root, text=count, bg="#373058", fg="#fff")
    label_pass_numb.place(x=550, y=center_height - (7 - row) * 50 - 10)
    count = count + 1

for vertical in range(0, len(used_words_arr[0:5])):

    definition = str(index_numb) + ". " + def_word(used_words_arr[vertical])

    if len(definition) >= 200: #b długa definicja
        for z in range(58, len(definition)):
            if definition[z] == ' ':
                cutting_point1 = z
                break
        for y in range(128, len(definition)):
            if definition[y] == ' ':
                cutting_point2 = y
                break
        for x in range(188,len(definition)):
            if definition[x] == ' ':
                cutting_point3 = x

        definition1 = definition[0:cutting_point1]
        definition2 = definition[cutting_point1:cutting_point2]
        definition3 = definition[cutting_point2:cutting_point3]
        definition4 = definition[cutting_point3:]
        canvas.create_text(50, 300 + position * 50, text=definition1, font="Arial", fill="#fff", anchor=W)
        position = position + 1
        canvas.create_text(50, 300 + position * 50, text=definition2, font="Arial", fill="#fff", anchor=W)
        position = position + 1
        canvas.create_text(50, 300 + position * 50, text=definition3, font="Arial", fill="#fff", anchor=W)
        position = position + 1
        canvas.create_text(50, 300 + position * 50, text=definition4, font="Arial", fill="#fff", anchor=W)
        position = position + 1

    if len(definition) >= 140:
        for z in range(58, len(definition)):
            if definition[z] == ' ':
                cutting_point1 = z
                break
        for y in range(128, len(definition)):
            if definition[y] == ' ':
                cutting_point2 = y
                break

        definition1 = definition[0:cutting_point1]
        definition2 = definition[cutting_point1:cutting_point2]
        definition3 = definition[cutting_point2:]
        canvas.create_text(50, 300 + position * 50, text=definition1, font="Arial", fill="#fff", anchor=W)
        position = position + 1
        canvas.create_text(50, 300 + position * 50, text=definition2, font="Arial", fill="#fff", anchor=W)
        position = position + 1
        canvas.create_text(50, 300 + position * 50, text=definition3, font="Arial", fill="#fff", anchor=W)
        position = position + 1

    if len(definition) > 70 and len(definition) < 140:
        for z in range(58, len(definition)):
            if definition[z] == ' ':
                cutting_point1 = z
                break
        definition1 = definition[0:cutting_point1]
        definition2 = definition[cutting_point1:]
        canvas.create_text(50, 300 + position * 50, text=definition1, font="Arial", fill="#fff", anchor=W)
        position = position + 1
        canvas.create_text(50, 300 + position * 50, text=definition2, font="Arial", fill="#fff", anchor=W)
        position = position + 1

    if len(definition) <= 70:
        canvas.create_text(50, 300 + position * 50, text=definition, font="Arial", fill="#fff", anchor=W)
        position = position + 1

    index_numb = index_numb + 1

position = 1

for hori in range(len(used_words_arr[4:]), len(used_words_arr)):  # printowanie definicji na tk
    definition = str(index_numb) + ". " + def_word(used_words_arr[hori])
    if len(definition) >= 140:
        for z in range(58, len(definition)):
            if definition[z] == ' ':
                cutting_point1 = z
                break
        for y in range(128, len(definition)):
            if definition[y] == ' ':
                cutting_point2 = y
                break

        definition1 = definition[0:cutting_point1]
        definition2 = definition[cutting_point1:cutting_point2]
        definition3 = definition[cutting_point2:]
        canvas.create_text(1400, 300 + position * 50, text=definition1, font="Arial", fill="#fff", anchor=W)
        position = position + 1
        canvas.create_text(1400, 300 + position * 50, text=definition2, font="Arial", fill="#fff", anchor=W)
        position = position + 1
        canvas.create_text(1400, 300 + position * 50, text=definition3, font="Arial", fill="#fff", anchor=W)
        position = position + 1

    if len(definition) > 70 and len(definition) < 140:
        for z in range(58, len(definition)):
            if definition[z] == ' ':
                cutting_point1 = z
                break
        definition1 = definition[0:cutting_point1]
        definition2 = definition[cutting_point1:]
        canvas.create_text(1400, 300 + position * 50, text=definition1, font="Arial", fill="#fff", anchor=W)
        position = position + 1
        canvas.create_text(1400, 300 + position * 50, text=definition2, font="Arial", fill="#fff", anchor=W)
        position = position + 1

    if len(definition) <= 70:
        canvas.create_text(1400, 300 + position * 50, text=definition, font="Arial", fill="#fff", anchor=W)
        position = position + 1

    index_numb = index_numb + 1

for x in range(0, 15):  # tworzenie input boxów krzyzówki
    for y in range(0, 15):
        array2[x][y] = Entry(justify=CENTER, font='Arial', textvariable=StringVar)
        for i in range(0, len(final_password)):
            if x == coords[i][0] and y == coords[i][1]:
                canvas.create_window(x1 + 25 + y * 50, y1 + 25 + x * 50, window=array2[x][y], width=50, height=50)
                label = Label(root, text=i + 1, bg="#fff")
                label.place(x=x1 + y * 50 + 30, y=y1 + x * 50 + 1)
                i = i + 1
                break
            if x != coords[i][0] and y != coords[i][1] and arr[x][y] != 1 and arr[x][y] != 0:
                canvas.create_window(x1 + 25 + y * 50, y1 + 25 + x * 50, window=array2[x][y], width=50, height=50)

for z in range(0, len(final_password)):  # tworzenie disabled input boxów hasła na dole
    tablica[z] = Entry(justify=CENTER, font='Arial', bg="#ffd", textvariable=StringVar, state=DISABLED,
                       disabledbackground="#fff")
    tab_labels_pass[z] = Label(root, text=z + 1, bg="#fff")
    canvas.create_window(starting_x + z * 50, y0 + 100, window=tablica[z], width=50, height=50)
    tab_labels_pass[z].place(x=starting_x + z * 50 + 11, y=y0 + 76)

root.mainloop()
