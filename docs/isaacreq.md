# Test Cases 

Test data:
```python
test_user = User(
    email='test_frontend@test.com',
    name='testuser',
    password=generate_password_hash('test_frontendA1$')
)
```

## Test Case R1.P.1 - The login form can be submitted as a POST request to the current URL

Mocking:

- Mock `backend.get_user` to return a `test_user` instance 

Actions: 

- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- click element `input[type="submit"]`
- validate that no error has occured (400s/500s errors, etc)

## Test Case R1.P.2.1 - Email and password both cannot be empty

Note: these checks should be done clientside first, to prevent the client from sending pointless requests that will obviously return an error. The server should just return a generic "incorrect username and password" when a invalid request is manually submitted. 

Actions:

- open /login
- click element `input[type="submit"]`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R1.P.2.2 - Password cannot be empty

Actions: 
- open /login
- enter `test_user`'s email into the element `#email`
- click element `input[type="submit"]`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R1.P.2.3 - Email cannot be empty

Actions: 
- open /login
- enter `test_user`'s password into the element `#password`
- click element `input[type="submit"]`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R1.P.2.4 - Both are not empty 

Actions: 
- open /login
- enter `test_user`'s email into the element `#email`
- enter `test_user`'s password into the element `#password`
- click element `input[type="submit"]`
- validate that there is no error and you are redirected to /

## Test Case R1.P.3.1 - Email has format local@domain.ext

Note: This test should also be done clientside, and honestly it doesn't really even need to exist, (at least for /login) just say the email and/or password is incorrect) 

Actions:

- For the following emails: `["Test.test.com", "test@test@test.com"]`
- open /login 
- Enter email in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R1.P.3.2 - Local part has illegal characters 

Actions:

- For the following emails: `[test\"(test,:;<>[\\]@test.com", "test\"test test@test.com", "tggg,,,@test.com"]` 
- open /login 
- Enter email in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is an `#error` element that contains the message "email/password format is incorrect



## Test Case R1.P.3.3 - Valid Emails work

Actions:

- For the following emails: `["test@test.com", "tst123@testmail.org", "this'isactuallyv{ok@wtf.lol"]` 
- open /login 
- Enter email in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is no error and that we are redirected to /

## Test Case R1.P.3.4 - Email too long

Actions:

- open /login 
- Enter `12345678901234567890123456789012345678901234567890123456789012341234567890123456789012345678901234567890123456789012345678901234@test.com`in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R1.P.3.5 - "." cannot be consecutive or at the start or end.

Actions:

- For the following emails: `["test..test@test.com", "test.test@test..com",".test@test.com", "test.@test.com"]` 
- open /login 
- Enter email in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R1.P.4.1 - Password too short

Note: Why is this in the login api endpoint, we really should not care about what they enter, in fact these should not even be chacked clientside and instead should be allowed to pass through to the server, so that it eats up the client's rate limit tokens. Users should be 1000000% sure that the password they are entering in is not only valid, but  is actually indeed their password. 

Actions:

- open /login
- Enter a valid email in element `#email` (ex. `test@test.com`)
- Enter `a1A!` into element `#password`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R1.P.4.2 - Password missing special 

Note: Why is this in the login api endpoint, we really should not care about what they enter, in fact these should not even be chacked clientside and instead should be allowed to pass through to the server, so that it eats up the client's rate limit tokens. Users should be 1000000% sure that the password they are entering in is not only valid, but  is actually indeed their password. 

Actions:

- open /login
- Enter a valid email in element `#email` (ex. `test@test.com`)
- Enter aaaAAA111 into element `#password`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R1.P.4.3 - Missing number 

Note: Why is this in the login api endpoint, we really should not care about what they enter, in fact these should not even be chacked clientside and instead should be allowed to pass through to the server, so that it eats up the client's rate limit tokens. Users should be 1000000% sure that the password they are entering in is not only valid, but  is actually indeed their password. 

Actions:

- open /login
- Enter a valid email in element `#email` (ex. `test@test.com`)
- Enter `aaaAAA!!!!` into element `#password`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"



## Test Case R1.P.4.4 - Missing lowercase 

Note: Why is this in the login api endpoint, we really should not care about what they enter, in fact these should not even be chacked clientside and instead should be allowed to pass through to the server, so that it eats up the client's rate limit tokens. Users should be 1000000% sure that the password they are entering in is not only valid, but  is actually indeed their password. 

Actions:

- open /login
- Enter a valid email in element `#email` (ex. `test@test.com`)
- Enter AAAA1111!!!! into element `#password`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R1.P.4.5 - missing uppercase 

Note: Why is this in the login api endpoint, we really should not care about what they enter, in fact these should not even be chacked clientside and instead should be allowed to pass through to the server, so that it eats up the client's rate limit tokens. Users should be 1000000% sure that the password they are entering in is not only valid, but  is actually indeed their password. 

Actions:

- open /login
- Enter a valid email in element `#email` (ex. `test@test.com`)
- Enter `aaa111!!!!` into element `#password`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R1.P.4.6 - Valid passwords work

Actions:

- For the following passwords: `["aaaaa1$A, "abct)432A"]`

- open /login

- Enter a valid email in element `#email` (ex. `test@test.com`)

- Validate that there is no error and we are redirected to /

  

## Test Case R1.P.5 - For any formatting errors, render the login page and show the message 'email/password format is incorrect'

Covered by test cases R1.P.2, R1.P.3, R1.P.4.

## Test Case R1.P.6 - If the email/password are correct redirect to /

Mock:

- Mock `backend.get_user` to return a `test_user` instance 

Actions: 

- open /login
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- click element `input[type="submit"]`
- validate that a redirect to / has occured

## Test Case R1.P.7.1 - incorrect password 

Mock:

- Mock `backend.get_user` to return a `test_user` instance 

Actions: 

- open /login
- enter `test_user`'s email into element `#email`
- enter `Password1$` into element `#password`
- click element `input[type="submit"]`
- validate that we have been redirected to /login and there is an element `#error` that says "email/password combination incorrect"

## Test Case R1.P.7.2 - incorrect email

Mock:

- Mock `backend.get_user` to return a `test_user` instance 

Actions: 
- open /login
- enter `test_user@wrong.com` into element `#email`
- enter `test_user`'s password into element `#password`
- click element `input[type="submit"]`
- validate that we have been redirected to /login and there is an element `#error` that says "email/password combination incorrect"

## Test Case R1.P.7.3 - incorrect both email and password

Mock:

- Mock `backend.get_user` to return a `test_user` instance 

Actions: 
- open /login
- enter `wrong@wrong.com` into element `#email`
- enter `Wrrrr0ng!` into element `#password`
- click element `input[type="submit"]`
- validate that we have been redirected to /login and there is an element `#error` that says "email/password combination incorrect"

## Test Case R2.P.1 - The registration form can be submitted as a POST request to the current URL

Actions: 

- open /register
- enter `test_user`'s name into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that no error has occured

## Test Case R2.P.2 - Email, password, password2 all have to satisfy the same requirements as defined in R1

## Test Case R2.P.2.1 - Email and password both cannot be empty

Note: these checks should be done clientside first, to prevent the client from sending pointless requests that will obviously return an error. The server should just return a generic "incorrect username and password" when a invalid request is manually submitted. 

Actions:

- open /register
- click element `input[type="submit"]`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R2.P.2.2 - Password cannot be empty

Actions: 

- open /register
- enter `test_user`'s email into the element `#email`
- click element `input[type="submit"]`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R2.P.2.3 - Email cannot be empty

Actions: 

- open /register
- enter `test_user`'s password into the element `#password`
- click element `input[type="submit"]`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R2.P.2.4 - Both are not empty 

Actions: 

- open /register
- enter `test_user`'s email into the element `#email`
- enter `test_user`'s password into the element `#password`
- click element `input[type="submit"]`
- validate that there is no error and you are redirected to /

## Test Case R2.P.2.5 - Email has format local@domain.ext

Note: This test should also be done clientside, and honestly it doesn't really even need to exist, (at least for /login) just say the email and/or password is incorrect) 

Actions:

- For the following emails: `["Test.test.com", "test@test@test.com"]`
- open /register
- Enter email in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R2.P.2.6 - Local part has illegal characters 

Actions:

- For the following emails: `[test\"(test,:;<>[\\]@test.com", "test\"test test@test.com", "tggg,,,@test.com"]` 
- open /register
- Enter email in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is an `#error` element that contains the message "email/password format is incorrect



## Test Case R2.P.2.7 - Valid Emails work

Actions:

- For the following emails: `["test@test.com", "tst123@testmail.org", "this'isactuallyv{ok@wtf.lol"]` 
- open /register 
- Enter email in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is no error and that we are redirected to /

## Test Case R2.P.2.8 - Email too long

Actions:

- open /register
- Enter `12345678901234567890123456789012345678901234567890123456789012341234567890123456789012345678901234567890123456789012345678901234@test.com`in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R2.P.2.9 - "." cannot be consecutive or at the start or end.

Actions:

- For the following emails: `["test..test@test.com", "test.test@test..com",".test@test.com", "test.@test.com"]` 
- open /register
- Enter email in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R2.P.2.10 - Password too short

Actions:

- open /register
- Enter a valid email in element `#email` (ex. `test@test.com`)
- Enter `a1A!` into element `#password`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R2.P.2.11 - Password missing special  

Actions:

- open /register
- Enter a valid email in element `#email` (ex. `test@test.com`)
- Enter aaaAAA111 into element `#password`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R2.P.2.12 - Missing number 

Actions:

- open /register
- Enter a valid email in element `#email` (ex. `test@test.com`)
- Enter `aaaAAA!!!!` into element `#password`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"



## Test Case R2.P.2.13 - Missing lowercase 

Actions:

- open /register
- Enter a valid email in element `#email` (ex. `test@test.com`)
- Enter AAAA1111!!!! into element `#password`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R2.P.2.14 - missing uppercase 

Actions:

- open /register
- Enter a valid email in element `#email` (ex. `test@test.com`)
- Enter `aaa111!!!!` into element `#password`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

## Test Case R2.P.2.15 - Valid passwords work

Actions:

- For the following passwords: `["aaaaa1$A, "abct)432A"]`

- open /login

- Enter a valid email in element `#email` (ex. `test@test.com`)

- Validate that there is no error and we are redirected to /

  

## Test case R2.P.3.1 - Password and password2 are not the same

Actions:

- open /register
- enter `test_user`'s name into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `notTheS4m3!` into element `#password2`
- click element `input[type="submit"]`
- validate that there has been an error message `passwords do not match`

## Test case R2.P.3.2 - Password and password2 are the same

Actions:

- open /register
- enter `test_user`'s name into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there is no error and we have been redirected to /login

## Test case R2.P.4.1 - Username not alphanumeric
Note: there seems to be a typo in the original specifications, requiring a redirect to /login rather than /register.
Actions:

- open /register
- enter `"$+-="` into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and an error message `name format is incorrect.

## Test case R2.P.4.2 - username empty

Note: there seems to be a typo in the original specifications, requiring a redirect to /login rather than /register.
Actions:

- open /register
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and an error message `name format is incorrect.

## Test case R2.P.4.3 - Username has space at start

Note: there seems to be a typo in the original specifications, requiring a redirect to /login rather than /register.
Actions:

- open /register
- enter ` " test"` into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and an error message `name format is incorrect.

## Test case R2.P.4.4 - Username has space at end

Note: there seems to be a typo in the original specifications, requiring a redirect to /login rather than /register.
Actions:

- open /register
- enter ` "test "` into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and an error message `name format is incorrect.

## Test case R2.P.4.5 - valid usernames work

- For the following usernames: `["bob", "test123", "bob ashtast"]`
- open /register
- enter the username into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and no error 

## Test case R2.P.5.1 - Username too short 
Note: there seems to be a typo in the original specifications, requiring a redirect to /login rather than /register.
Actions:

- open /register
- enter "uu" into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and an error message `name format is incorrect`

## Test case R2.P.5.2 - Username too long

Note: there seems to be a typo in the original specifications, requiring a redirect to /login rather than /register.
Actions:

- open /register
- enter "12345678901234567890" into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and an error message `name format is incorrect`
- For the following usernames: `["uuu", "2345678901234567890"]`
- open /register
- enter the username into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and no error

## Test case R2.P.5.3 - valid names work

Note: there seems to be a typo in the original specifications, requiring a redirect to /login rather than /register.
Actions:

- For the following usernames: `["uuu", "2345678901234567890"]`
- open /register
- enter the username into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and no error

## Test case R2.P.6 - formatting errors, redirect to /login with message '{} format is incorrect'.format(attrib)
covered in R2.P.5, R2.P.4

## Test case R2.P.7 - if the email already exists, show the message 'this email has been ALREADY used`

Mock:

- Mock `backend.get_user` to return a `test_user` instance 

Action:
- open /register
- enter `test_user`'s username into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and an error message `this email has been ALREADY used`

- open /register
- enter `test_user`'s username into element `#name`
- enter `new@email.com` into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and no error 
- 
## Test case R2.P.8 - if no error create new user, set balance to 5000, go to /login page

Action: 

- open /register
- enter `test_user`'s username into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that we have been redirected to /login.
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- click element `input[type="submit"]`
- verify we are directed to / and the balance is 5000 .

## Test Case R7.P.1 - Logout will invalidate the current session and redirect to the login page. After logout the user should not be able to access restricted pages

Note: The requirements do not state that you must be logged in to view /buy or /update or /sell, which you probably should be required to be.

Action:

- open /logout
- verify that you are redirected to /login
- verify that you cannot view /. 




# Summary 
| Specification                                                | ID       | Purpose                                                      |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ |
| The login form can be submitted as a POST request to the current URL (/login) | R1.P.1   | To see if the login form can be submitted as a post request  |
| Email and password both cannot be empty                      | R1.P.2.1 | Email and password both cannot be empty                      |
| Email and password both cannot be empty                      | R1.P.2.2 | Password cannot be empty                                     |
| Email and password both cannot be empty                      | R1.P.2.3 | Email cannot be empty                                        |
| Email and password both cannot be empty                      | R1.P.2.4 | Both are empty                                               |
| Email has to follow addr-spec defined in RFC 5322            | R1.P.3.1 | Email has format local@domain.ext                            |
| Email has to follow addr-spec defined in RFC 5322            | R1.P.3.2 | Local part has illegal characters                            |
| Email has to follow addr-spec defined in RFC 5322            | R1.P.3.3 | Valid Emails work                                            |
| Email has to follow addr-spec defined in RFC 5322            | R1.P.3.4 | Email too long                                               |
| Email has to follow addr-spec defined in RFC 5322            | R1.P.3.5 | "." cannot be consecutive or at the start or end.            |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R1.P.4.1 | password shorter than 6 chars                                |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R1.P.4.2 | missing special character                                    |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R1.P.4.3 | missing number                                               |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R1.P.4.4 | missing lowercase letter                                     |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R1.P.4.5 | missing uppercase letter                                     |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R1.P.4.6 | valid passwords still work                                   |
| For any formatting errors, render the login page and show the message 'email/password format is incorrect' | R1.P.5   | Actually covered by R1.P.2, R1.P.3, R1.P.4.                  |
| If the email/password are correct, redirect to /             | R1.P.6   | If the email/password are correct, redirect to /             |
| Otherwise, redirect to /login and show message 'email/password combination incorrect' | R1.P.7.1 | Test incorrect password.                                     |
| Otherwise, redirect to /login and show message 'email/password combination incorrect' | R1.P.7.2 | Test incorrect email.                                        |
| Otherwise, redirect to /login and show message 'email/password combination incorrect' | R1.P.7.3 | Test incorrect email and password                            |
| The registration form can be submitted as a POST request to the current URL (/register) | R2.P.1   | The registration form can be submitted as a POST request to the current URL (/register) |
| Email, password, password2 all have to satisfy the same requirements as defined in R1 | R2.P.2   |                             |
| Email and password both cannot be empty                      | R2.P.2.1 | Email and password both cannot be empty                      |
| Email and password both cannot be empty                      | R2.P.2.2 | Password cannot be empty                                     |
| Email and password both cannot be empty                      | R2.P.2.3 | Email cannot be empty                                        |
| Email and password both cannot be empty                      | R2.P.2.4 | Both are empty                                               |
| Email has to follow addr-spec defined in RFC 5322            | R2.P.2.5 | Email has format local@domain.ext                            |
| Email has to follow addr-spec defined in RFC 5322            | R2.P.2.6 | Local part has illegal characters                            |
| Email has to follow addr-spec defined in RFC 5322            | R2.P.2.7 | Valid Emails work                                            |
| Email has to follow addr-spec defined in RFC 5322            | R2.P.2.8 | Email too long                                               |
| Email has to follow addr-spec defined in RFC 5322            | R2.P.2.9 | "." cannot be consecutive or at the start or end.            |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R2.P.2.10 | password shorter than 6 chars                                |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R2.P.2.11 | missing special character                                    |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R2.P.2.12 | missing number                                               |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R2.P.2.13 | missing lowercase letter                                     |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R2.P.2.14 | missing uppercase letter                                     |
| Password has to meet the required complexity: min length 6, at least 1 upper case, at least 1 lower case, at least 1 special char | R2.P.2.15 | valid passwords still work                                   |
| Password and password2 have to be exactly the same           | R2.P.3.1 | Password and password2 are different                         |
| Password and password2 have to be exactly the same           | R2.P.3.2 | Password and password2 are the same                          |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. | R2.P.4.1 | Username not alphanumeric                                    |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. | R2.P.4.2 | Username empty                                               |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. | R2.P.4.3 | Usernames starts with space                                  |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. | R2.P.4.4 | Usernames ends with space                                    |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. | R2.P.4.5 | Valid names work                                             |
| User name has to be longer than 2 characters and less than 20 characters. | R2.P.5.1 | name too short                                               |
| User name has to be longer than 2 characters and less than 20 characters. | R2.P.5.2 | name too long                                                |
| User name has to be longer than 2 characters and less than 20 characters. | R2.P.5.3 | valid names work                                             |
| For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute) | R2.P.6   | Covered in previous tests                                    |
| f the email already exists, show message 'this email has been ALREADY used' | R2.P.7   | If the email already exists, show message 'this email has been ALREADY used' |
| If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page | R2.P.8   | Check if no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page |
| Logout will invalid the current session redirect to the login page. After logout, the user shouldn't be able to access restricted pages. | R7.P.1   | Check if the current session redirects to the login page. After logout, the user shouldn't be able to access restricted pages. |

- How did your team organize the documentations of the test cases (e.g. where did you store the test case markdown file for each team member).
We followed the format specified in the assingment document.

As of this commit, we are just making separate branches with our own requirement md files, later when we are all done, we will probably create a docs/requirements folder and add them all into there with proper names, and also create an index file containing all the tables combined into one.

- Your understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub.

Selenium is a browser automation framework for ui testing. Pytest is a testing framework to actually run the tests. We will use pytest to run the actual tests,which consist of selenium actions. Once there is actual test code, we will use github's CI so that we can verify each commit passes all of our tests. PR's will only be merged if they are passing and reviewed. 

- How are you going to organize different test case code files? (a folder for a specification?)

We will probably use a folder per specification. Moving files around later shouldn't be that big of an issue either. 
