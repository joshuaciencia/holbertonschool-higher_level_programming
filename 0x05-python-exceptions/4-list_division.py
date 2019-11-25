#!/usr/bin/python3
def list_division(l1, l2, l):
    l3 = []
    for i in range(l):
        r = 0
        try:
            r = l1[i] / l2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            l3.append(r)
    return l3
