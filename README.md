CAP 2.0
=======

A study tool specially designed for those who need to pass the CAP exam in Spain. This web application performs web scraping of the questions from the Spanish Ministry of Transport website, selects the links of the topics of the questions, accesses each one of them and downloads all the questions, creating a file with the raw data. The data is organized and presented to the user randomly, allowing you to test your knowledge in a challenging and efficient way.

In addition, the application has a system for counting correct answers, wrong answers and unanswered questions, which is done through javascript and saved in cookies in the user's browser so that you do not lose your progress.

Getting Started
---------------

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

Copy code

`Python 3.6 or higher
Flask
beautifulsoup4
requests`

### Installing

A step by step series of examples that tell you how to get a development env running

1.  Clone the repository

bashCopy code

`git clone https://github.com/thiagoc-machado/cap-2.0.git`

1.  Install the required packages

Copy code

`pip install -r requirements.txt`

1.  Run the application

Copy code

`python app.py`

Deployment
----------

The application is deployed on <https://cap-empc.onrender.com/>

Built With
----------

-   [Flask](http://flask.palletsprojects.com/en/2.1.x/) - The web framework used
-   [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) - Used for web scraping
-   [requests](https://pypi.org/project/requests/) - Used for making HTTP requests

Future Improvements
-------------------

-   Organizing questions by topic
-   Creating a login system to control users

Author
------

-   Thiago Machado - [thiagoc-machado](https://github.com/thiagoc-machado)

License
-------

This project is licensed under the MIT License - see the [LICENSE.md](https://chat.openai.com/LICENSE.md) file for details.
