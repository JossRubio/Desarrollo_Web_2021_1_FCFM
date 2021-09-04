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

head = '''
<!DOCTYPE html>
<html lang="en">
   <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title> Tarea 2 </title>
        <link rel="stylesheet" type="text/css" href="../css_T2/styles_T2.css">
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
        <script language="javascript" text="text/javascript" src="../scripts_T2/coordenadas.js"></script>
    </head>
'''

b1 = '''
   <body>
        <center><h1>Avistamiento de insectos</h1></center>
        <ul class="menu">
            <li><a href="Portada_T2.py" class="hover">Portada</a></li>
            <li><a href="../Informar_Avistamiento_T2.html" class="hover">Informar Avistamiento</a></li>
            <li><a href="Listado_T2.py" class="hover">Listado de Avistamientos</a></li>
            <li><a href="../Estadisticas_T2.html" class="hover">Estadísticas</a></li>
        </ul>
        <!-- <a href="">Portada</a> -->
        <br>
        <strong>¡Hola!</strong>, ¿sabias que debido a muchos efectos relacionados con el cambio climático muchos insectos han cambiado
        se han desplazado y se encuentran dispersos por toda la ciudad?. Como este desplazamiento ha sido nuestra responsabilidad,
        hemos diseñado esta aplicación para poder localizarlos, y de esta forma idear planes efectivos para poder reubicarlos en un
        mismo sitio :D.
        <br>
        <br>
        Para esto <strong>¡necesitamos tu ayuda!</strong>, estos bichos estan en todas partes por lo que si encuentras algunos
        ¡registralo aquí!. <strong>¡Mira!</strong>, estos son algunos de los especimenes que han registrado nuestros colaboradores :D.
        <br>
        <br>
        <center>Tenemos registros de insectos en las comunas marcadas en este mapa <strong>:DD</strong>, aleja el zoom para ver mas comunas jejeje</center>
        <br>
        <center>
        <div id="mapid" style="width: 600px; height: 400px;"></div></center>
        <br>
        <br>
        <center>
        <table>
            <tr>
                <th>Fecha - hora</th>
                <th>Comuna</th>
                <th>Sector</th>
                <th>Tipo</th>
                <th>Foto</th>
            </tr>

'''
print(head, file=utf8stdout)
print(b1, file=utf8stdout)

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

comunas_unicas = sorted(comunas_unicas)

#print(comunas_unicas, file=utf8stdout)

#print(data[-1], file=utf8stdout)
#print([data[-1][1].month ,data[-1][3]], file=utf8stdout)
#print(data[-1][2], file=utf8stdout)

#cross_test = insecto.cross_info('avistamiento', 'comuna_id, sector', 'id', 2)
#print(cross_test[0][1], file=utf8stdout)

#cross_test_2 = insecto.cross_info('foto', 'ruta_archivo', 'detalle_avistamiento_id', 2)
#print(cross_test_2[0])

# Recolectando la información de la portada de los últimos 5 avistamientos
for d in data[-5:]:
    avistamiento_id = d[-1]
    comuna_id_and_sector = insecto.cross_info('avistamiento', 'comuna_id, sector', 'id', avistamiento_id)
    comuna = insecto.cross_info('comuna', 'nombre', 'id', comuna_id_and_sector[0][0])
    sector = comuna_id_and_sector[0][1]
    fotos_det = insecto.cross_info('foto', 'ruta_archivo', 'detalle_avistamiento_id', d[0])
    row_init =f"""
    <tr>
        <th>{str(d[1])}</th>
        <th>{str(comuna[0][0])}</th>
        <th>{str(sector)}</th>
        <th>{str(d[2])}</th>
        <th>
    """
    row_foto = f"""
        """
    for k in range(fotos_det[:5].__len__()):
        row_foto_k = f"""<img src='../media/{str(fotos_det[k][0])}.jpg' width="120" height="120">"""
        row_foto += row_foto_k

    row_end = f"""</th>
    </tr>"""
    row = row_init + row_foto + row_end
    print(row, file=utf8stdout)

b2_1 = '''
        </table>
    </body>
    <script>
    // Carga de datos desde el servidor.

    let data = new FormData();
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'comunas_to_map.py')
    xhr.timeout = 700;
    xhr.onload = function (data){
        // Obtención de la data del servidor y cambio de formato.
        let data_console = data.currentTarget.responseText;
        let data_log = data_console.slice(0, data_console.length-2).replaceAll('[','');
        data_log = data_log.replaceAll(']','').replaceAll("'","");
        data_log = data_log.split(',');
        let comunas_avist = [];
        for (let i=0; i<data_log.length; i++){
            var comuna_i = data_log[i];
            if (i==0){
                comunas_avist.push(comuna_i);
            }
            else {
             comunas_avist.push(comuna_i.slice(1));
            };
        };
        console.log(comunas_avist)
    
        // Visualización del mapa
        var mymap = L.map('mapid').setView([51.505, -0.09], 13);
    
    	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    		maxZoom: 18,
    		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
    			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    		id: 'mapbox/streets-v11',
    		tileSize: 512,
    		zoomOffset: -1
    	}).addTo(mymap);
    
    	for (let k=0; k<comunas_avist.length; k++){
    	    L.marker(coordenadas[comunas_avist[k]]).addTo(mymap).bindPopup('''

b2_2 = f'''
    		"<b>Comuna: " + comunas_avist[k] + "</b> <br>"
'''

b2_3 = '''
).openPopup();
        };
    };
    '''

b2 = b2_1 + b2_2 + b2_3

b_end = f"""
    xhr.send(data)
    </script>
</html>
"""

print(b2, file=utf8stdout)
print(b_end, file=utf8stdout)