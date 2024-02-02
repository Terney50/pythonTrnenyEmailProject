Feature: Trneny Indra Avitech email test case

  Scenario: Email login (Block 1)
    Given Open browser
    When Log in to email
    Then Check that you are logged in
    When Logout from email


  Scenario: Send email (Block 2)
    Given Open browser
    When Log in to email
    Then Check that you are logged in
    When Write a new email message
    And Send the message to professorcze@gmail.com
    And Logout from email


  Scenario: Send email with attachment (Block 3)
    Given Open browser
    When Log in to email
    Then Check that you are logged in
    When Write a new email message
    And Add attachment to the email
    And Send the message to professorcze@gmail.com
    And Logout from email