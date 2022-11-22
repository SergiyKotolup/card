x = int(input('how old r u?'))
if x < 18:
    print('u r child')
else:
    n = (str(input('name:')))
    print(n)
    m = 10
    p = 'upload'
    for q in p:
        print(q*100)
    if n == "ivan":
        print("no")

    elif n == "vlad":
        print("nono")

    elif n == ('max'):
        print("mini")

    else:
        print("cool")

    if n == 'max':
        print('MINI')
    elif n == 'ivan':
        print('NONO')
    elif n == 'vlad':
        print('NO')
    else:
        k = (int(input('card:')))
        print(k)

        m = 10
        while m:
            m += 10
            if m == 100000:
                break
            print(m)

        if k < 4000:
            print('it\'s not mastercard or visa')

        elif k > 6000:
            print('it\'s not ms or visa')

        else:
            print('thank u)')

