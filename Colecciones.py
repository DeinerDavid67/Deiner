#Acceso Basico

p = [12,43,23,53]
primero = p[0] #12
ultimo = p[-1] #53

#Listas Anidadas

12 = [22, true,"txt", [1, 2]]
valor = 12[3][1] #accede al 2

print(len(p))



#######################################

l = [0,1,2,3,4,5,6,7,8,9]

sub = l[2:6]

ini = l[:4]
fin = l[5:]

paso = l[::2]

neg = l[-4:-1]

#######################################


x = [12,34,654,23,34,6,3,3]

x[1] = 15

x.append(67)
x.insert(30,20)
x.extend([5,6])

x.remove(20)
n = x.pop()
x[1:4] = [26,50,48] 

######################################

persona = {

"nombre": "Deiner",
"edad": 20,
"ciudad": "Cienaga"

}
n = persona["nombre"]
