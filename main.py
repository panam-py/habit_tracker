import requests
from datetime import datetime

from requests.api import delete, head

PIXELA_ENDPOINT = "https://pixe.la/v1/users/"

print("WELCOME TO THE HABIT TRACKER!")

while True:
    user_choice = input("What would you like to do 1. Create a new user, 2. Create a graph, 3. Create a pixel, 4. Edit a pixel, 5. Delete a pixel (Enter any other key to quit): ")
    if user_choice == "1":
        token = input("Enter a token for the new user: ")
        username = input("Create a username: ")
        agreeTermsOfService = input("Do you agree to the terms of service('yes' or 'no'): ").lower()
        notMinor = input("Are you over 18(yes or no): ").lower()

        user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": agreeTermsOfService,
        "notMinor": notMinor,
        }

        createUser = requests.post(url=PIXELA_ENDPOINT, json=user_params)
        message = createUser.json()["message"]
        if 'Success' in message:
            print("User Successfully Created")
        else:
            print(f"Unsuccessful: {message}")
    elif user_choice == "2":
        username = input("Enter the username: ")
        GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}{username}/graphs"

        id = input("Enter a new id for this graph(id must start with a letter): ")
        name = input("Enter a name for this graph: ")
        unit = input("Enter a unit of measurement for this graph: ")
        type = input("Enter the data type to be used in this graph(Enter 'float' or 'int'): ")
        color = input("What color should be used for this graph(shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black) are supported as color kind.): ")

        graph_params = {
            "id": id,
            "name": name,
            "unit": unit,
            "type": type,
            "color": color,
        }

        token2 = input("Enter the user's token: ")
        header = {
            "X-USER-TOKEN": token2
        }

        createGrid = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=header)
        message = createGrid.json()["message"]
        if 'Success' in message:
            print(f"Grid successfully created, you can view it graphically here: https://pixe.la/v1/users/{username}/graphs/{id}.html")
        else:
            print(f"Unsuccessful: {message}")
    elif user_choice == "3":
        username = input("Enter the username: ")
        graph_id = input("Enter the id of the graph you want to add this pixel to: ")
        PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{graph_id}"
        system_time = input("Do you want to write your own date or a system generated date(Enter 'sys' for system generated date or 'hum' to type in a date): ").lower()
        
        if system_time == 'sys':
            today = datetime.now()
            today = today.strftime("%Y%m%d")
        elif system_time == 'hum':
            today = input("Enter yearmonthday in this format without spaces(Example: 20200130): ")
        quantity = input("What is the quantity done today: ")
        
        pixel_params = {
        "date": today,
        "quantity": quantity,
        }

        token2 = input("Enter the user's token: ")
        header = {
            "X-USER-TOKEN": token2
        }

        createPixel = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=header)
        message = createGrid.json()["message"]
        if 'Success' in message:
            print(f"Pixel Successfully Created, You can view the grid graphically here:  https://pixe.la/v1/users/{username}/graphs/{graph_id}.html")
        else:
            print(f"Unsuccessful: {message}")
    elif user_choice == "4": 
        date = input("Enter the date of the pixel you want to edit in this format without spaces(Example: 20200130): ")
        PIXEL_EDIT_ENDPOINT = f"{PIXEL_ENDPOINT}/{date}"
        quantity = input("Enter the new quantity of thsi pixel: ")
        username = input("Enter the username of the user: ")
        graph_id = input("Enter the id of the graph that contains this pixel: ")
        
        pixel_edit_params = {
        "quantity": "50"
        }

        token2 = input("Enter the user's token: ")
        header = {
            "X-USER-TOKEN": token2
        }
        
        editPixel = requests.put(url=PIXEL_EDIT_ENDPOINT, json=pixel_edit_params, headers=header)
        message = editPixel.json()["message"]
        if 'Success' in message:
            print(f"Pixel Edited Successfully, You can view the grid graphically here:  https://pixe.la/v1/users/{username}/graphs/{graph_id}.html")
        else:
            print(f"Unsuccessful: {message}")
    elif user_choice == "5":
        date = input("Enter the date of the pixel you want to delete in this format without spaces(Example: 20200130): ")
        PIXEL_DELETE_ENDPOINT = f"{PIXEL_ENDPOINT}/{date}"
        username = input("Enter the username of the user: ")
        graph_id = input("Enter the id of the graph that contains this pixel: ")

        token2 = input("Enter the user's token: ")
        header = {
            "X-USER-TOKEN": token2
        }

        deletePixel = requests.delete(url=PIXEL_EDIT_ENDPOINT, headers=header)
        message = deletePixel.json()["message"]
        if 'Success' in message:
            print(f"Pixel Deleted Successfully, You can view the grid graphically here:  https://pixe.la/v1/users/{username}/graphs/{graph_id}.html")
        else:
            print(f"Unsuccessful: {message}")
    else:
        break