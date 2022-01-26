# menza.py - Zobrazení jídelníčku menz na VUT

## provozy
 -  5 - Menza Starý pivovar
 - 10 - Menza Purkyňova
 - 18 - Pizzerie Mozzarella
 - ... (podle ID v url na [webu KAM](http://www.kam.vutbr.cz//default.aspx?p=otdo))

## Termux
Při spuštění v Termuxu dokáže vytvořit notifikaci s jídelníčkem. Vyžaduje Python a Termux API.

### Ikona na plochu
Pomocí Termuxu lze vytvořit [widgety/ikony](https://github.com/termux/termux-widget) na plochu, které spustí skript a vytvoří notifikaci s jídelníčkem. Pro příklad viz [`.shortcuts`](https://github.com/ss11mik/menza.py/tree/master/.shortcuts).

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
