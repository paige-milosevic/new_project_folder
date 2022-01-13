from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friends import Friend
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html",all_friends=friends)

@app.route('/create_friend', methods=['POST'])
def create_friend():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    Friend.save()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

