
// Función para mostrar el modal de agregar producto
const btnEliminarProduct = document.querySelectorAll('.btnEliminarProducto');
const btnModidficar = document.querySelectorAll('.btnModificarProducto');


btnEliminarProduct.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        let id=btn.getAttribute('data-idProducto');    
        
        let url=btn.getAttribute('href');
        
        console.log(url);
        Swal.fire({
            title: '¿Estás seguro de eliminar el inflable # '+id+' ?',
            text: "No podrás revertir esta acción",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, Eliminar'
        }).then((result) => {
            if (result.isConfirmed) {
                location.href = url;
            }
        });
    });
});

btnModidficar.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        let id=btn.getAttribute('data-idProducto');
        let url=btn.getAttribute('href');
        console.log(url);
        Swal.fire({
            title: '¿Estás seguro de modificar el inflable # '+id+' ?',
            text: "Se modificará el inflable",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, Modificar'
        }).then((result) => {
            if (result.isConfirmed) {
                location.href = url;
            }
        });
    });
});

/*
btnModidficar.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        console.log(e.target.href);
        let url=btn.getAttribute('href');
        let id=btn.getAttribute('data-idProducto');  
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
}); */