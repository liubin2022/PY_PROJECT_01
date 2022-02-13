*** Settings ***
Library           ../../TestCase/Application01/TestCase01.py

*** Test Cases ***
testcast0001
    ${aa}    Set Variable    aa
    log    ${aa}
    aaa
