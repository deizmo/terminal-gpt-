import g4f
import sys
g4f.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args
jews=''
for arg in sys.argv[1:]:
    arg = str(arg)
    jews = jews +" "+ arg
print(jews[0:3])
argument = jews[0:3]
i = 0
if jews == '':
    print('no argument')
# Automatic selection of provider
while True:
    if i == 0:
        pass
    else:
        jews = str(input(':'))
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": jews}],
    )
    jews = " "
    i = 1
    print(response)

    if argument == ' -1':
        print(' \n Session has ended ')
        break
    else:
        pass


def gpt(jews):
    jews = str(jews)
    response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": jews}],
)
def gpt_answer():
    pass