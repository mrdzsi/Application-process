from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    mentor_name = request.args.get('mentor-last-name')
    city_name = request.args.get('city-name')
    mentor_details = None

    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif city_name:
        mentor_details = data_manager.get_mentors_by_location(city_name)
    elif not mentor_name and not city_name:
        mentor_details = data_manager.get_mentors()

    return render_template('mentors.html',
                           mentors=mentor_details,
                           mentor_name=mentor_name,
                           city_name=city_name)


@app.route('/applicants', methods=['GET', 'POST'])
def display_applicants():
    application_code = None
    applicants = None
    headers = None

    headers = data_manager.get_column_names(headers)
    applicants = data_manager.get_applicants()

    return render_template('applicants.html',
                           applicants=applicants,
                           headers=headers
                           )


@app.route('/applicants')
def applicants_list():
    name = request.args.get('applicant-first-name')
    email = request.args.get('email-ending')
    applicant_details = None

    if name:
        applicant_details = data_manager.get_applicant_data_by_name(name)
    elif email:
        applicant_details = data_manager.get_applicant_data_by_email(email)
    elif not name and not email:
        applicant_details = data_manager.get_applicants()

    return render_template('applicant_details.html',
                           applicants_details=applicant_details,
                           )


@app.route('/applicants/<application_code>', methods=['GET', 'POST'])
def display_applicant_details(application_code):
    applicant_details = data_manager.get_applicant_details(application_code)
    print(applicant_details)

    print(applicant_details[0])

    for applicant in applicant_details:
        print(applicant)

    return render_template('applicant_details.html',
                           applicant_details=applicant_details,
                           application_code=application_code
                           )


@app.route('/add-applicant')
def add_applicant():
    pass


# @app.route('/delete-applicant/<email-ending>', methods=['GET','POST'])
# def delete_applicant(application_code):
#     email = request.args.get('email-ending')
#
#     if email:
#         data_manager.remove_applicant_by_email
#         return redirect('/applicants')
#
#     pass


if __name__ == '__main__':
    app.run(debug=True)
