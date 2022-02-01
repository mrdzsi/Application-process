from typing import List, Dict
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor, last_name):
    query = ("""
        SELECT first_name, last_name, city
        FROM mentor
        WHERE last_name = %(l_n)s ORDER BY first_name;
        """)
    params = {'l_n': last_name}
    cursor.execute(query, params)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_location(cursor, city):
    query = ("""
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city = %(city)s ORDER BY first_name;
        """)
    params = {'city': city}
    cursor.execute(query, params)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicants(cursor):
    query = """
        SELECT first_name, last_name, phone_number, email, application_code
        FROM applicant
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_name(cursor, name):
    query = ("""
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE first_name = %(name)s OR last_name = %(name)s ORDER BY first_name;
        """)
    params = {'name': name}
    cursor.execute(query, params)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_email(cursor, email):
    query = ("""
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE email ~ %(email_ending)s ORDER BY first_name;
        """)
    params = {'email_ending': email}
    cursor.execute(query, params)
    return cursor.fetchall()


@database_common.connection_handler
def get_column_names(cursor, headers):
    query = ("""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'applicant' AND column_name  NOT IN ('id');
    """)
    params = {'headers': headers}
    cursor.execute(query, params)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_details(cursor, application_code):
    query = sql.SQL("""
        SELECT first_name, last_name, phone_number, email, application_code
        FROM applicant
        WHERE application_code = {application_code};
        """).format(application_code=sql.Literal(application_code))
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def update_phone_number(cursor, application_code, new_phone):
    query = sql.SQL("""
        UPDATE applicant
        SET phone_number = {new_phone}
        WHERE application_code = {application_code};
        """).format(application_code=sql.Literal(application_code),
                    new_phone=sql.Literal(new_phone))
    cursor.execute(query)


@database_common.connection_handler
def delete_applicant_by_id(cursor, application_code):
    query = sql.SQL("""
        DELETE 
        FROM applicant
        WHERE application_code = {application_code};
        """).format(application_code=sql.Literal(application_code))
    cursor.execute(query)


@database_common.connection_handler
def remove_applicant_by_email(cursor, email):
    query = ("""
        DELETE
        FROM applicant
        WHERE email ~ %(email_ending)s;
        """)
    params = {'email_ending': email}
    cursor.execute(query, params)
    return cursor.fetchall()
