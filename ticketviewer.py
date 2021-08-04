import requests
# Global variables 
URL2="https://zccfranko.zendesk.com/api/v2/tickets.json?page[size]=100"#change the subdomain of URL2 to that of your account
PER_PAGE=25
URL = "https://zccfranko.zendesk.com/api/v2/tickets.json?page[size]=25"#change the subdomain of URL to that of your account
AUTH = ("david.okoro@rocketmail.com", "zccaccount") #fill in your email and password

# Do HTTP requests
response = requests.get(url=URL, auth=AUTH)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print("Status:", response.status_code, "Problem with the request. Exit.")
    
# Decode the JSON response into a dictionary and use the data
data = response.json()
LAST_PAGE_INVALID=data["links"]["prev"]
# Lists menu options for the user and prompts user to make a choice. 
def menu():
    print("*"*13,"MENU","*"*12)
    print("Enter 1 to view all the tickets")
    print("Enter 2 to view a single ticket")
    print("Enter q to quit")
    print("*"*31)


    user_input=input().lower()
    while True:
        if user_input == "1":
            print("")
            get_tickets()
        elif user_input == "2":
            get_ticket()
        elif user_input == "q":
            print("\nThanks for using ticket viewer.\n")
            exit()
        else:
            print("Wrong Choice, Please pick and enter one of the options from the menu.\n")
            print("*"*13,"MENU","*"*12)
            print("Enter 1 to view all the tickets")
            print("Enter 2 to view a single ticket")
            print("Enter q to quit")
            print("*"*31)
            user_input=input().lower()

# Welcomes the user, prints out the menu and prompts user for a response.
def welcome():
    print("WELCOME TO THE TICKET VIEWER")
    option=input("Type menu to view options or q to quit viewer: ").lower()
    print("")
    while True:
        if option == "menu":
            menu()

        elif option == "q":
            print("Thanks for launching ticket viewer")
            print("Have a nice day.")
            exit()

        else:
            option=input("Type menu to view options: ").lower()

# Builds list of tickets of no more than 25 tickets
def all_tickets(data,total):
    start=total*PER_PAGE -24
    for entry in data["tickets"]:
        print("|",end="")
        print(str(start),end = "  ")
        print("'"+"Ticket with subject:",entry["subject"] +"' submitted by", end = " '")
        print(str(entry["submitter_id"]) + "' on", end = " '")
        print(entry["created_at"], end = "'\n")
        print("*")
        start+=1
    return  
        

# Prints list of tickets
def get_tickets():
    url = URL
    # Keeps track of the page
    params={"page":1}
    while True:
        #Do the HTTP request
        response=requests.get(url,auth=AUTH)
        if response.status_code != 200:
            print("Status:", response.status_code, "Problem with the request. Exiting.")
            break
        # Decode the JSON response into a dictionary and use the data
        data=response.json()
        
        all_tickets(data,params["page"])
        
        print("\n------------------------------------------------------------------------------\nSelect view options:")
        print("\t'next'   | Go to next page")
        print("\t'prev'   | Go to previous page")
        print("\t'select' | Select a specific ticket")
        print("\t'menu'   | Return to the menu")
        print("\t'q'      | To quit the viewer.")
        print("------------------------------------------------------------------------------")
        selection = input("\nWhat do you want to do? ").lower()

        if selection == "next":
            # Check if there is a next page
            if data["meta"]["has_more"]:
                # Move to the next page 
                url=data["links"]["next"]

                # Increment page to keep track of page, and update page when moving to the next page
                params["page"]+=1
            else:
                print("Sorry that's the last page")
                print("here's that page again incase you need it")
                print("\n")

        elif selection == "q":
            print("\nThanks for using ticket viewer.\n")
            exit()
         
        elif selection == "prev":
            # Check if there is a previous page
            if data["links"]["prev"] == LAST_PAGE_INVALID:
                # Go back to the previous page
                print("There is no previous")
                print("here's that page again incase you need it")
                print("")
                url=URL
                # decrement params[page] to keep track of page, and update page when accessing previous pages.
                params["page"]=1
            else:
                url=data["links"]["prev"]

                params["page"]-=1
        
        elif selection == "menu":
            break

        elif selection == "select":
            get_ticket()  
            break
            
        else:
            print("That wasn't one of my options, try again :)")
            print("Here's that page again in case you need it\n")
    menu()          
    


#Retrieve user's selected ticket and displays it. 
def get_ticket():
    raw=requests.get(url=URL2,auth=AUTH)
    data=raw.json()
    user_input=input("Enter the ticket number: ")
    page=data["tickets"]

    try:
        ret=page[int(user_input)%100 - 1]
    except IndexError:
        print("Sorry, there's no ticket with that number\n")
        menu()
    # Checks if user's selected ticket number is above the number of tickets
    if int(user_input) > len(page):
        print("Sorry, there's no ticket with that number\n")
        menu()
        
    # Prints user's selected ticket 
    else:
        print("\nSUBJECT: "+ret["subject"])
        print("ID: ",ret["id"])
        print("CREATED: "+ret["created_at"],"\n\n\n\n")
        print("DESCRIPTION: "+ret["description"],'\n')
        
    menu()

def main():
    welcome()
    
if __name__ == "__main__":
    main()