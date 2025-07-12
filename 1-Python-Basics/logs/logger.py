import logging

# Configure logging to show debug messages
# Configure logging
logger = logging.basicConfig(
    filename = 'app.log',
    filemode = 'w',
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y - %m - %d %H:%M:%S'
)


def add(a, b):
    logging.debug(f"Adding {a} and {b}")
    return a + b

logging.debug("Logger is set up")
result = add(5, 10)
print(f"Result: {result}")