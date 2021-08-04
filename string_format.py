#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "Erik", age = 33)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("Erik",33)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("Erik",33)

print(txt1)
print(txt2)
print(txt3)
