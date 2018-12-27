$(document).ready(function() {

  function SchoolsViewModel() {
    var self = this;
    self.schools = ko.observableArray([]);

    $.getJSON("/schools", function(data) {
      self.schools(data);
    });
    self.selectedSchool = ko.observable();
  };

  ko.applyBindings(new SchoolsViewModel());

});
