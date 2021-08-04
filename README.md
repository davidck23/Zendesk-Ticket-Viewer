INTRODUCTION:

    Welcome to Zendesk CLI ticket viewer, this viewer connects to the zendesk API, requests all the the tickets for your account, displays them in a list and also shows relevant details of single ticket selected by the user.

INSTALLATION:

    There are different applications to run ticket viewer, i'll suggest using visual studio code and if you don't have it you can download it by clicking this link."https://code.visualstudio.com/download".

    To run Zendesk CLI ticket viewer, Ensure you have python installed on your system. After downloading, when you launch the visual studio code, check the top of the page and click on the "Termianl" option, then click on "New Terminal".The terminal will open below the page. Now you can simply check if you have python by typing "python" in the terminal. If you have it installed the version will be printed and the python shell starts by showing ">>>". Else, there will be an error "command not found". To install python click the link "https://www.python.org/downloads/" 

    The requests module is a key module to successfully run ticketviewer.py. To install request: 

    * Go back to the Visual Studio code terminal and do this below:

    * To install requests, run this command in your terminal or command prompt
        $ python -m pip install requests

    * Request are developed on GitHub, you can clone the public repository by also typing this in the cmd or terminal:
        $ git clone git://github.com/psf/requests.git

    * Now you have a copy of the source, you can embed it into your python package. run this command in your terminal
        $ cd requests
        $ python -m pip install requests .

After the installations, it's now time to launch the Ticket Viewer("ticketviewer.py"). Check the top of the visual studio code app and click on "File", then click on "Open File" to open the program "ticketviewer.py". Once it's open in visual studio code, in the source code at the top of the page, change the subdomain of "URL2" and "URL" to that of your account and remove the curly braces(https://{subdomain}.zendesk.com/api/v2/tickets.json). Then, fill in your email and password in the "AUTH" global variable (AUTH = ("email address, password")). 

Click on run at the top of the page and select run without debugging OR hold Ctrl and press F5 .

Usage:
You should see this in the terminal below after you run the program,

WELCOME TO THE TICKET VIEWER
Type menu to view options or q to quit viewer: 

respond with a "menu" to view the menu or "q" to quit the program.

You should see the menu below after inputting "menu"
************* MENU ************
Enter 1 to view all the tickets
Enter 2 to view a single ticket
Enter q to quit
*******************************
To select an option simply type it in and hit enter as instructed. Selecting q will exit the interface with the message "Thanks for using ticket viewer"

In the menu above, Selecting 1 will present the first 25 available tickets with the option to page through any other available tickets and select any specific ticket. Selecting 2 will prompt for a ticket number and allow a more detailed display of the selected ticket's details.