import requests
from datetime import datetime
import random

url_post = 'http://127.0.0.1:5000/api/alerts/insert'
url_put = 'http://127.0.0.1:5000/api/alerts/update'
url_get = 'http://127.0.0.1:5000/api/alerts'
#
alert_name = ["QES000_0000_STEP_0","QES000_0010_STEP_1","QES000_0020_STEP_2","QES000_0030_STEP_3","QES000_0040_STEP_4","QES000_0050_STEP_5"]
alert_status = ["Open","Pending","Closed"]
alert_level = ["Information","Warning","Error","Critical"]
trigger_src = ["python-api","console","airflow-prod","pbs-queue","jobsubmit","PW.X"]
alert_msg = ["disk full","Job Completed","Job started","Job completed abnormally", "Job running longer than expected time"]
response_msg = ["fixed","fixed by itself","work in progress","progress"]
updated = ["python-api","console","airflow-prod","pbs-queue","jobsubmit"]



def insert_alert():

    for iter in range(50):
        
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        time = now.strftime("%H:%M:%S")
        date_time = now.strftime("%m/%d/%Y %H:%M:%S")
            

        data = {
        "AlertName" : random.choice(alert_name),
        "AlertStatus" : "Open",
        "AlertMsg" : random.choice(alert_msg),
        "AlertLevel" : random.choice(alert_level),
        "TriggerTime" : date_time,
        "TriggerSource" : random.choice(trigger_src)
        }

        response = requests.post(url_post, json=data)
        if response.status_code == 200:
            print("Message from insert_alert POST %d : OK" % (response.status_code))
        else:
            print("Message from insert_alert POST %d : Failed" % (response.status_code))

def pending_alert():
    for iter in range(50):
        now1 = datetime.now()
        date_time = now1.strftime("%m/%d/%Y %H:%M:%S")
        
        
        data1 = { 
        "ResponseMSG":random.choice(response_msg),
        "ResponseTime":date_time,
        "UpdatedBy":random.choice(updated),
        "AlertStatus":"Pending",
        "AlertId":random.randint(1,100)
        }
        
        
        response = requests.put(url_put, json=data1)
        if response.status_code == 200:
            print("Message from pending_alert PUT %d : OK" % (response.status_code))
        else:
            print("Message from pending_alert PUT %d : Failed" % (response.status_code))
            
            

def close_alert():
    for iter in range(50):
        now2 = datetime.now()
        date_time = now2.strftime("%m/%d/%Y %H:%M:%S")
        
        
        data1 = { 
        "ResponseMSG":random.choice(response_msg),
        "ResponseTime":date_time,
        "UpdatedBy":random.choice(updated),
        "AlertStatus":"Closed",
        "AlertId":random.randint(1,1000)
        }
        
        response = requests.put(url_put, json=data1)
        if response.status_code == 200:
            print("Message from close_alert PUT %d : OK" % (response.status_code))
        else:
            print("Message from close_alert PUT %d : Failed" % (response.status_code))
            


insert_alert()
pending_alert()
close_alert()