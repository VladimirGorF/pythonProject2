# задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую
# последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7]
#  [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]

l = [1, 5, 2, 3, 4, 1, 7, 8, 15, 1]
max = 0
min = 0
max_Sequence = []


def seek_max_Sequence(l):
    len_max = 1
    for i in range(len(l)):
        max_in = 0
        min_in = 0

        len_in = 1
        k = 1
        while l[i] + k in l:
            max_in = l[i] + k
            len_in += 1
            k += 1

        k = 1
        if (l[i] - k) in l:
            while (l[i] - k) in l:
                min_in = l[i] - k
                len_in += 1
                k += 1
        else:
            min_in = l[i]

        if l[i] == 0 and len_in > len_max:
            min_in = l[i]
        elif len_in > len_max and l[i] > max_in:
            max_in = l[i]
        elif len_in > len_max:
            len_max = len_in
            max_Sequence.append(max_in)
            max_Sequence.insert(0, min_in)
    return max_Sequence


print(seek_max_Sequence(l))











