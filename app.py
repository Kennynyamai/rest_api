from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        self.name = name

@app.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    
    name = data['name']

    new_person = Person(name=name)

    try:
        db.session.add(new_person)
        db.session.commit()
        return jsonify({'message': 'Person added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get(user_id)

    if person is None:
        return jsonify({'error': 'Person not found'}), 404

    return jsonify({'id': person.id, 'name': person.name})

# UPDATE operation - Modify details of an existing person by ID
@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    name = data['name']

    person = Person.query.get(user_id)

    if person is None:
        return jsonify({'error': 'Person not found'}), 404

    try:
        person.name = name
        db.session.commit()
        return jsonify({'message': 'Person updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
# DELETE operation - Remove a person by ID
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get(user_id)

    if person is None:
        return jsonify({'error': 'Person not found'}), 404

    try:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500





if __name__ == '__main__':
    # When running this script directly, start the development server
    from flask_migrate import upgrade
    with app.app_context():
        upgrade()
    # Start the development server
    app.run(debug=False)
    




