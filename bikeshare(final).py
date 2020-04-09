import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO(done): get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
def get(city):
    try:
        city = input("Enter city (chicago, new york city, washington): ")
    except ValueError: 
        print("That is not a valid input!")
    # TO DO(done): get user input for month (all, january, february, ... , june)
def get(month):
    try:
        month = input("Enter month (all, january, february,..., june): ")
    except ValueError: 
        print("That is not a valid input!")
    # TO DO(done): get user input for day of week (all, monday, tuesday, ... sunday)
def get(day):
    try:
        weekday = input("Enter day of week (all, monday, tuesday, ... sunday): ")
    except ValueError: 
        print("That is not a valid input!")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO (done/iO): display the most common month
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    popular_month = df['month'].mode()[0]
    print("the most common month is", popular_month)

    # TO DO (done/iO): display the most common day of week
    df['weekday'] = pd.to_datetime(df['Start Time']).dt.weekday_name
    popular_weekday = df['weekday'].mode()[0]
    print("the most common day of week is", popular_weekday)

    # TO DO (done/iO): display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    popular_hour = df['hour'].mode()[0]
    print("the most common start hour: ", popular_hour, "of the clock")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO (done/iO): display most commonly used start station
    df['StartStation'] = pd.DataFrame(df,columns=['Start Station'])
    StartStation = df['StartStation'].value_counts().idxmax()
    print("most commonly used start station is:", StartStation)

    # TO DO (done/iO): display most commonly used end station
    df['EndStation'] = pd.DataFrame(df,columns=['End Station'])
    EndStation = df['EndStation'].value_counts().idxmax()
    print("most commonly used end station is:", EndStation)    

    # TO DO (done/iO): display most frequent combination of start station and end station trip
    StationComb = df['Start Station'] + " --> " + df['End Station']
    StationComb = StationComb.value_counts().idxmax()
    print("most frequent combination of start station and end station is:", StationComb)      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO (done/iO): display total travel time
    TTT = sum(df['Trip Duration'])
    TTT = TTT / 3600
    print("the total travel time is ", TTT, " hours")

    # TO DO (done/iO): display mean travel time
    drives = df['Trip Duration'].shape[0]
    MTT = (TTT / drives)*60
    print("the mean travel time is ", int(MTT), " minutes for", drives , "journeys")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO (done/iO): Display counts of user types
    df['usertype'] = pd.DataFrame(df,columns = ['User Type'])
    user_types = df['usertype'].value_counts()
    print("Display of counts of user types", "\n", user_types)

    # TO DO (done/iO): Display counts of gender
    df['gender'] = pd.DataFrame(df,columns = ['Gender'])
    user_gender = df['gender'].value_counts()
    print("Display of counts of gender types", "\n", user_gender)

    # TO DO (done/iO): Display earliest, most recent, and most common year of birth
    df['yob'] = pd.DataFrame(df,columns = ['Birth Year'])
    user_birth = df['yob'].value_counts().idxmax()
    user_birth_min = df['yob'].min()
    user_birth_max = df['yob'].max()
    print("The most common year of birth is: ", user_birth, "\n", "The most recent year of birth is: ", user_birth_max, "\n","The earliest year of birth is: ", user_birth_min, "\n",)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
#if you found any misstakes or have better lines of code - please provide the solutions and tips via mail to faas.fabian@t-online.de