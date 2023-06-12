from db import get_db


def insert_alert(AlertName,AlertStatus,AlertMsg,AlertLevel,TriggerTime,TriggerSource):
    created_alert = {}
    
    try:
        db = get_db()
        cursor = db.cursor()
        statement = "INSERT INTO ALERT_TABLE (AlertName,AlertStatus,AlertMsg,AlertLevel,TriggerTime,TriggerSource) VALUES (?,?,?,?,?,?)"
        cursor.execute(statement, [AlertName,AlertStatus,AlertMsg,AlertLevel,TriggerTime,TriggerSource])
        db.commit()
        created_alert = get_by_alertid(cursor.lastrowid)
        
    except:
        db.rollback()
    finally:
        db.close()
        
    return created_alert


def update_alert(ResponseMSG,ResponseTime, UpdatedBy, AlertStatus,AlertId):
    updated_alert = {}
    try:
        db = get_db()
        cursor = db.cursor()
        statement = "UPDATE ALERT_TABLE SET ResponseMSG = ?, ResponseTime = ?, UpdatedBy = ?, AlertStatus = ? WHERE AlertId =?"
        cursor.execute(statement, [ResponseMSG,ResponseTime, UpdatedBy, AlertStatus,AlertId])
        db.commit()
        updated_alert = get_by_alertid(AlertId)
        
    except:
        db.rollback()
        updated_alert = {}
    finally:
        db.close()
        
    return updated_alert
    
    
#------------------------------
# Method to get all the alerts.
#------------------------------
def get_alerts():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM ALERT_TABLE"
    cursor.execute(query)
    return cursor.fetchall()

#------------------------------
# Method to get all the alerts by AlertId.
#------------------------------
def get_by_alertid(AlertId):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM ALERT_TABLE WHERE AlertId = ?"
    cursor.execute(statement, [AlertId])
    return cursor.fetchone()