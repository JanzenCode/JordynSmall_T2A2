from controllers.UserController import UserController

@app.route('/', methods=['GET'])
def index():
    return 'Hello World! TEST'

@app.route('/register/', methods=['POST'])
def register():
    return '<p>user added successfully</p>'
