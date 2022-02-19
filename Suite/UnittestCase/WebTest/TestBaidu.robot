*** Settings ***
Library           ../../../TestCase/UnittestCase/WebTest/TestBaidu.py

*** Test Cases ***
TestBaidu
    [Setup]    setUp
    test_baidu
    [Teardown]    tearDown
