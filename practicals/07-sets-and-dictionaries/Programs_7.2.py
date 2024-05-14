#!/usr/bin/env python3

if __name__ == '__main__':



    def indi_letters(x,b):
        x = set(x)
        b = set(b)
        union = x.union(b)
        union = list(union)
        intersect = list(set(x) & set(b))
        s_d = x.symmetric_difference(b)
        s_d = list(s_d)
        print(union)
        print(intersect)
        print(s_d)



    indi_letters('cheese','beer')

