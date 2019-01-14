## Wykonaj skrypt Pythona, działający podobnie jak kalkulator (np http://42.pl/ipcalc/)
## Dany jest adres IPv4 i liczba bitów maski.
## Wypisz w postaci binarnej i dziesiętnej:
##    - adres sieci;
##    - adres pierwszego hosta;
##    - adres ostatniego hosta;
##    - adres rozgłoszeniowy (broadcast).
## Przykład: 
## >>> wpisz IP oraz liczbę bitów maski oddzielone spacją 212.191.99.68 27
## Zakładając że maska = 11111111.11111111.11111111.11100000
## Adres sieci - uzyskujemy poprzez IP AND maska
##  ('212.191.99.64', '11010100.10111111.01100011.01000000')
## Adres pierwszego hosta - uzyskujemy poprzez (IP AND maska) + 1
##  ('212.191.99.65', '11010100.10111111.01100011.01000001')
## Adres rozgłoszeniowy - uzyskujemy poprzez IP OR (NOT maska)
##  ('212.191.99.95', '11010100.10111111.01100011.01011111')
## Adres ostatniego hosta - uzyskujemy poprzez IP OR (NOT maska) -1
##  ('212.191.99.94', '11010100.10111111.01100011.01011110')

# Import
import re

def printDecimal(table):
    return '.'.join([str(value) for value in table])

def printBinnary(table):
    return '.'.join([bin(number)[2:].zfill(8) for number in table])

# Wypisanie z klawiatury
while 1:
    try:
        ip, mask = input('Enter IP address and number of bit mask: ').split(' ')

        # Tworzenie tablicy IP i maski posieci.
        IP = [int(number) for number in ip.split('.')]
        if len(IP) != 4:
            System.err.println("Podany adres IP jest niepoprawny. Podaj wartości jeszcze raz.")
            
        Mask = [0, 0, 0, 0]

        for i in range(32):
            Mask[int(i/8)] += 2**(i%8) * (1 if (i < int(mask)) else 0)
        
        break
    except ValueError:
        System.err.println("Podano niepoprawne argumenty. Podaj adres IP w formacie [0.0.0.0] i maskę podsieci po spacji w formacie [00].")

# Adres IP sieci
networkIP = [IP[i] & Mask[i] for i in range(4)]

# Adres IP pierwszego hosta
firstIP = networkIP.copy()
firstIP[3] += 1

# Adres IP rozgłoszeniowy
broadcastIP = [networkIP[i] + abs(Mask[i]-255) for i in range(4)]

# Adres IP ostatniego hosta
lastIP = broadcastIP.copy()
lastIP[3] -= 1

# Wyświetlenie wyników

print('You entered on input:',
      '\tIP address:\t' + printDecimal(IP),
      '\t           \t' + printBinnary(IP),
      '\tAddress mask:\t' + printDecimal(Mask),
      '\t             \t' + printBinnary(Mask),
      '\nThis IP address is in network: ',
      '\tNetwork IP address:        \t' + printDecimal(networkIP),
      '\t                           \t' + printBinnary(networkIP),
      '\tFirst available IP address:\t' + printDecimal(firstIP),
      '\t                           \t' + printBinnary(firstIP),
      '\tLast available IP address: \t' + printDecimal(lastIP),
      '\t                           \t' + printBinnary(lastIP),
      '\tNetwork IP address:        \t' + printDecimal(broadcastIP),
      '\t                           \t' + printBinnary(broadcastIP),
      sep='\n')
