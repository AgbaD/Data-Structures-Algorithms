#!/usr/bin/python3
# Author:   Dami Agba


def dcp_621(d):
    sort_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    letters, length, curr= {}, 0, []
    for j in range(len(sort_d)):
        this = sort_d[j]
        if curr == []:
            length += this[1]
            pattern = this[0].split('-')
            letters[pattern[0]] = 1
            letters[pattern[1]] = 1
            curr = pattern
        else:
            pattern = this[0].split('-')
            if pattern[0] in letters.keys() or pattern[1] in letters.keys():
                if pattern[0] in letters and pattern[1] in letters:
                    if letters[pattern[0]] > 1 or letters[pattern[1]] > 1:
                        pass
                    else:
                        letters[pattern[0]] += 1
                        letters[pattern[1]] += 1
                        length += this[1]
                elif pattern[0] in letters and pattern[1] not in letters:
                    if letters[pattern[0]] > 1:
                        pass
                    else:
                        letters[pattern[0]] += 1
                        letters[pattern[1]] = 1
                        length += this[1]
                elif pattern[0] not in letters and pattern[1] in letters:
                    if letters[pattern[1]] > 1:
                        pass
                    else:
                        letters[pattern[0]] = 1
                        letters[pattern[1]] += 1
                        length += this[1]
                else:
                    letters[pattern[0]] = 1
                    letters[pattern[1]] = 1
                    length += this[1]
    return length
    

if __name__ == "__main__":
    d = {"a-b": 3, "a-c": 5, "a-d": 8, "d-e": 2, "d-f": 4, "e-g": 1, "e-h": 1}
    print(dcp_621(d))
