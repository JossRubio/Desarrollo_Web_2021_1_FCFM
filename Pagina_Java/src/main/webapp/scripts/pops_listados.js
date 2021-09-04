// Funciones complementarias para la aparición de la información de la base de datos.
// Combinación con comandos de python para poder desplegar la información del database en páginas.

function pop_table(){
  document.getElementById("Table").style.display = "table";
}

function pop_block(id_block){
  id_block = String(id_block)
  document.getElementById(id_block).style.display = "block";
}

function hide_table(){
  document.getElementById("Table").style.display = "none";
}

