//R5 && R6

R5 - /Update
    R5.1 - Name of ticket must be alpha numeric, cannot have leading/trailing spaces
	test data: 
		t_name_spaces = '   leading and trailing spaces    '
		t_name_invalid = 'ticket1 @#$'
		t_name_invalid = ',.,.,.,.,.,.$#%#!#%#'
		t_name_valid1 = 'ticket1'
		t_name_valid2 = 'ticket 1'

	mocking:
		Mock backend.get_user to get a test user instance

	actions:
		- open /logout
		- open /login
		- enter test user email into #email, password into #password
		- click element input[type="submit"]
		- open /update
		- enter test data into #ticketname
		- click element input[type="submit"]
		- for each test data, validate that the user is redirected back to / and the following messages are shown:
			1. "ticket name cannot begin/end with a space, cannot update ticket name."
			2/3. "ticket name must be alphanumeric only, cannot update ticket name."
			4. "ticket name updated to: ticket1."
			5. "ticket name updated to: ticket 1."

    R5.2 - max 60 characters in name
	test data:
		t_name_78 = 'abcdegfhijklmnopqrstuvwxyzabcdegfhijklmnopqrstuvwxyzabcdegfhijklmnopqrstuvwxyz'
		t_name_empty = ''
		t_name_61spaces = '                                                             '
		t_name_60 = 'abcdefghijklmnopqrstuvwxyz aaaaaaaaaaaaabbbbbbbbbbcccccccccc'

	mocking: 
		Mock backend.get_user to get a test user instance

	actions:
		- open /logout
		- open /login
		- enter test user email into #email, password into #password
		- click element input[type="submit"]
		- open /update 
		- enter test data into #ticketname
		- click element input[type="submit"]
		- for each test data, validate that the user is redirected back to / with the following messages:
			1. "ticket name exceeds character limit (60), cannot update ticket name."
			2. "ticket name must contain at least (1) character, cannot update ticket name."
			3. "ticket name cannot begin/end with a space, cannot update ticket name."
			4. "ticket name updated to: -----" (t_name_60 in blank)


    R5.3 - ticket quantity must be 0 < n <= 100
	test data:
		quantity1 = 0
		quantity2 = -4
		quantity3 = 101
		quantity4 = 1
		quantity5 = 100

	mocking: 
		Mock backend.get_user to get a test user instance

	actions:
		- open /logout
		- open /login
		- enter test user email into #email, password into #password
		- click element input[type="submit"]
		- open /update
		- enter test data into #quantity
		- click element input[type="submit"]
		- for each test data validate that the user is redirected back to / with the following messages:
			1. "ticket quantity must be greater than zero."
			2. "ticket quantity must be greater than zero."
			3. "maximum ticket quantity is 100."
			4. "ticket quantity updated to 1."
			5. "ticket quantity updated to 100."

    R5.4 - ticket price must be in the range [10, 100] (inclusive)
	test data:
		price1 = 0.00
		price2 = 9.99
		price3 = -10.00
		price4 = 100.10
		price5 = 10.00
		price6 = 100.00

	mocking: 
		Mock backend.get_user to get a test user instance

	actions:
		- open /logout
		- open /login
		- enter test user email into #email, password into #password
		- click element input[type="submit"]
		- open /update
		- enter test data into #price
		- click element input[type="submit"]
		- for each test data validate that the user is redirected back to / with the following messages:
			1. "minimum price must be at least 10.00"
			2. "minimum price must be at least 10.00"
			3. "minimum price must be at least 10.00"
			4. "maximum price of a ticket is 100.00"
		- for the last two test data, validate that the message box displays these:
			5. "price updated to $10.00."
			6. "price updated to $100.00."

    R5.5 - Date of ticket must be in YYYYMMDD format
	test data:
		date1 = 03312020
		date2 = 20203104
		date3 = 20201031
	
	mocking: 
		Mock backend.get_user to get a test user instance
	
	actions:
		- open /logout
		- open /login
		- enter test user email into #email, password into #password
		- click element input[type="submit"]
		- open /update
		- enter test data into #date
		- click element input[type="submit"]
		- for each test data validate that the user is redirected back to / with the following messages:
			1. "invalid date format"
			2. "invalid date format"
			3. "date updated to: 20201031"

    R5.6 - ticket must exist in database
	test data:
		temp_ticket = ticket (
			name = "ticket1"
			...
		)

		invalid_name = "ticket2"
		valid_name = "ticket1"	
	mocking:
		Mock backend.get_user to get a test user instance
		mock backend.get_ticket to return temp_ticket instance
	
	actions:
		- open /logout
		- open /login
		- enter test user email into #email, password into #password
		- click element input[type="submit"]
		open /update
		enter invalid_name/valid_name into #ticket_name field
		click element input[type="submit"]
		validate that for invalid_name the user is redirected back to / with the message:
			1. "Ticket2 could not be found, ticket not updated"
		validate that for valid_name the user is given the message:
			2. "ticket found, information updated"


    R6.1 - Name of ticket must be alpha numeric, cannot have leading/trailing spaces
        test data:
                t_name_spaces = '   leading and trailing spaces    '
                t_name_invalid = 'ticket1 @#$'
                t_name_invalid = ',.,.,.,.,.,.$#%#!#%#'
                t_name_valid1 = 'ticket1'
                t_name_valid2 = 'ticket 1'

        mocking: 
		Mock backend.get_user to get a test user instance

        actions:
		- open /logout
		- open /login
		- enter test user email into #email, password into #password
		- click element input[type="submit"]
                - open /buy
                - enter test data into #ticketname
                - click element input[type="submit"]
                - for each test data, validate that the user is redirected back to / and the following messages are shown:
                        1. "invalid ticket name, cannot purchase ticket."
                        2/3. "invalid ticket name, cannot purchase ticket."
                        4. "ticket purchased" (assuming all other conditions are met)
                        5. "ticket purchased" (assuming all other conditions are met)

    R6.2 - max 60 characters in name
        test data:
                t_name_78 = 'abcdegfhijklmnopqrstuvwxyzabcdegfhijklmnopqrstuvwxyzabcdegfhijklmnopqrstuvwxyz'
                t_name_empty = ''
                t_name_61spaces = '                                                             '
                t_name_60 = 'abcdefghijklmnopqrstuvwxyz aaaaaaaaaaaaabbbbbbbbbbcccccccccc'

        mocking: 
		Mock backend.get_user to get a test user instance

        actions:
		- open /logout
		- open /login
		- enter test user email into #email, password into #password
		- click element input[type="submit"]
                - open /buy
                - enter test data into #ticketname
                - click element input[type="submit"]
                - for each test data, validate that the user is redirected back to / with the following messages:
                        1. "ticket name exceeds character limit (60), cannot purchase ticket."
                        2. "ticket name must contain at least (1) character, cannot purchase ticket."
                        3. "ticket name cannot begin/end with a space, cannot purchase ticket."
                        4. "ticket purchased" (assuming all other conditions are met)

    R6.3 - ticket quantity must be 0 < n <= 100
        test data:
                quantity1 = 0
                quantity2 = -4
                quantity3 = 101
                quantity4 = 1
                quantity5 = 100

        mocking: 
		Mock backend.get_user to get a test user instance

        actions:
		- open /logout
		- open /login
		- enter test user email into #email, password into #password
		- click element input[type="submit"]
                - open /buy
                - enter test data into #quantity
                - click element input[type="submit"]
                - for each test data validate that the user is redirected back to / with the following messages:
                        1. "ticket quantity must be greater than zero."
                        2. "ticket quantity must be greater than zero."
                        3. "maximum ticket quantity is 100."
                        4. "purchased 1 ticket."
                        5. "purchased 100 tickets."

    R6.4 - ticket name must exist in database and that ticket quantity is more than buy quantity
	test data:
		test_ticket = ticket(
			owner = temp@temp.ca
			name = 'test_ticket_1'
			qty = 10
			...
		)

		bad_name = 'test_ticket_2'
		bad_qty = 11
		good_name = 'test_ticket_1'
		good_qty = 4
		

	mocking:
		Mock backend.get_user to get a test user instance
		Mock backend.get_ticket to get a test ticket instance

	actions:
		- open /logout
		- open /login
		- enter test user email into #email, password into #password
		- click element input[type="submit"]
                - open /buy
		- enter bad_name/good_name test data into #buy_name and bad_qty/good_qty into #buy_quantity
		- validate that bad_name/bad_qty redirects user to / and display the following error messages:
			1. "ticket does not exist."/"invalid purchase quantity."
		- validate that good_name/good_qty displays the following messages:
			1. "ticket purchased"

    R6.5 - user has more balance than ticket price * quantity + service fee + tax
	test_data:
		test_ticket = ticket(
			...
			name = 'test_ticket_1'
			qty = 10
			price = 10
			...
		)

		test_user = user(
			...
			balance = 100
		)

		good_qty = 1
		bad_qty = 10
			
	mocking:
		Mock backend.get_user to get a test user instance
		Mock backend.get_ticket to get a test ticket instance

	actions:
		- open /logout
		- open /login
		- enter test user email into #email, password into #password
		- click element input[type="submit"]
                - open /buy
		- enter good_qty into #buy_quantity
		- validate that the user is redirected to / with the message:
			1. "Successfully purchased 1 ticket"
			(and deduct the ticket price*qty + tax + service fee from user balance)
		- validate that the user is redirected to / with the message:
			2. "Insufficient balance."	
