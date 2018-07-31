def boxPrint(sym, w, h):
    if len(sym) != 1:
        raise Exception('Symbol must be a single character string')
    if w <= 2:
        raise Exception('Width must be greater than 2')
    if h <= 2:
        raise Exception('Height must be greater than 2')
    print(sym * w)
    for i in range(h-2):
        print(sym + ' ' * (w-2) + sym)
    print(sym * w, '\n')


for settings in (('a', 3, 3), ('b', 1, 3)):
    try:
        boxPrint(*settings)
    except Exception as err:
        print('An exception occured: ' + str(err))