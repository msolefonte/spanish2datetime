from spanish2datetime.spanish2datetime import spanish2datetime


for example in ['Hoy', 'Mañana por la mañana', 'Esta tarde', 'Ayer a las seis y media', 'El viernes que viene a las '
                'nueve de la noche', 'Dentro de dos semanas y cuatro días a las ocho y media de la tarde', 'Dentro de',
                'Mañana a las cinco de']:
    print(example + ': ' + str(spanish2datetime(example.lower().split(' '))))