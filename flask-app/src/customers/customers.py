from flask import Blueprint, request, jsonify, make_response
import json
from src import db


customers = Blueprint('customers', __name__)

# Get all customers from the DB
@customers.route('/customers', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('select id, company, last_name,\
        first_name, job_title, business_phone from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for customer with particular userID
@customers.route('/customers/<userID>', methods=['GET'])
def get_customer(userID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from customers where id = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@customers.route('/customers', methods=['PUT'])
def update_customer():
    
    # collecting data from the request object 
    the_data = request.json
    # current_app.logger.info(the_data)

    #extracting the variable
    cust_id = the_data['id']
    cust_first_name = the_data['first_name']
    cust_last_name = the_data['last_name']
    cust_company = the_data['company']   
    cust_job = the_data['job_title']
    cust_biz_phone = the_data['business_phone']


    # Constructing the query
    #query = 'UPDATE customers SET first_name = %s, last_name = %s, company = %s,  job_title = %s, business_phone = %s WHERE id = %s'
    #data = (cust_first_name, cust_last_name, cust_company, cust_job, cust_biz_phone, cust_id)
    # current_app.logger.info(query)
    query = 'UPDATE customers SET job_title = ' + cust_job + ' WHERE id = ' + cust_id
    
    # executing and committing the update statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'