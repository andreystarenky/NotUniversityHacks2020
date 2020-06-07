from flask import Flask
from flask import render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='black-dashboard-master',
            template_folder='black-dashboard-master\examples')

@app.route('/home')
def dashboard():
    return render_template("dashboard.html")

@app.route('/map')
def map():
    return render_template("map.html")

@app.route('/notifications')
def notifications():
    return render_template("notifications.html")

@app.route('/tables')
def tables():
    return render_template("tables.html")

if __name__ == '__main__':
    app.run(debug = True)