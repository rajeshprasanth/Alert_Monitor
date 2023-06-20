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

def delete_alert(AlertId):
    next_alert = {}
    try:
        db = get_db()
        cursor = db.cursor()
        statement = "DELETE FROM ALERT_TABLE WHERE AlertId =?"
        cursor.execute(statement, [AlertId])
        db.commit()
        next_alert = get_by_alertid(int(AlertId)+1)
        
    except:
        db.rollback()
        next_alert = {}
    finally:
        db.close()
        
    return next_alert
    
def delete_all():
    try:
        db = get_db()
        cursor = db.cursor()
        statement = "DELETE FROM ALERT_TABLE"
        cursor.execute(statement)
        db.commit()
        
    except:
        db.rollback()
    finally:
        db.close()
        
    return
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