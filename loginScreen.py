import PySimpleGUI as sg
import menuScreen

# Define the layout of the sign-up screen
def login():
    layout = [
        [sg.Text("Sign Up", font=("Helvetica", 20), justification="center")],
        [sg.Text("Username"), sg.Input(key="-USERNAME-")],
        [sg.Text("Password"), sg.Input(key="-PASSWORD-", password_char="*")],
        [sg.Button("Sign Up"), sg.Button("Cancel")]
    ]
    # Create the window
    window = sg.Window("Personal Finance Manager", layout, size=(400, 200))

    # Event loop to process events and user interactions
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break  # Exit the loop if the window is closed or "Cancel" button is clicked

        username = values["-USERNAME-"]
        password = values["-PASSWORD-"]

        # Perform sign-up processing
        # Here, you can save the user's details to a database or perform any necessary actions

        # Display a success message
        sg.popup("Sign Up Successful!")

        window.close()

    layout = [
        [sg.Text("Login", font=("Helvetica", 20), justification="center")],
        [sg.Text("Username"), sg.Input(key="-USERNAME-")],
        [sg.Text("Password"), sg.Input(key="-PASSWORD-", password_char="*")],
        [sg.Button("Login"), sg.Button("Cancel")]
    ]

    # Create the window
    window = sg.Window("Personal Finance Manager", layout, size=(400, 200))

    # Event loop to process events and user interactions
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break  # Exit the loop if the window is closed or "Cancel" button is clicked

        userUsername = values["-USERNAME-"]
        userPassword = values["-PASSWORD-"]

        # Perform login validation
        if userUsername == username and userPassword == password:
            # window.close();
            sg.popup("Login Successful!")
            menuScreen.menu()
        else:
            sg.popup("Invalid username or password. Please try again.")

        # Close the window
    window.close()

