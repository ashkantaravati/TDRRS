# Specifications
## A Brief Introduction
IAUCTB Reservation System for Thesis Defense Conference Room ,which was actually my bachelor's project, is a simple responsive web-based information system that makes possible for the IAUCTB students to reserve a time and place for their thesis defense sessions as it has been a pain for the faculty of engineering to handle tremendous requests for conference rooms from students. It also makes it easier to be informed about ongoing defense sessions.
## System Specifications
This software is developed using Django, a web framework for Python, as its backend, and bootstrap (css framework) and jQuery (JavaScript library) as its frontend rendered using DTL (Django Template Language).

## Screenshots


# Product Requirements
## Developed
* Login
* Logout
* Display last login datetime in dashboard
* Use django statics feature
* Use Django url resolution feature
* A base layout
* Create dashboard page
* Create defenseTime page
* Create myRequest page
* View all DefenseTimes in a table
* Submit a request using AJAX
* Change Password Feature
* Student Class
* ReservationRequest Class
* Refactor Views and URL configs 
* Jalali DateTime
* jDateTime Widget in admin site
* Use PEP-8
* Submit reservation requests by inserting into database
* string representations
* Authorization
* Add Staff Model
* Add Professor Model
* Wrap User creation for Students in Student Creation and same for Staff
* Check if already reserved by this User
* Use Django form for login
* Make forms Persian
* only view current semester DefenseTimes
* Authentication control for each GET
* Cancel reservation requests
* A view for deleting ReservationRequests
* dashboard user info summary
* Submit DefenseTime
* automatic pagination for dateTimes
* Finalize Models
* search in table (criteria)
* Add number of reservations per DefenseTime
* Public View for DefenseTimes in current semester

## Secondary TODO
* Personal notifications
* Progressbar in dashboard
* Put IAU icon in base
* Settings Page with change password and change theme
* Change Theme
* Side Menu selected item CSS class
* Student bulk insert
* make sidebar fullheight
* Change Django Admin Site layout to match base
* seperate into several apps
* Reset Password Feature
* Right Align tables
* IDEA: merge DefenseTimes and User-Requests in the same template