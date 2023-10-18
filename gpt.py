import g4f
import sys
g4f.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args


def main_without_termianlArgs():
    while True:
        history.append({"role": "user", "content": jews})

        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=history,
        )
        i = 1
        print(response)
        print(history)

        if argument == ' -1':
            print(' \n Session has ended ')
            break
        else:
            pass

        jews = " "

def main_withArgs():
    while True:
        jews = str(input(':'))
        history.append({"role": "user", "content": jews})
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=history,
        )
        i = 1
        print(response)

        jews = " "


history = []
argument = ""
try:
    for arg in sys.argv[1:]:
        arg = str(arg)
        jews = jews +" "+ arg
    #print(jews[0:3])
    argument = jews[0:3]
    i = 0
    
    main_without_termianlArgs()
except:
    main_withArgs()
