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
    - [x] Re-driect to success page upon successful review submission

* Confirmation Page (upon successful feedback)
    - [x] Display confirmation that feedback was received
    - [x] Different response from each rep based on their rating
    - [x] Email confirmation with feedback review in body

* Employee Review Page
    - [x] Login required to view page
    - [x] Re-direct to login page if not already logged in
    - [ ] Allow users to see employee's overall rating & comments

* User Registration Page
    - [x] Validate user input before submission
    - [x] Unique emails to prevent duplicate accounts
    - [x] Save new user in DB
    - [x] Re-direct user to login after creating new account
    - [x] Display success message notifying user account was created

* Login Page
    - [x] Validate user credentials before login
    - [x] Re-direct to profile page after login

* User Profile
    - [x] Redirect to login page if user is not logged in
    - [x] Redirect to profile page upon successful login
    - [x] Welcome message displayed
    - [ ] Display user account data points (# of feedback submissions, last login, etc)

