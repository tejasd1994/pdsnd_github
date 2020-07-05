import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
    while True:
        try:
            city = input("Enter the name of the city to analyze \n")
            if city.title() in ["Chicago","New York", "Washington"]:
                print("Thanks for the input , city selected is {}".format(city))
                break
        finally:
            if city.title() in ["Chicago","New York", "Washington"]:
                print("Get ready to choose the month for which data is needed")
            else:
                print("Please enter the city name correctly again")





    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Please enter the specified month for which you need data or all  \n")
            if month.title() in ['January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' ,                                    'November' , 'December', 'All']:
                print("Thanks for the month information, month selected is {}".format(month))
                break
        finally:
            if month.title() in ['January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' ,                                'November' , 'December', 'All']:
                print("Get ready to choose the day of the week")
            else:
                print("The month you choose does not exist, Please try again")




    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:

            day = input("Please enter the specified day for which you need data or select all  \n")
            if day.title() in ['Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday' , 'All']:
                print("Thanks for the day information, day selected is {}".format(day))
                break
        finally:
            if day.title() in ['Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday' , 'All']:
                print("Thanks for the city , month and day data")
            else:
                print("The day you choose does not exist, Please enter again")


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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.title()])

 # convert the Start Time column to datetime
    df['Start Time'] =  pd.to_datetime(df['Start Time'])
 # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # if user selects all then dont use any filters , if user selects any month then use filter

    if month.title() == 'All':
        print('No month filter is applied')
    else:
        # use the index of the months list to get the corresponding int
        dict_m = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6 ,'July' : 7 ,'August' : 8 , 'September' : 9 , 'October' : 10 , 'November' : 11 , 'December' : 12}
        # filter by month to create the new dataframe
        df = df[df.month ==  dict_m[month.title()]]


    # filter by day of week if applicable
    if day.title() == 'All':
        print('No day filter applied')
    else:
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week == day.title()]

    return df





def time_stats(df ,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # if users chooses all months calculate the most popular month and display it
    if month.title() == 'All':
        most_common_month = df['month'].mode()[0]
        #convert month number into month name:
        #iterate through the dictionary and break when y is equal to the most_common_month
        dict_m = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6  ,'July' : 7 ,'August' : 8 , 'September' : 9 , 'October' : 10 , 'November' : 11 , 'December' : 12}
        for x , y in dict_m.items():
            if y == most_common_month:
                break
        print('The most common month is: ' , x)
    else:
        #if the month is equal to other than all then show data for that month only.
        print('Data will be shown for ', month.title())


    # TO DO: display the most common day of week
    if day.title() == 'All':
        most_common_day = df['day_of_week'].mode()[0]
        print('Most common day is: ' , most_common_day)
    else:
        print("Data will be shown for", day.title())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    m_common_hr = df['hour'].mode()[0]
    print('most common hour is : ' , m_common_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_startst = df['Start Station'].value_counts()
    print("most common start station is :", most_common_startst.index[0])

    # TO DO: display most commonly used end station

    most_common_endst = df['End Station'].value_counts()
    print("most common end station is :", most_common_endst.index[0])


    # TO DO: display most frequent combination of start station and end station trip
    freq_comb_station = df['Start Station'] + "--" + df['End Station']
    print('frequent combination of station is : ' , freq_comb_station.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time in minutes is: ', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean of travel time is : ' , mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print('counts of user types \n',user_types_counts)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('counts of gender is ' ,gender_count)
    except:
        print('No data for gender counts for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    #MOST COMMON YEAR OF BIRTH
    try:
        common_year_birth = df['Birth Year'].mode()[0]
        print('Most common birth year is ' , common_year_birth)
    except:
        print('No birth year data for this city')
    #MOST RECENT BIRTH YEAR
    try:
        recent_birth_year = df['Birth Year'].max()
        print('Most recent birth year ' , recent_birth_year)
    except:
        print('No birth year data for this city')
    #MOST EARLIEST BIRTH YEAR
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('Most earliest birth year ' , earliest_birth_year)
    except:
        print('No birth year data for this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        z = 0
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # Ask user for 5 lines of raw data until user says no.
        while z >= 0:
            Answer = input('Would you like to see first 5 lines of raw data,enter yes or no: ')
            if Answer == "yes":
                print(df[z:z+5])
                z = z + 5
            else:
                print("Ok")
                break

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart ? Enter yes or no. \n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
