// See https://jsfiddle.net/api/post/library/pure/
let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 40.4406, lng: -79.9959 },
    zoom: 12,
  });
    console.log("Executed");
}
