from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return formatted_date
def calculate_future_date(days):
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Date after {days} days: {formatted_future_date}")
    return formatted_future_date

def main():
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)
if __name__ == "__main__":
    main()