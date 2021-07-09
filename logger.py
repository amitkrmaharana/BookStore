import logging

logging.basicConfig(filename='book_store_errors.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)
