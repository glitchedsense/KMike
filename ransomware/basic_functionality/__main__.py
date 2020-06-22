import logging
from .encrypt_files import start_encryption
from .decrypt_files import start_decryption
from .utils import get_files_to_be_encrypted


logger = logging.getLogger(__name__)

# TODO: Find a better way to store the configuration variables
# TODO: Manual Garbage Collection
# TODO: Add proper logging
# TODO: Add license and Disclaimer


def encrypt_button_handler():
    logger.info("ENCRYPTION STARTED")
    current_directory = "/Users/surya/Desktop/encrypt_test"
    # current_directory = os.path.dirname(os.path.abspath(__file__))
    list_of_files_to_be_encrypted = get_files_to_be_encrypted(current_directory)
    start_encryption(list_of_files_to_be_encrypted)
    logger.info("ENCRYPTION DONE")


def decrypt_button_handler():
    logger.info("DECRYPTION STARTED")
    start_decryption()
    logger.info("DECRYPTION DONE")