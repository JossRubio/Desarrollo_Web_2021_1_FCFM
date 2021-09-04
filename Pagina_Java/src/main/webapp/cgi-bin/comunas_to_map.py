#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb;

cgitb.enable()
from validador_servidor import Insecto

print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

insecto = Insecto(host="localhost", user="root", password="", database="tarea2")
data = insecto.get_info("detalle_avistamiento")
data_avist = insecto.get_info('avistamiento')

comunas_avist = []

for k in range(data_avist.__len__()):
    comuna_nombre = insecto.cross_info('comuna', 'nombre', 'id', data_avist[k][1])
    comunas_avist.append(comuna_nombre[0][0])

comunas_unicas = []

for com in comunas_avist:
    if com in comunas_unicas:
        continue
    else:
        comunas_unicas.append(com)

print(sorted(comunas_unicas), file=utf8stdout)