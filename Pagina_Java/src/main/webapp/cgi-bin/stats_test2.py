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

data_types = []

for k in range(data.__len__()):
    data_types.append(data[k][2])

insect_types = []

for type in data_types:
    if type in insect_types:
        continue
    else:
        insect_types.append(type)

count_types = []
for type in sorted(insect_types):
    count_types.append(data_types.count(type))

print(count_types, file=utf8stdout)