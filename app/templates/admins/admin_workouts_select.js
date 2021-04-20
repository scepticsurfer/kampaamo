let workoutsAll = function(event) {
    event.preventDefault();

    // deleting existing options if exist
    let selectHeads=document.querySelectorAll('#head_table>tr');
    let tableTrs = document.querySelectorAll('#workouts_all > tr');
    tableTrs.forEach(function(tableTr) {
        tableTr.remove();
    });
    selectHeads.forEach(function(selectHead) {
        selectHead.remove();
    });

    // fetching available options    
    let url = 'get_workouts_admin.php?date_from=' + document.querySelector('#date_from').value + '&date_to=' 
                                                      + document.querySelector('#date_to').value+ '&title='
                                                      + document.querySelector('#title').value+ '&trainer='
                                                      + document.querySelector('#trainer').value 
                                                      ;
    fetch(url)
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        let head_table=document.getElementById('head_table')
        content_head=`<tr>
        <th class="d-none">id </th>
        <th scope="col">Päivämäärä</th>
        <th scope="col">Ajankohta</th>
        <th scope="col">Liikuntalaji</th>
        <th scope="col">Ohjaaja</th>
        <th scope="col">Vapaat paikat</th>
        <th scope="col">Tila</th>
        <th scope="col">Muokaa</th>
        <th scope="col">Ilmoita</th>                                                             
    </tr>
        `
        head_table.innerHTML += content_head;
        let trTable = document.querySelector('#workouts_all');
        data.forEach(item => {               
            // attaching options to select
            content = `<tr>
                      <td class="d-none">${item.workout_id}</td>
                       <td>${item.date}</td>
                       <td>${item.time}</td>
                       <td>${item.title}</td>
                       <td>${item.trainer}</td>
                       <td>${item.free_slots}</td>
                       <td>${item.status}</td>
                       <td><a href="new_change_workout.php?workout_id=${item.workout_id}" class="btn custom-green-buy">Muokaa</a></td>                
                       <td><a href="get_participants.php?workout_id=${item.workout_id}" class="btn custom-green-buy">Osallistujat</a></td>
                       </tr>
            `;
            trTable.innerHTML += content;
        });
    }).catch(function(err) {
        console.log(err);
    });
};

//document.addEventListener('DOMContentLoaded', populateTrainers);
document.querySelector('#find_workouts').addEventListener('click', workoutsAll);
//document.querySelector('#title').addEventListener('change', populateTrainers);