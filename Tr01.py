#valami = 12  
var1 = "12" #string

#valami = int(input("Írj be egy számot.")) 

#print('valami')
#print(valami + 10)
#print(int(var1) + 10) #string átalakítás integerbe

#print(type (valami))
#print(type (var1))

lis = [] # lista
dic = {} # szótár
tup = () # tuple nem változik a tartalom
hal = set () # halmaz 

lis1 = [ 'alma', 21, True, False ]
#print(lis1[0])

#'kulcs key' "érték value" pár 
dic1 = {'neve': "Lajos", "kora": 32, 'lakhelye': "Tiszaújváros", 'fizet': 331000}
#print(dic1['neve'])

tup1 = ("Lajos", 32, "Tiszaújváros", 432000)
#print(tup1[2])

hal1 = {5, 9, 'alma', 21, True, False}
#print (9 in hal1)

lis1.append("szerda")

#új elem bevitele
dic1['ujkulcs'] = 123
hal2 = hal1 | {"szerda"} #AltGr + W

hal1.add("kedd")

#törlések
#lis1.pop() #utolsó elem törlés
#lis1.pop(0) # számozott törlése
#lis1.remove('alma')

dic1.pop('kora')

#hal1.remove('alma')
#halx = {'alma'}
hal2 = hal1 - {'alma'} # - halx


#for elem in hal2:
#	print(elem)
#for elem in dic1.items():
#	print(elem)
#for elem in dic1.keys():
#	print(elem)
#for elem in dic1.values():
#	print(elem)

print( lis1[::] )
print( lis1[4:1:-1] )
print( lis1[::-1] )
print( lis1[::2] )



#str parancs
#int parancs

# ctrl-B
# python --version
