$(document).ready(function() {

  function SchoolsViewModel() {
    // Data
    var self = this
    self.folders = ['News', 'Schedule', 'Roster'];
    self.chosenFolderId = ko.observable();
    self.chosenFolderData = ko.observable();
    self.schools = ko.observableArray([]);
    self.selectedRosterData = ko.observableArray([]);
    self.selectedTeam = ko.observable();
    self.selectedSchool = ko.observable();
    self.selectedNewsArticles = ko.observableArray([]);
    self.selectedScheduleData = ko.observableArray([]);

    // Behaviours
    $.getJSON("/schools", function(data) {
      self.schools(data);
    });

    /*self.selectedRoster = function(school) {
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
    });*/

    self.selectedTeam.subscribe(function(newValue) {
      self.selectedSchool = newValue.school;
    });

    self.goToFolder = function(folder) {
      self.chosenFolderId(folder);
      route = "/" + folder
      self.chosenFolderData(null); // Stop showing a folder
      $.getJSON(route, { school: self.selectedSchool }, self.chosenFolderData);
    };


    /* self.goToSchool = function(school) { location.hash = school };
    self.goToFolder = function(folder) { location.hash = folder }; */



    // client side routes
    /*Sammy(function() {
      this.get('#:folder', function() {
          self.chosenFolderId(this.params.folder);
          self.chosenMailData(null);
          $.get("/mail", { folder: this.params.folder }, self.chosenFolderData);
      });

      this.get('#:folder/:mailId', function() {
          self.chosenFolderId(this.params.folder);
          self.chosenFolderData(null);
          $.get("/mail", { mailId: this.params.mailId }, self.chosenMailData);
      });

        this.get('', function() { this.app.runRoute('get', '#News') });
    }).run();*/

  };

  ko.applyBindings(new SchoolsViewModel());

});
