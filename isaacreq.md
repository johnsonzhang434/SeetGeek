
| Target              | ID     | Purpose                                                                                                                                  |
|---------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------|
| R1 /login [POST]    |        |                                                                                                                                          |
|                     | R1.P.1 | The login form can be submitted as a POST request to the current URL (/login)                                                            |
|                     | R1.P.2 | Email and password both cannot be empty                                                                                                  |
|                     | R1.P.3 | Email has to follow addr-spec difined in RFC 5322                                                                                        |
|                     | R1.P.4 | Password has to meet the required complexity: min lenght 6, at least 1 upper case, at least 1 lower case, at least 1 special char        |
|                     | R1.P.5 | For any formatting erros, render the login page and show the message 'email/password format is incorrect'                                |
|                     | R1.P.6 | If the email/password are correct, redirect to /                                                                                         |
|                     | R1.P.7 | Otherwise, redirect to /login and show message 'email/password combination incorrect'                                                    |
| R2 /register [POST] |        |                                                                                                                                          |
|                     | R2.P.1 | The registration form can be submitted as a POST request to the current URL (/register)                                                  |
|                     | R2.P.2 | Email, password, password2 all have to satisfy the same required as defined in R1                                                        |
|                     | R2.P.3 | Password and password2 have to be exactly the same                                                                                       |
|                     | R2.P.4 | User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.                   |
|                     | R2.P.5 | User name has to be longer than 2 characters and less than 20 characters.                                                                |
|                     | R2.P.6 | For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)        |
|                     | R2.P.7 | If the email already exists, show message 'this email has been ALREADY used'                                                             |
|                     | R2.P.8 | If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page   |
| R7 /logout [POST]   | R7.P.1 | Logout will invalid the current session redirect to the login page. After logout, the user shouldn't be able to access restricted pages. |


