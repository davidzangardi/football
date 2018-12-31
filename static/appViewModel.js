$(document).ready(function() {

  function SchoolsViewModel() {
    // Data
    var self = this
    self.folders = ['News', 'Schedule', 'Roster'];
    self.chosenFolderId = ko.observable();
    self.chosenFolderData = ko.observable();
    self.schools = ko.observableArray([]);
    self.selectedRosterData = ko.observableArray([]);
    self.selectedSchool = ko.observable();
    self.selectedNewsArticles = ko.observableArray([]);
    self.selectedScheduleData = ko.observableArray([]);

    // Behaviours
    $.getJSON("/schools", function(data) {
      self.schools(data);
    });

    self.selectedRoster = function(school) {
      $.getJSON("/rosters", { school: school }, function(data) {
        self.selectedRosterData(data);
      });
    };

    self.selectedNews = function(school) {
      $.getJSON("/news", { school: school }, function(data) {
        self.selectedNewsArticles(data);
      });
    };

    self.selectedSchedule = function(school) {
      $.getJSON("/schedules", { school: school }, function(data) {
        self.selectedScheduleData(data);
      });
    };

    self.selectedSchool.subscribe(function(newValue) {
      self.selectedRoster(newValue.school);
      self.selectedNews(newValue.school);
      self.selectedSchedule(newValue.school);
    });




  };

  ko.applyBindings(new SchoolsViewModel());

});
