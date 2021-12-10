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


@app.route('/applicants-phone')
def applicants_list():
    applicant_first_name = request.args.get('applicant-name')

    if applicant_first_name:
        applicant_details = data_manager.get_applicant_data_by_name(applicant_first_name)
    else:
        redirect('/index.html')

    return render_template('applicants.html',
                           applicant_first_name=applicant_first_name)




if __name__ == '__main__':
    app.run(debug=True)
