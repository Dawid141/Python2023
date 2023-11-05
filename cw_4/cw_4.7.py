def flatten(sequence):
    flattened_list = []

    for item in sequence:
        if isinstance(item, (list, tuple)):
            flattened_list.extend(flatten(item)) #sprawdzamy czy element jest sekwencja, jesli tak to wywolujemy rekurencyjnie funkcje zeby
        else:                                    #niejako "rozebrac" sekwencje na elementy podstawowe, kiedy to zrobimy i element nie bedzie juz
            flattened_list.append(item)          #w sekwencji, dodajemy go do wczesniej przygotowanej listy wynikowej

    return flattened_list

seq = [1, [2, (7), [9, 5]], (6, [4, 8]),[12, 30], [9, [10, [5]]]]
flatten(seq)
print(flatten(seq))
