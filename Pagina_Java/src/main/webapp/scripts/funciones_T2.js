// Funciones para la validación y llenado de secciones de la seccion avistamiento

// Función alerta.
function alerta(text_alerta){
          alert(text_alerta);
          return false;
        }

let regiones = {
    "Región de Tarapacá": ['Camiña','Huara','Pozo Almonte','Iquique','Pica','Colchane','Alto Hospicio'],
    "Región de Antofagasta": ['Tocopilla','Maria Elena','Ollague','Calama','San Pedro Atacama','Sierra Gorda','Mejillones','Antofagasta','Taltal'],
    "Región de Atacama": ['Diego de Almagro','Chañaral','Caldera','Copiapo','Tierra Amarilla','Huasco','Freirina','Vallenar','Alto del Carmen'],
    "Región de Coquimbo": ['La Higuera','La Serena','Vicuña','Paihuano','Coquimbo','Andacollo','Rio Hurtado','Ovalle','Monte Patria','Punitaqui','Combarbala','Mincha','Illapel','Salamanca','Los Vilos'],
    "Región de Valparaíso": ['Petorca','Cabildo','Papudo','La Ligua','Zapallar','Putaendo','Santa Maria','San Felipe','Pencahue','Catemu','Llay Llay','Nogales','La Calera','Hijuelas','La Cruz','Quillota','Olmue','Limache','Los Andes','Rinconada','Calle Larga','San Esteban','Puchuncavi','Quintero','Viña del Mar','Villa Alemana','Quilpue','Valparaiso','Juan Fernandez','Casablanca','Concon','Isla de Pascua','Algarrobo','El Quisco','El Tabo','Cartagena','San Antonio','Santo Domingo'],
    "Región del Libertador Bernardo Ohiggins": ['Mostazal','Codegua','Graneros','Machali','Rancagua','Olivar','Doñihue','Requinoa','Coinco','Coltauco','Quinta Tilcoco','Las Cabras','Rengo','Peumo','Pichidegua','Malloa','San Vicente','Navidad','La Estrella','Marchigue','Pichilemu','Litueche','Paredones','San Fernando','Peralillo','Placilla','Chimbarongo','Palmilla','Nancagua','Santa Cruz','Pumanque','Chepica','Lolol'],
    "Región del Maule": ['Teno','Romeral','Rauco','Curico','Sagrada Familia','Hualañe','Vichuquen','Molina','Licanten','Rio Claro','Curepto','Pelarco','Talca','Pencahue','San Clemente','Constitucion','Maule','Empedrado','San Rafael','San Javier','Colbun','Villa Alegre','Yerbas Buenas','Linares','Longavi','Retiro','Parral','Chanco','Pelluhue','Cauquenes'],
    "Región del Biobío": ['Tome','Florida','Penco','Talcahuano','Concepcion','Hualqui','Coronel','Lota','Santa Juana','Chiguayante','San Pedro de la Paz','Hualpen','Cabrero','Yumbel','Tucapel','Antuco','San Rosendo','Laja','Quilleco','Los Angeles','Nacimiento','Negrete','Santa Barbara','Quilaco','Mulchen','Alto Bio Bio','Arauco','Curanilahue','Los Alamos','Lebu','Cañete','Contulmo','Tirua'],
    "Región de La Araucanía": ['Renaico','Angol','Collipulli','Los Sauces','Puren','Ercilla','Lumaco','Victoria','Traiguen','Curacautin','Lonquimay','Perquenco','Galvarino','Lautaro','Vilcun','Temuco','Carahue','Melipeuco','Nueva Imperial','Puerto Saavedra','Cunco','Freire','Pitrufquen','Teodoro Schmidt','Gorbea','Pucon','Villarrica','Tolten','Curarrehue','Loncoche','Padre Las Casas','Cholchol'],
    "Región de Los Lagos": ['San Pablo','San Juan','Osorno','Puyehue','Rio Negro','Purranque','Puerto Octay','Frutillar','Fresia','Llanquihue','Puerto Varas','Los Muermos','Puerto Montt','Maullin','Calbuco','Cochamo','Ancud','Quemchi','Dalcahue','Curaco de Velez','Castro','Chonchi','Queilen','Quellon','Quinchao','Puqueldon','Chaiten','Futaleufu','Palena','Hualaihue'],
    "Región Aisén del General Carlos Ibáñez del Campo": ['Guaitecas','Cisnes','Aysen','Coyhaique','Lago Verde','Rio Ibañez','Chile Chico','Cochrane','Tortel',"O'Higins"],
    "Región de Magallanes y la Antártica Chilena": ['Torres del Paine','Puerto Natales','Laguna Blanca','San Gregorio','Rio Verde','Punta Arenas','Porvenir','Primavera','Timaukel','Antartica'],
    "Región Metropolitana de Santiago": ['Tiltil','Colina','Lampa','Conchali','Quilicura','Renca','Las Condes','Pudahuel','Quinta Normal','Providencia','Santiago','La Reina','Ñuñoa','San Miguel','Maipu','La Cisterna','La Florida','La Granja','Independencia','Huechuraba','Recoleta','Vitacura','Lo Barrenechea','Macul','Peñalolen','San Joaquin','La Pintana','San Ramon','El Bosque','Pedro Aguirre Cerda','Lo Espejo','Estacion Central','Cerrillos','Lo Prado','Cerro Navia','San Jose de Maipo','Puente Alto','Pirque','San Bernardo','Calera de Tango','Buin','Paine','Peñaflor','Talagante','El Monte','Isla de Maipo','Curacavi','Maria Pinto','Melipilla','San Pedro','Alhue','Padre Hurtado'],
    "Región de Los Ríos": ['Lanco','Mariquina','Panguipulli','Mafil','Valdivia','Los Lagos','Corral','Paillaco','Futrono','Lago Ranco','La Union','Rio Bueno'],
    "Región Arica y Parinacota": ['Gral. Lagos','Putre','Arica','Camarones'],
    "Región del Ñuble": ['Cobquecura','Ñiquen','San Fabian','San Carlos','Quirihue','Ninhue','Trehuaco','San Nicolas','Coihueco','Chillan','Portezuelo','Pinto','Coelemu','Bulnes','San Ignacio','Ranquil','Quillon','El Carmen','Pemuco','Yungay','Chillan Viejo']
};

let comunas_id = {
    "Región de Tarapacá": [10301,10302,10303,10304,10305,10306,10307],
    "Región de Antofagasta": [20101, 20102, 20201, 20202, 20203, 20301, 20302, 20303, 20304],
    "Región de Atacama": [30101, 30102, 30201, 30202, 30203, 30301, 30302, 30303, 30304],
    "Región de Coquimbo": [40101, 40102, 40103, 40104, 40105, 40106, 40201, 40202, 40203, 40204, 40205, 40301, 40302, 40303, 40304],
    "Región de Valparaíso": [50101, 50102, 50103, 50104, 50105, 50201, 50202, 50203, 50204, 50205, 50206, 50301, 50302, 50303, 50304, 50305, 50306, 50307, 50401, 50402, 50403, 50404, 50501, 50502, 50503, 50504, 50505, 50506, 50507, 50508, 50509, 50601, 50701, 50702, 50703, 50704, 50705, 50706],
    "Región del Libertador Bernardo Ohiggins": [60101, 60102, 60103, 60104, 60105, 60106, 60107, 60108, 60109, 60110, 60111, 60112, 60113, 60114, 60115, 60116, 60117, 60201, 60202, 60203, 60204, 60205, 60206, 60301, 60302, 60303, 60304, 60305, 60306, 60307, 60308, 60309, 60310],
    "Región del Maule": [70101, 70102, 70103, 70104, 70105, 70106, 70107, 70108, 70109, 70201, 70202, 70203, 70204, 70205, 70206, 70207, 70208, 70209, 70210, 70301, 70302, 70303, 70304, 70305, 70306, 70307, 70308, 70401, 70402, 70403],
    "Región del Biobío": [80201, 80202, 80203, 80204, 80205, 80206, 80207, 80208, 80209, 80210, 80211, 80212, 80301, 80302, 80303, 80304, 80305, 80306, 80307, 80308, 80309, 80310, 80311, 80312, 80313, 80314, 80401, 80402, 80403, 80404, 80405, 80406, 80407],
    "Región de La Araucanía": [90101, 90102, 90103, 90104, 90105, 90106, 90107, 90108, 90109, 90110, 90111, 90201, 90202, 90203, 90204, 90205, 90206, 90207, 90208, 90209, 90210, 90211, 90212, 90213, 90214, 90215, 90216, 90217, 90218, 90219, 90220, 90221],
    "Región de Los Lagos": [100201, 100202, 100203, 100204, 100205, 100206, 100207, 100301, 100302, 100303, 100304, 100305, 100306, 100307, 100308, 100309, 100401, 100402, 100403, 100404, 100405, 100406, 100407, 100408, 100409, 100410, 100501, 100502, 100503, 100504],
    "Región Aisén del General Carlos Ibáñez del Campo": [110101, 110102, 110103, 110201, 110202, 110301, 110302, 110401, 110402, 110403],
    "Región de Magallanes y la Antártica Chilena": [120101, 120102, 120201, 120202, 120203, 120204, 120301, 120302, 120303, 120401],
    "Región Metropolitana de Santiago": [130101, 130102, 130103, 130201, 130202, 130203, 130204, 130205, 130206, 130207, 130208, 130209, 130210, 130211, 130212, 130213, 130214, 130215, 130216, 130217, 130218, 130219, 130220, 130221, 130222, 130223, 130224, 130225, 130226, 130227, 130228, 130229, 130230, 130231, 130232, 130301, 130302, 130303, 130401, 130402, 130403, 130404, 130501, 130502, 130503, 130504, 130601, 130602, 130603, 130604, 130605, 130606],
    "Región de Los Ríos": [100101, 100102, 100103, 100104, 100105, 100106, 100107, 100108, 100109, 100110, 100111, 100112],
    "Región Arica y Parinacota": [10101, 10102, 10201, 10202],
    "Región del Ñuble": [80101, 80102, 80103, 80104, 80105, 80106, 80107, 80108, 80109, 80110, 80111, 80112, 80113, 80114, 80115, 80116, 80117, 80118, 80119, 80120, 80121]
}

let regiones_array = Object.keys(regiones);
let opciones_region = '<option value="0" id="select_region">Seleccione una región</option>';

for (let i=0; i<regiones_array.length; i++) {
    opciones_region += '<option value="'+ String(i+1) + '" id="region_ ' + String(i) + '">'
    + regiones_array[i] +'</option>';
}

document.getElementById("Region").innerHTML = opciones_region;

function comunas_region(region_id) {
    var Comunas =  regiones[regiones_array[region_id-1]];
    var html_comuna = '<option value="comuna_0"> Seleccione una comuna </option>';
    // var html_comuna = '';
    for (let i = 0; i < Comunas.length; i++) {
        html_comuna += "<option value=" + String(comunas_id[regiones_array[region_id-1]][i]) + ">" + Comunas[i] + "</option>";
    }
    return html_comuna;
}

var regSelected = document.getElementById("Region");
regSelected.addEventListener("change", event => {
    var elementSelected = regSelected.options[regSelected.selectedIndex].value;
    if (elementSelected==0){
        document.getElementById("comuna").innerHTML = '<option value="comuna_0"> Seleccione una comuna </option>';
    } else{
    var comunas_html = comunas_region(elementSelected);
    document.getElementById("comuna").innerHTML = comunas_html;}
})

// Configuración de despliegue de regiones
var sector_string = document.getElementById("sector_inp");
sector_string.addEventListener("change", event=>{
  var len_sector = sector_string.value.length;
  if (len_sector > 100){alerta("El texto no puede tener más de 100 carácteres");}
})

// Configuración del formulario de avistamiento.

function string_avistamiento(n_avistamiento) {
    var avistamiento_string = '<div class="section_name"> <strong>Informacion de avistamiento.</strong> </div>'
    +  '<!-- Fecha y hora  -->'
    +  '<div id="avistamiento_dia_'+ String(n_avistamiento) +'" class="entrada">'
    +  '    <div class="entrada_nombre">Día hora:</div>'
    +  '    <input type="text" name="dia-hora-avistamiento' + String(n_avistamiento) + '" id="dia-hora-avistamiento' + String(n_avistamiento) + '" value="">'
    +  '</div>'
    +  '<!-- Tipo  -->'
    +  '<div id="avistamiento_tipo_'+ String(n_avistamiento) +'" class="entrada">'
    +  '    <div class="entrada_nombre"> Tipo: </div>'
    +  '    <select name="tipo-avistamiento-'+ String(n_avistamiento) +'" id="tipo-avistamiento-'+ String(n_avistamiento) +'">'
    +  '        <option value="Seleccione Tipo"> Seleccione Tipo</option>'
    +  '        <option value="no sé"> no sé </option>'
    +  '        <option value="Insecto"> Insecto </option>'
    +  '        <option value="Arácnido"> Arácnido </option>'
    +  '        <option value="Miriápodo"> Miriápodo </option>'
    +  '    </select>'
    +  '</div>'
    +  '<!-- Estado  -->'
    +  '<div id="avistamiento_estado_'+ String(n_avistamiento) +'" class="entrada">'
    +  '    <div class="entrada_nombre">Estado:</div>'
    +  '    <select name="estado-avistamiento-'+ String(n_avistamiento) +'" id="estado-avistamiento-'+ String(n_avistamiento) +'">'
    +  '        <option value="Seleccione Estado"> Seleccione Estado </option>'
    +  '        <option value="no sé"> No sé </option>'
    +  '        <option value="Vivo"> Vivo </option>'
    +  '        <option value="Muerto"> Muerto </option>'
    +  '    </select>'
    +  '</div>'
    +  '<!-- Foto  -->'
    +  '<div id="avistamiento_foto_' + String(n_avistamiento) +'" class="entrada">'
    +  '    <div class="entrada_clase">Foto de Avistamiento:</div>'
    +  '    <input type="file" name="foto-avistamiento' + String(n_avistamiento) +'1" value="Subir Foto"'
    +             'id="foto-avistamiento' + String(n_avistamiento) +'1">'
    +  '</div>';
    return avistamiento_string;
}

// Parametros que contienen las cantidades variables de avistamientos y fotos añadidas
let num_avistamiento = 1;
let photos_added = 1;
let fotos_avistamiento = [photos_added]         // Arreglo vacío, donde se añadiran la cantidad de fotos por avistamiento

let Avist_string = string_avistamiento(num_avistamiento);

// Añadiendo la configuración inicial
document.getElementById("section_avistamiento").innerHTML = Avist_string;

// Función para añadir otra foto
function add_photo() {
    photos_added += 1;
    // Guardando el string que contiene las fotos
    var photo_string = '<br><input type="file" id="foto-avistamiento'+ String(num_avistamiento) + String(photos_added) +'" name="foto-avistamiento'+ String(num_avistamiento) + String(photos_added) +'" value="Subir Foto">';
    if (photos_added > 5) {
        alerta("No se pueden ingresar mas de 5 fotos");
        return false;
    }
    else {
      document.getElementById("avistamiento_foto_" + String(num_avistamiento)).innerHTML += photo_string;
      fotos_avistamiento[num_avistamiento-1] = photos_added
      return true;
    }
    return false
    }

// Función para añadir otro avistamiento
function repeat_avistamiento() {
    photos_added = 1;
    fotos_avistamiento.push(photos_added)
    num_avistamiento += 1;
    var Avistamiento_string = string_avistamiento(num_avistamiento);
    document.getElementById("section_avistamiento").innerHTML += Avistamiento_string;
    return false;
}

// Función de Envío, esta corresponde a la función final al terminar la validación.
function Envio(){
            Swal.fire({
              title: '¿Esta seguro que desea enviar esta información?',
              showDenyButton: true,
              // showCancelButton: true,
              confirmButtonText: `Si, estoy total y absolutamente seguro`,
              denyButtonText: `No estoy seguro, quiero volver al formulario`,
            }).then((result) => {
              /* Read more about isConfirmed, isDenied below */
              if (result.isConfirmed) {
                Swal.fire('Saved!', '', 'success');
                alert("Hemos recibido su información, muchas gracias por colaborar!");
                document.forms["form_avistamiento"].submit();
              } else if (result.isDenied) {
                Swal.fire('Vuelta al formulario', '', 'info');
              }
            })
            }


// Función de Validación, esta contiene la validación de cada sección del formulario.
function validacion() {
    // Validación de la región.
    var region_selected = document.getElementById("Region");
    var value_region = region_selected.options[region_selected.selectedIndex].value;
    if (value_region == "0") {
      alerta("Seleccione una región!")
      return false;
    }
    // Validación de la comuna.
    var com_selected = document.getElementById("comuna");
    var value_comuna = com_selected.options[com_selected.selectedIndex].value;
    if (value_comuna == "comuna_0") {
      alerta("Selecciona una comuna");
      return false;
    }
    // Validación del nombre
    var contacto_nombre = document.getElementById("nombre");
    var nombre = contacto_nombre.value;
    var regex = /^[a-z,A-Z ]*$/;
    if (nombre.length < 2 || nombre.length > 100 || !regex.test(nombre)) {
      alerta("Nombre invalido, este debe tener entre 2 y 100 carácteres ,no debe incluir números y no tener tildes.");
      return false;
    }
    // Validación del mail.
    var mail = document.getElementById("email");
    var regex_mail = /^[a-z,A-Z@.]*$/;
    if (!regex_mail.test(mail.value)) {
      alerta("mail con el formato invalido, incluya una dirección válida.");
      return false;
    }

    // Validación del numero de teléfono.
    var phone = document.getElementById("celular");
    var phone_number = phone.value;
    if (phone_number == ""){
      alerta("Ingrese un número telefónico");
      return false;
    }
    if (regex.test(phone_number)){
        alerta("Celular invalido, ingrese solo números.");
        return false;
    }

    // Validación de la sección de avistamiento.
    for (let i = 0; i < num_avistamiento; i++) {
      // Validación del campo si esta vacío
      var HoraAvistamiento = document.getElementById("dia-hora-avistamiento" + String(i+1));
      var value_date = HoraAvistamiento.value;
      if (value_date == ""){
          alerta("Fecha de avistamiento "+ String(i+1) +" vacía, ingrese una fecha y hora");
          return false;
      }

      // Identificación de caracteres validos en el campo
      var regex_date = /^[0-9,/: ]*$/;
      if (!regex_date.test(value_date)) {
      alerta("Fecha de avistamiento "+ String(num_avistamiento) +" con formato invalido, no incluya letras, solo numeros y los caracteres /, :.");
      return false;}

      // Validación de formato de ingreso (caracteres minimos para que la fecha sea válida)
      var date_process = value_date.slice(0,19);
      var regex_number = /^[0-9 ]*$/;
      var date_separate = '/';
      var hour_separate = ':';
      var date_alert =  "Fecha de avistamiento "+ String(num_avistamiento) +" con formato invalido, formato yyyy/mm/dd hh:mm:ss, el ingreso de los segundos es opcional.";
      if (date_process[4] != date_separate || date_process[7] != date_separate || date_process.length < 16) {
          alerta(date_alert);
          return false;
      }
      if (date_process.length > 16){
          if (date_process[16] != hour_separate){
            alerta(date_alert);
            return false;
          }
          date_process = date_process.slice(0,16) + date_process.slice(17);
      }
      if (date_process[13] != hour_separate){
          alerta(date_alert);
          return false;
      }

      // Eliminando los caracteres especiales de las posiciones de interes.
      date_process = date_process.slice(0,13) + date_process.slice(14);
      date_process = date_process.slice(0,7) + date_process.slice(8);
      date_process = date_process.slice(0,4) + date_process.slice(5);
      console.log(date_process);

      // Evaluando el formato.
      if (!regex_number.test(date_process)) {
          alerta(date_alert);
          return false;
      }

      // Evaluando los numeros ingresados.
      var year = date_process.slice(0,4);
      var month = date_process.slice(4,6);
      var day = date_process.slice(6,8);
      var hour = date_process.slice(9,11);
      var min = date_process.slice(11,13);
      var sec = date_process.slice(-2);

      if (year > 2021 || month > 12 || day > 30 || hour > 23 || min > 59 || sec > 59){
          alerta('Fecha u hora invalida, asegurese que se encuentren los valores correctos y un año anterior al 2021');
          return false;
      }

      // Validación de los tipos de avistamientos
      var TipoAvistamiento = document.getElementById("tipo-avistamiento-" + String(i+1));
      var value_tipo = TipoAvistamiento.options[TipoAvistamiento.selectedIndex].value;
      if (value_tipo == "Seleccione Tipo") {
        alerta("Seleccione el tipo del avistamiento " + String(i+1));
        return false;
      }
      // Validación de los estados de los avistamientos
      var EstadoAvistamiento = document.getElementById("estado-avistamiento-" + String(i+1));
      var value_estado = EstadoAvistamiento.options[EstadoAvistamiento.selectedIndex].value
      if (value_estado == "Seleccione Estado") {
        alerta("Seleccione el estado del avistamiento " + String(i+1));
        return false;
      }

      //Validación de las imágenes.
      var fotos_por_avistamiento = fotos_avistamiento[i];
      // Validación del formato de las imagenes.
      for (let j=0; j<fotos_por_avistamiento; j++){
          var imagen = document.getElementById("foto-avistamiento"+ String(i+1)+String(j+1));
          if (imagen.value == ""){
              alerta("Imagen n°:"+String(j+1) +" del avistamiento n°:"+String(i+1)+" vacía" +
                  ", ingrese un archivo con formato .jpg o .PNG");
              return false;
          }
          var imagen_format = imagen.value.slice(-3);
          if (imagen_format == "jpg" || imagen_format == "PNG" || imagen_format == "peg"){
              continue
          }
          else {
              alerta("Imagen n°:"+String(j+1) + " del avistamiento n°:" +String(i+1)+"" +
                  "tiene un formato incorrecto, ingrese archivos con extensión .jpg o .PNG");
              return false;
          }

      }
    }
    return Envio();
}

document.getElementById("botones").innerHTML = '<button onClick="add_photo()">Agregar Foto</button>'
        + '<button onclick="repeat_avistamiento()">Informar otro avistamiento en este sector</button>'
        + '<br>'
        + '<br>'

document.getElementById("envio_form").innerHTML = '<button type="button" name="button_test"'
        + ' onclick="validacion();" class="envio_button"> Enviar información de avistamiento </button>';


