'''
Integer to Roman

@author: Sahana Basapathi
IDE: Atom
'''
#function to convert integer to Roman
def intToRoman(num):
    mapping = [(1000, 'M'), (900, 'CM'), (500, 'D'),\
            (400, 'CD'), (100, 'C'), (90, 'XC'), \
              (50, 'L'), (40, 'XL'), (10, 'X'), \
               (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    answer = ''
    #loop through each symbol
    for pair in mapping:
        value, roman = pair

        #count gives the number of copies of a symbol
        count, num = divmod(num, value)
        answer += (count * roman)

    return answer
