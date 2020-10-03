document.querySelector('#location-btn').addEventListener('click', getUserLocation)

function getUserLocation() {
  function successCallback(position) {
    // Send position.coords.latitude, position.coords.longitude, position.coords.altitude to api
  }

  function errorCallback(err) {
    // Show pop up with err message
  }

  navigator.geolocation.getCurrentPosition(successCallback, errorCallback)
}