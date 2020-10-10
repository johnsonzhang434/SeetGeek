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
- validate that no error has occured

## Test Case R1.P.2 - Email and password both cannot be empty

Note: these checks should be done clientside first, to prevent the client from sending pointless requests that will obviously return an error. The server should just return a generic "incorrect username and password" when a invalid request is manually submitted. 


Actions:

- open /login
- click element `input[type="submit"]`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"
- open /login
- enter `test_user`'s email into the element `#email`
- click element `input[type="submit"]`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"
- open /login
- enter `test_user`'s password into the element `#password`
- click element `input[type="submit"]`
- validate that there is an `#error` element that contains the message "email/password format is incorrect"
- open /login
- enter `test_user`'s email into the element `#email`
- enter `test_user`'s password into the element `#password`
- click element `input[type="submit"]`
- validate that there is no error and you are redirected to /

## Test Case R1.P.3 - Email has to follow addr-spec defined in RFC 5322

Note: This test should also be done clientside, and honestly it doesn't really even need to exist, (at least for /login) just say the email and/or password is incorrect) 

Actions:

- For the following emails: `["Test.test.com", "test@test@test.com", "test\"(test,:;<>[\\]@test.com", "test\"test test@test.com", "12345678901234567890123456789012345678901234567890123456789012341234567890123456789012345678901234567890123456789012345678901234@test.com", "test..test@test.com", "test.test@test..com"]` 
- open /login 
- Enter email in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

- For the following emails: `["test@test.com", "tst123@testmail.org"]` 
- open /login 
- Enter email in element `#email`
- enter a valid password in `#password` (ex. `Password1!`)
- validate that there is no error and that we are redirected to /

## Test Case R1.P.4 - Password has to meet the required complexity: min lenght 6, >1 upper, >1 lower, >1 special.

Note: Why is this in the login api endpoint, we really should not care about what they enter, in fact these should not even be chacked clientside and instead should be allowed to pass through to the server, so that it eats up the client's rate limit tokens. Users should be 1000000% sure that the password they are entering in is not only valid, but  is actually indeed their password. 

Actions:

- For the following passwords: `["a1A!","aaaAAA111", "aaaAAA!!!!", "AAAA1111!!!!", "aaa111!!!!"]`
- open /login
- Enter a valid email in element `#email` (ex. `test@test.com`)
- validate that there is an `#error` element that contains the message "email/password format is incorrect"

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

## Test Case R1.P.7 - Otherwise redirect to /login asnd show the message 'email/password combination incorrect'

Mock:

- Mock `backend.get_user` to return a `test_user` instance 

Actions: 

- open /login
- enter `test_user`'s email into element `#email`
- enter `Password1$` into element `#password`
- click element `input[type="submit"]`
- validate that we have been redirected to /login and there is an element `#error` that says "email/password combination incorrect"
- open /login
- enter `test_user@wrong.com` into element `#email`
- enter `test_user`'s password into element `#password`
- click element `input[type="submit"]`
- validate that we have been redirected to /login and there is an element `#error` that says "email/password combination incorrect"
- open /login
- enter `wrong@wrong.com` into element `#email`
- enter `Wrrrr0ng!` into element `#password`
- click element `input[type="submit"]`
- validate that we have been redirected to /login and there is an element `#error` that says "email/password combination incorrect"
- open /login 
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- click element `input[type="submit"]`
- validate that we have been redirected to / without error


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

See R1.P.*, replace `login` with `register` and repeat `password` but replaced with `password2` as well.

## Test case R2.P.3 - Password and password2 have to be exactly the same

Actions:

- open /register
- enter `test_user`'s name into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `notTheS4m3!` into element `#password2`
- click element `input[type="submit"]`
- validate that there has been an error message `passwords do not match`

- open /register
- enter `test_user`'s name into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there is no error and we have been redirected to /login

## Test case R2.P.4 - Username has to be non-empty, alphanumeric-only, and space allowed if not first or last character
Note: there seems to be a typo in the original specifications, requiring a redirect to /login rather than /register.
Actions:

- For the following usernames: `["$+-=", "", " ", " test", "test "]`
- open /register
- enter the username into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and an error message `name format is incorredct.`

- For the following usernames: `["bob", "test123", "bob ashtast"]`
- open /register
- enter the username into element `#name`
- enter `test_user`'s email into element `#email`
- enter `test_user`'s password into element `#password`
- enter `test_user`'s password into element `#password2`
- click element `input[type="submit"]`
- validate that there has been a redirect to /login and no error 

## Test case R2.P.5 - Username has to be 2>lenght>20
Note: there seems to be a typo in the original specifications, requiring a redirect to /login rather than /register.
Actions:

- For the following usernames: `["uu", "12345678901234567890"]`
- open /register
- enter the username into element `#name`
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

## Test case R2.P.6 - if the email already exists, show the message 'this email has been ALREADY used`

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
## Test case R2.P.7 - if no error create new user, set balance to 5000, go to /login page

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
- verify user balance is 5000.

## Test Case R7.P.1 - Logout will invalidate the current session and redirect to the login page. After logout the user should not be able to access restricted pages

Note: The requirements do not state that you must be logged in to view /buy or /update or /sell, which you probably should be required to be.

Action:

- open /logout
- verify that you are redirected to /login
- verify that you cannot view /. 




# Summary 
| Target              | ID     | Purpose                                                                                                                                  |
|---------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------|
| R1 /login [POST]    |        |                                                                                                                                          |
|                     | R1.P.1 | The login form can be submitted as a POST request to the current URL (/login)                                                            |
|                     | R1.P.2 | Email and password both cannot be empty                                                                                                                                                             |
|                     | R1.P.3 | Email has to follow addr-spec defined in RFC 5322                                                                                                                                                  |
|                     | R1.P.4 | Password has to meet the required complexity: min lenght 6, at least 1 upper case, at least 1 lower case, at least 1 special char                                                                                 |
|                     | R1.P.5 | For any formatting errors, render the login page and show the message 'email/password format is incorrect'                                                                                                          |
|                     | R1.P.6 | If the email/password are correct, redirect to /                                                                                         |
|                     | R1.P.7 | Otherwise, redirect to /login and show message 'email/password combination incorrect'                                                    |
| R2 /register [POST] |        |                                                                                                                                          |
|                     | R2.P.1 | The registration form can be submitted as a POST request to the current URL (/register)                                                 |
|                     | R2.P.2 | Email, password, password2 all have to satisfy the same requirements as defined in R1                                           |
|                     | R2.P.3 | Password and password2 have to be exactly the same                                                                                       |
|                     | R2.P.4 | User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.                   |
|                     | R2.P.5 | User name has to be longer than 2 characters and less than 20 characters.                                                                |
|                     | R2.P.6 | For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)        |
|                     | R2.P.7 | If the email already exists, show message 'this email has been ALREADY used'                                                             |
|                     | R2.P.8 | If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page   |
| R7 /logout [POST]   | R7.P.1 | Logout will invalid the current session redirect to the login page. After logout, the user shouldn't be able to access restricted pages. |

- How did your team organize the documentations of the test cases (e.g. where did you store the test case markdown file for each team member).
We followed the format specified in the assingment document.

As of this commit, we are just making separate branches with our own requirement md files, later when we are all done, we will probably create a docs/requirements folder and add them all into there with proper names, and also create an index file containing all the tables combinined into one.

- Your understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub.

Selenium is a browser automation framework for ui testing. Pytest is a testing framework to actually run the tests. We will use pytest to run the actual tests,which consist of selenium actions. Once there is actual test code, we will use github's CI so that we can verify each commit passes all of our tests. PR's will only be merged if they are passing and reviewed. 

- How are you going to organize different test case code files? (a folder for a specification?)

We will probably use a folder per specification. Moving files around later should't be that big of an issue either. 
