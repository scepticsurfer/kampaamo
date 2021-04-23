let workoutsAvailable = function(event) {
    event.preventDefault();

    // deleting existing options if exist
    let selectTd = document.querySelectorAll('#workouts_available > tr');
    let selectHeads=document.querySelectorAll('#head_table>tr');
    selectTd.forEach(function(selectTd) {
        selectTd.remove();
    });
    selectHeads.forEach(function(selectHead) {
        selectHead.remove();
    });
    // fetching available options
    let url = '/customers/client_page/aviableServises.json?date_from=' + document.querySelector('#date_from').value + '&date_to=' 
                                                      + document.querySelector('#date_to').value+ '&workout='
                                                      + document.querySelector('#title').value+ '&trainer='
                                                      + document.querySelector('#trainer').value
                                                      ;
    fetch(url)
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        let head_table=document.getElementById('head_table')
        content_head=`<tr>
                        <th scope="col">Päivämäärä</th>
                        <th scope="col">Ajankohta</th>
                        <th scope="col">Liikuntalaji</th>
                        <th scope="col">Ohjaaja</th>
                        <th scope="col">Vapaat paikat</th>
                        <th scope="col">Ajan varaus</th>                        
                    </tr> `
        head_table.innerHTML += content_head;
        let trSelect = document.querySelector('#workouts_available');
        data.forEach(item => {               
            // attaching options to select
            content = `<tr>
                        <td>${item.date}</td>
                        <td>${item.time}</td>
                        <td>${item.title}</td>
                        <td>${item.trainer}</td>
                        <td>${item.free_slots}</td>
                        <td><a href="" class="btn custom-green-buy">Varaa
                            </a></td>                       
                       </tr>
            `;
            trSelect.innerHTML += content;
        });
    }).catch(function(err) {
        console.log(err);
    });
};

//document.addEventListener('DOMContentLoaded', populateTrainers);
document.querySelector('#find_available').addEventListener('click', workoutsAvailable);
//document.querySelector('#title').addEventListener('change', populateTrainers);