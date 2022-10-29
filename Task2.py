# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#
with open('incoming_Text', 'r') as f:
    text = f.read()

def Coding(text):
    text_cod = []
    i = 0
    while i < len(text) - 2:
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count = count + 1
            i = i + 1
        text_cod += str(count) + text[i]
        i += 1
    return "".join(text_cod)


with open('encoding_Text', 'w') as file:
    file.write(f'{Coding(text)}')

with open('encoding_Text', 'r') as fh:
    text_decod = fh.read()

text_finish = [i for i in text_decod]
indexes = []


def index_Count(text_decod):
    for i in text_finish:
        if i.isdigit():
            indexes.append(int(i))
    return indexes


def text_Decoder(indexes):
    TEXT = ''
    k = 0
    for i in range(1, len(text_finish), 2):
        TEXT += text_finish[i] * indexes[k]
        k += 1
    return TEXT


index_Count(text_decod)

with open('Decoding_Text', 'w') as dt:
    dt.write(f'{text_Decoder(indexes)}')








