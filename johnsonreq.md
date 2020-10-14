Test Data:
```python
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

```python
test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    date='20200901'
)
```

## Test Case R3.1 - If the user is not logged in, redirect to login page

Mocking:

- Mock backend.get_user to return a test_user instance

Actions: 
- open /logout (to invalid any logged-in sessions may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- verify if user has not logged in, open /login
- validate that no error has occured

## Test Case R3.2 - This page shows a header 'Hi {}'.format(user.name)

Mocking:

- Mock backend.get_user to return a test_user instance

Actions:

- open /logout (to invalid any logged-in sessions may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- validate that there is no error and that we are redirected to /
- validate that the current page shows a header  `'Hi {}'.format(user.name)` element

## Test Case R3.3 - This page shows user balance.

Mocking:

- Mock backend.get_user to return a test_user instance

Actions:

- open /logout (to invalid any logged-in sessions may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- validate that there is no error and that we are redirected to /
- validate that the current page shows a `user balance`

## Test Case R3.4 - This page shows a logout link, pointing to /logout
Mocking:

- Mock backend.get_user to return a test_user instance

Actions:

- open /logout (to invalid any logged-in sessions may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- validate that there is no error and that we are redirected to /
- validate that the current page shows a `logout` link
- validate that when the `logout` link is clicked, you are redirected to /logout

## Test Case R3.5 - This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return ticket instance

Actions:

- open /logout (to invalid any logged-in sessions may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- validate that there is no error and that we are redirected to /
- validate that all available `tickets` are not `expired`
- validate that valid tickets have a `#quantity`,  `#owner's email`, and `#price element`.
- validate that no `expired`  tickets are on the current page

## Test Case R3.6 -  This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date

Mocking:

- Mock backend.get_user to return a test_user instance

Actions:

- open /logout (to invalid any logged-in sessions may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- validate that there is no error and that we are redirected to /
- validate that the current page shows a `ticket-sell form`

## Test Case R3.7 - This page contains a form that a user can buy new tickets. Fields: name, quantity

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return ticket instance

Actions:

- open /logout (to invalid any logged-in sessions may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- validate that there is no error and that we are redirected to /
- validate that the current page shows a `ticket-buy form`

## Test Case R3.8 - The ticket-selling form can be posted to /sell 

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return ticket instance

Actions:

- open /logout (to invalid any logged-in sessions may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- validate that there is no error and that we are redirected to /
- validate that the current page shows a `ticket-selling form`
- validate that when the `ticket-selling form` is clicked, you are redirected onto the `/sell` Route
- open /sell
- enter test_ticket's name into element `#ticket_name`
- enter test_ticket's quantity into element `#ticket_quantity`
- enter test_ticket's price into element `#ticket_price`
- enter test_ticket's expiration date into element `#ticket_date`
- click element `input[type="submit"]`
- open /
- validate that the `ticket` has been uploaded for sale on user profile page

## Test Case R3.9 - The ticket-buying form can be posted to /buy

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return ticket instance

Actions:

- open /logout (to invalid any logged-in sessions may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- validate that there is no error and that we are redirected to /
- validate that the current page shows a `ticket-buying form`
- validate that when the `ticket-buying form` is clicked, you are redirected onto the `/buy` Route
- open /buy
- enter test_ticket's name into element `#ticket_name`
- enter test_ticket's quantity into element `#ticket_quantity`
- click element `input[type="submit"]`
- open /
- validate that the `ticket` has been bought on user profile page

## Test Case R3.10 - The ticket-update form can be posted to /update

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return ticket instance

Actions:

- open /logout (to invalid any logged-in sessions may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- validate that there is no error and that we are redirected to /
- validate that the current page shows a `ticket-buying form`
- validate that when the `ticket-update form` is clicked, you are redirected onto the `/update` Route
- open /update
- enter test_ticket's name into element `#ticket_name`
- enter test_ticket's quantity into element `#ticket_quantity`
- enter test_ticket's price into element `#ticket_price`
- enter test_ticket's expiration date into element `#ticket_exprdate`
- click element `input[type="submit"]`
- open /
- validate that the `ticket` has been updated on user profile page

## Test Case R8.1.1 - For any other requests except the ones above, the system should return a 404 error 

Actions:
- open /*
- validate that you are redirected to `404 error page`.

## Test Case R8.1.2 - For any other requests except the ones above, the system should return a 404 error 
Mocking:

- Mock backend.get_user to return a test_user instance

Actions:

- open /logout (to invalid any logged-in sessions may exist)
- open /register
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- validate that there is no error and that we are redirected to /
- open /buy
- open /sell
- open /update
- open /logout


# Summary
|Specification | Test case ID  | Purpose  |
|-|-|-|
|If the user is not logged in, redirect to login page  |R3.1| Check to see if login action failed |
|This page shows a header 'Hi {}'.format(user.name) |R3.2| Check to see if username formatting has not failed |
|This page shows user balance.  |R3.3| Check if user balance is displayed on current page  |
|This page shows a logout link, pointing to /logout  |R3.4| Check if the logout action works correctly |
|This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.  |R3.5| Check if tickets are valid/available |
| This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date  |R3.6| Check if the submit-form is present |
|This page contains a form that a user can buy new tickets. Fields: name, quantity  |R3.7| Check if a buy-form is present |
|The ticket-selling form can be posted to /sell  |R3.8| Check if the tickets can be displayed as being sold|
|The ticket-buying form can be posted to /buy  |R3.9| Check if tickets can be displayed as being bought|
|The ticket-update form can be posted to /update  |R3.10| Check if tickets can be displayed as updated |
| | |
|For any other requests except the ones above, the system should return a 404 error  |R8.1.1| Check if an invalid request returns 404 error |
|For any other requests except the ones above, the system should return a 404 error |R8.1.2| Check if valid requests won't return 404 error|

- How did your team organize the documentations of the test cases (e.g. where did you store the test case markdown file for each team member).
  
  Currently we have created our own branches and have assigned different test cases for each member. We then individually created our individual md files for our requirements and stored it in our individual branch.
  We will later combine the our md tables into one probably.

- Your understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub.
  
  Use pytest to run tests because pytest is a testing framework and use selenium actions in those tests as 
  selenium is a browser automation framework. Then use github's CI to verify that each commit we do passes all of our test cases.
  
- How are you going to organize different test case code files? (a folder for a specification?)
  
  Use different folders for different specifications then organize test case code files according to specifcations.
