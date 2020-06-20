from pytz import timezone

def to_local(datetime, loc_timezone='Asia/Jakarta'):
    utctz = timezone('UTC')
    loctz = timezone(loc_timezone)

    return utctz.localize(datetime).astimezone(loctz)