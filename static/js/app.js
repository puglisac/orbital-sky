document.querySelector('#location-btn').addEventListener('click', getUserLocation)

const wwd = new WorldWind.WorldWindow("globe");

wwd.addLayer(new WorldWind.BMNGOneImageLayer());
wwd.addLayer(new WorldWind.BMNGLandsatLayer());
wwd.addLayer(new WorldWind.CoordinatesDisplayLayer(wwd));
wwd.addLayer(new WorldWind.ViewControlsLayer(wwd));

function getUserLocation() {

  async function successCallback(position) {
    const userData = {
      alt: position.coords.altitude ? position.coords.altitude : 0,
      label: 'Your Location',
      lat: position.coords.latitude,
      long: position.coords.longitude,
    }
    generatePlacemark(userData);
    const resp = await axios.get(`/satellites/api/${userData.lat}/${userData.long}/${userData.alt}/70`);
    resp.data.forEach((sat) => {
      const satData = {
        alt: sat.sat_location.satalt,
        label: `${sat.sat_info.satname}`,
        lat: sat.sat_location.satlat,
        long: sat.sat_location.satlng,
      }
      generatePlacemark(satData);
    });
  };

  function errorCallback(err) {
    console.log(err);
    alert('Something went wrong. Please try again.')
  }

  navigator.geolocation.getCurrentPosition(successCallback, errorCallback)
}

function generatePlacemark(data) {
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
  const position = new WorldWind.Position(data.lat, data.long, data.alt);
  const placemark = new WorldWind.Placemark(position, true, placemarkAttributes);
  placemark.label = `${data.label}` +
    "\nLat " + placemark.position.latitude.toPrecision(4).toString() + "\n" +
    "Lon " + placemark.position.longitude.toPrecision(5).toString();
  placemark.alwaysOnTop = true;
  placemarkLayer.addRenderable(placemark);
}