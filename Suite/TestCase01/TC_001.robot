*** Settings ***
Library           ../../TestCase/Application01/TestCase01.py

*** Test Cases ***
testcast0001
    ${aa}    Set Variable    123
    log    ${aa}
    aaa
