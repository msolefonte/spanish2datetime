from datetime import datetime, timedelta

numbers_spanish = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once',
                   'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve', 'veinte',
                   'veintiuno', 'veintidós', 'veintitrés', 'veinticuatro', 'veinticinco', 'veintiséis', 'veintisiete',
                   'veintiocho', 'veintinueve', 'treinta', 'treinta y uno', 'treinta y dos', 'treinta y tres',
                   'treinta y cuatro', 'treinta y cinco', 'treinta y seis', 'treinta y siete', 'treinta y ocho',
                   'treinta y nueve', 'cuarenta', 'cuarenta y uno', 'cuarenta y dos', 'cuarenta y tres',
                   'cuarenta y cuatro', 'cuarenta y cinco',  'cuarenta y seis', 'cuarenta y siete', 'cuarenta y ocho',
                   'cuarenta y nueve', 'cincuenta', 'cincuenta y uno', 'cincuenta y dos', 'cincuenta y tres',
                   'cincuenta y cuatro', 'cincuenta y cinco', 'cincuenta y seis', 'cincuenta y siete',
                   'cincuenta y ocho', 'cincuenta y nueve', 'sesenta']


def spanish2num(number, change_ending=False):
    """
    Turns spanish text into integer. Available numbers between 0 and 60, both included.

    :param number: String to turn into integer. Must be lower case.
    :param change_ending: Numbers ended in 'uno' are replaced by numbers ended in 'un'. For example: 'cuarenta y uno' is
    turned into 'cuarenta y un'.
    :returns integer: If there is a valid result.
    :returns None: If there is not.
    """
    if not change_ending:
        result = [i for i, num in enumerate(numbers_spanish) if num == number]
    else:
        result = [i for i, num in enumerate(numbers_spanish) if num.replace('uno', 'un') == number]
    if result:
        return result[0]
    return None


def spanish2datetime(sentence, pos=0, date=None):
    """
    Turns list of spanish text into datetime.

    :param sentence: List of words to analyze. Must be lowercase. For example: ['esta', 'mañana']
    :param pos: Current position, for recursive use.
    :param date: Current date, for recursive use.
    :return: DateTime that matches sentence.
    :raises TypeError: Error processing text. Exceptions are self explained.
    """
    if not date:
        date = datetime.now().replace(microsecond=0)
    try:
        if sentence[pos] == '':
            return date
    except IndexError:
            return date
    if sentence[pos] == 'luego':
        return date + timedelta(minutes=20)
    if sentence[pos] == 'hoy':
        return spanish2datetime(sentence, pos + 1, date)
    if sentence[pos] == 'ayer':
        return spanish2datetime(sentence, pos + 1, date + timedelta(days=-1))
    if sentence[pos] == 'mañana':
        return spanish2datetime(sentence, pos + 1, date + timedelta(days=1))
    if sentence[pos] == 'pasado':
        return spanish2datetime(sentence, pos+1, date + timedelta(weeks=-1))
    if sentence[pos] == 'el':
        try:
            pos += 1
            weekday = 0
            for day in ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']:
                if sentence[pos] == day:
                    days_ahead = weekday - date.weekday()
                    if days_ahead <= 0:
                        days_ahead += 7
                    return spanish2datetime(sentence, pos + 1, date + timedelta(days_ahead))
                weekday += 1
        except IndexError:
            pass
        raise TypeError('Error procesando [el] [{dia_semana}]')
    if sentence[pos] == 'por':
        try:
            pos += 2
            if sentence[pos] == 'mañana':
                date = date.replace(hour=7, minute=0, second=0)
            elif sentence[pos] == 'tarde':
                date = date.replace(hour=14, minute=0, second=0)
            elif sentence[pos] == 'noche':
                date = date.replace(hour=20, minute=0, second=0)
            else:
                raise TypeError('Error procesando [por] [la] [mañana/tarde/noche]')
            return spanish2datetime(sentence, pos+1, date)
        except TypeError:
            raise TypeError('Error procesando [por] [la] [mañana/tarde/noche]')
    if sentence[pos] == 'a':
        try:
            pos += 1
            if sentence[pos] == 'mediodía':
                date = date.replace(hour=12, minute=0, second=0)
                return spanish2datetime(sentence, pos + 1, date)
            if sentence[pos] == 'medianoche':
                date = date.replace(hour=0, minute=0, second=0) + timedelta(1)
                return spanish2datetime(sentence, pos + 1, date)
            if sentence[pos] != 'y' and sentence[pos] != 'menos':
                pos += 1
                if sentence[pos] == 'una':
                    sentence[pos] = 'uno'
                try:
                    hour = spanish2num(sentence[pos])
                    date = date.replace(hour=hour, minute=0, second=0)
                except TypeError:
                    pass
                return spanish2datetime(sentence, pos + 1, date)
            return spanish2datetime(sentence, pos, date)
        except IndexError:
            raise TypeError('Error procesando [a] [mediodía/medianoche/{hora}]')
    if sentence[pos] == 'y' or sentence[pos] == 'menos':
        try:
            add = True
            square = False
            try:
                if sentence[pos - 1] == 'a':
                    add = False
                    if pos == 1:
                        square = True
            except TypeError:
                pass
            if sentence[pos] == 'y':
                mode = 1
            else:
                mode = 2
            pos += 1
            if sentence[pos] == 'cuarto':
                minutes = 15
            elif sentence[pos] == 'media':
                minutes = 30
            else:
                minutes = None
                if len(sentence) - pos > 2:
                    minutes = spanish2num(sentence[pos] + ' y ' + sentence[pos + 2])
                    if minutes:
                        pos += 2
                if not minutes:
                    minutes = spanish2num(sentence[pos])
            if add:
                if mode == 1:
                    return spanish2datetime(sentence, pos + 1, date + timedelta(minutes=minutes))
                else:
                    return spanish2datetime(sentence, pos + 1, date + timedelta(minutes=-minutes))
            else:
                if mode == 1:
                    date = date.replace(minute=minutes, second=0)
                else:
                    date = date.replace(minute=60-minutes, second=0)
                if square and date < date.now():
                    date += timedelta(hours=1)
                return spanish2datetime(sentence, pos + 1, date)
        except (TypeError, IndexError):
            raise TypeError('Error procesando [y/menos] [media/cuarto/{hora}]')
    if sentence[pos] == 'de':
        try:
            pos += 2
            if sentence[pos] == 'mañana':
                return spanish2datetime(sentence, pos + 1, date)
            elif sentence[pos] == 'tarde':
                return spanish2datetime(sentence, pos + 1, date + timedelta(hours=12))
            elif sentence[pos] == 'noche':
                if date.hour > 6:
                    date += timedelta(hours=12)
                return spanish2datetime(sentence, pos + 1, date)
        except IndexError:
            raise TypeError('Error procesando [de] [la] [mañana/tarde/noche]')
    if sentence[pos] == 'en' or sentence[pos] == 'dentro':
        if sentence[pos] == 'dentro':
            pos += 1
        pos += 1
        first_solved = False
        first_row = True
        while True:
            try:
                pos_temp, change = pos + 1, -1
                while change < 0 and pos_temp < len(sentence):
                    change_index = 0
                    for value in ['años', 'año', 'meses', 'mes', 'semanas', 'semana', 'días', 'día', 'horas', 'hora',
                                  'minutos', 'minuto', 'segundos', 'segundo']:
                        if sentence[pos_temp] == value:
                            change = int(change_index/2)
                            break
                        change_index += 1
                    pos_temp += 1
                if change < 0:
                    raise TypeError('Error procesando [en/dentro de] [n] [años/año/meses/mes/semanas/semana/días'
                                    '/día/horas/hora/minutos/minuto/segundos/segundos]')
                num = ''
                while pos < pos_temp - 1:
                    num += sentence[pos] + ' '
                    pos += 1
                value = spanish2num(num[:-1].replace('una', 'un'), True)
                if not value:
                    raise TypeError('Error procesando [en/dentro de] [n] [años/año/meses/mes/semanas/semana/días'
                                    '/día/horas/hora/minutos/minuto/segundos/segundos]')
                if change == 0:  # Years
                    date = date.replace(year=date.year + value, minute=0, second=0)
                elif change == 1:  # Months
                    date = date.replace(month=date.month + value, minute=0, second=0)
                elif change == 2:  # Weeks
                    date += timedelta(weeks=value)
                    date = date.replace(minute=0, second=0)
                elif change == 3:  # Days
                    date += timedelta(days=value)
                    date = date.replace(minute=0, second=0)
                elif change == 4:  # Hours
                    date += timedelta(hours=value)
                    date = date.replace(second=0)
                elif change == 5:  # Minutes
                    date += timedelta(minutes=value)
                elif change == 6:  # Seconds
                    date += timedelta(seconds=value)
                first_solved = True
                pos += 1
                pos_temp = pos
                if sentence[pos_temp] == 'y':
                    first_row = False
                    pos += 1
                    pos_temp += 1
                    if sentence[pos_temp] == 'medio' or sentence[pos_temp] == 'media':
                        if change == 0:  # Years
                            date = date.replace(month=date.month + 6, minute=0, second=0)
                        elif change == 1:  # Months
                            date += timedelta(days=14)
                        elif change == 2:  # Weeks
                            date += timedelta(days=4)
                        elif change == 3:  # Days
                            date += timedelta(hours=12)
                        elif change == 4:  # Hours
                            date += timedelta(minutes=30)
                        elif change == 5:  # Minutes
                            date += timedelta(seconds=30)
                        elif change == 6:  # Seconds
                            date += timedelta(milliseconds=500)
                        return spanish2datetime(sentence, pos_temp + 1, date)
                else:
                    return spanish2datetime(sentence, pos, date)
            except IndexError:
                if not first_row:
                    return spanish2datetime(sentence, pos, date)
                else:
                    if first_solved:
                        return date
                    else:
                        raise TypeError('Error procesando [en/dentro de] [n] [años/año/meses/mes/semanas/semana/días'
                                        '/día/horas/hora/minutos/minuto/segundos/segundos]')
    if sentence[pos] == 'que':
        try:
            pos += 1
            if sentence[pos] == 'viene':
                return spanish2datetime(sentence, pos + 1, date)
        except IndexError:
            raise TypeError('Error procesando [que] [viene]')
    if sentence[pos] == 'esta':
        try:
            pos += 1
            if sentence[pos] == 'mañana':
                return spanish2datetime(sentence, pos + 1, date.replace(hour=7, minute=0, second=0))
            if sentence[pos] == 'tarde':
                return spanish2datetime(sentence, pos + 1, date.replace(hour=14, minute=0, second=0))
            if sentence[pos] == 'noche':
                return spanish2datetime(sentence, pos + 1, date.replace(hour=20, minute=0, second=0))
        except IndexError:
            raise TypeError('Error procesando [esta] [mañana/tarde/noche]')

    tail = ''
    while pos < len(sentence):
        tail += sentence[pos] + ' '
        pos += 1
    raise TypeError('Error procesando ' + tail[:-1])
