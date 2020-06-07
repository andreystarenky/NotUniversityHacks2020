from flask import Flask
from flask import render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='black-dashboard-master',
            template_folder='black-dashboard-master\examples')

@app.route('/')
def hello():
    print("HELLO")
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug = True)