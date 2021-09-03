#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb;

cgitb.enable()
from validador_servidor import Insecto

print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

insecto = Insecto(host="localhost", user="root", password="", database="tarea2")
data_list = insecto.get_info("avistamiento")

head = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Listado de Avistamientos</title>
        <link rel="stylesheet" href="../css_T2/styles_T2.css">
        <script defer src="../scripts_T2/pops_listados.js"></script>
    </head>
'''

b1 = '''
<body>
    <center><h1>Listado de Avistamientos</h1></center>
    <ul class="menu">
        <li><a href="Portada_T2.py" class="hover">Portada</a></li>
        <li><a href="../Informar_Avistamiento_T2.html" class="hover">Informar Avistamiento</a></li>
        <li><a href="Listado_T2.py" class="hover">Listado de Avistamientos</a></li>
        <li><a href="../Estadisticas_T2.html" class="hover">Estadísticas</a></li>
    </ul>
    <br>
    <div class="texto_listado">
      Los registros se encuentran en la siguiente lista:
    </div>
    <br>
    <center>
    <table id="rows" style="display: table">
        <tr>
            <th>Fecha - hora </th>
            <th> Comuna </th>
            <th> Sector </th>
            <th> Nombre Contacto </th>
            <th> Total Avistamientos </th>
            <th> Total Fotos </th>
        </tr>
'''

print(head, file=utf8stdout)
print(b1, file=utf8stdout)


b_element = '''
   <center>
   <table id="filas" style="display: table">
     <tr id="fila_names" onclick="hide('filas'), pop('fila_info', 'block');" class="hover">
       <th> Fecha - hora </th>
       <th> Comuna </th>
       <th> Sector </th>
       <th> Nombre Contacto </th>
       <th> Total Avistamientos </th>
       <th> Total Fotos </th>
     </tr>
     <tr id="fila_1" onclick="hide('filas'), pop('fila_avistamiento_1', 'block');" class="hover">
         <td>2021-02-05 <p>14:53</p> </td>
         <td>Puente Alto</td>
         <td>Concha y Toro</td>
         <td>José Rubio</td>
         <td>5</td>
         <td>10</td>
     </tr>
     <tr id="fila_2" onclick="hide('filas'), pop('fila_avistamiento_2', 'block');" class="hover">
         <td>2021-02-28 <p>12:55</p> </td>
         <td>Puente Alto</td>
         <td>Concha y Toro</td>
         <td>Maria</td>
         <td>4</td>
         <td>12</td>
     </tr>
   </table>
   <div id="fila_info" style="display: none">
     <h3><strong>Lugar</strong></h3>
     <div class="section_list">
     <div class="entrada"><strong>Región:</strong> Metropolitana</div>
     <div class="entrada"><strong>Comuna:</strong> Puente Alto</div>
     <div class="entrada"><strong>Sector:</strong> Cerca de mi casa</div>
     </div>
     <br>
     <h3><strong>Datos de Contacto</strong></h3>
     <div class="section_list">
     <div class="entrada"><strong>Nombre:</strong> José Rubio</div>
     <div class="entrada"><strong>Email:</strong> jose.rubio@ug.uchile.cl</div>
     <div class="Celular"><strong>Celular:</strong> 9782286</div>
     </div>
     <br>
     <h3><strong>Avistamientos</strong></h3>
     <div class="section_list">
     <center><strong>1</strong></center>
     <br>
     <div class="entrada"><strong>Fecha:</strong> 2021/05/28 15:05:47</div>
     <div class="entrada"><strong>Tipo:</strong> Insecto</div>
     <div class="entrada"><strong>Estado:</strong> Vivo</div>
     <br>
     <div class="entrada"><strong>Imágenes:</strong></div>
     <div class="entrada"><img src="../Imagenes/libelula.jpg" height="200" width="200"></div>
     <div class="entrada"><img src="../Imagenes/elbicho.jpeg" height="200" width="200"></div>
     </div>
     <div class="section_list">
     <center><strong>2</strong></center>
     <br>
     <div class="entrada"><strong>Fecha:</strong> 2021/04/05 18:04:15</div>
     <div class="entrada"><strong>Tipo:</strong> Aracnido</div>
     <div class="entrada"><strong>Estado</strong> Muerto</div>
     <br>
     <div class="entrada"><strong>Imágenes:</strong></div>
     <div class="entrada"><img src="../Imagenes/saltamontes.jpg" height="200" width="200"></div>
     </div>
     <br>
     <button type="button" onclick="hide('fila_info'), pop('filas', 'table');">Ocultar avistamiento</button>
     <button type="button"><a href="Portada_T2.py">Volver a la Portada</a> </button>
   </div>
   <div id="fila_avistamiento_1" style="display: none">
     Info avistamiento 1
     <br>
     <button type="button" onclick="hide('fila_avistamiento_1'), pop('filas', 'table');">Ocultar avistamiento</button>
     <button type="button"><a href="Portada_T2.py">Volver a la Portada</a> </button>
   </div>
   <div id="fila_avistamiento_2" style="display: none">
     Info avistamiento 2
     <br>
     <button type="button" onclick="hide('fila_avistamiento_2'), pop('filas');">Ocultar avistamiento</button>
     <button type="button"><a href="Portada_T2.py">Volver a la Portada</a> </button>
   </div>
   </center>
'''

#print(b_element, file=utf8stdout)

# Invirtiendo el orden al mostrar la información.

data_list.reverse()

# Iteración para la obtención de la información
for d in data_list:
    comuna_d = insecto.cross_info("comuna", "nombre, region_id", "id", d[1])
    region_d = insecto.cross_info("region", "nombre", "id", comuna_d[0][1])
    det_ids_d = insecto.cross_info("detalle_avistamiento", "id, dia_hora, tipo, estado",
                                   "avistamiento_id", d[0])
    photos_d = []
    photos_q = []
    for i in range(det_ids_d.__len__()):
        fotos_i = insecto.cross_info("foto", "ruta_Archivo", "detalle_avistamiento_id", det_ids_d[i][0])
        photos_d.append(fotos_i)        # Incluyendo las rutas de archivos de las imagenes
        photos_q.append(fotos_i.__len__())
    row_init = f"""
    
      <tr id="fila_avistamiento_{str(d[0])}" onclick="hide('rows'), pop('info_{str(d[0])}','block');" class="hover">
          <td>{str(d[2])}</td>
          <td>{comuna_d[0][0]}</td>
          <td>{d[3]}</td>
          <td>{str(d[4])}</td>
          <td>{str(det_ids_d.__len__())}</td>
          <td>{str(sum(photos_q))}</td>
      </tr>
    """
    # Información del avistamiento.

    row_info_init = f"""
    <div id="info_{str(d[0])}" style="display: none">
        <strong>Lugar</strong>
        <div class="section_list">
            <div class="entrada"><strong>Región: </strong>{str(region_d[0][0])}</div>
            <div class="entrada"><strong>Comuna: </strong>{str(comuna_d[0][0])}</div>
            <div class="entrada"><strong>Sector: </strong>{str(d[3])}</div>
        </div>
        <br>
        <h3><strong>Datos de Contacto</strong></h3>
        <div class="section_list">
            <div class="entrada"><strong>Nombre: </strong>{str(d[4])}</div>
            <div class="entrada"><strong>Email: </strong>{str(d[5])}</div>
            <div class="entrada"><strong>Celular: </strong>{str(d[6])}</div>
        </div>
        <br>
        <h3><strong>Avistamientos</strong></h3>
    """
    row_info_avist = f""""""

    for k in range(det_ids_d.__len__()):
        row_info_avist_k_init = f"""
        <div class="section_list">
        <center><strong>Avistamiento {str(k+1)}</strong></center>
        <div class="entrada"><strong>Dia hora: </strong>{str(det_ids_d[k][1])}</div>
        <div class="entrada"><strong>Tipo: </strong>{str(det_ids_d[k][2])}</div>
        <div class="entrada"><strong>Estado: </strong>{str(det_ids_d[k][3])}</div>
        <br>
        <div class="entrada"><strong>Imágenes</strong></div>
        """

        row_info_avist_k_photo = f""""""
        for photos_k in photos_d[k]:
            for photo in photos_k:
                pic = f"""
                <div class="entrada"><img src="../media/{str(photo)}.jpg" height="200" width="200"></div>
                """
                row_info_avist_k_photo += pic

        row_info_avist_k_end = f"""
        </div>
        """
        row_info_avist += row_info_avist_k_init + row_info_avist_k_photo + row_info_avist_k_end
    row_info_end = f"""
    <br>
    <button type="button" onclick="hide('info_{str(d[0])}'), pop('rows', 'table');">Ocultar avistamiento</button>
    <button type="button"><a href="Portada_T2.py">Volver a la Portada</a> </button>
    </div>
    """
    row_info = row_info_init + row_info_avist + row_info_end
    row = row_init + row_info
    print(row, file=utf8stdout)

# Información del avistamiento.


b_end = """
    </center>
    </table>
    </body>
</html>
"""
print(b_end, file=utf8stdout)