Feature: Send Email

  Scenario: Successful send to saved contact
    Given the user is logged into the email
    When the user clicks on the new message button
    Then the user should see new message component
    When the user clicks on insert contacts button
    Then the user should see the insert contacts component
    When the user selects a contact from the contact list
    And the user clicks on insert contacts
    Then the user should see the selected contact in the recipients input
    When the user enters the email subject and body
    And the user clicks on the send button
    Then the email should be sent successfully

  Scenario: Successful send with attachement to saved contact
    Given the user is logged into the email
    When the user clicks on the new message button
    Then the user should see new message component
    When the user clicks on insert contacts button
    Then the user should see the insert contacts component
    When the user selects a contact from the contact list
    And the user clicks on insert contacts
    Then the user should see the selected contact in the recipients input
    When the user attaches the attachment
    And the user enters the email subject and body
    Then the user should see saved label in the footer
    When the user clicks on the send button
    Then the email should be sent successfully
