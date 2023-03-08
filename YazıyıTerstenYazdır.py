name = input("Your name:")
liste = []
length = len(name)
i = 0
def Reverse(lst):
    lst.reverse()
    return lst

while i < length:
    liste.append(name[i])
    i += 1
lst = liste
liste2 = Reverse(lst)

name2 = "".join(liste2)
print(name2)