import PySimpleGUI as sg
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
import menuScreen
import databaseConnect
import psycopg2  # Assuming psycopg2 is used for PostgreSQL interaction


def get_user_stocks(username):
    """
    Retrieves the list of stocks saved by the user from the database.

    Args:
    - username (str): The username of the user whose stocks are to be retrieved.

    Returns:
    - list or None: List of stocks (JSONB array) if found, else None.
    """
    conn = databaseConnect.connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute('SELECT stocks FROM "userInfo" WHERE username = %s', (username,))
            result = cur.fetchone()
            cur.close()
            conn.close()

            if result:
                stock_list = result[0]  # Assuming stocks is stored as a JSONB array
                return stock_list
            else:
                return None
        except psycopg2.Error as e:
            print("Error fetching user stocks:", e)
            return None


def addStock(user, stock):
    """
    Adds a stock to the user's profile in the database.

    Args:
    - user (str): The username of the user to whom the stock is added.
    - stock (str): The stock symbol to be added.

    """
    conn = databaseConnect.connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            # Update the stocks array for the specified user
            cur.execute("""
                        UPDATE "userInfo"
                        SET stocks = ARRAY_APPEND(stocks, %s)
                        WHERE username = %s
                        """, (stock, user))
            conn.commit()  # Commit the transaction
            print(f"Stock {stock} added successfully for user {user}")

        except psycopg2.Error as e:
            conn.rollback()  # Rollback changes if there's an error
            print("Error adding user stocks:", e)

        finally:
            cur.close()  # Close cursor
            conn.close()  # Close connection


def getInfo(username):
    """
    Creates and manages the main window of the Personal Finance Manager application.

    Args:
    - username (str): The username of the logged-in user.

    """
    # Define the layout of the window
    layout = [
        [sg.Text('Enter Stock Ticker Symbol:')],
        [sg.Input(key='-INPUT-', size=(100, 50))],
        [sg.Button('Submit'), sg.Button('Back'), sg.Button('Add Stock to Profile'), sg.Button('My Stocks')],
        [sg.Text('Company Info:')],
        [sg.Output(size=(500, 500), key='-OUTPUT-')]
    ]

    # Create the window
    window = sg.Window('Personal Finance Manager', layout, size=(600, 600))

    # Event loop to process events and interact with the window
    while True:
        event, values = window.read()

        # Close the window if the user clicks the 'Exit' button or closes the window
        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Back':
            window.close()
            menuScreen.menu()

        # Process the input when the 'Submit' button is clicked
        if event == 'Submit':
            user_input = str(values['-INPUT-'])
            api_key = '9QS4OVT4F4N2BPT1'

            # Initialize Alpha Vantage API clients
            fd = FundamentalData(key=api_key)
            ts = TimeSeries(key=api_key)

            # Get quote endpoint data (latest price)
            data, meta_data = ts.get_quote_endpoint(user_input)
            latest_price = data['05. price']

            # Get company overview data
            data, meta_data = fd.get_company_overview(user_input)
            company_name = data['Name']
            industry = data['Industry']
            description = data['Description']

            # Format the output
            output = f'\nCompany Name: {company_name}\n\n' + \
                     f'Industry: {industry}\n\n' + \
                     f'Description: {description}\n' + \
                     f'\nCurrent price of {user_input}: ${latest_price}'

            # Print the output to the output box
            print(output)

        # Add functionality for the 'Add Stock to Profile' button
        if event == 'Add Stock to Profile':
            user_input = str(values['-INPUT-'])
            addStock(username, user_input)  # Add stock to user's profile
            sg.popup('Stock added to profile.')  # Notify user

        # Add functionality for the 'My Stocks' button
        if event == 'My Stocks':
            stock_list = get_user_stocks(username)  # Retrieve user's saved stocks
            if stock_list:
                stock_list_text = '\n'.join(stock_list)
                sg.popup_scrolled('Your Stocks:', stock_list_text, size=(75, 20))
            else:
                sg.popup('No stocks found for the user.')

    # Close the window
    window.close()



