<%@ page import="dcc.cc5002.model.Tarea4DB" %>
<%@ page import="java.sql.ResultSet" %>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Evaluación de Fotos</title>
    <link rel="stylesheet" href="css/styles.css">
    <script src="scripts/sweetalert2.all.js"></script>
    <script defer>
        function pop_imagen(num_imagen){
            let str_imagen = String(num_imagen);
            document.getElementById("imagen_"+str_imagen).style.display = "block"
        }

        function hide_imagen(num_imagen) {
            let str_imagen = String(num_imagen);
            document.getElementById("imagen_"+str_imagen).style.display = "none";
        }

        function pop_formulario(){
            document.getElementById("formulario").style.display = "block"
        }

        function pop_table(){
            document.getElementById("Table").style.display = "table";
        }

        function hide_table(){
            document.getElementById("Table").style.display = "none";
        }

        function pop_block(id_block){
            id_block = String(id_block)
            document.getElementById(id_block).style.display = "block";
        }

        function hide_block(id_block){
            id_block = String(id_block)
            document.getElementById(id_block).style.display = "none";
        }
    </script>
    <style>
        table th:hover{
            background: #cccccc;
            color: #000140;
        }
    </style>
</head>
<body>
<center><h1> Evaluación de fotos </h1></center>
<br>
Tenemos diversas imágenes en nuestro repositorio. Te gusta alguna de las fotos?, quisieras dejar tu opinión sobre
la imagen mostrada?. Si es así, entonces haz click en alguna de las imágenes dejadas por los usuarios y hazles saber tu
visión sobre la imagen aportada!.

<br>
<center><strong><h3>Imágenes</h3></strong></center>
<center>
<table id="Table" style="display: table">
<%
    try {
        Tarea4DB db = new Tarea4DB("tarea2", "root", "");

        ResultSet data_count = db.getTotalData("foto");
        int count = 0;
        while (data_count.next()){
            count += 1;
        }



        ResultSet data =db.getTotalData("foto");
        String Date = db.getDate();
        int k = 0;
        int id = count;

        while (data.next()){
            if (k==0){
                out.print("<tr> <th> " +
                "<img src='media/" + data.getString(2) + ".jpg' width='120' height='120' onclick='hide_table(), pop_block(" + new String(String.valueOf(id)) + "), pop_formulario();'> </th>");
                out.print("<div id='"+ new String(String.valueOf(id)) +"' style='display: none'>" +
        " <center> <img src='media/" + data.getString(2) + ".jpg' width='800' height='600' > </center>" +
        " <form method='post' action='tarea4'> " +
            " <div class='section_list'> " +
                " <div class='entrada_nombre'> Comentario </div> " +
                " <textarea rows='20' cols='50' name='Comment' placeholder='Ingrese su comentario'></textarea> " +
                " <br> " +
                " <div class='entrada_nombre'> Evaluar foto </div>" +
                " <select name='Note'> " +
                    " <option> 1 </option> " +
                    " <option> 2 </option> " +
                    " <option> 3 </option> " +
                    " <option> 4 </option> " +
                    " <option> 5 </option> " +
                    " <option> 6 </option> " +
                    " <option> 7 </option> " +
                    " </select> " +
                " <input name='Photo' value='"+ new String(String.valueOf(id)) +"' style='display: none'> " +
                " <input type='text' name='Date' value='"+ Date +"' style='display: none'> " +
                " <br> " +
                " <br> " +
                " <button type='submit'> Comentar y Evaluar </button> " +
                " </div> " +
            " </form> " +
        " <br> " +
        " <center> " +
            " <button type='button' onclick='hide_block("+ new String(String.valueOf(id)) +"), pop_table()'> Seleccionar otra foto </button> " +
            " </center> " );
                ResultSet data_notes = db.getPartialData("comentario_foto","foto_bicho", new String(String.valueOf(id)));
                Double mean_id = 0.0;
                int j=0;
                while(data_notes.next()){
                    int int_note= Integer.valueOf(data_notes.getString(4));
                    mean_id += int_note;
                    j += 1;
        };
                 Double Mean_id = (mean_id)/(j);
                out.print("<div class='section_list'> " +
            " <div class='entrada_nombre'> Nota Promedio: </div> " +
            " " + new String(String.valueOf(Mean_id)) + " " +
            " </div> " +
        " <br> " +
        " <br> ");
                out.print( " <center> <h3>Comentarios asociados a esta foto </h3> </center> ");
                ResultSet data_notes2 = db.getPartialData("comentario_foto","foto_bicho", new String(String.valueOf(id)));
                while (data_notes2.next()){
                    out.print("<div class='section_list'> " +
            " <div class='entrada_nombre'> Comentario: </div> " +
            " "+ data_notes2.getString(3) +" " +
            " <br> " +
            " <div class='entrada_nombre'>Fecha: </div> " +
            " " + data_notes2.getString(2) + " "  +
            "</div> ");
        }
                out.print("</div>");
                k += 1;
                id -= 1;
            }
            else if (k>0 & k<3){
                out.print("<th> " +
                "<img src='media/" + data.getString(2) + ".jpg' width='120' height='120' onclick='hide_table(), pop_block(" + new String(String.valueOf(id)) + ");'> </th>");
                out.print("<div id='"+ new String(String.valueOf(id)) +"' style='display: none'>" +
        " <center> <img src='media/" + data.getString(2) + ".jpg' width='800' height='600' > </center>" +
        " <form method='post' action='tarea4'> " +
            " <div class='section_list'> " +
                " <div class='entrada_nombre'> Comentario </div> " +
                " <textarea rows='20' cols='50' name='Comment' placeholder='Ingrese su comentario'></textarea> " +
                " <br> " +
                " <div class='entrada_nombre'> Evaluar foto </div>" +
                " <select name='Note'> " +
                    " <option> 1 </option> " +
                    " <option> 2 </option> " +
                    " <option> 3 </option> " +
                    " <option> 4 </option> " +
                    " <option> 5 </option> " +
                    " <option> 6 </option> " +
                    " <option> 7 </option> " +
                    " </select> " +
                " <input name='Photo' value='"+ new String(String.valueOf(id)) +"' style='display: none'> " +
                " <input type='text' name='Date' value='"+ Date +"' style='display: none'> " +
                " <br> " +
                " <br> " +
                " <button type='submit'> Comentar y Evaluar </button> " +
                " </div> " +
            " </form> " +
        " <br> " +
        " <center> " +
            " <button type='button' onclick='hide_block("+ new String(String.valueOf(id)) +"), pop_table()'> Seleccionar otra foto </button> " +
            " </center> ");
        ResultSet data_notes = db.getPartialData("comentario_foto","foto_bicho", new String(String.valueOf(id)));
        Double mean_id = 0.0;
        int j=0;
        while(data_notes.next()){
        int int_note= Integer.valueOf(data_notes.getString(4));
        mean_id += int_note;
        j += 1;
        };
        Double Mean_id = (mean_id)/(j);
        out.print("<div class='section_list'> " +
            " <div class='entrada_nombre'> Nota Promedio: </div> " +
            " "+ new String(String.valueOf(Mean_id)) +" " +
            " </div> " +
        " <br> " +
        " <br> ");
        out.print( " <center> <h3>Comentarios asociados a esta foto </h3> </center> ");
        ResultSet data_notes2 = db.getPartialData("comentario_foto","foto_bicho", new String(String.valueOf(id)));
        while (data_notes2.next()){
        out.print("<div class='section_list'> " +
            " <div class='entrada_nombre'> Comentario: </div> " +
            " "+ data_notes2.getString(3) +" " +
            " <br> " +
            " <div class='entrada_nombre'>Fecha: </div> " +
            " " + data_notes2.getString(2) + " "  +
            "</div> ");
        }
        out.print("</div>");
        k += 1;
        id -= 1;
            }
            else {
                out.print("<th> " +
                "<img src='media/" + data.getString(2) + ".jpg' width='120' height='120' onclick='hide_table(), pop_block(" + new String(String.valueOf(id)) + ")';> </th> </tr>");
                out.print("<div id='"+ new String(String.valueOf(id)) +"' style='display: none'>" +
    " <center> <img src='media/" + data.getString(2) + ".jpg' width='800' height='600' > </center>" +
    " <form method='post' action='tarea4'> " +
        " <div class='section_list'> " +
            " <div class='entrada_nombre'> Comentario </div> " +
            " <textarea rows='20' cols='50' name='Comment' placeholder='Ingrese su comentario'></textarea> " +
            " <br> " +
            " <div class='entrada_nombre'> Evaluar foto </div>" +
            " <select name='Note'> " +
                " <option> 1 </option> " +
                " <option> 2 </option> " +
                " <option> 3 </option> " +
                " <option> 4 </option> " +
                " <option> 5 </option> " +
                " <option> 6 </option> " +
                " <option> 7 </option> " +
                " </select> " +
            " <input name='Photo' value='"+ new String(String.valueOf(id)) +"' style='display: none'> " +
            " <input type='text' name='Date' value='"+ Date +"' style='display: none'> " +
            " <br> " +
            " <br> " +
            " <button type='submit'> Comentar y Evaluar </button> " +
            " </div> " +
        " </form> " +
    " <br> " +
    " <center> " +
        " <button type='button' onclick='hide_block("+ new String(String.valueOf(id)) +"), pop_table()'> Seleccionar otra foto </button> " +
        " </center> ");
    ResultSet data_notes = db.getPartialData("comentario_foto","foto_bicho", new String(String.valueOf(id)));
    Double mean_id = 0.0;
    int j=0;
    while(data_notes.next()){
    int int_note= Integer.valueOf(data_notes.getString(4));
    mean_id += int_note;
    j += 1;
    };
    Double Mean_id = (mean_id)/(j);
    out.print("<div class='section_list'> " +
        " <div class='entrada_nombre'> Nota Promedio: </div> " +
        " "+ new String(String.valueOf(Mean_id)) +" " +
        " </div> " +
    " <br> " +
    " <br> ");
    out.print( " <center> <h3>Comentarios asociados a esta foto </h3> </center> ");
    ResultSet data_notes2 = db.getPartialData("comentario_foto","foto_bicho", new String(String.valueOf(id)));
    while (data_notes2.next()){
    out.print("<div class='section_list'> " +
        " <div class='entrada_nombre'> Comentario: </div> " +
        " "+ data_notes2.getString(3) +" " +
        " <br> " +
        " <div class='entrada_nombre'>Fecha: </div> " +
        " " + data_notes2.getString(2) + " "  +
        "</div> ");
    }
    out.print("</div>");
                k = 0;
                id -= 1;
            }
            }

        } catch(Exception e) {
        System.out.println(e);
    }
%>
</table>
</center>
</body>
</html>