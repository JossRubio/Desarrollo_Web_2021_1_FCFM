# Desarrollo_Web_2021_1_FCFM
Desarrollo de una pagina web de avistamientos de insectos, esta contiene diversas funcionalidades programadas en html, js, python y java 

Autor: José Manuel Rubio Cienfuegos.

Hola! la pagina consiste en un formulario que añade datos de avistamiento e imagenes de insectos (las imágenes pueden ser cualquier imagen de formato .jpg), se tienen diversas funcionalidades como un mapa donde se muestra donde fueron los avistamientos (corresponde un mapa de Chile ya que el formulario contiene información de búsqueda para Chile), un registro de las estadísticas de los tipos de avistamientos, estado, fecha, etc.

La página posee diversas funcionalidades, fue programada en HTML, JavaScript y Python. Mientras que otras funcionalidades fueron programadas en Java. Para poder visualizar la página correctamente se necesita un IDE de Python, preferiblemente Pycharm ya que el sistema fue programado en dicho IDE, también es necesario el uso de un sistema de gestión de bases de datos de SQL, se utilizó XAMPP donde para subir la información y revisar el funcionamiento de forma local, para ello se activó Apache y MySQL. 

FUNCIONAMIENTO DE PAGINA DE FORMA LOCAL:

Una vez descargados el IDE y XAMPP, se debe activar Apache y MySQL, entonces se debe ejecutar el archivo 'tarea2.sql' con alguna herramienta  de base de datos, en este trabajo se utilizó MySQL Workbench. Finalizando esto, en la terminal de python del IDE se debe ejecutar el siguiente comando para habilitar la conexión de manera local: "python -m http.server --bind localhost --cgi 10000", cabe destacar que el número mostrado al final puede variar ya que este representa el puerto donde se realizará la conexión.

Una vez se tenga esto, entonces para visualizar la página se debe ingresar a cualquier navegador y en la barra de url se tiene que ingresar "localhost:10000", en caso de que se cambie el puerto al ejecutar el comando mencionado en el parrado anterior, entonces tambien el numero de este ultimo tambien debe cambiarse por el seleccionado anteriormente.

FUNCIONAMIENTO DE FUNCIONALIDADES PARA JAVA:

Se tienen una funcionalidades que fueron programadas en Java, para poder revisar y ejecutar el sistema apropiadamente se debe leer el Readme de la carpeta Pagina Java.

Cualquier duda o sugerencia respecto a esta página contactar a aihanrob@gmail.com o jose.rubio@ug.uchile.cl
