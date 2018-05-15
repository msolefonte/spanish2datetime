# spanish2datetime

## Description
Python3 script able to turn spanish text into datetime.

## Installation (On work)

If you already have [Python3](http://www.python.org/) on your system you can install the library simply by downloading
the distribution, unpack it and install in the usual fashion:

```bash
python3 setup.py install
```

You can also install it using a popular package manager with

```bash
pip3 install spanish2datetime
```

or

```bash
easy_install spanish2datetime
```

## Dependencies

- There is no dependencies but Python3.

## Quick Start

To get started, simply install spanish2datetime import spanish2datetime and use it:
```python
from spanish2datetime import spanish2datetime

example = 'Hoy'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(datetime))
>>> 'Hoy: 2018-05-15 13:51:48'

example = 'Mañana por la mañana'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(datetime))
>>> 'Mañana por la mañana: 2018-05-16 07:00:00'

example = 'Esta tarde'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(datetime))
>>> 'Esta tarde: 2018-05-15 14:00:00'

example = 'Ayer a las seis y media'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(datetime))
>>> 'Ayer a las seis y media: 2018-05-14 06:30:00'

example = 'El viernes que viene a las nueve de la noche'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(datetime))
>>> 'El viernes que viene a las nueve de la noche: 2018-05-18 21:00:00'

example = 'Dentro de dos semanas y cuatro días a las ocho y media de la tarde'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(datetime))
>>> 'Dentro de dos semanas y cuatro días a las ocho y media de la tarde: 2018-06-02 20:30:00'

example = 'Dentro de'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(e))
>>> TypeError: Error procesando [en/dentro de] [n] [años/año/meses/mes/semanas/semana/días/día/horas/hora
              /minutos/minuto/segundos/segundos]

example = 'Mañana a las cinco de'
datetime = spanish2datetime(example.lower().split(' '))
print(example + ': ' + str(e))
>>> TypeError: Mañana a las cinco de: Error procesando [de] [la] [mañana/tarde/noche]
```
## Documentation (On work)

https://spanish2datetime.readthedocs.io/en/latest/

## Reporting Issues

If you have suggestions, bugs or other issues specific to this library, file them [here](https://github.com/WolfyLPDC/spanish2datetime/issues). Or just send me a pull request.

## Version

- 1.0 - 15/05/2018 - Initial release.
