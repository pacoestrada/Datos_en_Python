#copiamos el diccionario de donde sacaremos los datos.

personal = {
 '09514247N': {"perfil": ["desarrollador de software","cocina" ],
               'edad': 28,
               'salario': 35000,
               "incorporación": 2005,
               "empresa_ant": "IBM",
               "pais": "España"},
 '12547895E': {"perfil": ["desarrollador de software", "control de calidad"  ],
               'edad': 28,
               'salario': 28000,
               "pais": "España"},
 '01235842B': {"perfil": [ "gestión logística","control de calidad", "transporte"],
               'edad': 28,
               'salario': 47000,
               "empresa_ant": "Amazon",
               "pais": "España"},
 '47854141S': {"perfil": [ "inventario","control de calidad", "gestión de proyectos"  ],
               'edad': 28,
               'salario': 50000,
               "incorporación": 2000,
               "pais": "España"},
 '12345678G': {'edad': 28,
               'salario': 62000,
               "pais": "España"},
 '56789023T': {"perfil": ["desarrollador de videojuegos" ],
               'edad': 28,
               'salario': 29000,
               "pais": "España"}
}
#accedemos al diccionario utilizando el NIF '56789023T', y actualizamos el valor de la clave 'salario' multiplicándolo por 1.1 (lo que equivale a un incremento del 10%).

personal['56789023T']['salario'] *= 1.1
#si quisieramos imprimir el nuevo salario descomentamos las siguientes dos líneas este código

nuevo_salario = personal['56789023T']['salario']
print (int(nuevo_salario))
