# *** Settings ***
# Variables    ../config/env_config.yml
# Library      SeleniumLibrary

# *** Variables ***
# ${ENVIRONMENT}      ${dev}  

# *** Test Cases ***
# Example Test
#     Log    Environnement : ${ENVIRONMENT}
#     Log    Base URL : ${ENVIRONMENT}[base_url]
#     Open Browser    ${ENVIRONMENT}[base_url]     ${ENVIRONMENT}[browser]


*** Settings ***
Variables    ../config/env_config.yml
Library      SeleniumLibrary
Resource     ../resources/homePage/actions.robot
Resource     ../resources/loginPage/actions.robot

*** Variables ***
${ENVIRONMENT}     dev  # Valeur par défaut

*** Test Cases ***
Example Test
    [Tags]    656121
    # [Documentation]    Ceci est un exemple de test utilisant les variables d'environnement
    # Log    Environnement : ${ENVIRONMENT}
    # Log    Base URL : ${${ENVIRONMENT}.base_url}
    # Open Browser     ${${ENVIRONMENT}.base_url}    ${${ENVIRONMENT}.browser}
    fill login form   user   password
    Maximize Browser Window
    Close Browser

Example Test 2
    IF    '${ENVIRONMENT}' == 'dev'
        Log    Exécution dans l'environnement DEV
        Open Browser    ${dev.base_url}    ${dev.browser}
    ELSE IF    '${ENVIRONMENT}' == 'staging'
        Log    Exécution dans l'environnement STAGING
        Open Browser    ${staging.base_url}    ${staging.browser}
    ELSE IF    '${ENVIRONMENT}' == 'prod'
        Log    Exécution dans l'environnement PROD
        Open Browser    ${prod.base_url}      ${prod.browser}
    END
    Maximize Browser Window
    Close Browser
