< !DOCTYPE html >
  <head>
    <title>KnockoutJS Simple Example</title>
    <script src="https://ajax.aspnetcdn.com/ajax/knockout/knockout-3.1.0.js"
      type="text/javascript"></script>
  </head>

  <body>
    <!-- This is called "view" of HTML markup that defines the appearance of UI -->

      <p>First String: <input data-bind="value: firstString" /></p>
    <p>Second String: <input data-bind="value: secondString" /></p>

    <p>First String: <strong data-bind="text: firstString">Hi</strong></p>
    <p>Second String: <strong data-bind="text: secondString">There</strong></p>

    <p>Derived String: <strong data-bind="text: thirdString"></strong></p>

    <script>
      <!-- This is called "viewmodel". This javascript section defines the data and
         behavior of UI -->

         function AppViewModel() {
        this.firstString = ko.observable("Enter First String");
      this.secondString = ko.observable("Enter Second String");

            this.thirdString = ko.computed(function() {
               return this.firstString() + " " + this.secondString();
   }, this);
}

// Activates knockout.js
ko.applyBindings(new AppViewModel());
      </script>

  </body>
</html >
