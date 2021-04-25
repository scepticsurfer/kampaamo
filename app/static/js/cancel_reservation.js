
let changeTables = function (event) {
    var element = event.target;
    // console.log(element.tagName);
    if (element.tagName === 'A') {
        if (element.parentElement.tagName !== 'TD') {
            return;
        }
        event.preventDefault();
        let cancel_id = element.parentElement.parentElement.children[0].innerHTML
        //let time = element.parentElement.parentElement.children[2].innerHTML
        let master = element.parentElement.parentElement.children[4].innerHTML
        Swal.fire({
            title: '',
            text: "Haluatko varmasti peruuttaa varauksesi?",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Kyllä!',
            cancelButtonText: 'En halua'
        }).then((result) => {
            if (result.isConfirmed) {
                let url = '/customers/client_page/cancelReservation.json?cancel_id=' + cancel_id  + '&master='+ master;
                fetch(url)
                    .then(function (response) {
                        return response.json();
                    }).then(function (data) {
                        if (data == "true"){
                            element.parentElement.parentElement.remove();
                            Swal.fire(
                                'Peruutettu!',
                                'Varauksesi peruutettu .',
                                'success'
                            )
                        } else{Swal.fire({
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
