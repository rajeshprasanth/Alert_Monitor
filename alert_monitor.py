from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Alert_Monitor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Alert(db.Model):
    __tablename__ = "ALERT_TABLE"
    AlertId = db.Column(db.Integer, primary_key=True)
    AlertName  = db.Column(db.String(256), index=True)
    AlertStatus = db.Column(db.String(16), index=True)
    AlertMsg = db.Column(db.String(512))
    AlertLevel = db.Column(db.String(16), index=True)
    TriggerTime = db.Column(db.String(16))
    TriggerSource = db.Column(db.String(16), index=True)
    ResponseMsg = db.Column(db.String(512))
    ResponseTime = db.Column(db.String(16))
    UpdatedBy = db.Column(db.String(16), index=True)
db.create_all()


@app.route('/')
def index():
    alerts_print = Alert.query
    return render_template('alert_table.html', title='Alert Monitor',
                           alerts=alerts_print)


if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(host='127.0.0.1', port=5001, debug=False)
