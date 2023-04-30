# Project Helpdesk prototype

A Very Simple Implementation Of A Basic Helpdesk application Concept Based On raising tickets and resolving these. Written In Python 3.9. This repository is meant for beginners to assist them in their learning of Python.


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Authors

- Pranav V


## Features

- Create Helpdesk tickets
- Displaying the tickets
- Resolve tickets
- Display ticket stats
- Issue New password for Password change requests


## Contributing

Contributions are always welcome!

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Documentation

Before running the software make sure to make data folder called my_test in your D: drive for the data file, or the software will fail.
Create a folder named ‘my_test’ under the D Drive of PC for the data file that store tickets. This is a CSV file and can be opened with MS Excel.

The application has 2 files under helpdesk package namely main.py and ticketing.py. It uses ticketing class and file_utility class along with main.

Execution: python helpdesk\main.py
To create a ticket press the number 1 on your keyboard.

Select from the following choices:
0: Exit
1: Submit Help desk ticket
2: Show all tickets
3: Respond to ticket by number
4: Re-open resolved ticket
5: Display ticket stats

As this is a prototype software you enter anything you want when it ask for;

Staff ID:20230
Name:Iona Smith
email Id:smith99@gmail.com

When entering the problem you will be prompted with a type of problem.
if you want a password change tye in the problem description password change and the app will create a random password for you to use.

e.g: Enter description of problem: password change.

Any else must typed manually of what the issue is. 

e.g: Enter description of problem: PC issues.

Once the issue is tpyed manually and you have descripted what the issue and pressed enter, your ticket will look like this.

Enter description of problem : PC issue

Do you have another ticket to submit? (Y/N)

Press the N key on your keyboard to exit out of the ticket.

And you will go back to the main menu.

Select from the following choices:
0: Exit
1: Submit Help desk ticket
2: Show all tickets
3: Respond to ticket by number
4: Re-open resolved ticket
5: Display ticket stats

If there is nothing else to do press the 0 key on your keyboard to exit out of the app.





