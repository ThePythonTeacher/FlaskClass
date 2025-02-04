from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS
app = Flask(__name__)
CORS(app)



@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()    #Get JSON data from the frontend
    name = data['name']
    email = data['email']
    print(name, email)

    if not name or not email:
        return jsonify({'status': 'error', 'message': 'All fields are required'}), 400

    return jsonify({'status': 'success', 'message': f'Form submitted by {name} with email {email}'})






if __name__ == '__main__':
    app.run(debug=False)
