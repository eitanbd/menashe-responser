import json 
import requests
import datetime
import time
import os
import logging
import poller_responser

dir_path = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(filename=os.path.join(dir_path , 'appLog.log'), format='%(levelname)s:%(message)s',level=logging.INFO)
logging.info('Log file created. first app log')

poller_responser.main()

     
