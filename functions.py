mySentence = 'loves color';

color_List = ['red','blue','pink','purple','black','green'];

def color_function(name):
    lst =[]
    for i in color_List:
        msg = "{0} {1} {2}".format(name, mySentence, i)
        lst.append(msg)
    return lst


lst = color_function('Zavier');
for i in lst:
    print(i)
