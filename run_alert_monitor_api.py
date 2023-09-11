#---------------------------------------------------------------------------------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the 
# Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or 
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
#---------------------------------------------------------------------------------------------------------------------------------------------
from apps.config.config import Config
from apps.api import create_app
import sys
import logging
from art import *
from os import getpid
#
app = create_app(Config)
#
logging.basicConfig(filename='./logs/run_api.log', filemode='w', format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)
#
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
#
if __name__ == "__main__":
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    fh=open("./pids/alert_monitor_api.pid", "w")
    fh.write(str(getpid()))
    fh.close()
    print(text2art("Alert Monitor - API", font="small"))
    app.run(host=Config.API_HOST_ADDRESS, port=Config.API_PORT_NUMBER, debug=False)