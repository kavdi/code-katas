"""This file contains a function that returns the int that apears an odd number of times in a list of integers, the best practice solution was:
            def find_it(seq):
                for i in seq:
                    if seq.count(i)%2!=0:
                        return i
 """


def find_it(seq):
    """This function returns the integer that is in the list an odd number of times"""
    for i in seq:  
      y = seq.count(i)
      if y % 2 != 0:
        return i
        break


#6kyu