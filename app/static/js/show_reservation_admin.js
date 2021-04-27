let reservationsAll = function(event) {
    event.preventDefault();

    // deleting existing options if exist
    let selectHeads=document.querySelectorAll('#head_table>tr');
    let tableTrs = document.querySelectorAll('#reservations_all > tr');
    tableTrs.forEach(function(tableTr) {
        tableTr.remove();
    });
    selectHeads.forEach(function(selectHead) {
        selectHead.remove();
    });

    // fetching available options    
    let url = '/admins/reservation_admin/servicesRegistration.json?date_from=' + document.querySelector('#date_from').value + '&date_to=' 
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
        <th scope="col">Asiakas</th> 
        <th scope="col">Asiakkaan puhelinnumero</th>                                                                        
    </tr>
        `
        head_table.innerHTML += content_head;
        let trTable = document.querySelector('#reservations_all');
        data.forEach(item => {               
            // attaching options to select
            content = `<tr>
                       <td class="d-none">${item.reservation_id}</td>
                       <td>${item.date}</td>
                       <td>${item.time}</td>
                       <td>${item.service_name}</td>
                       <td>${item.hairdresser_name}</td>
                       <td>${item.client_name}</td>
                       <td>${item.phone_number}</td>                
                       
                       </tr>
            `;
            trTable.innerHTML += content;
        });
    }).catch(function(err) {
        console.log(err);
    });
};

//document.addEventListener('DOMContentLoaded', populateTrainers);
document.querySelector('#find_services').addEventListener('click', reservationsAll);
//document.querySelector('#title').addEventListener('change', populateTrainers);