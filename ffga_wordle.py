import re
import io
words_seq_by_freq = io.open("txt/words_seq_by_freq.txt", mode="r", encoding='utf-8').read().lower().split(sep=',')
words_seq_by_letterq = io.open("txt/words_seq_by_letterq.txt", mode="r", encoding='utf-8').read().lower().split(sep=',')
print ('Пожалуйста, вводите буквы нижним регистром, то есть строчные. Вместо "ё" надо использовать "е". Если нет буквы определённого цвета, то просто жмёте enter','Позиции (номер буквы в слове) вводите цифрами. Несколько букв или цифр отделяются друг от друга пробелами. По окончание ввода жмёте enter','Если нужно будет сделать ещё один прогон, то введённые ранее значения надо будет внести ещё раз.','Например, если загадано слово "пикет", а вы попробовали "зенит", то у вас будут "з" и "н" серые, "т" зелёная, а "е" и "и" - жёлтые.','И вводить будет нужно вот так: з н <enter> т <enter> 5 <enter> е и <enter> 2 4','',sep='\n')

pattern_red = [letter for letter in input("Введите буквы, которых точно НЕТ в слове (серые): ").split()]
outlist = []
for letter in pattern_red:
    letter_for_outlist = fr"{letter}"
    outlist.extend([word for word in words_seq_by_letterq if re.search(letter_for_outlist, word)])

pattern_green_let = [letter for letter in input("Введите буквы, которые точно известны (зелёные): ").split()]
while True:
    try:
        pattern_green_pos = [int(position) for position in input("Введите позиции для зелёных букв: ").split()]
    except ValueError:
        print ('Ошибка! Нужно ввести только цифру - позицию буквы или нескольких букв (через пробел)')
    else:
        break
filtered = words_seq_by_letterq
counter = 0
for every_value in pattern_green_let:
    filtered = [word for word in filtered if pattern_green_let[counter] == word[int(pattern_green_pos[counter]) - 1]]
    counter = counter + 1

pattern_yellow_let = [letter for letter in input("Введите буквы, которые известны (жёлтые): ").split()]
while True:
    try:
        pattern_yellow_pos = [int(position) for position in input("Введите позиции для жёлтых букв (т.е. где она не должна быть): ").split()]
    except ValueError:
        print ('Нужно ввести только цифру - позицию буквы или нескольких букв (через пробел)')
    else:
        break
counter = 0
for letter in pattern_yellow_let:
    letter_for_yellowfilterlist = fr"{letter}"
    filtered = [word for word in filtered if re.search(letter_for_yellowfilterlist, word)]
for every_value in pattern_yellow_let:
    outlist.extend([word for word in filtered if pattern_yellow_let[counter] == word[int(pattern_yellow_pos[counter]) - 1]])
    counter = counter + 1

for word in outlist:
    if word in filtered:
        filtered.remove(word)

print('','Возможные слова:',filtered, sep='\n')