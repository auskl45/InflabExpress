
const btnModificar = document.querySelectorAll('.btnModificarEnvio');
const btnCancelar = document.querySelectorAll('.btnCancelarEnvio');
const btnCompletar = document.querySelectorAll('.btnCompletarEnvio');

btnModificar.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        let datos=btn.getAttribute('data-envio');    
        datos=datos.split(",");
        console.log(datos[0]);
        $("#txtIdEnvio").val(datos[0]);
        $("#txtDestinatario").val(datos[2]);
        $("#txtFechaRealizado").val(datos[3].trim());
        //console.log( datos.split(","));
        console.log(typeof datos);
        $("#exampleModalCenter").modal("show");
    });
});

btnCancelar.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        let id=btn.getAttribute('data-idEnvio');    
          
        let url=btn.getAttribute('href'); 
        console.log(url);
        Swal.fire({
            title: '¿Estás seguro de cancelar el envio # '+id+' ?',
            text: "No podrás revertir esta acción",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                location.href = url;
            }
        });
    });
});

btnCompletar.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        console.log(e.target.href);
        let url=btn.getAttribute('href');
        let id=btn.getAttribute('data-idEnvio');  
        console.log(url);  
        Swal.fire({
            title: '¿Se ha completado el envio correctamente # '+id+'?',
            text: "No podrás revertir esta acción",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, ha sido enviado correctamente'
        }).then((result) => {
            if (result.isConfirmed) {
                console.log(e.target.href);
                location.href = url;
            }
        });
    });
});