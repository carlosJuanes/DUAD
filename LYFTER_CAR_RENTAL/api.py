from werkzeug.exceptions import HTTPException
from flask import Flask, request, abort, json, jsonify
from db import PgManager
from repositories import UserRepository, CarRepository, RentalRepository, db_manager, BaseRepository

app=Flask(__name__)

#CREATE A NEW USER
@app.route("/users", methods=['POST'])
def add_user():
    users_repo=UserRepository(db_manager)

    try:
        request_body=request.json
        for value in request_body.values():
            if not value:
                abort(400, "complete all required fields")        
        if users_repo.validate_user(request_body['email'], request_body['user_name']):
            abort(400, "Email or username already exists")
        if not users_repo.create_user(**request_body):
            abort(500, "Error creating user")
        return jsonify(message="user created successfully"), 201
    
    except ValueError as e:
        return jsonify(message=str(e)),400
    except HTTPException as e:
        return e
    except Exception as e:
        return jsonify(message=str(e)),500



#CREATE A NEW CAR
@app.route("/cars", methods=['POST'])
def add_car():
    car_repo=CarRepository(db_manager)

    try:
        request_body=request.json
        for value in request_body.values():
            if not value:
                abort(400, "complete all required fields")
        if car_repo.valid_car(request_body['vin_number']):
            abort(400, "the car already exist")
        if not car_repo.created_car(**request_body):
            abort(500, "Error creating the new car")
        return jsonify(message="car added successfully"),201
    
    except ValueError as e:
        return jsonify(message=str(e)),400
    except HTTPException as e:
        return e    
    except Exception as e:
        return jsonify(message=str(e)),500


#CREATE A MEW RENTAL 
@app.route("/rentals", methods=['POST'])
def created_rental():
    rental_repo=RentalRepository(db_manager)
    user_repo=UserRepository(db_manager)
    car_repo=CarRepository(db_manager)

    try:
        request_body=request.json
        for value in request_body.values():
            if not value:
                abort(400, "complete all required fields")
        if not user_repo.validated_existence(request_body['user_id']):
            abort(404, "user not found")
        if not car_repo.validated_existence(request_body['car_id']):
            abort(404, "car not found")
        if not car_repo.is_car_available(request_body['car_id']):
            abort(404, 'the car is not available')
        if not rental_repo.rental_car(**request_body):
            abort(500, "Error creating a new rental")
        car_repo.update_car_status(request_body['car_id'], 'rented')
        return jsonify(message="Rental successfully completed"), 201

    except ValueError as e:
        return jsonify(message=str(e)),400
    except HTTPException as e:
        return e 
    except Exception as e:
        return jsonify(message=str(e)),500


#UPDATE CAR STATUS
@app.route("/cars/<int:id>", methods=['PATCH'])
def update_car_status(id):
    car_repo=CarRepository(db_manager)
    request_body=request.json

    try:
        if 'car_status' in request_body:
            if request_body.get('car_status') not in ('rented', 'available', 'disabled'):
                raise ValueError ("the status is invalid select from: 'rented', 'available', 'disabled'")
        if not car_repo.validated_existence(id):
            abort(404, "The car was not found.")
        new_status=request_body.get('car_status')
        if not car_repo.update_car_status(id, new_status):
            abort(500, "Error updating car status")
        return jsonify(message="car_status update successfully"), 200
    
    except ValueError as e:
        return jsonify(message=str(e)), 400
    except HTTPException as e:
        return e 
    except Exception as e:
        return jsonify(message=str(e)), 500
        

#UPDATE USER STATUS
@app.route("/users/<int:id>", methods=['PATCH'])
def update_user_status(id):
    user_repo=UserRepository(db_manager)
    request_body=request.json

    try:
        if not user_repo.validated_existence(id):
            abort(404, "user not found")
        if 'account_status' in request_body:
            if request_body.get('account_status') not in ('regular', 'suspended', 'delinquent'):
                raise ValueError("the account status is invalid select from: 'regular', 'suspended', 'delinquent'")
        new_status=request_body.get('account_status')
        if not user_repo.update_account_status(id, new_status):
            abort(500, "Error updating user status")
        return jsonify(message="account status update successfully"), 200
    
    except ValueError as e:
        return jsonify(message=str(e)), 400
    except HTTPException as e:
        return e 
    except Exception as e:
        return jsonify(message=str(e)), 500


#COMPLETE A RENTAL
@app.route("/rentals/<int:rental_id>/<int:car_id>", methods=['PATCH'])
def completed_rental(rental_id, car_id):
    rental_repo=RentalRepository(db_manager)

    try:
        if not rental_repo.get_rental_by_id(rental_id):
            abort(404, "the rental was not found")
        if not rental_repo.completed_rental(rental_id, car_id):
            abort(500, "Error completing rental")
        return jsonify(message="rental completed successfully"), 200
    
    except ValueError as e:
        return jsonify(message=str(e)), 400
    except HTTPException as e:
        return e 
    except Exception as e:
        return jsonify(message=str(e)), 500
    


#UPDATE RENTAL STATUS
@app.route("/rentals/<int:id>", methods=['PATCH'])
def update_rental_status(id):
    rental_repo=RentalRepository(db_manager)
    request_body=request.json

    try:
        if 'rental_status' in request_body:
            if request_body.get('rental_status') not in ('available', 'rented', 'canceled'):
                raise ValueError ("The status is invalid; select from: available, rented, canceled.")
        new_status=request_body.get('rental_status')
        if not rental_repo.get_rental_by_id(id):
            abort(404, "No results were found in the database.")
        if not rental_repo.update_status(id, new_status):
            abort(500, "Error updating rental status")
        return jsonify(message="rental status updated successfully"), 200
    
    except ValueError as e:
        return jsonify(message=str(e)),400
    except Exception as e:
        return jsonify(message=str(e)), 500


#FLAG A USER AS DELINQUENT
@app.route("/users/<int:id>/flag", methods=['PATCH'])
def flag_delinquent(id):
    user_repo=UserRepository(db_manager)

    try:
        if not user_repo.validated_existence(id):
            abort(404, "user not found")
        if not user_repo.turn_delinquent(id):
            abort(500, "error updating account status")
        return jsonify(massage="user status updating to delinquent successfully"), 200
    
    except ValueError as e:
        return jsonify(message=str(e)), 400
    except HTTPException as e:
        return e 
    except Exception as e:
        return jsonify(message=str(e)), 500


#GET ALL USER BY FILTERS
@app.route("/users", methods=['GET'])
def get_all_users():
    base_repo=BaseRepository(db_manager)
    table_name="users"
    filter=request.args

    try:
        result=base_repo.get_by_filter(table_name, filter)
        if not result:
            abort(404, "users not found")
        return jsonify(result), 200
    
    except ValueError as e:
        return jsonify(message=str(e)), 400
    except HTTPException as e:
        return e 
    except Exception as e:
        return jsonify(message=str(e)), 500


#GET ALL CARS BY FILTERS
@app.route("/cars", methods=['GET'])
def get_all_cars():
    base_repo=BaseRepository(db_manager)
    table_name="cars"
    filter=request.args

    try:
        result=base_repo.get_by_filter(table_name, filter)
        if not result:
            abort(404, "cars not found")
        return jsonify({"cars":result}), 200
    
    except ValueError as e:
        return jsonify(message=str(e)), 400
    except HTTPException as e:
        return e 
    except Exception as e:
        return jsonify(message=str(e)), 500


#GET ALL RENTS BY FILTERS
@app.route("/rentals", methods=['GET'])
def get_all_rentals():
    base_repo=BaseRepository(db_manager)
    table_name="rentals"
    filter=request.args

    try:
        result=base_repo.get_by_filter(table_name, filter)
        if not result:
            abort(404, "rental not found")
        return jsonify({"rentals":result}), 200
    
    except ValueError as e:
        return jsonify(message=str(e)), 400
    except HTTPException as e:
        return e 
    except Exception as e:
        return jsonify(message=str(e)), 500


if __name__ =="__main__":
    app.run(host="localhost", port=5000, debug=True)