# DunderMifflin Feedback App

###### Small Flask application that allows users to rate their purchase experience with the notorious DunderMifflin Scranton branch. 

## Features List

* General
    - [x] Dark mode
    - [ ] Allow users to switch between Dark/Light mode
    - [x] 404 page for invalid requests

* Feedback Page
    - [x] Form collects users' info about a recent purchase
    - [x] Forum validation (missing fields & prevents duplicate submissions based on order numbers)

* Confirmation Page (upon successful feedback)
    - [x] Display confirmation that feedback was received
    - [x] Different response from each rep based on their rating
    - [x] Email confirmation with feedback review in body

* Employee Review Page (work in progress)
    - [ ] User authentication for login 
    - [ ] Allow users to see employee's overall rating & comments

* User Registration Page
    - [x] Validate user input before submission
    - [x] Re-direct user to login after creating new account

* User Profile
    - [ ] Dynamic welcome message
    - [ ] Display user account data points (# of feedback submissions, etc)

