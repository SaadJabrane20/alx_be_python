from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("current date and time: ",date)
    return current_date

def calculate_future_date(current_date):
    days_to_add = int(input("Enter number of days : "))
    future_date = current_date + timedelta(days= days_to_add)
    print("Future date: ",future_date.strftime("%Y-%m-%d"))
    return future_date