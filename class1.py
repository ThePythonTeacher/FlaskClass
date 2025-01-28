from flask import Flask, request, render_template
from database_function import login, gte_the_details, search_name
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("hello.html")


@app.route("/print", methods=['GET'])
def print_name():

    data = request.args.get('name')
    return "welcome %s" %data



@app.route("/pass/<name>", methods=['GET'])
def pass_name(name):
    result = search_name(name)
    if len(result)!=0:

        return str(result)
    else:
        return str("No records found")


@app.route("/put_json", methods=['POST'])
def bala():

    data = request.get_json()

    name = data['name']
    age  = data['age']
    login(name, age)
    print(name, age )
    return "welcome %s" %name



@app.route("/get_json", methods=['GET'])
def get_user_details():

    result  = gte_the_details()

    json_result = []

    for data in result:

        id = data[0]
        age = data[1]
        name = data[2]

        dict_result = {'id': id, 'age': age, 'name':name }

        json_result.append(dict_result)

        print(json_result)



    return str(json_result)


if __name__ == "__main__":

    app.run(port=5002)




