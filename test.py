from random import choice
from convertClass import convertClass as cc

conv = cc('./arguments.txt')

#menu def 
def generateKey():
    subject = input('materia>> ')
    notebook = input('quaderno>> ')
    print('---------------------')
    print('key >> ' + conv.generate(subject, notebook))
    print('---------------------')
    input()

def argumentList():
    for val in conv.arg.keys():
        print(val)
    print('---------------------')
    input()

def addArguments():
    pass

def delArguments():
    print('... work in progress ...')
    input()

#menu
if __name__ == '__main__':
    while True:
        print('---------------------')
        print('I     main menu     I')
        print('---------------------')
        print('I 1.generate key    I')
        print('I 2.translate key   I')
        print('I 3.arguments list  I')
        print('I 4.add arguments   I')
        print('I 5.del arguments   I')
        print('---------------------')
        print('I 0.exit            I')
        print('---------------------')
        choice_val = input(' >> ',)
        print('---------------------')

        if choice_val == '1':
            generateKey()
        elif choice_val == '2':
            pass
        elif choice_val == '3':
            argumentList()
        elif choice_val == '4':
            addArguments()
        elif choice_val == '5':
            delArguments()
        elif choice_val == '0':
            break
        else:
            print('... wrong value ...')
            input()

# a.argument_add('info', 4)
# print(a.getMaxValue())
# print(a.translateArg('mate'))
