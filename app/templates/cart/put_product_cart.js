let changeTables = function (event) {
    var element = event.target;
    if (element.tagName === 'A') {
        if (element.innerHTML !== 'OSTAA') {
            return;
        }
        event.preventDefault();

        let product_name = element.parentElement.parentElement.children[0].children[0].innerHTML
        let url = 'cart/product_to_cart.php?product_name=' + product_name;
        fetch(url)
            .then(function (response) {
                return response.json();
            }).then(function (data) {
                if (data.result == "true") {
                    Swal.fire({
                        title: '',
                        text: 'Tuote lisätty ostoskoriin.',
                        icon: 'success',
                        confirmButtonText: 'Sulje'
                    })
                } else {
                    if (data.registration == "false") {
                        Swal.fire({
                            title: '',
                            text: 'Kirjaudu tai luo tili. Se on ilmaista ja vie vain pari minuuttia.',
                            icon: 'warning',
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
                }

            }).catch(function (err) {
                console.log(err);
            });
    }
};

//document.addEventListener('DOMContentLoaded', populateTrainers);
document.addEventListener('click', changeTables);
//document.querySelector('#title').addEventListener('change', populateTrainers);