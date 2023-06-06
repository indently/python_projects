import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit


def main():
    # Habits
    habits: list[Habit] = [
        track_habit('Coffee', datetime(2023, 6, 3), cost=1, minutes_used=5),
        track_habit('Alcohol', datetime(2023, 6, 5, 22), cost=5, minutes_used=15),
        track_habit('Sugar drinks', datetime(2023, 5, 16, 19), cost=1, minutes_used=3),
        track_habit('Being lazy', datetime(2021, 1, 1, 10), cost=1, minutes_used=3),
    ]

    # Creates a Dataframe
    df = pd.DataFrame(habits)

    # Create a nice table
    print(tabulate(df, headers='keys', tablefmt='psql'))


if __name__ == '__main__':
    main()
