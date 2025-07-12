import os
import logging
from datetime import datetime


# Setup log filename with timestamp
log_filename = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, log_filename)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

