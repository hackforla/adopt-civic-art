var $ = require('jquery');

function initMap() {
  var locations = [];
  var $artworksContainer = $('.artworks');
  var $artworks = $('.artworks li');
  var pin = '/dist/img/pin--red.svg';
  var pinSelected = '/dist/img/pin--blue.svg';
  var lastMarker;

  $artworks.each(function (index) {
    locations.push($(this).data());
  });

  var map = new google.maps.Map(document.getElementById('map'), {
    center: new google.maps.LatLng(34.127813, -118.3129888),
    zoom: 9,
    scrollwheel: false,
    mapTypeControl: false,
    streetViewControl: false
  });

  for (var i = 0; i < locations.length; i++) {
    var marker = new google.maps.Marker({
      position: {
        lat: locations[i].lat,
        lng: locations[i].lon
      },
      map: map,
      title: locations[i].title,
      id: locations[i].id,
      icon: pin
    });

    google.maps.event.addListener(marker, 'click', (function(marker, i) {
      return function() {
        if (lastMarker) {
          lastMarker.setIcon(pin);

          if (lastMarker.id !== i) {
            $artworks.removeClass('selected');

            $('.artworks').animate({
              scrollTop: $artworks.eq(i).position().top + $artworksContainer.scrollTop()
            }, 750, function () {
              $artworks.eq(i).addClass('selected');
            });
          }
        }
        else {
          $('.artworks').animate({
            scrollTop: $artworks.eq(i).position().top + $artworksContainer.scrollTop()
          }, 750, function () {
            $artworks.eq(i).addClass('selected');
          });
        }

        marker.setIcon(pinSelected);

        lastMarker = marker;
        lastMarker.id = i;
      }
    })(marker, i));
  }
}

window.initMap = initMap;
