from flask import Flask, request, abort, json, jsonify
from db import PgManager
from repositories import UserRepository, CarRepository, RentalRepository, db_manager, BaseRepository

app=Flask(__name__)

#crear un nuevo usuario
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
        users_repo.create_user(**request_body)
        return jsonify(message="user created successfully"), 201
    
    except ValueError as e:
        return jsonify(message=str(e)),400
    except Exception as e:
        return jsonify(message=str(e)),500



#crear un nuevo vehiculo
@app.route("/cars", methods=['POST'])
def add_car():
    car_repo=CarRepository(db_manager)

    try:
        request_body=request.json
        for value in request_body.values():
            if not value:
                abort(400, "complete all required fields")
        if car_repo.valid_car(request_body['vin_number']):
            abort("the car already exist")
        car_repo.created_car(**request_body)
        return jsonify(message="car added successfully"),201
    
    except ValueError as e:
        return jsonify(message=str(e)),400
    except Exception as e:
        return jsonify(message=str(e)),500


#crear una renta 
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
        rental_repo.rental_car(**request_body)
        return jsonify(message="Rental successfully completed"), 201

    except ValueError as e:
        return jsonify(message=str(e)),400
    except Exception as e:
        return jsonify(message=str(e)),500


#cambiar el estado de un automovil
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
        car_repo.update_car_status(id, new_status)
        return jsonify(message="car_status update successfully"), 200
    
    except ValueError as e:
        return jsonify(message=str(e)), 400
    except Exception as e:
        return jsonify(message=str(e)), 500
        

#cambiar el estado del usuario
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
        user_repo.update_account_status(id, new_status)
        return jsonify(message="account status update successfully"), 200
    
    except ValueError as e:
        return jsonify(message=str(e)), 400
    except Exception as e:
        return jsonify(message=str(e)), 500


#completar un alquiler
@app.route("/rentals/<int:rental_id>/<int:car_id>", methods=['PATCH'])
def completed_rental(rental_id, car_id):
    rental_repo=RentalRepository(db_manager)

    try:
        if not rental_repo.get_rental_by_id(rental_id):
            abort(404, "the rental was not found")
        rental_repo.completed_rental(rental_id, car_id)
        return jsonify(message="rental completed successfully"), 200
    
    except ValueError as e:
        return jsonify(message=str(e)), 400
    except Exception as e:
        return jsonify(message=str(e)), 500
    


#cambiar el estado de un alquiler
@app.route("/rentals/<int:id>", methods=['PATCH'])
def update_rental_status(id):
    rental_repo=RentalRepository(db_manager)
    request_body=request.json

    try:
        if 'rental_status' in request_body:
            if request_body.get('rental_status') not in ('available', 'rented', 'cancelled'):
                raise ValueError ("The status is invalid; select from: available, rented, cancelled.")
        new_status=request_body.get('rental_status')
        rental_repo.get_rental_by_id(id)
        rental_repo.update_status(id, new_status)
        return jsonify(message="rental status updated successfully"), 200
    
    except ValueError as e:
        return jsonify(message=str(e)),400
    except Exception as e:
        return jsonify(message=str(e)), 500


#flagear un usuario como moroso
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
    except Exception as e:
        return jsonify(message=str(e)), 500


#listar todos los usuarios por filtro
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
    except Exception as e:
        return jsonify(message=str(e)), 500


#listar todos los automoviles por filtros
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
    except Exception as e:
        return jsonify(message=str(e)), 500


#listar todas las rentas por filtros
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
    except Exception as e:
        return jsonify(message=str(e)), 500


if __name__ =="__main__":
    app.run(host="localhost", port=5000, debug=True)