import os
os.system('rm keyGenerate.py')
os.system('rm convertClass.py ')
os.system('rm arguments.txt')

os.system('wget https://raw.githubusercontent.com/DoubleTroublePy/key-generation/main/test.py')
os.system('cp test.py keyGenerate.py')
os.system('rm test.py')

os.system('wget https://raw.githubusercontent.com/DoubleTroublePy/key-generation/main/convertClass.py')
os.system('wget https://raw.githubusercontent.com/DoubleTroublePy/key-generation/main/arguments.txt')
