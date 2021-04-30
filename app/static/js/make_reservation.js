let changeTables = function (event) {
    var element = event.target;
    // console.log(element.tagName);
    if (element.tagName === 'A') {
        if (element.parentElement.tagName !== 'TD') {
            return;
        }
        event.preventDefault();
        let id_in_timetable = element.parentElement.parentElement.children[0].innerHTML
        let url = '/customers/reservation/makeReservation.json?id_in_timetable=' + id_in_timetable 
        
        fetch(url)
            .then(function (response) {
                return response.json();
            }).then(function (data) {
                if (data == "true") {
                    element.parentElement.parentElement.remove();
                    Swal.fire({
                        title: '',
                        text: 'Paikka varattu. Tervetuloa harjoiteluun!',
                        icon: 'success',
                        confirmButtonText: 'Sulje'
                    })
                } else {
                    if (data.existing == "true") {
                        Swal.fire({
                            title: '',
                            text: 'Sinulla on jo treeni tänä aikana',
                            icon: 'error',
                            confirmButtonText: 'Sulje'
                        })
                    }
                    else {
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