from spanish2datetime.spanish2datetime import spanish2datetime

print('# CORRECT USE')

example = 'Mañana por la mañana'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(datetime))

example = 'Esta tarde'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(datetime))

example = 'Ayer a las seis y media'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(datetime))

example = 'El viernes que viene a las nueve de la noche'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(datetime))

example = 'Dentro de dos semanas y cuatro días a las ocho y media de la tarde'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(datetime))

print('\n\n# EXCEPTIONS')

example = 'Dentro de'
try:
    datetime = spanish2datetime(example.lower().split(' '))
except TypeError as e:
    print(example + ': ' + str(e))

example = 'Mañana a las cinco de'
try:
    datetime = spanish2datetime(example.lower().split(' '))
except TypeError as e:
    print(example + ': ' + str(e))

example = 'A las och'
try:
    datetime = spanish2datetime(example.lower().split(' '))
except TypeError as e:
    print(example + ': ' + str(e))

example = 'A las seis y'
try:
    datetime = spanish2datetime(example.lower().split(' '))
except TypeError as e:
    print(example + ': ' + str(e))