const mostrarAlerta=(titulo, texto, icono, botonConfirmacion )=>{
    Swal.fire({
        title: titulo,
        text: texto,
        icon: icono,
        confirmButtonText: botonConfirmacion
    });
}