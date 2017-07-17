var $ = require('jQuery');

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: new google.maps.LatLng(34.0849232, -118.8557029),
    zoom: 9,
    scrollwheel: false,
    mapTypeControl: false,
    streetViewControl: false
  });

  $('.artworks li').each(function (index) {
    new google.maps.Marker({
      position: {
        lat: $(this).data('lat'),
        lng: $(this).data('lon')
      },
      map: map,
      title: $(this).data('title')
    });
  });
}

window.initMap = initMap;
