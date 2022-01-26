#!/usr/bin/env python3
#
# Parser jidelnicku menz VUT pro Termux
# po spusteni zobrazi aktualni jidelnicek v notifikaci
#
# krome Python3 (a knihoven viz nize) vyzaduje Termux-API
#
# pouziti: python3 menza.py [-b] [-t] id_menzy
# (c) ss11mik, 2021-2022

# TODOs
#  ceny
#  slozeni
#  samostatne notifikace pro kazde jidlo


try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import urllib.request
import re
import os
import sys
import argparse


parser = argparse.ArgumentParser(usage=None)

parser.add_argument('provoz',
                    help='ID provozu (5 - 28)',
                    nargs='?')

parser.add_argument('-b',
                    '--no-bageta',
                    action='store_true',
                    default=False,
                    dest='i_dont_like_bageta',
                    help='Vynechat bagety',
                    required=False)

parser.add_argument('-t',
                    '--terumx',
                    action='store_true',
                    default=False,
                    dest='termux',
                    help='Zobrazit notifikaci (pouze pro Termux)',
                    required=False)


args = parser.parse_args()

i_dont_like_bageta = args.i_dont_like_bageta
termux = args.termux

provoz = args.provoz
if provoz == None:
    print("zadejte cislo provozu: ", end="")
    provoz = input()

parsed_menu = ""



try:
    with urllib.request.urlopen('http://www.kam.vutbr.cz/?p=menu&provoz={}'.format(provoz)) as f:
        html = f.read().decode('utf-8')
        parsed_html = BeautifulSoup(html, "html.parser")
except urllib.error.URLError:
    print("Chyba pripojeni.")
    exit(2)

try:
    menu = parsed_html.body.find('script', attrs={'type' : 'text/javascript'}).text
    provoz_jmeno = str(parsed_html.body.find('h1')).split("<br/>")[0].replace("<h1>", "")
except AttributeError as e:
    err_msg = "Stravovací provoz je zavřený nebo nastala chyba."

    print(err_msg)
    os.system('termux-notification -t "{}"'.format(err_msg))

    exit(3)


menu = menu.split("\r\n")

for i in range(len(menu)):
    menu[i] = menu[i].lstrip()

    menu[i] = re.sub(r'^a\[[0-9]\]', '', menu[i])

    if menu[i].startswith(" = \"<b>"):
        menu[i] = re.sub(r' = "<b>', '', menu[i])
        menu[i] = str(menu[i][:menu[i].index("</b>")])

        if i_dont_like_bageta and menu[i] == "Bageta" or  menu[i] == "Bageta special":
            pass
        else:
            parsed_menu += (menu[i]) + '\n'

parsed_menu = parsed_menu.rstrip()



if termux:
    os.system('termux-notification -t "{}" -c "{}"'.format(provoz_jmeno, parsed_menu))
else:
    print("{}:".format(provoz_jmeno))
    print(parsed_menu)
