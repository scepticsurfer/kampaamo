let workoutsAvailable = function(event) {
    event.preventDefault();

    // deleting existing options if exist
    let selectTd = document.querySelectorAll('#services_available > tr');
    let selectHeads=document.querySelectorAll('#head_table>tr');
    selectTd.forEach(function(selectTd) {
        selectTd.remove();
    });
    selectHeads.forEach(function(selectHead) {
        selectHead.remove();
    });
    // fetching available options
    let url = '/customers/reservation/servicesAvailable.json?date_from=' + document.querySelector('#date_from').value + '&date_to=' 
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
                        <th class="d-none">Id in timetable </th>
                        <th scope="col">Päivämäärä</th>
                        <th scope="col">Ajankohta</th>
                        <th scope="col">Palvelu</th>
                        <th scope="col">Osaaja</th>
                        <th scope="col">Hinta(€) </th>
                        <th scope="col">Ajanvaraus</th>                        
                    </tr> `
        head_table.innerHTML += content_head;
        let trSelect = document.querySelector('#services_available');
        data.forEach(item => {               
            // attaching options to select
            content = `<tr>
                        <td class="d-none">${item.timetable_id}</td>
                        <td>${item.date}</td>
                        <td>${item.time}</td>
                        <td>${item.service_name}</td>
                        <td>${item.username}</td>
                        <td> ${item.price}</td>
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