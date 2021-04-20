let populateTrainers = function() {
    // deleting existing options if exist
    let selectOptions = document.querySelectorAll('#trainer > option');
    selectOptions.forEach(function(selectOption) {
        selectOption.remove();
    });

    // fetching available options
    let url = 'get_trainers.php?title_id=' + document.querySelector('#title').value;
    fetch(url)
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        let trainerSelect = document.querySelector('#trainer');
        data.forEach(item => {
            // attaching options to select
            content = `<option value="${item.id}">${item.name}</option>`;
            trainerSelect.innerHTML += content;
        });
    }).catch(function(err) {
        console.log(err);
    });
};

document.addEventListener('DOMContentLoaded', populateTrainers);
document.querySelector('#title').addEventListener('change', populateTrainers);