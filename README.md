# Application Process

## Story

Handling the application process at Codecool has always been a tedious task.
Finally, the HR department figured out that using only Python and long lists cannot continue if they want to get information quickly.
To improve data management, they collaborate with you to test out something they just heard about: "databases".

Luckily they managed to assemble a database which can be described by the following Entity-Relationship Diagram.

![application process assignment.png](media/web-python/application-process-assignment.png)

They need your help to write the application which runs queries on this database, so they can quickly get information about Applicants and Mentors.

The HR department wants answers to the following questions:

## What are you going to learn?

- Understand basic SQL commands (SELECT, UPDATE, DELETE, INSERT).
- Execute SQL queries from Python code.
- Display the results on a webpage using the Jinja2 template engine.
- CSS basics


## Tasks

1. We already have a list where we can see every mentor in Codecool on the `/mentors` route but we need to extend it a little.
    - Unfortunately we have a bug and the `Filter by mentor last name` feature is not working. Fix this feature so that when searching for the last name "Simpson", the result is the following.
  - Bart Simpson - Budapest
  - Homer Simpson - Warsaw
  - Lisa Simpson - Budapest
    - On the `/mentors` page, there is a separate form with a submit button and a `<select name="city-name">` tag with five city options: Bucharest, Budapest, Kraków, Miskolc, and Warsaw.
    - Submitting the form with `Miskolc` selected redirects to `/mentors?city-name=miskolc`, where the following mentors are listed.
  - Bugs Bunny - Miskolc
  - Bob Sponge - Miskolc
  - Yogi Bear - Miskolc
  - Porky Pig - Miskolc

2. We had chat with an applicant, some Jemima. We don't remember her name, but she left her hat at the school. We want to call her to give back her hat. To look professional, we also need her full name when she answers the phone.
    - On the main page (`/`), there is a separate form inside the `<section class="search">` tag, with one input with an `applicant-name` name attribute and a submit button.
    - Submitting the form with the name `Jemima` redirects to the result page on the `/applicants-phone` route. This page lists the following applicants.
  - Name: Jemima Cantu, Phone number: 003620/423-4261
  - Name: Jemima Foreman, Phone number: 003620/834-6898
    - In the `data_manager.py` there is a `get_applicant_data_by_name` function that returns a list of dictionaries with `full_name` and `phone_number` keys for the applicants.

3. We called Jemima and she said it is not her hat. It belongs to another girl, who went to the famous Adipiscingenimmi University. Write a query to get the same information as before. The only thing we know about her is her school e-mail address ending in `adipiscingenimmi.edu`
    - On the main page (`/`), there is a separate form inside the `<section class="search">` tag, with one input with an `email-ending` name attribute and a submit button.
    - Submitting the form with the email ending of `adipiscingenimmi.edu` redirects to a result page on the `/applicants-phone` route. This page lists the following applicant.
  - Name: Jane Forbes, Phone number: 003670/653-5392
    - In the `data_manager.py` there is a `get_applicant_data_by_email_ending` function that returns a list of dictionaries with `full_name` and `phone_number` keys for the found applicants.

4. The recruiters want to see all applicants on one page with all the data we have about them.
    - There is a link to the `/applicants` route from the main page in the `<nav>` tag.
    - On the `/applicants` page, all applicants are listed in a well-formed table.
    - In the `data_manager.py` there is a `get_applicants` function that returns a list of dictionaries with `first_name`, `last_name`, `phone_number`, `email` and `application_code` keys for all applicants.

5. An applicant, Ursa William, told us that her phone number changed to 003670/223-7459. We need a new page where we can see her details and update her phone number.
    - There is a link to every applicant in the table at the `/applicants` route. The new link must be `/applicants/91220`, where the number is the application code of the applicant, in this case Ursa William.
    - On the `/applicants/<code>` page, every detail is shown for the applicant whose application code is the `<code>` part of the URL.
    - On this page, there is a form with `POST` method and the action is the same page it is on. In this form there is one input with a `new-phone` name attribute and a submit button.
    - When submitting, the form saves the new phone number and writes an `UPDATE` query that changes this data in the database for this applicant. At the end, it redirects to the same page, so that refreshing the page does not resend the POST request.
    - Create a `Delete applicant` link on this page that points to the `/applicants/<code>/delete` URL. The `<code>` part of the URL is an application code (such as `/applicants/91220/delete`). Clicking on the link, the applicant is deleted and the page redirects to the `/applicants` page.

6. Arsenio, an applicant told us that he and his friend applied to Codecool. They both want to cancel the process, because they got an investor for the site they run: `mauriseu.net` Write a DELETE query to remove all the applicants who applied with emails from this domain (that is, the e-mail address contains this domain after the @ sign).
    - On the `/applicants` page, there is a form with `POST` method after the table. There is one input with `email-ending` name attribute and a submit button.
    - Submitting the form with the email ending of `mauriseu.net` deletes all applicants whose email addresses contain this domain. Then the page redirects to the `/applicants` page.

7. After the last call, a new applicant appeared at the school and he wants to enter the application process. His first and last name is `Markus Schaffarzyk`. His phone number is `003620/725-2666`, and e-mail address is `djnovusgroovecoverage.com` Our generator gave him the application code `54823`.
    - There is a link to the `/add-applicant` page on the `/applicants` page.
    - On the `/add-applicant` page there is a form with `POST` method with an input field for every data and a submit button.
    - After submitting the form and INSERTing the data, the page redirects to the applicant's page. (Use the unique application code for the URL.)

8. Your task is to create a special design for the app. Of course you do not have to create some elaborate design with lots of images and artwork. The purpose of the task is to practice your newly acquired CSS knowledge. You can use the existing `main.css` file.
    - A design is created using at least the following CSS selectors.
  - body, h1, footer
  - id selector
  - some class selectors
  - a selector which selects tags inside another tag
  - a selector which changes different elements at once (You can use comma as a separator for this.)
    - The design is altered using at least the following properties.
  - font-family, color, background-color, text-align
  - padding, margin, width, height, top, left
  - display, position

Remember, the goal is to practice CSS, not to spend tens of hours to create a wonderful design. Still, if you want to, you can unleash your inner creativity dragon. Just make sure you do that after everything else :)

## General requirements

None

## Hints

- Use the SQL file that contains the sample data in the `data` folder in the git repo by performing the following steps.
    - Create a new database for the project.    
    - Start `psql` in a terminal at the `data` folder of the project.
    - Connect to the new database, for example `\connect application_process`.
    - Execute the commands in the SQL file `\i application_process_sample_data.sql`.
- Use concatenation for the `full_name` in your query, so that the result value is in a single column.


## Background materials

- <i class="far fa-exclamation"></i> [Best practices for Python/Psycopg/Postgres](project/curriculum/materials/pages/python/tips-python-psycopg-postgres.md)
- [Installing and setting up PostgreSQL](project/curriculum/materials/pages/tools/installing-postgresql.md)
- [Installing psycopg2](project/curriculum/materials/pages/tools/installing-psycopg2.md)
- [Setting up a database connection in PyCharm](project/curriculum/materials/pages/tools/pycharm-database.md)
- [Short guide about psql](http://postgresguide.com/utilities/psql.html)
- [PostgreSQL documentation page about psql](https://www.postgresql.org/docs/current/app-psql.html)
- <i class="far fa-book-open"></i> [Introduction to HTML](project/curriculum/materials/tutorials/introduction-to-html.md)
- <i class="far fa-book-open"></i> [Pip and VirtualEnv](project/curriculum/materials/pages/python/pip-and-virtualenv.md)
- <i class="far fa-book-open"></i> [A web-framework for Python: Flask](project/curriculum/materials/pages/python/python-flask.md)
- <i class="far fa-book-open"></i> [Flask documentation](http://flask.palletsprojects.com/) (the Quickstart gives a good overview)
- <i class="far fa-book-open"></i> [Jinja2 documentation](https://jinja.palletsprojects.com/en/2.10.x/templates/)
- <i class="far fa-book-open"></i> [htmlreference.io](https://htmlreference.io/)
- <i class="far fa-book-open"></i> [HTML tutorials and references on MDN](https://developer.mozilla.org/en-US/docs/Web/HTML)

