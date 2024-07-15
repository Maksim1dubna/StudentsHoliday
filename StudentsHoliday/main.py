import csv
def write_holiday_cities(first_letter):
    # Open file
    with open('travel-notes.csv', newline='') as file_obj:
        reader_obj = csv.reader(file_obj, delimiter=' ', quotechar='|')
        list_main = []
        list_visited = []
        list_wanted = []
        list_No_One = []
        for row in reader_obj:
            letter = row[0]
            if letter.startswith(first_letter) == True:
                main_row = ' '.join(row)
                list_main.append(main_row.split(','))
        for i in range(len(list_main)):
            element = list_main[i].pop()
            list_wanted.append(element)
            list_main[i].pop(0)
            element = list_main[i].pop(0)
            list_visited.append(element)
        element = ''
        for el in list_visited:
            element += str(el + ';')  # Превращаем каждый элемент списка в строку
        list_visited = element.split(';')
        element = ''
        for el in list_wanted:
            element += str(el + ';')  # Превращаем каждый элемент списка в строку
        list_wanted = element.split(';')
        list_visited.pop()
        list_wanted.pop()
        list_visited = list(set(list_visited))
        list_wanted = list(set(list_wanted))
        for i in range(len(list_wanted)):
            if list_wanted[i] not in list_visited:
                list_No_One.append(list_wanted[i])
        list_visited.sort()
        list_wanted.sort()
        list_No_One.sort()
        print(f'Посетили: {list_visited}')
        print(f'Хотят посетить: {list_wanted}')
        print(f'Никогда не посещали: {list_No_One}')
        print(f'Следующим городом будет: {list_No_One[0]}')
        with open('holiday.csv', 'w', newline='') as csvfile:
            fieldnames = ['Visited', 'Wants to visit', 'Never visited', 'Next City']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Visited': ', '.join(list_visited),
                             'Wants to visit': ', '.join(list_wanted),
                             'Never visited': ', '.join(list_No_One),
                             'Next City': list_No_One[0]})
    return 0
write_holiday_cities("L")