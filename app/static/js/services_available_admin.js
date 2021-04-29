let servicesAll = function(event) {
    event.preventDefault();

    // deleting existing options if exist
    let selectHeads=document.querySelectorAll('#head_table>tr');
    let tableTrs = document.querySelectorAll('#services_all > tr');
    tableTrs.forEach(function(tableTr) {
        tableTr.remove();
    });
    selectHeads.forEach(function(selectHead) {
        selectHead.remove();
    });

    // fetching available options    
    let url = '/admins/admin_page/servicesAvailableAdmin.json?date_from=' + document.querySelector('#date_from').value + '&date_to=' 
                                                                     + document.querySelector('#date_to').value+ '&service_id='
                                                                     + document.querySelector('#service').value+ '&hairdresser_id='
                                                                     + document.querySelector('#hairdresser').value
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
        <th scope="col">Hinta(€)</th>
        <th scope="col">Tila</th>
        <th scope="col">Muokaa</th>
                                                                    
    </tr>
        `
        head_table.innerHTML += content_head;
        let trTable = document.querySelector('#services_all');
        data.forEach(item => {               
            // attaching options to select
            content = `<tr>
                       <td class="d-none">${item.timetable_id}</td>
                       <td>${item.date}</td>
                       <td>${item.time}</td>
                       <td>${item.service_name}</td>
                       <td>${item.username}</td>
                       <td>${item.price}</td>
                       <td>${item.status}</td>
                       <td><a href="/admins/new_change_workout?workout_id=${item.timetable_id}" class="btn custom-green-buy">Muokaa</a></td>                
                       
                       </tr>
            `;
            trTable.innerHTML += content;
        });
    }).catch(function(err) {
        console.log(err);
    });
};

//document.addEventListener('DOMContentLoaded', populateTrainers);
document.querySelector('#find_services').addEventListener('click', servicesAll);
//document.querySelector('#title').addEventListener('change', populateTrainers);