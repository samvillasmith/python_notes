import logging

# Configure logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y - %m - %d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arithmetic App")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} and {b}, result: {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} by {b}, result: {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Division by zero error: {a} / {b}")
        return None

add(5, 10)
divide(10, 0)
divide(10, 2)
logger.info("Application started")