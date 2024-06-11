Feature: Login and Logout of Email

  Scenario: Successful login and logout
    Given the user navigates to the email login page
    When the user enters valid credentials
    And the user clicks on the login button
    Then the user should see the inbox
    When the user opens the user dropdown menu
    And the user clicks on the logout button
    Then the user should be redirected to the login page
