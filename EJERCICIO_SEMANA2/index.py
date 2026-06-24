'''
Sistema de clasificación de rendimiento: 
Solicita al usuario su nota (0-20) y 
su asistencia (%). Si la nota es mayor 
o igual a 11 y la asistencia es mayor o
igual al 70%, se aprueba. De lo contrario, 
se desaprueba. Además, otorga menciones especiales
para notas mayores a 17 con asistencia completa.
'''
nota= float(input("Ingresa la nota: "))
asistencia= float(input("Ingresa la asistencia: "))

if nota>=11 and asistencia>=70:
    print("Aprobado")
    if asistencia==100 and nota>=17:
        print("Especial")
else:
    print("Desaprobaste")
