#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb;

cgitb.enable()
from validador_servidor import Insecto

print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

insecto = Insecto(host="localhost", user="root", password="", database="tarea2")
data = insecto.get_info('detalle_avistamiento')

head = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Estadisticas de los Avistamientos</title>
        <link rel="stylesheet" href="../css/styles_T1.css">
        <script language="javascript" type="text/javascript" src="http://www.flotcharts.org/flot/source/jquery.js"></script>
        <script language="javascript" type="text/javascript" src="http://www.flotcharts.org/flot/source/jquery.canvaswrapper.js"></script>
        <script language="javascript" type="text/javascript" src="http://www.flotcharts.org/flot/source/jquery.colorhelpers.js"></script>
        <script language="javascript" type="text/javascript" src="http://www.flotcharts.org/flot/source/jquery.flot.js"></script>
        <script language="javascript" type="text/javascript" src="http://www.flotcharts.org/flot/source/jquery.flot.saturated.js"></script>
        <script language="javascript" type="text/javascript" src="http://www.flotcharts.org/flot/source/jquery.flot.browser.js"></script>
        <script language="javascript" type="text/javascript" src="http://www.flotcharts.org/flot/source/jquery.flot.drawSeries.js"></script>
        <script language="javascript" type="text/javascript" src="http://www.flotcharts.org/flot/source/jquery.flot.uiConstants.js"></script>
        <script language="JavaScript" type="text/javascript" src="../scripts/ajax_test.js"></script>
        <script type="text/javascript">
        let data = new FormData();
        let xhr = new XMLHttpRequest();
        xhr.open('POST', 'stats_test.py');
        xhr.timeout = 300;
        xhr.onload = function (data){
            $(function() {

		let d1 = total_resize_2d(data.currentTarget.responseText);
		var options = {
			series: {
				lines: {
					show: true,
					lineWidth: 2
				},
				points: {
					show: true
				}
			},
			xaxis: {
				tickDecimals: 0,
				tickSize: 1
			}
		};

		$.plot("#placeholder", [d1], options);

		// Add the Flot version string to the footer

		$("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
	});}
	xhr.send(data)
	    </script>
    </head>
'''


print(head, file=utf8stdout)

b1 = '''
  <body>
        <center><h1>Estadisticas de los Avistamientos</h1></center>
        <ul class="menu">
            <li><a href="Portada_T2.py" class="hover">Portada</a></li>
            <li><a href="../Informar_Avistamiento_T2.html" class="hover">Informar Avistamiento</a></li>
            <li><a href="Listado_T2.py" class="hover">Listado de Avistamientos</a></li>
            <li><a href="Estadisticas.py" class="hover">Estadísticas</a></li>
        </ul>
    <div class="texto_estadisticas">
      <br>
      <strong>¡Tenemos varios registros en nuestras página web!</strong>, con tu ayuda podremos tener
      muchos más. <strong> ¡Gracias por colaborar! </strong>
    </div>
    <div id="content">
        <div class="demo-container">
            <div id="placeholder" class="demo-placeholder">
            </div>
        </div>
    </div>
'''

print(b1, file=utf8stdout)

end = '''
    </body>
</html>
'''

# Extrayendo las fechas para la obtención del conteo de avistamientos por dia.

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

#print(days_array, file=utf8stdout)

#print(end, file=utf8stdout)