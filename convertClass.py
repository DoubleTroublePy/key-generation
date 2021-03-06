
# import
from os import supports_bytes_environ, write, path
import regex as re
import datetime as dt

class convertClass:
    arg_ind = str
    arg = {}

    # setup the file whit a set of values
    def __init__(self, arguments_ind:str) -> None:
        if path.exists(arguments_ind):
            file = open(arguments_ind, 'r+')
        else:
            file = open(arguments_ind, 'w+')
        self.arg_ind = arguments_ind
        for line in file:
            key = re.search('([a-zA-Z]*.):', line)
            value = re.search(':([1-9]*.)', line)
            if key and value:
                key = key.group(1)
                value = value.group(1)
                self.arg[key] = value
        file.close()
    
    # mode 1 => given a key return the value
    # mode 0 => given a value return the key  
    def translateArg(self, key:str, mode:int) -> int:
        if mode:
            if key in self.arg:
                return int(self.arg[key])
        else:
            if key in self.arg.values():
                val_list = self.arg.values()
                key_list = self.arg.keys()
                position = list(val_list).index(key)
                return list(key_list)[position]
        return False

    # if the ex numeber>9 then convert in the corrispoding char
    def translateNum(self, key:str, mode:int) -> int:
        data = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f',
        }
        if mode:
            if key > 9:
                return data[key]
        else:
            if key in data.values():
                val_list = data.values()
                key_list = data.keys()
                position = list(val_list).index(key)
                return list(key_list)[position]
        return key

    # translate a dec-->hex
    def translateHex(self, key_frag:str) -> int:
        num = 0
        key_frag = key_frag[::-1]
        for ind in range(len(key_frag)):
            tmp_key_frag = self.translateNum(key_frag[ind], 0)
            num += (int(tmp_key_frag) * (16**ind))
        return int(num)

    # arr-->string TODO find a better way to do this, this metod is stupid
    def toString(self, arr:list) -> str:
        string = ''
        for num in reversed(arr):
            string += str(num)
        return string

    # hex-->convert 
    def convertNum(self, num:int) -> str:
        base = 16
        rest = []
        while num >= base:
            rest.append( self.translateNum( int(num%base), 1) )
            num = num / base
        rest.append( self.translateNum( int(num%base), 1) )
        num = num / base
        return self.toString(rest)
    
    # generate the key using a dictonary for the string and then converting evrithing in hex
    # the data in a yy-mm-dd format is automatic generated  
    def generateKey(self, sub:str, num:int, pag:int) -> int:
        id = ''
        date = dt.datetime.now()
        sub = sub.casefold()
        sub = self.translateArg(sub, 1)
        if sub and num.isnumeric() and pag.isnumeric() :
            id += self.convertNum(sub)
            id += '.'
            id += self.convertNum(int(date.year))
            id += '.'
            id += self.convertNum(int(date.month))
            id += '.'
            id += self.convertNum(int(date.day))
            id += '.'
            id += self.convertNum(int(num))
            id += '.'
            id += self.convertNum(int(pag))
            return id
        return 'false'

    # Convert a key in a uman comprensible string
    def decriptKey(self, key:int) -> str:
        digest = ''
        tmp_digest = ''
        lock = 0
        for ind in range(len(key)):
            if ind == len(key) - 1 and key[ind] != '' or key[ind] != '.':
                tmp_digest += key[ind] 
            else:   # if there is a point convert the hex string to decimal, the first value is converted to a word
                if not lock:
                    tmp_digest = str(self.translateHex(str(tmp_digest)))
                    digest += str(self.translateArg(tmp_digest, 0))
                    lock = 1
                else:
                    digest += str(self.translateHex(str(tmp_digest)))
                if ind != len(key)-2:
                    digest += '.'

                tmp_digest = ''
        return digest

   # add a new value to the dictionary and to the the file  
    def argument_add(self, key:int, value:int) -> bool:
            if not (key in self.arg.keys()):
                file = open(self.arg_ind, 'a')
                write_val = '\n' + str(key) + ':' + str(value)
                file.write(write_val)
                file.close()
                self.arg[key] = value
                return True
            else: 
                return False

    def argument_del(self, key) -> None:
        pass

    def getMaxValue(self) -> int:
        return max(self.arg.values())
    
    # if the path exist extapolate the keys and values and assing them to the 
    # dictionary
    def changeFilePath(self, file_path:str) -> bool:
        if path.exists(file_path):
            self.arg = {}
            file = open(file_path, 'r+')
            self.arg_ind = file_path
            for line in file:
                key = re.search('([a-zA-Z].):', line)
                value = re.search(':(\d*)', line)
                if key and value:
                    key = key.group(1)
                    value = value.group(1)
                    self.arg[key] = value
            file.close()
            return True
        else:
            return False