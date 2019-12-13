*** settings ***
Documentation   To know how many options to run robot file

*** Variables ***
${ONE}     99

*** Test Cases **
Testcase:1
    Sleep     1s
    Log    TestCase 1 ==> ${ONE}   ERROR

Testcase:2
    Sleep     1s
    Log    Version 5.6 TestCase 2    ERROR

Testcase:3
    Sleep     1s
    Log    Version 5.6 TestCase 3    ERROR


