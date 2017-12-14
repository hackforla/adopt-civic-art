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

  var marker = [];

  for (var i = 0; i < locations.length; i++) {
    marker[i] = new google.maps.Marker({
      position: {
        lat: locations[i].lat,
        lng: locations[i].lon
      },
      map: map,
      title: locations[i].title,
      id: i,
      icon: pin
    });

    google.maps.event.addListener(marker[i], 'click', (function(marker, i) {
      return function() {
        if (lastMarker) {
          lastMarker.setIcon(pin);

          // only animate selected artwork if it's a new click
          // prevent re-animation if clicking on a highlighted pin
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
          // if no artwork marker is selected yet, then animate and select first one
          $('.artworks').animate({
            scrollTop: $artworks.eq(i).position().top + $artworksContainer.scrollTop()
          }, 750, function () {
            $artworks.eq(i).addClass('selected');
          });
        }

        marker[i].setIcon(pinSelected);

        // keep track of last selected artwork
        lastMarker = marker[i];
      }
    })(marker, i));
  }


  $artworks.hover(function () {
    $artworks.removeClass('selected');

    // unset last hovered or selected marker
    if (lastMarker) {
      lastMarker.setIcon(pin);
    }

    // set marker to current hovered artwork
    marker[$(this).index()].setIcon(pinSelected);

    lastMarker = marker[$(this).index()];
  }, function () {
    // reset all selected artwork markers after unhover
    marker[$(this).index()].setIcon(pin);
  });
}

window.initMap = initMap;
