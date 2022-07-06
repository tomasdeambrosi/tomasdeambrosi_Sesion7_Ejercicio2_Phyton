'''En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. 
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación 
para calcular el tiempo que queda de trabajo.'''

import time

horaActual = time.strftime('%H')
minutoActual = time.strftime('%M')
segundoActual = time.strftime('%S')

if int(horaActual) >= 19:
    print('Es hora de que te vayas a casa')
else:
    print('Faltan {} horas, {} minutos y {} segundos para que te vayas a casa'.format(18-int(horaActual), 59-int(minutoActual), 59-int(segundoActual)))