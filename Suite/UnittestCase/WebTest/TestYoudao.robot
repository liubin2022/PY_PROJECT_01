*** Settings ***
Library           ../../../TestCase/UnittestCase/WebTest/TestYoudao.py

*** Test Cases ***
TestYoudao
    [Setup]    setUp
    test_youdao
    [Teardown]    tearDown
