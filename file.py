from regex import F
import torch
from collections import defaultdict


ans = []
def EightQueens() -> int:
    
    back(0, [], set(), set(), set())
    return len(ans)


def back(i, list2, sub_set, add_set, j_set):
    if i == 7:
        for j in range(8):
            if i - j in sub_set or i + j in add_set or j in j_set:
                continue
            tem_list = list2[:]
            tem_list.append(j)
            ans.append(tem_list)
        return
    for j in range(8):
        if i - j in sub_set or i + j in add_set or j in j_set:
            continue
        sub_set.add(i - j)
        add_set.add(i + j)
        j_set.add(j)
        list2.append(j)
        back(i + 1, list2, sub_set, add_set, j_set)
        list2.pop()
        j_set.remove(j)
        add_set.remove(i + j)
        sub_set.remove(i - j)


def showResult(l1):
    res = []
    for i in range(8):
        l2 = ['*'] * 8
        l2[l1[i]] = 'Q'
        res.append(l2)
        print(l2)


if __name__ == '__main__':
    print(EightQueens())
    showResult(ans[0])
