# DunderMifflin Feedback App

###### Small Flask application that allows users to rate their experience buying paper from notorious DunderMifflin Scranton branch. 

## Features List

* General
    - [x] Dark mode
    - [ ] Allow users to switch between Dark/Light mode
    - [ ] 404 page for invalid requests

* Feedback Page
    - [x] Form collects users' info about a recent purchase
    - [x] Forum validation (missing fields & prevents duplicate submissions based on order numbers)

* Confirmation Page
    - [x] Display confirmation that feedback was received
    - [x] Different response from each rep based on their rating
    - [x] Email confirmation with feedback review in body

* Employee Review Page (work in progress)
    - [ ] User authentication for login 
    - [ ] Allow users to see employee's overall rating & comments