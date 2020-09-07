import logging

logger = logging.getLogger(__name__)


class GPIO:
    BCM = "bcm"

    IN = "in"
    OUT = "out"

    @classmethod
    def setmode(cls, a):
        logger.info("[GPIO.setmode] Mode is set to {}".format(a))

    @classmethod
    def setup(cls, a, b):
        logger.info("[GPIO.setup] {} is set to {}".format(a, b))

    @classmethod
    def output(cls, a, b):
        logger.info("[GPIO.output] {} is set to {}".format(a, b))


GPIO = GPIO()
