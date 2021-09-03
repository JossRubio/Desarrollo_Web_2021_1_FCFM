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

dates = []
for k in range(data.__len__()):
    dates.append(data[k][1])

days = []
for k in range(dates.__len__()):
    try:
        days.append(dates[k].day)
    except:
        continue

days_array = []
days_month = 30
for k in range(days_month):
    days_array.append([k+1, days.count(k+1)])

print(days_array, file=utf8stdout)