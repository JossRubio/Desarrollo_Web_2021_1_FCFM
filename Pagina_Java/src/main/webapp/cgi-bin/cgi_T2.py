#!/usr/bin/python3
import cgi
import cgitb
from validador_servidor import Insecto

cgitb.enable()

print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage()
insecto = Insecto(host="localhost",user="root", password="", database="tarea2")

keys_list_sorted = sorted(form.keys())

n_avistamientos = 0

for key in keys_list_sorted:
    last_character = key[-1]
    try:
        q_avistamiento = int(last_character)
        n_avistamientos += 1
    except:
        if n_avistamientos >= 1:
            break
        else:
            continue


# Iteración para la obtención de una lista con la cantidad de fotos por avistamientos detectados.
fotos_avistamiento = []

for k in range(keys_list_sorted.__len__()):
    key = keys_list_sorted[k]       # Llave actual a evaluar
    key_post = keys_list_sorted[k+1]        # Llave posterior
    if key[:-2] == 'foto-avistamiento':     # Evaluando las condiciones si la llve corresponde a las fotos
        avistamiento_actual = int(key[-2])
        q_fotos = int(key[-1])
        try:
            future_avistamiento = int(key_post[-2])
            if avistamiento_actual == future_avistamiento:  # Si la proxima llave tiene el mismo avistamiento, entonces sigue
                continue
            else:
                fotos_avistamiento.append(q_fotos)  # En caso contrario guarda el ultimo valor obtenido
        except:
            try:
                future_foto = int(key_post[-1])     # Analizando si es posible convertir la siguiente variable a un entero
            except:
                fotos_avistamiento.append(q_fotos)
                break
    else:
        continue

# Separando la data recibida en 3 tuplas

# Datos de contacto
data = (
    form['comuna'].value, form['dia-hora-avistamiento1'].value, form['sector_inp'].value,
    form['nombre'].value, form['email'].value, form['celular'].value
)

# Datos de avistamiento
data_avist = ()

for k in range(n_avistamientos):
    dia_k = form['dia-hora-avistamiento'+str(k+1)].value
    tipo_k = form['tipo-avistamiento-'+str(k+1)].value
    estado_k = form['estado-avistamiento-'+str(k+1)].value
    data_avist += (dia_k, tipo_k, estado_k)


data_fotos = ()
k = 1

for i in fotos_avistamiento:
    for j in range(i):
        foto_avist = form['foto-avistamiento'+str(k)+str(j+1)]
        data_fotos += (foto_avist,)
    k += 1

#print(data_fotos)
#print('Avistamientos:')
#print(n_avistamientos)
#print('---')
#print('Fotos')
#print(fotos_avistamiento)

insecto.save_avistamiento(data=data, data_avist=data_avist, data_foto=data_fotos, avistamientos=n_avistamientos,
                          fotos=fotos_avistamiento)

#print(data_fotos)
#print('Avistamientos:')
#print(n_avistamientos)
#print('---')
#print('Fotos')
#print(fotos_avistamiento)
html_sucess = f'''
    <!DOCTYPE html>
<html lang="en">
   <head>
        <meta charset="UTF-8">
        <title> Tarea 2 </title>
        <link rel="stylesheet" href="../css/styles_T2.css">
        <style>
            
        </style>
    </head>
    <body>
        <center><h1>Avistamiento de insectos</h1></center>
        <ul class="menu">
            <li><a href="Portada_T2.py" class="hover">Portada</a></li>
            <li><a href="../Informar_Avistamiento_T2.html" class="hover">Informar Avistamiento</a></li>
            <li><a href="Listado_T2.py" class="hover">Listado de Avistamientos</a></li>
            <li><a href="../Estadisticas_T2.html" class="hover">Estadísticas</a></li>
        </ul>
        <center>
        <div class="section_list">
            <center> <strong>Información enviada con éxito! </strong></center>
        </div>
        <br>
        <br>
        <button type="button"><a href="../Informar_Avistamiento_T2.html">Informar otro avistamiento</a> </button>
        <button type="button"><a href="Portada_T2.py">Volver a la Portada</a> </button>
        </center>
    </body>
</html>
'''
print(html_sucess, file=utf8stdout)