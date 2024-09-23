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
Library    ../librairies/icdc/LaptopActions/LaptopActionsLibrary.py
Library      SeleniumLibrary

*** Variables ***
${ENVIRONMENT}     dev  # Valeur par défaut

*** Test Cases ***                      
Test_Import_Lib
    [Tags]   xxx   xxx
    [Documentation]    Ceci est un exemple de test utilisant les variables d'environnement
    LaptopActionsLibrary.Press Key    tab
    LaptopActionsLibrary.Hold And Press Key       Ctrl      tab
    


    
