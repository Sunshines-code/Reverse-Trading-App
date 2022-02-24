var myMap = L.map("map", {
    center: [15.5994, -28.6731],
    zoom: 3
});

L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
}).addTo(myMap);


var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

d3.json(url).then(function (response) {
    var circlecolor = "";
    for (var i = 0; i < 1000; i++) {

    if (response.features[i].geometry.coordinates[2] > 20) {
        circlecolor = "red";
    }
    else if (response.features[i].geometry.coordinates[2] > 4) {
        circlecolor = "yellow";
    }
    else if (response.features[i].geometry.coordinates[2] > 1) {
        circlecolor = "green";
    }
    else {
        circlecolor = "blue";
    }
var location = response.features[i].properties.place
    L.circle([response.features[i].geometry.coordinates[1], response.features[i].geometry.coordinates[0]], {
        color: "white",
        fillColor: circlecolor,
        fillOpacity: 0.70,
        radius: response.features[i].properties.mag * 15000
    }).bindPopup("<h1>" + location+ "</h1> <hr> <h3>Depth: "+ response.features[i].geometry.coordinates[2] + "</h3>"
    +"<br>"+ "<hr> <h3>Magnitude: "+ response.features[i].properties.mag+ "</h3>" +"</br>")
    .addTo(myMap);
    }
   });
