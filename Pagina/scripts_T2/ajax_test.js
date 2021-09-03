// Función para redimensionar a 2 dimensiones un array ingresado
function resize_2d(arr){
    let new_array = [];
    let len_arr = arr.length;
    for (let k=0; k<len_arr; k+=2){
        x_value = arr[k];
        y_value = arr[k+1];
        new_array.push([x_value, y_value])
    };
    return new_array;
}

// Función para convertir un arreglo textual de python bidimensional en el formato disponible para los graficos en js.
function string_to_array(arr, resize2d){
    let arr_out = arr.slice(0,arr.length - 2)  // Removiendo los 2 ultimos elementos del arreglo (vienen /r/n al final del string)
    arr_out = arr_out.replaceAll('[','');
    arr_out = arr_out.replaceAll(']','');
    arr_out = arr_out.replaceAll(' ','');
    //console.log(arr_out)
    let arr_separated = [];     // Inicialización para la serie con los valores separados.
    for (let l=0; l<arr_out.length; l++){
        let take_after = 1;
        // Si al evaluar los terminos estos se encuentra un coma entonces
        if (arr_out[l] == ','){
            continue;
        };
        // Si al evaluar el termino, se tiene que el posterior tambien corresponde a un numero entonces.
        if (!isNaN(Number(arr_out[l]))){
            if (!isNaN(Number(arr_out[l-1]))){
                continue;
            }
            while (!isNaN(Number(arr_out[l+take_after]))){
                take_after += 1;
            }
        };

        let string_add = arr_out.slice(l, l+take_after);
        arr_separated.push(string_add);

    }
    //console.log(arr_separated)
    //console.log(arr_separated.length)
    arr_final = [];
    for (let i=0; i<arr_separated.length; i++){
        arr_final.push(Number(arr_separated[i]));
    }
    if (resize2d){
    arr_out = resize_2d(arr_final);
    return arr_out}

    return arr_final;
}

// Función para convertir un string a un arreglo númerico.

