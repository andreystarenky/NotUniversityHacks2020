from flask import Flask
from flask import render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='black-dashboard-master',
            template_folder='black-dashboard-master\examples')

@app.route('/home')
def dashboard():
    print("HELLO")
    return render_template("dashboard.html")

@app.route('/map')
def map():
    print("HELLO")
    return render_template("map.html")

@app.route('/notifications')
def notifications():
    print("HELLO")
    return render_template("notifications.html")

@app.route('/tables')
def tables():
    print("HELLO")
    return render_template("tables.html")

if __name__ == '__main__':
    app.run(debug = True)