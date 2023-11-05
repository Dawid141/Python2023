def sum_seq(sequence):
    total = 0

    for item in sequence:
        if isinstance(item, (list, tuple)):  #chodzi o to że rozbijamy elementy na jak najmniejsze sekwencje i sumujemy niejako w górę (od szczegolu do ogolu)
            total += sum_seq(item)
        elif isinstance(item, int):
            total += item

    return total

seq = [[1, 2, 3], (4, (5)), [6, [7, 3, 8, [9]]]]
print(sum_seq(seq))
