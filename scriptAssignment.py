import os

fName = 'Apple.txt'

fPath = 'C:\\Script_Assignment\\'

apple = 'C:\\Script_Assignment\\Apple.txt'

banana = 'C:\\Script_Assignment\\Banana.txt'

cherries = 'C:\\Script_Assignment\\cherries.txt'

dates = 'C:\\Script_Assignment\\dates.txt'

elderberry = 'C:\\Script_Assignment\\elderberry.txt'

fig = 'C:\\Script_Assignment\\fig.txt'

gooseberries = 'C:\\Script_Assignment\\gooseberries.txt'

honeydew = 'C:\\Script_Assignment\\honeydew_melon.txt'

kiwi = 'C:\\Script_Assignment\\kiwi.txt'

lime = 'C:\\Script_Assignment\\lime.txt'







Apple = os.path.getmtime(apple)
print (Apple)

Banana = os.path.getmtime(banana)
print (Banana)

Cherries = os.path.getmtime(cherries)
print (Cherries)

Dates = os.path.getmtime(dates)
print (Dates)

Elderberry = os.path.getmtime(elderberry)
print (Elderberry)

Fig = os.path.getmtime(fig)
print (Fig)

Gooseberries = os.path.getmtime(gooseberries)
print (Gooseberries)

Honeydew = os.path.getmtime(honeydew)
print (Honeydew)

Kiwi = os.path.getmtime(kiwi)
print (Kiwi)

Lime = os.path.getmtime(lime)
print (Lime)












abPath = os.path.join(fPath, fName)
print(abPath)
