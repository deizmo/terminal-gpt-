import g4f
import sys
g4f.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args
jews = sys.argv[1]
i = 0
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