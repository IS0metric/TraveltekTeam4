var destination = "Puerto Quenzal";

$('#video-container').html('<iframe id="ytplayer" type="text/html" width="720" height="405" src="https://www.youtube.com/embed/?listType=search&list=' + destination + ' travel" frameborder="0" allowfullscreen>');

function initMap() {
    var geocoder = new google.maps.Geocoder();
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: {lat: -34.397, lng: 150.644}
    });
    geocodeAddress(geocoder, map);       
}

function geocodeAddress(geocoder, resultsMap) {
    var address = destination;
    geocoder.geocode({'address': address}, function(results, status) {
        if (status === 'OK') {
        resultsMap.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
            map: resultsMap,
            position: results[0].geometry.location
        });
        } else {
        alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}