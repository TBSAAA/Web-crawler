from datetime import datetime, timedelta
import time

currentDateAndTime = datetime.now()


# currentDateAndTime = currentDateAndTime.strftime("%Y/%m/%d")
# print("The current date and time is", currentDateAndTime)


# print (datetime.now()+timedelta(days=-1))
# number_of_pagination =int(327653)/20 + 1
# print("image".format(time.time()))
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    str1 = '1'

    str2 = '64.5'

    str3 = '都撒到'

    str4 = '–'

    print(is_number(str1))

    print(is_number(str2))

    print(is_number(str3))

    print(is_number(str4))

    print(float(str2))
