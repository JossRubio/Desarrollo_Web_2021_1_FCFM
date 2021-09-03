// Funciones complementarias para la aparición de la información de la base de datos.
// Combinación con comandos de python para poder desplegar la información del database en páginas.

function pop(id_listado, form){
  document.getElementById(id_listado).style.display = form;
}

function hide(id_listado){
  document.getElementById(id_listado).style.display = "none";
}

