import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
#asctime -> time
#levelname -> kind of logging
#module -> from where we are logging into file
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  #logs into file
        logging.StreamHandler(sys.stdout)   #logs into terminal
    ]
)

logger = logging.getLogger("textSummarizerLogger")