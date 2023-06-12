import sqlite3
DATABASE_NAME = "Alert_Monitor.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = """
        CREATE TABLE IF NOT EXISTS ALERT_TABLE ( AlertId INTEGER PRIMARY KEY AUTOINCREMENT, -- Job Id
                                                AlertName VARCHAR(256) NOT NULL, -- Job name
                                                AlertStatus  VARCHAR(16) NOT NULL, -- Alert Status : Open, Closed, Acknowledged
                                                AlertMsg  VARCHAR(1024) NOT NULL, -- Alert Messages
                                                AlertLevel  VARCHAR(16) NOT NULL, -- Alert Level : Information, Warning, Error, Critical
                                                TriggerTime VARCHAR(16) NOT NULL, -- Time at which alert is triggered
                                                TriggerSource VARCHAR(16) NOT NULL, -- Source that triggered the alert
                                                ResponseMsg VARCHAR(1024) NULL, -- Response Message
                                                ResponseTime VARCHAR(16) NULL, -- Time at which Response is posted
                                                UpdatedBy VARCHAR(16) NULL-- User who updated the Response
                                               );
            """
    db = get_db()
    cursor = db.cursor()
    cursor.execute(tables)
        
        
        
        
create_tables()