import pytz
from datetime import datetime


def convert_est_to_utc(est_time):
    """
    :param est_time: EST time is a datetime object of class --> <class 'datetime.datetime'>
    :return: UTC time
    """
    try:
        utc = pytz.utc
        current_utc = current_est.astimezone(tz=utc)
        return current_utc
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    est = pytz.timezone('US/Eastern')
    current_est = datetime.now(tz=est)
    print(type(current_est))
    UTC_time = convert_est_to_utc(current_est)
    print(UTC_time)
