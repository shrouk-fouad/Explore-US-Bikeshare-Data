import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

for city in CITY_DATA : 
    pd.read_csv(CITY_DATA[city]).dropna(inplace=True)

name = input("what is your name? ")

cities = ('chicago','new york city','washington')

months_list = ['january', 'february', 'mars', 'april', 'may', 'june', 'all']

days_list = ['monday', 'tuseday', 'wednesday', 'thursday', 'friday','saturday', 'sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print(f'Hello {name}! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city =input("Choose which city you want to display its data : chicago, new york city, washington :\n").lower()
        if city in cities :
            break
        else:
            print("please choose correct answer")

    # get user input for month (all, january, february, ... , june)
    while True: 
        month = input("choose what month you want to display its data or 'all' if you want all months \n'january', 'february', 'mars', 'april', 'may', 'june' : \n").strip().lower()
        if month in months_list:
            break
        else : 
            print("please choose correct answer")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("choose what day you want to display its data or 'all' if you want all days\n 'monday', 'tuseday', 'wednesday', 'thursday', 'friday','saturday', 'sunday': \n").strip().lower()
        if day in days_list:
            break
        else:
            print("please choose correct answer")

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_of_week
    df['hour'] = df['Start Time'].dt.hour
   

    if month != 'all':
        month = months_list.index(month) +1
        df = df[df['month'] == month]
        print(f"Data is filterd according to chosen month : {month}")
    if day != 'all':
        day = days_list.index(day) +1
        df = df[df['day'] == day]
        print(f"Data is filterd according to chosen day : {day}")
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most common month of travel is : {common_month}")
    

    # display the most common day of week
    common_day = df['day'].mode()[0]
    print(f"Most common day of travel is : {common_day}")

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print(f"Most common hour of travel is : {common_hour}:00 ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"most common start station is  : {common_start_station}")

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"most common end station is  : {common_end_station}")

    # display most frequent combination of start station and end station trip
    trip_road =  df['Start Station'] +' to '+ df['End Station']
    frequent_trip_road = trip_road.mode()[0]
    print(f"most frequent road of trips is: from {frequent_trip_road}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time is : {total_travel_time} mins")

    # display mean travel time
    avg_travel_time = int(df['Trip Duration'].mean())
    print(f"Total travel time is : {avg_travel_time} mins")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_of_users_type = df['User Type'].value_counts()
    print(f"Counts of user types : \n {count_of_users_type}\n")

    # Display counts of gender
    if city == 'washington':
        print("sorry, counts of gender for this city is not available")
    else : 
        count_of_gender = df['Gender'].value_counts()
        print(f"Counts of gender is : \n {count_of_gender}\n")

    # Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print("sorry, birth year information for this city is not available")
    else : 
        earliest_BY = int(df['Birth Year'].min())
        print(f">Earliest birth year is : {earliest_BY}")

        most_recent_BY = int(df['Birth Year'].max())
        print(f">Most recent birth year is : {most_recent_BY}")

        most_common_BY = int(df['Birth Year'].mode()[0])
        print(f">Most common birth year is : {most_common_BY}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data():
    df = pd.read_csv(CITY_DATA[city])
    str_row = 1
    while True:
        answer = input("Do you want to display 5 lines of raw data? Yes / No :").strip().lower() 
        if answer == 'yes':
            print(df.iloc[str_row:str_row+5])
            str_row += 5 
        elif answer == 'no':
            print(f"We hope this information was useful for you {name})")
            break
        else :
            print("please enter correct answer")

    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
