#!/usr/bin/python3

def get_distance(lst):
    indexes = []
    distance, i = 0, 0
    for v in lst:
        if v == 1:
            indexes.append(i)
        i += 1
    for i in range(len(indexes) - 1):
        if indexes[i + 1] - indexes[i] > 1:
            distance += indexes[i + 1] - (indexes[i] + 1)
            indexes[i + 1] = indexes[i] + 1
    return distance



if __name__ == "__main__":
    lst = [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]
    print(get_distance(lst))
