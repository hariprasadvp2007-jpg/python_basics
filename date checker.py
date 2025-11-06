from datetime import datetime

def is_valid_date(date_str):
    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")

        start_date = datetime(1900, 1, 1)
        end_date = datetime(2050, 12, 31)

        if start_date <= date <= end_date:
            print(f"{date_str} is a valid date.")
        else:
            print(f"{date_str} is out of valid range (1900-2050).")

    except ValueError:
        print(f"{date_str} is not a valid date format or invalid date")

date_input = input("Enter a date (dd-mm-yyyy) : ")
is_valid_date(date_input)






















