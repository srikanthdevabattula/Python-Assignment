from flask import Flask, request, jsonify
from models import db, User
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

@app.route('/api/users', methods=['GET'])
def search_users():
    first_name = request.args.get('first_name')

    if not first_name:
        return jsonify(message="Missing 'first_name' parameter"), 400

    matching_users = User.query.filter(User.first_name.startswith(first_name)).all()

    if matching_users:
        result = [{"id": user.id, "first_name": user.first_name, "last_name": user.last_name,
                   "age": user.age, "gender": user.gender, "email": user.email,
                   "phone": user.phone, "birth_date": user.birth_date.strftime('%Y-%m-%d')}
                  for user in matching_users]
        return jsonify(users=result)
    else:
        response = requests.get(f'https://dummyjson.com/users/search?q={first_name}')
        data = response.json()

        for user_data in data:
            new_user = User(first_name=user_data["first_name"], last_name=user_data["last_name"],
                            age=user_data["age"], gender=user_data["gender"],
                            email=user_data["email"], phone=user_data["phone"],
                            birth_date=datetime.strptime(user_data["birth_date"], '%Y-%m-%dT%H:%M:%S.%fZ').date())
            db.session.add(new_user)
        db.session.commit()

        return jsonify(users=data)

if __name__ == '__main__':
    app.run(debug=True)
