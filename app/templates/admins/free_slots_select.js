
let selectFreeSlots = function() {
     //deleting existing options if exist
    let selectInputs = document.querySelectorAll('#free_max_slots > input');
    selectInputs.forEach(function(selectInput) {
       selectInput.remove();
 });

    // fetching available options
    let workout_id="";
    if(document.querySelector('#workout_id')){workout_id=document.querySelector('#workout_id').value}
    let url = 'get_free_slots.php?title_id=' + document.querySelector('#title').value+ '&workout_id='
                                               + workout_id;
    fetch(url)
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        let free_slots_select = document.querySelector('#free_max_slots');
            content = `<input type="text" class="form-control" name="free_slots" id="free_slots"value="${data}" readonly>`;
            free_slots_select.innerHTML += content;
    }).catch(function(err) {
        console.log(err);
    });
}

document.addEventListener('DOMContentLoaded', selectFreeSlots);
document.querySelector('#title').addEventListener('change', selectFreeSlots);
