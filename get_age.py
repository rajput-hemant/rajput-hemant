from datetime import datetime as date


def get_age(birthday):
    duration = (date.now() - birthday).total_seconds()

    def get_years():
        return divmod(duration, 31557600)  # a year = 31557600 seconds

    def get_months(seconds):
        return divmod(seconds, 2629800)  # a month = 2629800 seconds

    def get_days(seconds):
        return divmod(seconds, 86400)  # a day = 86400 seconds

    def total_duration():
        years = get_years()
        months = get_months(years[1])
        days = get_days(months[1])

        return [int(years[0]), int(months[0]), int(days[0])]

    age = total_duration()

    return f"{age[0]} years, {age[1]} months, {age[2]} days"


with open("README.md", "r", encoding="utf-8") as file:
    data = file.readlines()

data[28] = f"  Uptime: {get_age(date(2002, 10, 2))}\n"

with open("README.md", "w", encoding="utf-8") as file:
    file.writelines(data)
