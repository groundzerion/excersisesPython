#parzyste czy nieparzyste

print('Podaj liczbe: ')
liczba = int(input())
reszta = liczba % 2

if reszta == 0:
  print('Podana przez ciebie liczba jest liczba parzysta')
else:
  print('Podana przez ciebie liczba jest liczba  nieparzysta')
