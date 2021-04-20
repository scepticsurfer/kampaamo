
let trainerTimetable = function(event) {
    event.preventDefault();

    // deleting existing options if exist
    let selectTd = document.querySelectorAll('#timetable_row > tr');
    let selectHeads=document.querySelectorAll('#head_table>tr');
    selectTd.forEach(function(selectTd) {
        selectTd.remove();
    });
    selectHeads.forEach(function(selectHead) {
        selectHead.remove();
    });
    // fetching available options
    let url = 'get_workouts.php?date_from=' + document.querySelector('#date_from').value + '&date_to=' + document.querySelector('#date_to').value;
    fetch(url)
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        let head_table=document.getElementById('head_table')
        content_head=`<tr>
        <th scope="col">Päivämäärä</th>
        <th scope="col">Ajankohta</th>
        <th scope="col">Liikuntalaji</th>
        <th scope="col">Vapaat paikat</th>
        <th scope="col">Osallistujat</th>
        <th scope="col">Tila</th>
    </tr> `
        head_table.innerHTML += content_head;
        let trSelect = document.querySelector('#timetable_row');
        data.forEach(item => {
            // attaching options to select
            content = `<tr>
                       <td>${item.date}</td>
                       <td>${item.time}</td>
                       <td>${item.title}</td>
                       <td>${item.free_slots}</td>
                       <td>${item.participants}</td>
                       <td>${item.status}</td>
                       </tr>
            `;
            trSelect.innerHTML += content;
        });
    }).catch(function(err) {
        console.log(err);
    });
};

//document.addEventListener('DOMContentLoaded', populateTrainers);
document.querySelector('#show').addEventListener('click', trainerTimetable);
//document.querySelector('#title').addEventListener('change', populateTrainers);
