#### Test case R1.1 - If the user hasn't logged in, show the login page

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - validate that the current page has `#h1` element with text `Log In`


#### Test case R1.2 - the login page has a message that by default says 'please login'

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - validate that current page contains `#message` element
 - validate that `#message` element contains text `please login`


#### Test case R1.3 - If the user has logged in, redirect to the user profile page

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /login again
 - validate that current page contains `#welcome-header` element


#### Test case R1.4 - The login page provides a login form which requests two fields: email and passwords

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - validate that current page contains `#form` element
 - validate that `#form` element contains `input[name="email"]` and `input[name="password"]` elements


#### Test case R2.1 - If the user has logged in, redirect back to the user profile page /

Mocking:
 - Mock backend.get_user to return a test_user instance

 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /register
 - validate that current page contains `#welcome-header` element


#### Test case R2.2 - otherwise, show the user registration page

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /register
 - validate that the current page contains `input[class="btn btn-primary"][value="register"]` element


#### Test case R2.3 - the registration page shows a registration form requesting: email, user name, password, password2

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /register
 - validate that current page contains `input[name="email"]`
 - validate that current page contains `input[name="name"]`
 - validate that current page contains `input[name="password"]`
 - validate that current page contains `input[name="password2"]`


#### Test case R4.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_all_tickets to return a test_tickets instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - navigate to /sell
 - enter valid test ticket data into each field
 - validate that the ticket name attribute value only contains letters and numbers
 - validate that the ticket name attribute value does not begin or end with a space

#### Test case R4.2 - The name of the ticket is no longer than 60 characters

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_all_tickets to return a test_tickets instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - navigate to /sell
 - enter valid test ticket data into each field
 - validate that the ticket name attribute value is less than 61 characters


#### Test case R4.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100.

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_all_tickets to return a test_tickets instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - navigate to /sell
 - enter valid test ticket data into each field
 - validate that the ticket quantity attribute value is greater than 0 and less than 101


#### Test case R4.4 - Price has to be of range [10, 100]

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_all_tickets to return a test_tickets instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - navigate to /sell
 - enter valid test ticket data into each field
 - validate that the ticket price attribute value is between 10 and 100


#### Test case R4.5 - Date must be given in the format YYYYMMDD (e.g. 20200901)

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_all_tickets to return a test_tickets instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - navigate to /sell
 - enter valid test ticket data into each field
 - validate that the ticket date attribute value is given in the correct format (8 numerical digits)


#### Test case R4.6 - For any errors, redirect back to / and show an error message

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_all_tickets to return a test_tickets instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - navigate to /sell
 - enter invalid test ticket data
 - click `input[type="submit"][name="sell"]`
 - validate that current page contains `#welcome-header` element
 - validate that current page contains `#error-message` element


#### Test case R4.7 - The added new ticket information will be posted on the user profile page

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_all_tickets to return a test_tickets instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - navigate to /sell
 - enter valid test ticket data
 - click `input[type="submit"][name="sell"]`
 - validate that current page contains `#welcome-header` element
 - validate that ticket name, quantity, price, and date attribute values all match the test ticket data


| Specification                                                                                     | Test Case ID | Purpose                                                                                                          |
|---------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------|
| If the user hasn't logged in, show the login page                                                 | R1.1         | Check that the login page is being displayed                                                                     |
| The login page has a message that by default says 'please login'                                  | R1.2         | Check that the message is displayed on the login page                                                            |
| If the user has logged in, redirect to the user profile page                                      | R1.3         | Check that the profile page is being displayed                                                                   |
| The login page provides a login form which requests two fields: email and passwords               | R1.4         | Check that these two fields are present on the login page                                                        |
| If the user has logged in, redirect back to the user profile page /                               | R2.1         | Check that the profile page is being displayed                                                                   |
| otherwise, show the user registration page                                                        | R2.2         | Check that the registration page is being displayed                                                              |
| The registration page shows a registration form requesting: email, user name, password, password2 | R2.3         | Check that registration page looks for input from all four of these fields                                       |
| The name of the ticket has to be alphanumeric-only                                                | R4.1.1       | Check if the selling actions succeed when the ticket names is alphanumeric-only                                  |
| The name of the ticket has to be alphanumeric-only                                                | R4.1.2       | Check if the selling actions fail when the ticket names contains special characters                              |
| The name of the ticket can only have a space if it is the first or last character                 | R4.1.3       | Check if the selling actions succeed when the ticket name uses a space somewhere other than the beginning or end |
| The name of the ticket can only have a space if it is the first or last character                 | R4.1.4       | Check if the selling actions fail when the ticket name uses a space at the beginning or end                      |
| The name of the ticket is no longer than 60 characters                                            | R4.2.1       | Check if the selling actions succeed when the ticket name is 60 characters or less                               |
| The name of the ticket is no longer than 60 characters                                            | R4.2.2       | Check if the selling actions fail when the ticket name is greater than 60 characters                             |
| The quantity of the tickets has to be more than 0, and less than or equal to 100.                 | R4.3.1       | Check if the selling actions succeed when the ticket quantity is greater than 0 and less than 101                |
| The quantity of the tickets has to be more than 0, and less than or equal to 100.                 | R4.3.2       | Check if the selling actions fail when the ticket quantity is 0 or less                                          |
| The quantity of the tickets has to be more than 0, and less than or equal to 100.                 | R4.3.3       | Check if the selling actions fail when the ticket quantity is greater than 100                                   |
| Price has to be of range [10, 100]                                                                | R4.4.1       | Check if the selling actions succeed when the ticket price is between 10 and 100                                 |
| Price has to be of range [10, 100]                                                                | R4.4.2       | Check if the selling actions fail when the ticket price is less than 10                                          |
| Price has to be of range [10, 100]                                                                | R4.4.3       | Check if the selling actions fail when the ticket price is greater than 100                                      |
| Date must be given in the format YYYYMMDD (e.g. 20200901)                                         | R4.5.1       | Check if the selling actions succeed when the ticket date is in the correct format                               |
| Date must be given in the format YYYYMMDD (e.g. 20200901)                                         | R4.5.2       | Check if the selling actions fail when the ticket date is not in the correct format                              |
| For any errors, redirect back to / and show an error message                                      | R4.6         | Check that the current page is / and that an error message has been displayed                                    |
| The added new ticket information will be posted on the user profile page                          | R4.7         | Check that the ticket information is visible on the profile page                                                 |


Each member of our team cloned the assignment repo and made our own local markdown file.
Once completed, we reviewed one another's markdown files through pull-requests,
then merged all completed markdown files to the master.

Each of us also cloned the CI-Python repo to practice running the server on our own devices.
This helped me practice some git commands and gave me a better understanding of how web
servers work.
Each time we merge a branch, github checks to make sure all tests are passed. This idea of
continuous integration ensure the code works at each step along the way.

Our group will create a specifications folder to hold all of our test code.
