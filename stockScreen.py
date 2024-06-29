import datetime
import PySimpleGUI as sg
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
import menuScreen

def getInfo():
    # Define the layout of the window
    layout = [
        [sg.Text('Enter Stock Ticker Symbol:')],
        [sg.Input(key='-INPUT-', size=(100, 50))],
        [sg.Button('Submit'), sg.Button('Back')],
        [sg.Text('Company Info:')],
        [sg.Output(size=(500, 500), key='-OUTPUT-')]
    ]

    # Create the window
    window = sg.Window('Personal Finance Manager', layout, size=(500, 500))

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

    # Close the window
    window.close()

