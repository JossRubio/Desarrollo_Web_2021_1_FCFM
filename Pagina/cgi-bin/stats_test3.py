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

month_states = []
for k in range(data.__len__()):
    month_states.append([data[k][1].month, data[k][3]])

# Obteniendo la cantidad de estados de avistamientos por mes.
states = ['no sé','vivo', 'muerto']
meses = 12
meses_estado = []
for state in states:
    for mes in range(1, meses+1):
        # Estados de avistamientos por mes.
        mes_estados = []
        for d in range(month_states.__len__()):
            if mes == month_states[d][0]:
                mes_estados.append(month_states[d][1]) # Agregando todos los estados posibles por mes.
            else:
                continue
        meses_estado.append(mes_estados.count(state))

print(meses_estado, file=utf8stdout)