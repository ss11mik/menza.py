# menza.py - Zobrazení jídelníčku menz na VUT

## provozy
 -  5 - Menza Starý pivovar
 - 10 - Menza Purkyňova
 - 18 - Pizzerie Mozzarella
 - ... (podle ID v url na [webu KAM](http://www.kam.vutbr.cz//default.aspx?p=otdo))

## Termux
Při spuštění v Termuxu dokáže vytvořit notifikaci s jídelníčkem. Vyžaduje Python a Termux API.

## použití
```
usage: menza.py [-h] [-b] [-t] [provoz]

positional arguments:
  provoz           ID provozu (5 - 28)

optional arguments:
  -h, --help       show this help message and exit
  -b, --no-bageta  Vynechat bagety
  -t, --terumx     Zobrazit notifikaci (pouze pro Termux)
```
