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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("pls enter the city u want :)---> ").lower()
    while city not in (['chicago','new york city','washington']):
        print("ooops , wrong city name pls try again :)")
        city=input("pls enter the city u want :)---> ").lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("pls enter a valid month : ").lower()
    while month not in (['january','february','march','april','may','june']):
        print("re enter the month :(")
        month = input("provide the input here -----> : ").lower()
     
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("pls enter the day : ").lower()
    while day not in (['saturday','sunday','monday','tuesday','wednesday','thursday','friday']):
        print("re enter the month :(")
        day = input("provide the valid  day here pls -----> : ").lower()
    
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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
    



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # because the month data it self in the original data works with the number of the month , i've to do the next 2 steps 
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]
    print("the most common month is : ".format(months[common_month - 1]))

    # TO DO: display the most common day of week
    print("the most common week is : ".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("the most common hour is : ".format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most common start station is : ".format(df['Start Station'].mode()[0]))
    


    # TO DO: display most commonly used end station
    print("the most common end station is : ".format(df['End Station'].mode()[0]))
    
    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'] + ' to ' + df['End Station']
    print(f'The most popular trip is: from {popular_trip.mode()[0]}')
 
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('the Total Travel Time : {}'.format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('the Mean Travel Time : {}'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("count of users : {}".format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print(df['Gender'].value_counts())
   
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        print("earliest year of birth {} ".format(df['Birth_Year'].min()))
        print("recent year of birth {} ".format(df['Birth_Year'].max()))
        print("the most common year of birth {} ".format(df['Birth Year'].mode()[0]))    
    else : print("There is no birth year information in this city.")
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):
    
    """
    Displays 5 rows of data or more for the selected city.
    Args:
        parameter (df): The data frame .
    Returns:
        it just print's the data .
    """
    raw_data = 0
    while 1:
        choice = input("Do you want to see 5 raw data? Yes or No  ").lower()
        if choice not in ['yes', 'no']:
            choice = input("You wrote the wrong word. Please type Yes or No.  ").lower()
    
        elif choice == 'yes':
            print(df.iloc[raw_data : raw_data + 5])
            raw_data += 5   
        else :break
            
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
