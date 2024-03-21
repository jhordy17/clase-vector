# punto 1
lista1 = list()

# punto 2
lista2 = [1,2,3,4,5,6,7,8,9]
print('///LA LISTA ES:///')
print(lista2)

# punto 3
print('tamaño de la lista:',len(lista2))
      
# punto 4      
print('primer elemento es:',lista2[0],'elemento central:',lista2[4],'ultimo elemento:',lista2[8])

# punto 5
Tipos_de_datos_mezclados = ['jhordin','19','166cm','soltero','pozon/14 de febrero']
print(Tipos_de_datos_mezclados)

# punto 6
it_companies = ['Facebook', 'Google','Microsoft','Apple', 'IBM','Oracle','Amazon']
print(it_companies)

# punto 7
it_companies.append('Instagram')
print(it_companies)

#punto 8
print(it_companies.index('Google')) 
 
#punto 9
print(sorted(it_companies))

# punto 10
it_companies.sort(reverse=True) 
print(it_companies)

# punto 11
it_companies.pop(0)
print(it_companies)

# punto 12
it_companies.clear()
print(it_companies)