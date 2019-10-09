import  logging 


# create and configure logger 


LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename= "/home/awyoonisj/leetCode/loggin_messages.log", level= logging.DEBUG, format=LOG_FORMAT, filemode="w" )



logger= logging.getLogger()
logger.info("our first message")
logger.debug("this is hamless message")
logger.warning("I am sorry but you can not do that sir!")
logger.error("this is an error in the code sxb")
logger.critical("the entire servers are down")

print(logger.level)





def calculate_quadratic(a, b, c):
    pass  
