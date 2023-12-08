
def whatis(obj, recurse_if_length_less_than=8, spacing=1):
    printable=[int, float]
    
    pad=" "*(spacing-1)
    if type(obj) in printable:
        print(pad, obj)
    else:
        print(pad, type(obj))

    try:
        print(pad, "Shape:", obj.shape)
    except:
        try:
            print(pad, "Length:", len(obj))
        except:
            pass

    if type(obj) == tuple or type(obj) == list:
        if len(obj) < recurse_if_length_less_than:
            print()
            for ind, i in enumerate(obj):
                print(pad+" ","Index",ind)
                whatis(i, recurse_if_length_less_than=recurse_if_length_less_than, spacing=spacing+1)
                print()
