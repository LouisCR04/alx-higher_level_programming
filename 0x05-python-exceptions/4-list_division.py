#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for i in range(list_length):
        try:
            l3 = my_list_1[i] / my_list_2[i]
            my_list_3.append(l3)
        except IndexError:
            print("out of range")
            my_list_3.append(0)
        except ZeroDivisionError:
            my_list_3.append(0)
            print("division by 0")
        except TypeError:
            my_list_3.append(0)
            print("wrong type")
        finally:
            pass
    return (my_list_3)
