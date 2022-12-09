from datetime import datetime as date
from dateutil import relativedelta


def get_age(birthday):
    """
    Returns the length of time since I was born
    e.g. 'XX years, XX months, XX days'
    """

    def format_plural(unit):
        """
        Returns a properly formatted number
        e.g.
        'day' + format_plural(diff.days) == 5
        >>> '5 days'
        'day' + format_plural(diff.days) == 1
        >>> '1 day'
        """
        return "s" if unit != 1 else ""

    diff = relativedelta.relativedelta(date.today(), birthday)
    return "{} {}, {} {}, {} {}".format(
        diff.years,
        "year" + format_plural(diff.years),
        diff.months,
        "month" + format_plural(diff.months),
        diff.days,
        "day" + format_plural(diff.days),
    )


with open("README.md", "r", encoding="utf-8") as file:
    data = file.readlines()

data[28] = f"  Uptime: {get_age(date(2002, 10, 2))}\n"

with open("README.md", "w", encoding="utf-8") as file:
    file.writelines(data)
