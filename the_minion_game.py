def minion_game(s):
    # your code goes here
    n = len(s)
    s = enumerate(s)

    vocales = ['A','E','I','O','U']
    cuentaS = 0
    cuentaK = 0

    for i in s:
        if i[1] in vocales:
            cuentaK += n-i[0]
        else:
            cuentaS += n-i[0]

    if cuentaK > cuentaS:
        print('Kevin', cuentaK)
    elif cuentaK < cuentaS:
        print('Stuart', cuentaS)
    else:
        print('Draw')