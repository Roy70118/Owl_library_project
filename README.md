Owl Library Book Borrowing System
Project Description
The Owl Library Book Borrowing System is a REST API service that allows users to borrow and return books from the Owl Library. The system tracks the availability of books and manages the borrowing and returning process, taking into account the library's unique policies.
Key Features

   . Users can search for and view available books
   . Users can borrow books, with restrictions for popular authors
   . Users can return books within 14 days
   . The system provides information on when a user can borrow a specific book

Technologies Used

    Python
    Django
    Django REST Framework

Usage

    Search for available books using the /books/ endpoint
    Borrow a book by sending a PUT request to the /borrow/<owl_id>/ endpoint
    Return a book by sending a PUT request to the /return/<owl_id>/ endpoint
    Check when a user can borrow a specific book by sending a GET request to the /availability/<owl_id>/?email=<user_email> endpoint
