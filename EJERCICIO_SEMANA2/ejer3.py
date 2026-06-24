'''
Evaluación de estudiantes: 
Dado un array de estudiantes (nombre, notas[]),
calcula el promedio individual y 
muestra los que aprobaron (promedio ≥ 11) y 
su mención (suficiente, bueno, excelente). 
'''
estudiantes=[
    {"nombre": "Ana", "notas": [15,16,7]},
    {"nombre": "Pepe", "notas": [12,15,2]},
     {"nombre": "Lucho", "notas": [17,15,7]}
]
for estudiante in estudiantes:
    promedio= sum(estudiante["notas"])/len(estudiante["notas"])
    if promedio>=11:
        if promedio>=17:
            print(f"EXCELENTE - {promedio}")
        elif promedio>=15:
            print(f"BUENO- {promedio}")
        else:
            print(f"Suficiente- {promedio}")
    else:
        print("DESAPROBADO")