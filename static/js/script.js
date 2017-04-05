/*global $*/
/*global L*/

/*
 * Initialize Map
 */
L.mapbox.accessToken = 'pk.eyJ1IjoibWF0aWtpbjkiLCJhIjoiYjMyMjBjZTE4NWUxMDkxOWZjZjFjZWEzZTcxNDUxOTkifQ._ldFl3e17jCs7aWm6zMZ3Q';
var mymap = L.map('map-display').setView([34.15, -118.24], 9);
L.mapbox.styleLayer('mapbox://styles/matikin9/cim5bt1q100iy9jkpl7ff9d1h').addTo(mymap);

$.getJSON('/js/toptenv1.json', function(data) {
    $.each( data, function( key, val ) {
        var $popup = $("<div>", { 
        	"id": key
        });
        
        // Create element with restaurant info.
        $popup.append("<h1>" + val.title + "</h1>");
        $popup.append("<p>" + val.desc.substring(0, 100) + "..." + "</p>");
        
        var m = L.marker([val.lat, val.lng])
            	 .bindPopup($popup[0])
            	 .addTo(mymap);
    });
});