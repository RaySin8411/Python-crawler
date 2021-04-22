### robot_test_keywords.robot ###

*** Settings ***

Library  robot_test_steps.py

*** Keywords ***

User network connected
    verify_network_is_connected

User browse Medium page
    open_browser_to_medium_page

User will see "${PageTitle}" keyword in page title
    verify_browser_title  ${PageTitle}