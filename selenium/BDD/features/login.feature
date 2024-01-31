Feature: Login
  Scenario: Login to the nopcommerence application
    Given Launch the browser
    When navigate to the application
    And enter  "admin@yourstore.com" and "admin"
    And click on submit button
    Then verify the dashboard heading in the home page