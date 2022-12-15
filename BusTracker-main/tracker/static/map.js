const map = new google.maps.Map(document.getElementById("map"), {
    center: new google.maps.LatLng(12.900504218997025, 80.22759925936454),
    zoom: 12,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
});

const directionsService = new google.maps.DirectionsService();

const directionsDisplay = new google.maps.DirectionsRenderer();

directionsDisplay.setMap(map);

var temp = {};

function calcRoute() {
    const out = document.getElementById('out')
    while (out.firstChild) {
        out.removeChild(out.lastChild);
    }
    var request = {
        origin: new google.maps.LatLng(12.90912456002448, 80.14238015243524),
        destination: new google.maps.LatLng(12.751791424068767, 80.14238015243524),
        travelMode: google.maps.TravelMode.TRANSIT,
        transitOptions: {
            modes: ['BUS']
        }
    }
    directionsService.route(request, function(result, status) {
        if(status == google.maps.DirectionsStatus.OK){
            // temp = result.routes[0];
            // var x = temp.legs[0].steps            
            // for (let i in x){
            //     const p = document.createElement('p')
            //     p.innerHTML = x[i].instructions
            //     out.appendChild(p)
            // }
            // const p = document.createElement('p')
            // p.innerText = "Fare - " + temp.fare.text
            // out.appendChild(p)
            // const q = document.createElement('p')
            // q.innerText = "Duration - " + temp.legs[0].duration.text
            // out.appendChild(q)
            directionsDisplay.setDirections(result);
        }
        else {
            const output = document.getElementById("out")
            directionsDisplay.setDirections({routes: []})
            map.setCenter(google.maps.LatLng(13.0826, 80.2707))
            output.innerText="404"
        }
    });
}

// var options = {
//     types: []
// }

// var ifrom = document.getElementById("ifrom");
// var auto1 = new google.maps.places.Autocomplete(ifrom, options)

// var ito = document.getElementById("ito");
// var auto2 = new google.maps.places.Autocomplete(ito, options)

// var getthere = document.getElementById("next");
// getthere.addEventListener('click',calcRoute);








// Initialize and add the map
// 12.751791424068767, 80.20377415001991
// 12.744827616271424, 80.19867819078947