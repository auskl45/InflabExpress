
const btnHecho = document.querySelectorAll('.btnHecho');
const btnEliminar = document.querySelectorAll('.btnCancelarPedido');
const btnProcesar = document.querySelectorAll('.btnProcesarPedido');

btnHecho.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        let id=btn.getAttribute('data-idPedido');    
        let url=btn.getAttribute('href'); 
        console.log(url);
        Swal.fire({
            title: '¿Estás seguro que ya ha completado el pedido # '+id+'?',
            text: "No podrás revertir esta acción",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, completado'
        }).then((result) => {
            if (result.isConfirmed) {
                console.log(e.target.href);
                location.href = url;
            }
        });
    });
});

btnEliminar.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        let id=btn.getAttribute('data-idPedido');    
          
        let url=btn.getAttribute('href'); 
        console.log(url);
        Swal.fire({
            title: '¿Estás seguro de cancelar el pedido # '+id+' ?',
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

btnProcesar.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        console.log(e.target.href);
        let url=btn.getAttribute('href');
        let id=btn.getAttribute('data-idPedido');  
        console.log(url);  
        Swal.fire({
            title: '¿Estás seguro de procesar el pedido # '+id+'?',
            text: "Se empezará a preparar el pedido",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, Procesar'
        }).then((result) => {
            if (result.isConfirmed) {
                console.log(e.target.href);
                location.href = url;
            }
        });
    });
});