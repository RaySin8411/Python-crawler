### robot_test_features.robot ###

*** Settings ***
Resource    robot_test_keywords.robot

*** Test Cases ***
Medium Page
    Given User network connected
    When User browse Medium page
    Then User will see "Medium" keyword in page title