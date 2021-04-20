let userName = function() {
    // deleting existing options if exist
   // let selectNames = document.querySelectorAll('#user_name');
   // selectNames.forEach(function(selectName) {
   //     selectName.remove();
   // });

    // fetching available options
    let url = '../forms/get_user_name.php'
    fetch(url)
    .then(function(response) {
        return response.json();
    }).then(function(data) {
        if (data!=""){
           
        document.getElementById('user_name').innerHTML=data   
        } 
    }).catch(function(err) {
        console.log(err);
    });
};

document.addEventListener('DOMContentLoaded', userName);
//document.querySelector('#title').addEventListener('change', populateTrainers);
