from spanish2datetime.spanish2datetime import spanish2num

print('USO NORMAL')

print('Menos uno -> -1 (Out of range 0-60)')
menos_uno = spanish2num('menos_uno')
print(menos_uno)

print('Cero -> 0')
cero = spanish2num('cero')
print(cero)

print('Cinco -> 5')
cinco = spanish2num('cinco')
print(cinco)

print('Veintiuno -> 21')
veintiuno = spanish2num('veintiuno')
print(veintiuno)

print('Treinta y tres -> 33')
treinta_y_tres = spanish2num('treinta y tres')
print(treinta_y_tres)

print('Sesenta y uno -> 61 (Out of range 0-60)')
sesenta_y_uno = spanish2num('sesenta y uno')
print(sesenta_y_uno)

print('\n\nUSO CON change_ending=True')

print('Veintiun -> 21')
veintiun = spanish2num('veintiun')
print(veintiun)

print('Veintiun -> 21 (With change_ending=True)')
veintiun = spanish2num('veintiun', True)
print(veintiun)

