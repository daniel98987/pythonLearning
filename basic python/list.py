#CRUD
familyNames = ['Daniel','Rene','Doris','Diana']
familyNames.insert(1,'camilo')

print(len(familyNames))
[print(x) for x in familyNames]

new_array  = [x for x in familyNames if x=='Daniel' ]
print(new_array)

