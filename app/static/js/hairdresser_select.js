let getHairdresser = function() {
    // deleting existing options if exist
    let selectOptions = document.querySelectorAll('#hairdresser > option');
    selectOptions.forEach(function(selectOption) {
        selectOption.remove();
    });

    // fetching available options
    let url = '/customers/reservation/hairdresser/<'+ document.querySelector('#service').value +'>' 
    fetch(url)
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        let hairdresserSelect = document.querySelector('#hairdresser');
        data.forEach(item => {
            // attaching options to select
            content = `<option value="${item.id}">${item.username}</option>`;
            hairdresserSelect.innerHTML += content;
        });
    }).catch(function(err) {
        console.log(err);
    });
};

document.addEventListener('DOMContentLoaded', getHairdressers);
document.querySelector('#tservice').addEventListener('change', getHairdressers);