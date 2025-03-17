from datetime import datetime

def times():
    #Returns a formatted timestamp.
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")