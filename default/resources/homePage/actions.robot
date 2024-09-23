*** Settings ***
Resource    locators.robot   # Import des locators de la homepage
Library     SeleniumLibrary

*** Keywords ***
Click Home Button
    [Documentation]  Ce mot-clé clique sur le bouton d'accueil
    Click Element    ${HOME_BUTTON}
-
Search for Item
    [Arguments]    ${search_term}
    [Documentation]  Ce mot-clé permet de rechercher un article
    Input Text    ${SEARCH_BAR}    ${search_term}
    Click Button  ${SUBMIT_BUTTON}

Click Login Button
    [Documentation]  Ce mot-clé clique sur le bouton de connexion
    Click Element    ${LOGIN_BUTTON}

Click Contact Us Button
    [Documentation]  Ce mot-clé clique sur le bouton "Contactez-nous"
    Click Element    ${CONTACT_US_BUTTON}