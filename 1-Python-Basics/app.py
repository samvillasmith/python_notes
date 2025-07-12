import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y - %m - %d %H:%M:%S',
    handlers = [
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithmeticApp')

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(10, 15)
multiply(15, 10)
divide(20, 0)
