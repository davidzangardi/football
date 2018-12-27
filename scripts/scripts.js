function teamInfo(name) {
  // deal with nothing is chosen
  if (name == "")
    return;

  // create new ajax object
  var ajax = new XMLHttpRequest();

  // when page is loaded have callback function fill div
  ajax.onreadystatechange = function() {
    if (ajax.readyState == 4 && ajax.status == 200) {
      $('#infodiv').html(ajax.responseText);
    }
  };

  //open requested file and transmit data
  ajax.open('GET', name + '.html', true);
  ajax.send();
}
