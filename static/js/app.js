var $ = require('jQuery');

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: new google.maps.LatLng(34.0639, -118.3592),
    zoom: 11,
    scrollwheel: false
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

$(function() {
  window.initMap = initMap;
});
