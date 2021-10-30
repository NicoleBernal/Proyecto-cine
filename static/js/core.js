var eliminando;
function cambiarRuta(ruta) {
    let frm = document.getElementById("formulario");
    frm.action = ruta;
    eliminando = false;
    if (ruta == "/funcion/eliminar"){
        eliminando =  true;
    }
}

function confirmarBorrado() {
    if (eliminando){
        let resp = confirm("Desea realmente borrar el registro?")
        return resp;
    }
    return true;
}