import requests

# Draws main menu
def draw_menu():
    print("\n1. GET")
    print("2. POST")
    print("3. PATCH")
    print("4. DELETE")
    print("5. EXIT")

# Ask for an option input from user in main menu
def take_input_menu():
    choice = int(input("Choose: "))
    return choice

# When user selects a request method (get, post, etc)
# it asks for url to make request on
def ask_url():
    url = input("Enter url: ")
    return url

# HTTP requests functions
def get_req():
    try:
        url = ask_url()
        # make request
        response = requests.get(url)
        # print response details
        print(response.status_code)
        passrint(response.json())
    except Exception as e:
        print(e)

def post_req(url):
    pass

def main():
    run = True
    while run:
        draw_menu()
        choice = take_input_menu()

        if choice == 1:
            get_req()
            continue
        
        elif choice == 2:
            post_req()
            continue
        
        elif choice == 5:
            break
        
        else:
            print("Invalid option")
            continue

main()
    
    








    
