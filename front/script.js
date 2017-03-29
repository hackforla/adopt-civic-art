/*global $*/
/*global L*/
/*global firebase*/

/*
 * Initialize Map
 */
L.mapbox.accessToken = 'pk.eyJ1IjoibWF0aWtpbjkiLCJhIjoiYjMyMjBjZTE4NWUxMDkxOWZjZjFjZWEzZTcxNDUxOTkifQ._ldFl3e17jCs7aWm6zMZ3Q';
var mymap = L.map('map-display').setView([34.0522, -118.2437], 13);
L.mapbox.styleLayer('mapbox://styles/matikin9/cim5bt1q100iy9jkpl7ff9d1h').addTo(mymap);

