import logging


# logging.basicConfig(filename = "test.log",
#                     level = logging.DEBUG,
#                     format = "%(asctime)s %(levelname)s %(message)s")


# num1 = int(input("Enter First number: "))
# num2 = int(input("Enter Secongd number: "))

# logging.info(f"User enter two number one is {num1} and another is {num2}")

# try:
#     result = num1/num2
#     print(result)
#     logging.info(f"user got : {result}")

# except Exception as e:
#     print("You can not able to divide any number by zero", e)
#     logging.error("Error has Happened")
#     logging.exception("Exception is" + str(e))




# logging.basicConfig(filename = "log.log",
#                     level = logging.DEBUG,
#                     format = "%(asctime)s %(levelname)s %(message)s %(filename)s %(lineno)d %(name)s")
# logging.debug("This is Debug Message")
# logging.info("This is info")
# logging.warning("Warning message")


# import logging

# logging.basicConfig(
#     filename= "server.log",
#     level = logging.INFO,
#     format= "%(asctime)s - %(levelname)s - %(message)s"

# )

# def login(user):
#     logging.info(f"{user} logged in")

# def error_test():
#     try:
#         1/0
#     except:
#         logging.exception("Crash!")

# login("Masum")
# error_test()



# ##1

# import logging

# logging.basicConfig(filename ="info.log", level = logging.INFO)
# logging.info("Program started")



# ##2.


# import logging

# logging.basicConfig(filename ="info.log", level = logging.WARNING)

# logging.warning("Low disk space")
# logging.error("File not found")



# ##3.

# import logging

# logging.basicConfig(filename ="info.log", level = logging.INFO,
#                     format = "%(levelname)s - %(message)s")
# logging.info("User logged in")


# ##4.

# import logging

# logging.basicConfig(filename= "appl.log", level=logging.INFO)
# logging.info("Saved Successfully")


##5.

import logging

# logging.basicConfig(filename= "appl.log", level=logging.ERROR)
# try:
#     10 / 0
# except Exception:
#     logging.exception("Division failed")


# logging.basicConfig(
#     level=logging.INFO,
#     format = "%(name)s - %(levelname)s - %(message)s"
# )

# logger = logging.getLogger("my_app")
# logger.info("App started")

# print(logging.getLogger().name)

# logger = logging.getLogger("my_app")


# logger = logging.getLogger("my_app")
# logger.setLevel(logging.INFO)

# logger.info("App start")
# logger.error("Problem found")



# logger = logging.getLogger("my_app")
# logger.setLevel(logging.INFO)


# console = logging.StreamHandler()
# logger.addHandler(console)

# logger.info("App start")
# logger.error("Problem found")


# logging.basicConfig(level=logging.INFO)

# logging.info("App start")
# logging.error("Problem found")



# logger = logging.getLogger("login")

# logger.setLevel(logging.INFO)


# logger.info("User login Success")
# logger.error("Password wrong")


# logging.basicConfig(level=logging.INFO)

# login = logging.getLogger("login")
# payment = logging.getLogger("payment")
# profile = logging.getLogger("profile")


# login.info("User login")
# payment.error("Payment fail")
# profile.info("Profile update")




# ##1.

# import logging

# logging.basicConfig(level = logging.DEBUG)

# bank = logging.getLogger("bank")

# bank.info("User opened app")
# bank.warning("Suspicious login attempt")
# bank.error("Transaction failed")
# bank.info("User logged out")


# ##2.

# import logging

# logging.basicConfig(level= logging.DEBUG)

# food = logging.getLogger("food")
# delivery = logging.getLogger("delivery")


# food.info("Order received")
# food.warning("Item out of stock")

# delivery.info("Rider assigned")
# delivery.warning("Address not found")



# logging.basicConfig(
#     filename="apps.log",
#     level = logging.INFO,
#     format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )

# logger = logging.getLogger("apps")
# logger.info("App started")
# logger.error("Something wrong")




import logging


logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler("appl.log")

console_handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Application started")

