This Django-based platform is designed to streamline wedding planning and guest management. It provides a user-friendly interface for creating events, managing guest lists, and tracking RSVPs.

## Features

User Authentication: Users can create accounts and log in to access the platform.
Event Creation: Create events with detailed information, including date, time, venue, and description.
* Venue Management: Add and manage venues, including capacity, contact information, and address.
* Guest Management: Add guests to events, track their RSVP status, and send personalized invitations.
* RSVP Tracking: Guests can easily RSVP to events and update their status as needed.
* Notifications: Send email and SMS notifications to guests about event updates, reminders, and important information.

## Installation

1. Clone the Repository:
```sh
git clone https://github.com/Isaiah-Ambi/Django-wedding-event-management.git
```

2. Set Up Virtual Environment:
	
```sh
	python -m venv venv source venv/bin/activate
```

3. Install Dependencies:
	```sh
	pip install -r requirements.txt 1
	```
4. Configure Database: Edit the settings.py file to configure your database settings.
5. Run Migrations:
 ```sh
python manage.py runserver
```
## Usage
1. User Registration:
	+ Create a new user account by providing the required information.
2. Event Creation:
	+ Log in to your account.
	+ Click the 'create event' button.
	+ Fill in the event details, including title, description, venue, dte, time
	+ save the event
3. Guest Management:
	+ Go to the event details page.
	+ Click the 'add guest' event.
	+ Enter the guest's information.
	+ save the guest
4. RSVP Tracking:
 	+Guests can log in to their accounts to rsvp events
 	They can also update their RSVP status as needed.
 	
 ## Contributing
 We welcome contributions to improve this platform. Feel free to fork the repository and submit pull requests.
 	
 ## Licence
 MIT