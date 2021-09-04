from os import path
from random import choice
from typing import KeysView
from convertClass import convertClass as cc

conv = cc('./arguments.txt')

#menu def 
def generateKey() -> None:
    notebook = input('quaderno>> ')
    subject = input('materia>> ')
    page = input('pagina>> ')
    print('---------------------')
    print('key >> ' + conv.generateKey(subject, notebook, page))
    print('---------------------')
    input()

def translateKey() -> None:
    key = input('key >> ')
    print('---------------------')
    print('key >> ' + str(conv.decriptKey(key)))
    print('---------------------')
    input()

def argumentList() -> None:
    keys = conv.arg.keys()
    values = conv.arg.values()
    for ind in range(len(keys)):
        print(str(list(values)[ind]), ' : ', str(list(keys)[ind]))
    print('---------------------')
    input()

def addArguments() -> None:
    print('max value >> ', str(conv.getMaxValue()))
    print('---------------------')
    key = input('key >> ')
    value = input('value >> ')
    print('---------------------')
    if conv.argument_add(key, value):
        print('... sucess ...')
    else:
        print('... error ...')
    print('---------------------')
    input()

def delArguments() -> None:
    print('... work in progress ...')
    input()

def changeFilePath():
    path = input('path >> ')
    print('---------------------')
    if conv.changeFilePath(path):
        print('... sucess ...')
    else:
        print('... error ...')
    print('---------------------')
    input()


def settings() -> None:
    while True:
        print('----------------------')
        print('I      options       I')
        print('----------------------')
        print('I 1.add arguments    I')
        print('I 2.del arguments    I')
        print('I 3.change file path I')
        print('I                    I')
        print('----------------------')
        print('I 0.exit             I')
        print('----------------------')
        choice_val = input(' >> ',)
        print('----------------------')

        if choice_val == '1':
                addArguments()
        elif choice_val == '2':
                delArguments()
        elif choice_val == '3':
            changeFilePath()
        elif choice_val == '0':
            return
        else:
            print('... wrong value ...')
            input()
    

#menu
if __name__ == '__main__':
    
    while True:
        print('----------------------')
        print('I     main menu      I')
        print('----------------------')
        print('I 1.generate key     I')
        print('I 2.translate key    I')
        print('I 3.arguments list   I')
        print('I                    I')
        print('I 9.settigns         I')
        print('----------------------')
        print('I 0.exit             I')
        print('----------------------')
        choice_val = input(' >> ',)
        print('----------------------')

        if choice_val == '1':
            generateKey()
        elif choice_val == '2':
            translateKey()
        elif choice_val == '3':
            argumentList()
        elif choice_val == '9':
            settings()
        elif choice_val == '0':
            break
        else:
            print('... wrong value ...')
            input()