from datetime import datetime
from dataclasses import dataclass


@dataclass
class Habit:
    name: str
    time_since: str
    remaining_days: str
    minutes_saved: float
    money_saved: str


def track_habit(name: str, start: datetime, cost: float, minutes_used: float) -> Habit:
    """
    Calculates the time elapsed, time remaining, cost, and minutes wasted on a habit.

    :param name: The name of the habit.
    :param start: The start date of the habit.
    :param cost: The cost of the habit per day.
    :param minutes_used: The amount of minutes used performing the habit.
    :return: Habit
    """

    goal: int = 60  # Days
    hourly_wage: int = 30  # Euros

    # Total time elapsed in seconds
    time_elapsed: float = (datetime.now() - start).total_seconds()

    # Convert timestamp into hours/days
    hours: float = round(time_elapsed / 60 / 60, 1)
    days: float = round(hours / 24, 2)

    # Random bonus details
    money_saved: float = cost * days
    minutes_used: float = round(days * minutes_used)
    total_money_saved: str = f'€{round(money_saved + (minutes_used / 60 * hourly_wage), 2)}'

    # Amount of days remaining until you break a habit
    days_to_go: float = round(goal - days)

    # Displayable information
    remaining_days: str = 'Cleared!' if days_to_go <= 0 else f'{days_to_go}'
    time_since: str = f'{days} days' if hours > 72 else f'{hours} hours'

    return Habit(name=name,
                 time_since=time_since,
                 remaining_days=remaining_days,
                 minutes_saved=minutes_used,
                 money_saved=total_money_saved)