from api.models import Purchases
from api.models import Products

import numpy as np


def frozenset2list(frozenset):
    rlist = []
    for item in frozenset:
        rlist.append(str(item))
    return rlist

def is_subvector(base, sub):
    if(len(base) == 0 or len(sub) == 0):
        return False
    index = 0
    for sub_elem in sub:
        for base_elem in base:
            flag = False
            if(base_elem == sub_elem):
                flag = True
                break
            #print(base_elem, sub_elem, flag)
        if(flag == False):
            break
    return flag

