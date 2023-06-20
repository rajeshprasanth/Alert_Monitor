from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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


@app.route('/eventmanager.html')
def eventmanager():
    alerts_print = Alert.query
    now = datetime.now()
    
    # Sunday, May 20, 2023 00:00:00
    #
    #
    current_day_full_text = now.strftime('%A')
    current_month_text = now.strftime('%B')
    current_day = now.strftime('%d')
    
    current_year_full = now.strftime('%Y')
    
    current_second= now.strftime('%S')
    current_minute = now.strftime('%M') 
    current_hour = now.strftime('%H')
    current_timzone = now.strftime('%Z')
    
    dt_string = current_day_full_text + ', ' + current_month_text + ' ' + current_day + ', ' + current_year_full + '   ' + current_hour + ':' + current_minute + ':' + current_second + current_timzone
        
    return render_template('eventmanager_template.html', title='Alert Monitor', alerts=alerts_print, date_string = dt_string)

@app.route('/statistics.html')
def statistics():
    # Sunday, May 20, 2023 00:00:00
    #
    #
    now = datetime.now()
    current_day_full_text = now.strftime('%A')
    current_month_text = now.strftime('%B')
    current_day = now.strftime('%d')
    
    current_year_full = now.strftime('%Y')
    
    current_second= now.strftime('%S')
    current_minute = now.strftime('%M') 
    current_hour = now.strftime('%H')
    current_timzone = now.strftime('%Z')
    
    dt_string = current_day_full_text + ', ' + current_month_text + ' ' + current_day + ', ' + current_year_full + '   ' + current_hour + ':' + current_minute + ':' + current_second + current_timzone
    
    alerts_cnt = {
    "open_tot" : db.session.query(Alert).filter(Alert.AlertStatus == 'Open').count(),
    "open_info" : db.session.query(Alert).filter(Alert.AlertStatus == 'Open').filter(Alert.AlertLevel == 'Information').count(),
    "open_warn" : db.session.query(Alert).filter(Alert.AlertStatus == 'Open').filter(Alert.AlertLevel == 'Warning').count(),
    "open_error" : db.session.query(Alert).filter(Alert.AlertStatus == 'Open').filter(Alert.AlertLevel == 'Error').count(),
    "open_crit" : db.session.query(Alert).filter(Alert.AlertStatus == 'Open').filter(Alert.AlertLevel == 'Critical').count(),
    "pend_tot" : db.session.query(Alert).filter(Alert.AlertStatus == 'Pending').count(),
    "pend_info" : db.session.query(Alert).filter(Alert.AlertStatus == 'Pending').filter(Alert.AlertLevel == 'Information').count(),
    "pend_warn" : db.session.query(Alert).filter(Alert.AlertStatus == 'Pending').filter(Alert.AlertLevel == 'Warning').count(),
    "pend_error" : db.session.query(Alert).filter(Alert.AlertStatus == 'Pending').filter(Alert.AlertLevel == 'Error').count(),
    "pend_crit" : db.session.query(Alert).filter(Alert.AlertStatus == 'Pending').filter(Alert.AlertLevel == 'Critical').count(),
    "close_tot" : db.session.query(Alert).filter(Alert.AlertStatus == 'Closed').count(),
    "close_info" : db.session.query(Alert).filter(Alert.AlertStatus == 'Closed').filter(Alert.AlertLevel == 'Information').count(),
    "close_warn" : db.session.query(Alert).filter(Alert.AlertStatus == 'Closed').filter(Alert.AlertLevel == 'Warning').count(),
    "close_error" : db.session.query(Alert).filter(Alert.AlertStatus == 'Closed').filter(Alert.AlertLevel == 'Error').count(),
    "close_crit" : db.session.query(Alert).filter(Alert.AlertStatus == 'Closed').filter(Alert.AlertLevel == 'Critical').count()
    }
    
    # 
    
    top_5_triggersrc = {}
    top_5_alerts = {}
    top_5_updaters = {}
    
    triggersrc = db.session.execute('''SELECT TriggerSource, count(TriggerSource) FROM ALERT_TABLE GROUP BY TriggerSource ORDER BY count(TriggerSource) DESC LIMIT 5;''')
    alertsname = db.session.execute('''SELECT AlertName, count(AlertName) FROM ALERT_TABLE GROUP BY AlertName ORDER BY count(AlertName) DESC LIMIT 5;''')
    updaters = db.session.execute('''SELECT UpdatedBy, count(UpdatedBy) FROM ALERT_TABLE GROUP BY UpdatedBy ORDER BY count(UpdatedBy) DESC LIMIT 5;''')
    
    for i in triggersrc:
       top_5_triggersrc[i['TriggerSource']] = i["count(TriggerSource)"]
       
    for i in alertsname:
       top_5_alerts[i['AlertName']] = i["count(AlertName)"]
       
    for i in updaters:
       top_5_updaters[i['UpdatedBy']] = i["count(UpdatedBy)"]

    
    top_5_list_keys =[]
    top_5_list_values =[]
    
    for i in range(5):
        try:
            top_5_list_keys.append(list(top_5_triggersrc.keys())[i])
            top_5_list_values.append(list(top_5_triggersrc.values())[i])
        except:
            top_5_list_keys.append("NULL")
            top_5_list_values.append("NULL")
            
    for i in range(5):
        try:
            top_5_list_keys.append(list(top_5_alerts.keys())[i])
            top_5_list_values.append(list(top_5_alerts.values())[i])
        except:
            top_5_list_keys.append("NULL")
            top_5_list_values.append("NULL")
        
    for i in range(5):
        try:
            top_5_list_keys.append(list(top_5_updaters.keys())[i])
            top_5_list_values.append(list(top_5_updaters.values())[i])
        except:
            top_5_list_keys.append("NULL")
            top_5_list_values.append("NULL")
        
    return render_template('statistics_template.html', title='Alert Monitor',date_string = dt_string, alerts_cnt_template = alerts_cnt, top_5_list_temp_keys = top_5_list_keys,top_5_list_temp_values = top_5_list_values )



@app.route('/dashboard.html')
def dashboard():
    alerts_print = Alert.query
    now = datetime.now()
    
    # Sunday, May 20, 2023 00:00:00
    #
    #
    
    current_day_full_text = datetime.now().strftime('%A')
    current_month_text = datetime.now().strftime('%B')
    current_day = datetime.now().strftime('%d')
    
    current_year_full = datetime.now().strftime('%Y')
    
    current_second= datetime.now().strftime('%S')
    current_minute = datetime.now().strftime('%M') 
    current_hour = datetime.now().strftime('%H')
    current_timzone = datetime.now().strftime('%Z')
    
    dt_string = current_day_full_text + ', ' + current_month_text + ' ' + current_day + ', ' + current_year_full + '   ' + current_hour + ':' + current_minute + ':' + current_second + current_timzone
    
    alerts_cnt = {
    "open_tot" : db.session.query(Alert).filter(Alert.AlertStatus == 'Open').count(),
    "open_info" : db.session.query(Alert).filter(Alert.AlertStatus == 'Open').filter(Alert.AlertLevel == 'Information').count(),
    "open_warn" : db.session.query(Alert).filter(Alert.AlertStatus == 'Open').filter(Alert.AlertLevel == 'Warning').count(),
    "open_error" : db.session.query(Alert).filter(Alert.AlertStatus == 'Open').filter(Alert.AlertLevel == 'Error').count(),
    "open_crit" : db.session.query(Alert).filter(Alert.AlertStatus == 'Open').filter(Alert.AlertLevel == 'Critical').count(),
    "pend_tot" : db.session.query(Alert).filter(Alert.AlertStatus == 'Pending').count(),
    "pend_info" : db.session.query(Alert).filter(Alert.AlertStatus == 'Pending').filter(Alert.AlertLevel == 'Information').count(),
    "pend_warn" : db.session.query(Alert).filter(Alert.AlertStatus == 'Pending').filter(Alert.AlertLevel == 'Warning').count(),
    "pend_error" : db.session.query(Alert).filter(Alert.AlertStatus == 'Pending').filter(Alert.AlertLevel == 'Error').count(),
    "pend_crit" : db.session.query(Alert).filter(Alert.AlertStatus == 'Pending').filter(Alert.AlertLevel == 'Critical').count(),
    "close_tot" : db.session.query(Alert).filter(Alert.AlertStatus == 'Closed').count(),
    "close_info" : db.session.query(Alert).filter(Alert.AlertStatus == 'Closed').filter(Alert.AlertLevel == 'Information').count(),
    "close_warn" : db.session.query(Alert).filter(Alert.AlertStatus == 'Closed').filter(Alert.AlertLevel == 'Warning').count(),
    "close_error" : db.session.query(Alert).filter(Alert.AlertStatus == 'Closed').filter(Alert.AlertLevel == 'Error').count(),
    "close_crit" : db.session.query(Alert).filter(Alert.AlertStatus == 'Closed').filter(Alert.AlertLevel == 'Critical').count()
    }
    
    
    return render_template('dashboard_template.html', title='Alert Monitor', date_string = dt_string, alerts_cnt_template = alerts_cnt)

if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(host='127.0.0.1', port=5001, debug=False)
