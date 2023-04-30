##  Main Logic
##
##
from ticketing import Ticketing, File_utility

_file_utility = None
_Ticketing = None
############################################################################
#  Option 1 Submit ticket
############################################################################
def option_submit_ticket():

    # Set a flag to indicate that polling is active.
    _function_active = True
    while _function_active:
        if not _file_utility.empty_file:
            _Ticketing.ticket_data = _file_utility.read_records()
        # ticket_response = _Ticketing.ticket_data_record
        ticket_response = {}
        _new_ticket_record = {}
        _new_ticket_number =_Ticketing.find_next_ticket_number()
        # Input variables set to None
        istaff_id = None
        istaff_name = None
        istaff_email = None
        iproblem_description = None
        ticket_response['TicketStatus'] = 'submitted'
        ticket_response['TicketResponse']= 'Not yet Provided'
        # Prompt for the person's staff id, name, email id,enter description of the problem for saving
        print (f" New Ticket number :{_new_ticket_number }")
        istaff_id = input("\nEnter your staff ID : ")
        istaff_name = input("Enter your name : ")
        istaff_email = input("Enter email id : ")
        print("If you require a new password type : Password change")
        iproblem_description = input("Enter description of problem : ")
        if (iproblem_description).upper() == 'PASSWORD CHANGE':
            ipassword = ''
            ipassword = new_password(istaff_id, istaff_name)
            print(f"New Password is: { ipassword}")
            ticket_response['TicketStatus'] = 'closed'
            ticket_response['TicketResponse']= 'New Password Generated :' + ipassword

        # Store the input responses in dictionary for record creation.
        ticket_response['TicketNumber'] = _new_ticket_number
        ticket_response['StaffID'] = istaff_id
        ticket_response['TicketOwner'] = istaff_name
        ticket_response['ContactEmail'] = istaff_email
        ticket_response['DescriptionOfIssue'] = iproblem_description

        #print(ticket_response) Enable this for debugging
# Append a new ticket record dictionary to list of records
        _Ticketing.ticket_data.append(ticket_response)
###    Find out if anymore ticket needs to be submitted.
        #  Write records to file
        _file_utility.write_records(_Ticketing.ticket_data)
        _repeat = input("Do you have another ticket to submit? (Y/N) ")
        if _repeat.upper() == 'Y':
           continue
        else:
           _function_active = False
#       Since now there are tickets in ticket data so file is not empty anymore
    if _file_utility.empty_file:
        _file_utility.empty_file= False
    return

def new_password(istaff_id,istaff_name):
    _password =''
    _password = str(istaff_id[0:2]) + str(istaff_name[0:3])
    return _password
############################################################################################
# main method
############################################################################################
if __name__ == "__main__":
    #   Initialize variables
    main_function_active = True
    my_tickets = []
    my_utility = None
    record_count = 0
# Holds Original Ticket_data from file
    _ticket_data = []
# Holds Original Ticket_data from file and updates
    _ticket_data_updated =[]

#   initialize class Ticketing
    _Ticketing = Ticketing()

    csvfile = r'D:\my_test\ticket.csv'
    #   initialize class File_utility
    _file_utility = File_utility(csvfile)

    #  Load data from file using File utility
    if not _file_utility.empty_file:
       _Ticketing.ticket_data = _file_utility.read_records()

    ### handle 0 records #################

    while main_function_active:
        menu_option = 0
        print("\nSelect from the following choices:")
        print("0: Exit")
        print("1: Submit Help desk ticket")
        print("2: Show all tickets")
        print("3: Respond to ticket by number")
        print("4: Re-open resolved ticket")
        print("5: Display ticket stats")
        print("--------------------------------------------------------------------------------------")
        try:
            menu_option = int(input("Enter menu selection 0-5 : "))

        except ValueError as e:
            print("That was not a number\n")
            continue
        if _file_utility.empty_file:
            if (menu_option == 0 ) or (menu_option == 1):
                pass
            else:
                print("No ticket records currently")
                continue
        try:
            if menu_option == 0:
                main_function_active == False
                exit()
            elif menu_option == 1:
                option_submit_ticket()

            elif menu_option == 2:
                _Ticketing.show_all_tickets()
            elif menu_option == 3:
                if not _file_utility.empty_file:
                    _Ticketing.ticket_data = _file_utility.read_records()
                    _ticket_data= _Ticketing.respond_to_ticket()
                    #  Write records to file
                    _file_utility.write_records(_Ticketing.ticket_data)
            elif menu_option == 4:
                if not _file_utility.empty_file:
                    _Ticketing.ticket_data = _file_utility.read_records()
                    _Ticketing.reopen_resolved_ticket()
                    #  Write records to file
                    _file_utility.write_records(_Ticketing.ticket_data)
            elif menu_option == 5:
                _Ticketing.ticket_stats()
            else:
                print("Error! Enter a valid menu selection")

        except Exception as e:
            print(e)
            print("Exception: Exiting the system \n")


