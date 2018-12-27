require(['knockout-3.4.2', 'appViewModel', 'domReady!'], function(ko, appViewModel) {
  ko.applyBindings(new appViewModel());
});
