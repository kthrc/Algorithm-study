from datetime import datetime
def solution(a, b):
    
    date = datetime(2016,a,b)
    day = datetime.weekday(date)
    day_list = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    
    return day_list[day]