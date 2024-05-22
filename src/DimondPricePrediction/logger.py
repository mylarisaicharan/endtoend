import logging
import os
from datetime import datetime

# Create a timestamped log filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory path
log_path = os.path.join(os.getcwd(), "logs")

# Create the log directory if it does not exist
os.makedirs(log_path, exist_ok=True)

# Define the complete log file path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    level=logging.INFO, 
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

if __name__=='__main__':
    logging.info("testing")
