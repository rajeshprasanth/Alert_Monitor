from flask import Flask, jsonify, request
import alert_controller
from db import create_tables

app = Flask(__name__)


@app.route("/api/alerts/insert", methods=["POST"])
def insert_alert():
    alert_details = request.get_json()
    AlertName = alert_details["AlertName"]
    AlertStatus = alert_details["AlertStatus"]
    AlertMsg = alert_details["AlertMsg"]
    AlertLevel = alert_details["AlertLevel"]
    TriggerTime = alert_details["TriggerTime"]
    TriggerSource = alert_details["TriggerSource"]
   
    result = alert_controller.insert_alert(AlertName,AlertStatus,AlertMsg,AlertLevel,TriggerTime,TriggerSource)
    return jsonify(result)


@app.route("/api/alerts/update", methods=["PUT"])
def update_alert():
    alert_details = request.get_json()
    ResponseMSG = alert_details["ResponseMSG"]
    ResponseTime = alert_details["ResponseTime"]
    UpdatedBy = alert_details["UpdatedBy"]
    AlertStatus = alert_details["AlertStatus"]
    AlertId = alert_details["AlertId"]
    result = alert_controller.update_alert(ResponseMSG,ResponseTime, UpdatedBy, AlertStatus,AlertId)
    return jsonify(result)
    
@app.route("/api/alerts/delete", methods=["DELETE"])
def delete_alert():
    alert_details = request.get_json()
    AlertId = alert_details["AlertId"]
    result = alert_controller.delete_alert(AlertId)
    return jsonify(result)
    
    
@app.route("/api/alerts/delete/all", methods=["DELETE"])
def delete_all():
    alert_details = request.get_json()
    result = alert_controller.delete_all()
    return jsonify(result)

@app.route('/api/alerts', methods=["GET"])
def get_alerts():
    alerts = alert_controller.get_alerts()
    return jsonify(alerts)


@app.route("/api/alerts/<AlertId>", methods=["GET"])
def get_alert_by_alertid(AlertId):
    alert = alert_controller.get_by_alertid(AlertId)
    return jsonify(alert)


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='127.0.0.1', port=5000, debug=False)