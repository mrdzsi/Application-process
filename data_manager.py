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
def get_applicant_data_by_name(cursor, first_name):
    query = ("""
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE first_name = %(f_n)s ORDER BY first_name;
        """)
    params = {'f_n': first_name}
    cursor.execute(query, params)
    return cursor.fetchall()
