# 1.  Declarate set()
my_set = set()

# 2, Coercion explicita to List to Tuple
my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)

# 3. sets() methods:
"""
add(value): agrega un valor único al set. Si se intenta agregar un valor que ya existe en el set, no ocurrirá ningún cambio.

remove(value): elimina un valor específico del set. Si el valor no existe, se generará un error.

discard(value): elimina un valor específico del set. Si el valor no existe, no se genera ningún error.

pop(): elimina y devuelve un elemento aleatorio del set.

clear(): vacía completamente el set.

len(): devuelve la cantidad de elementos que existen en el set.
"""

my_set = set()

# Agregar elementos al set
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.add(5)
my_set.add((3, 2, 1))

# Imprimir el set
print(my_set)  # Output: {1, 2, 3}

# Delete with pop()
my_set.pop()
print(f"After pop() method: {my_set}")

# Delete with remove()
my_set.remove(3)
print(f"After remove() method: {my_set}") # Traceback KeyError 1

# Delete with discord()
my_set.discard(1)
print(f"After discord() method: {my_set}") # Traceback KeyError 1

# Verificar si un elemento existe en el set
print(2 in my_set)  # Output: True

# Eliminar un elemento del set
my_set.remove(2)

# Verificar si un elemento existe en el set después de ser eliminado
print(2 in my_set)  # Output: False

# Vaciar el set
my_set.clear()

# Verificar el tamaño del set después de ser vaciado
print(len(my_set))  # Output: 0



# 4. Iterar sobre los elementos del set
# Create set()
my_set = {1, 2, 3, 4, 5}
print(type(my_set))
for element in my_set:
    print(element)

# Usando slice syntax
# Iterar sobre los elementos del set a partir del segundo elemento
for item in list(my_set)[1:]:
    print(item)


# 5.  Las intersecciones: método intersection() o el operador &.
# elementos presentes en dos o más sets al mismo tiempo
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1)
print(set2)

# Usando el método intersection()
intersection = set1.intersection(set2)
print(intersection)  # Output: {4, 5}

# Usando el operador &
intersection = set1 & set2
print(f"a & b:  {intersection}")  # Output: {4, 5}

# 6. método  union() o usando el operador: |
# No inserta elementos repetidos")
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print(a)
print(b)
# union = a | b 
union = a.union(b) 
print(f"a | b:  {union}") #{1, 2, 3, 4, 6, 8}

# 7. difference()) methods de conjuntos o usando el operador: -

# diferenciayb = a - b
diferenciayb = a.difference(b)
print("a - b:", diferenciayb)  # Output: {1, 3}

diferencibya = b - a
print("b - a:", diferencibya)  # Output: {8, 6}

# 8. print("5.4 diferencia simétrica de conjuntos usando el operador: ^
# es el conjunto que contiene los elementos de A y B que no son comunes.
#usando el operador ^
difsimetrica = a ^ b
print("a ^ b:", difsimetrica)  # Output: {1, 3, 6, 8}