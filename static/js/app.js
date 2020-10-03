document.querySelector('#location-btn').addEventListener('click', getUserLocation)

const wwd = new WorldWind.WorldWindow("globe");

wwd.addLayer(new WorldWind.BMNGOneImageLayer());
wwd.addLayer(new WorldWind.BMNGLandsatLayer());
wwd.addLayer(new WorldWind.CoordinatesDisplayLayer(wwd));
wwd.addLayer(new WorldWind.ViewControlsLayer(wwd));

function getUserLocation() {
  function successCallback(position) {
    const userLocation = {
      lat: position.coords.latitude,
      long: position.coords.longitude,
      alt: position.coords.altitude ? position.coords.altitude : 0,
    }
    addIconForUser(userLocation);
  }

  function errorCallback(err) {
    // Show pop up with err message
  }

  navigator.geolocation.getCurrentPosition(successCallback, errorCallback)
}

function addIconForUser(location) {
  const placemarkLayer = new WorldWind.RenderableLayer("Placemark");
  wwd.addLayer(placemarkLayer);
  const placemarkAttributes = new WorldWind.PlacemarkAttributes(null);
  placemarkAttributes.imageOffset = new WorldWind.Offset(
    WorldWind.OFFSET_FRACTION, 0.3,
    WorldWind.OFFSET_FRACTION, 0.0);
  placemarkAttributes.labelAttributes.color = WorldWind.Color.YELLOW;
  placemarkAttributes.labelAttributes.offset = new WorldWind.Offset(
    WorldWind.OFFSET_FRACTION, 0.5,
    WorldWind.OFFSET_FRACTION, 1.0);
  placemarkAttributes.imageSource = WorldWind.configuration.baseUrl + "images/pushpins/plain-red.png";
  const position = new WorldWind.Position(location.lat, location.long, location.alt);
  const placemark = new WorldWind.Placemark(position, true, placemarkAttributes);
  placemark.label = "Your Location\n" +
    "Lat " + placemark.position.latitude.toPrecision(4).toString() + "\n" +
    "Lon " + placemark.position.longitude.toPrecision(5).toString();
  placemark.alwaysOnTop = true;
  placemarkLayer.addRenderable(placemark);
}