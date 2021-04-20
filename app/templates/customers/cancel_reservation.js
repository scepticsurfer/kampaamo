
let changeTables = function (event) {
    var element = event.target;
    // console.log(element.tagName);
    if (element.tagName === 'A') {
        if (element.parentElement.tagName !== 'TD') {
            return;
        }
        event.preventDefault();
        let date = element.parentElement.parentElement.children[0].innerHTML
        let time = element.parentElement.parentElement.children[1].innerHTML
        //let title = element.parentElement.parentElement.children[2].innerHTML
        //let trainer = element.parentElement.parentElement.children[3].innerHTML
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
                let url = 'cancel_change_tables.php?date=' + date + '&time=' + time /*+ '&title=' + title + '&trainer=' + trainer*/;
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
