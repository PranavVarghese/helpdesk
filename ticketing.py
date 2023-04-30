import sys
import csv
import os.path

class File_utility:
    """A simple utility to help with read write and store data"""
    empty_file = True
    file_name = 'D:\\my_test\\ticket.csv'

    def __init__(self,file_name):
        self.check_open_file(file_name)
        return
    def read_records(self):
        ticket_data=[]
        file_obj= None
        _file_name =''
        _file_name = self.file_name
        try:
             with open( _file_name, 'r') as file_obj:
                ticket_data = list(csv.DictReader(file_obj))
             if ticket_data == []:
                self.empty_file = True
        except csv.Error as e:
           sys.exit('file {}, line {}: {}'.format(_file_name, ticket_data.line_num, e))
        return ticket_data

    def write_records(self,precords_list):
        try:
            with open(self.file_name, mode='w',newline="") as f:
                keys = ['TicketNumber', 'StaffID', 'TicketOwner', 'ContactEmail', 'DescriptionOfIssue','TicketStatus', 'TicketResponse']
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()  # add column names in the CSV file
                for record in precords_list:
                    writer.writerow(record)
        except FileNotFoundError as e:
               print (e)
        else:
            return

    def check_open_file(self,file_name):
        try:
            check_file = os.path.isfile(file_name)
            if check_file:
                 print (f"Ticket file can be opened as {file_name}")
                 self.file_name = file_name
                 self.empty_file = False
        except Exception as e:
            print(f"File named{file_name} could not be opened or not found")
            self.empty_file = True
        return


class Ticketing:
##################################################
# Initialize class
##################################################
    def __init__(self):
         self.initial_ticket_number =2000
         self.last_ticket_Number = 0
         self.ticket_data = []
         keys = ['TicketNumber', 'StaffID', 'TicketOwner', 'ContactEmail', 'DescriptionOfIssue', 'TicketStatus',
                 'TicketResponse']
         self.ticket_data_record = {}
         #self.ticket_data_record = dict.fromkeys(keys)
         # If no data, then start with 2001 otherwise find the last ticket number and add 1
         # Get the last Dict from the list of Dictionaries
         return
    def find_next_ticket_number(self):
        _next_ticket_Number = 0
        if self.ticket_data == []:
            self.last_ticket_Number = self.initial_ticket_number
        else:
            _last_record = next(reversed(self.ticket_data))
            self.last_ticket_Number = int(_last_record['TicketNumber'])
        _next_ticket_Number = self.last_ticket_Number + 1
        return _next_ticket_Number

#####################################################################
# Function 2 Show all tickets
#####################################################################
    def show_all_tickets(self):
        _ticket_records = []
        _ticket_records = self.ticket_data
        for _ticket_record in _ticket_records:
            print("-------------------------------------------------------------------")
            print(f": Ticket               : {_ticket_record['TicketNumber']}")
            print(f": Staff ID             : {_ticket_record['StaffID']}")
            print(f": Ticket Owner         : {_ticket_record['TicketOwner']}")
            print(f": Contact Email        : {_ticket_record['ContactEmail']}")
            print(f": Description Of Issue : {_ticket_record['DescriptionOfIssue']}")
            print(f": Ticket Status        : {_ticket_record['TicketStatus']}")
            print(f": Ticket Response      : {_ticket_record['TicketResponse']}")
            print("-------------------------------------------------------------------")
        return
    # Function 3 Respond to a ticket number
    #############################################
    def respond_to_ticket(self):
        _ticket_response =None
        _ticket_records = self.ticket_data
        if _ticket_records == []:
            print ("No ticket records to respond to")
            return
        try:
            _ticket_number = int(input("Please enter the ticket number to respond: "))
        except ValueError as e:
            print("That was not a number! \n")

        for _ticket_record in _ticket_records:
            if _ticket_record['TicketNumber'] == str(_ticket_number):
                print(f" Respond to Ticket: {_ticket_record['TicketNumber']}")
                _ticket_response = input("Enter response: ")
                _ticket_record['TicketStatus'] = 'closed'
                _ticket_record['TicketResponse'] = _ticket_response
                ## Do Update ################
                self.ticket_data = _ticket_records
                break
            else:
                continue
        return

    def reopen_resolved_ticket(self):
        _ticket_response =None
        _ticket_number = 0
        _ticket_records = self.ticket_data
        if _ticket_records == []:
            print ("No ticket records to respond to")
            return
        try:
            _ticket_number = int(input("Please enter the ticket number to respond: "))
        except ValueError as e:
            print("That was not a number! \n")

        for _ticket_record in _ticket_records:
            if _ticket_record['TicketNumber'] == str(_ticket_number) and _ticket_record['TicketStatus'] == 'closed':
                print(f"Re-opening Ticket: {_ticket_record['TicketNumber']}")
                _ticket_response = input("Enter response: ")
                _ticket_record['TicketStatus'] = 'open'
                _ticket_record['TicketResponse'] = _ticket_response
                self.ticket_data = _ticket_records
                break
            else:
                continue
        return

    def ticket_stats(self):
        _ticket_records = []
        _open_tickets=0
        _resolved_tickets=0
        _submitted_tickets=0

        _ticket_records = self.ticket_data
        for _ticket_record in _ticket_records:
             if _ticket_record['TicketStatus'].lower() == 'open':
                 _open_tickets=_open_tickets + 1
             if _ticket_record['TicketStatus'].lower() == 'closed':
                 _resolved_tickets=_resolved_tickets + 1
             if _ticket_record['TicketStatus'].lower() == 'submitted':
                 _submitted_tickets=_submitted_tickets + 1
        print("-------------------------------------------------------------------")
        print(f": Ticket Status - submitted : {_submitted_tickets}")
        print(f": Ticket Status - open : {_open_tickets}")
        print(f": Ticket Status - resolved : {_resolved_tickets}")
        print("-------------------------------------------------------------------")

