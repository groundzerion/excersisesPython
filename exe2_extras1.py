e#parzyste czy nieparzyste

print('Podaj liczbe: ')
liczba = int(input())
reszta = liczba % 2
reszta4 = liczba % 4

if reszta == 0:
  print('Podana przez ciebie liczba jest liczba parzysta')
else:
  print('Podana przez ciebie liczba jest liczba  nieparzysta')
 
if reszta4 ==0:
  print('Podana przez ciebie liczba jest podzielna przez 4')
else:
  print('Podana przez ciebie liczba nie jest podzielna przez 4')
