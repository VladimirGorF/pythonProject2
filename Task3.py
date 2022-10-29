# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.
#
text = 'Во поле береза абворожительная стояла абвгдейку читала'
text_list = text.split()
for i in range(len(text_list) - 2):
    if 'абв' in text_list[i]:
        text_list.remove(text_list[i])

print(" ".join(map(str, text_list)))
