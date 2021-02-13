# Code for Green & Zespół Szkół Politechnicznych im. Bohaterów Monte Cassino we Wrześni

<p align="center">
  <img src="https://raw.githubusercontent.com/pawel-kapela/code-for-green-particulate-matter-concentration-website/master/public/img/logo2.png" alt="Code for Green logo">
</p>

## Platforma czujnika mierzącego zanieczyszczenie powietrza przez pyły zawieszone PM1, PM2.5, PM10

### Czym to jest?

Jest to mikrokomputer Raspberry Pi 3 B+ lub Raspberry Pi Zero W z podłączonym czujnikiem pyłów zawieszonych Plantower PMS5003.

### Jak to działa?

Platforma ta co minutę sprawdza aktualne zanieczyszczenie powietrza i wysyła wynik do bazy danych.

### Jak złożyć i skonfigurować tę platformę?

Instalacja czujnika:
- Przeprowadź podstawową konfigurację Raspberry Pi
- Aktywuj port szeregowy (UART) urządzenia używając menu wywoływanego przez polecenie ```sudo raspi-config```:
  - **Interface Options** (opcje interfejsów)
  - **Serial** (port szeregowy)
 - Zgodnie z dokumentacją [czujnika](https://botland.com.pl/czujniki-czystosci-powietrza/6797-czujnik-pylu-czystosci-powietrza-pm25-pms5003-5v-uart.html) i [mikrokomputera](https://www.raspberrypi.org/documentation/usage/gpio/) (wszystkie obok siebie w następującej kolejności: zasilanie 5V, uziemienie, GPIO 14 - TXD - wyjście, GPIO 15 - RXD - wejście), podłącz czujnik do mikrokomputera używając jego portu szeregowego

Konfiguracja skryptu i jego połączenia z bazą danych oraz zaplanowanie jego uruchomień:
- Skonfiguruj połączenie czujnika z Internetem (np. poprzez Wi-Fi)
- Pobierz plik ze skryptem z repozytorium i umieść go w dowolnym katalogu
- Uzupełnij dane potrzebne do połączenia z bazą danych w pliku skryptu
```
database = mysql.connector.connect(
    host = "<adres_hosta>",
    user = "<nazwa_użytkownika_bazy_danych>",
    passwd = "<hasło_do_bazy_danych>",
    database = "<nazwa_bazy_danych>"
    
...

query = "INSERT INTO <nazwa_tabeli> (date, pm1, pm25, pm10) VALUES (%s, %s, %s, %s)"
)
```
- Nadaj skryptowi możliwość wykonywania się używając polecenia ```chmod +x <nazwa_pliku>```
- Skonfiguruj uruchamianie skryptu co minutę poprzez zawarty w sytemie mikrokomputera program ```cron``` ([ściągawka](https://devhints.io/cron))
- Sprawdź poprawność działania całości

Gratulacje! :) Właśnie udało Ci się podłączyć i skonfigurować platformę czujnika. Jeżeli masz wątpliwości, bądź coś nie działa, skontaktuj się ze mną poprzez e-mail: pawel.kapela@protonmail.com
