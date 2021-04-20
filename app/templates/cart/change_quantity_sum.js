let changeTables = function (event) {
    var element = event.target;
    if (element.tagName === 'A') {
            if(element.parentElement.parentElement.tagName !=='LI'){
                return;
            }

        event.preventDefault();
        let quantity = element.parentElement.parentElement.children[1].children[0].value
        let product_name = element.parentElement.parentElement.parentElement.children[0].children[0].children[0].innerHTML
        let product_price = element.parentElement.parentElement.parentElement.children[0].children[1].innerHTML
        let sum_product_before = element.parentElement.parentElement.children[1].children[2].innerHTML
        let sum_before = document.getElementById('sum').innerHTML
        let button_name = element.innerHTML
        Swal.fire({
            title: '',
            text: "Haluatko varmasti tehdä muutoksia?",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Kyllä!',
            cancelButtonText: 'Peruuta'
        }).then((result) => {
            if (result.isConfirmed) {
                let url = 'cancel_change_cart.php?quantity=' + quantity + '&product_name=' + product_name + '&product_price=' + product_price + '&button_name=' + button_name
                fetch(url)
                    .then(function (response) {
                        return response.json();
                    }).then(function (data) {
                        if (data.result == "true") {
                            if (data.button == "delete") {
                                element.parentElement.parentElement.parentElement.remove();
                                document.getElementById('sum').innerHTML = parseFloat(sum_before) - parseFloat(sum_product_before)
                                document.getElementById('amount').innerHTML = parseFloat(document.getElementById('amount').innerHTML) - 1
                            }
                            if (data.button == "update") {
                                let sum_product = parseFloat(quantity * product_price).toFixed(2)
                                element.parentElement.parentElement.children[1].children[2].innerHTML = sum_product + '€'
                                document.getElementById('sum').innerHTML = parseFloat(sum_before) - parseFloat(sum_product_before) + parseFloat(sum_product)
                            }

                            Swal.fire({
                                title: '',
                                text: 'Muutoksia tehty.',
                                icon: 'success',
                                confirmButtonText: 'Sulje'
                            })
                        } else {
                            Swal.fire({
                                title: 'Anteeksi! Jotain meni pieleen.',
                                text: 'Yritä uudelleen.',
                                icon: 'error',
                                confirmButtonText: 'Sulje'
                            })
                        }
                    })
            }
        });
    }
}


//document.addEventListener('DOMContentLoaded', populateTrainers);
document.addEventListener('click', changeTables);
//document.querySelector('#title').addEventListener('change', populateTrainers);