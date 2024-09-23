*** Settings ***
Library        SeleniumLibrary
Resource       locators.robot

*** Keywords ***
fill login form
    [Arguments]    ${username}    ${password}
    Input Text     ${username_field_locator}    ${username}
    Input Text     ${password_field_locator}    ${password}
    Click Button   ${login_button_locator}

Logout User
    Click Button  ${logout_button_locator}

