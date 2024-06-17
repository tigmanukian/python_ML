*** Settings ***
Documentation     This is a simple test case to open a web browser, wait for a few seconds, and then verify the page title.
Library           SeleniumLibrary
Library           BuiltIn

*** Variables ***
${BROWSER}        Chrome
${URL}            https://www.example.com
${EXPECTED TITLE} Example Domain

*** Test Cases ***
Open Browser, Wait, and Verify Page Title
    Open Browser    ${URL}    ${BROWSER}
    Sleep    5s   # Wait for 5 seconds
    Title Should Be    ${Example Domain}
    Close Browser
