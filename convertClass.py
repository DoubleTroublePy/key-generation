
# import
from os import write
import regex as re
import datetime as dt

class convertClass:
    arg_ind = str
    arg = {}

    def __init__(self, arguments_ind) -> None:
        file = open(arguments_ind, 'r+')
        self.arg_ind = arguments_ind
        for line in file:
            key = re.search('([a-zA-Z]*.):', line)
            value = re.search(':([1-9]*.)', line)
            if key and value:
                key = key.group(1)
                value = value.group(1)
                self.arg[key] = value
        file.close()
    
    def translateArg(self, key) -> int:
        return int(self.arg[key])
    
    def translateNum(self, key) -> int:
        data = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f',
        }
        if key > 9:
            return data[key]
        return key

    def toString(self, arr) -> str:
        string = ''
        for num in reversed(arr):
            string += str(num)
        return string

    def convertNum(self, num) -> str:
        base = 16
        rest = []
        while num >= base:
            rest.append( self.translateNum( int(num%base) ) )
            num = num / base
        rest.append( self.translateNum( int(num%base) ) )
        num = num / base
        return self.toString(rest)

    def generate(self, sub, num) -> int:
        id = ''
        date = dt.datetime.now()
        sub = sub.casefold()
        sub = self.translateArg(sub)
        id += self.convertNum(sub)
        id += '.'
        id += self.convertNum(int(date.year))
        id += '.'
        id += self.convertNum(int(date.month))
        id += '.'
        id += self.convertNum(int(date.day))
        id += '.'
        id += self.convertNum(int(num))
        return id

    def argument_add(self, key, value) -> None:
            if not (key in self.arg.keys()):
                file = open(self.arg_ind, 'a')
                write_val = '\n' + str(key) + ':' + str(value)
                file.write(write_val)
                file.close()
                self.arg[key] = value
            else: 
                return False

    def argument_del(self, key) -> None:
        pass

    def getMaxValue(self) -> int:
        return max(self.arg.values())