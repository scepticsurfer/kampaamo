let rezervWorkouts = function(event) {
    event.preventDefault();

    // deleting existing options if exist
    let selectWr = document.querySelectorAll('#reserv_row > tr');
    let selectHeads=document.querySelectorAll('#head_table > tr');
        selectWr.forEach(function(selectWr) {
        selectWr.remove();
    });
    selectHeads.forEach(function(selectHead) {
        selectHead.remove();
    });

    // fetching available options
    let url = 'get_client_workouts.php?date_from=' + document.querySelector('#date_from').value + '&date_to=' + document.querySelector('#date_to').value;
    fetch(url)
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        let head_table=document.getElementById('head_table')
        content_head=`<tr>
        <th scope="col">Päivämäärä</th>
        <th scope="col">Ajankohta</th>
        <th scope="col">Liikuntalaji</th>
        <th scope="col">Ohjaajat</th> 
        <th scope="col">Peruuta</th>                        
    </tr> `
        head_table.innerHTML += content_head;
        let trSelect = document.querySelector('#reserv_row');
        data.forEach(item => {
            // attaching options to select
            content = `<tr>
                       <td>${item.date}</td>
                       <td>${item.time}</td>
                       <td>${item.title}</td>
                       <td>${item.trainer}</td>
                       <td><a href="" class="btn custom-green-buy">Peruuta
                    </a></td>
                       </tr>                       
                    `;
            trSelect.innerHTML += content;
            
        });
    }).catch(function(err) {
        console.log(err);
    });
};

//document.addEventListener('DOMContentLoaded', rezervWorkouts);
document.querySelector('#client_select').addEventListener('click', rezervWorkouts);
//document.querySelector('#title').addEventListener('change', populateTrainers);