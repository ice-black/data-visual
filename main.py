color_data_set = 'C:/Users/HEZRON WEKESA/Desktop/carl/datasets/color_data.csv'

# Task 1

# Create the years and durations lists
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = {"years": [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020], "durations": [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]}

# Print the dictionary
print(movie_dict)

# Task 2
import pandas as pd

# Creating a DataFrame
durations_df = pd.DataFrame(movie_dict)
print(durations_df)

# Task 3
import matplotlib.pyplot as plt

plt.plot(durations_df['years'], durations_df['durations'], marker='o', linestyle='-')
plt.xlabel('years')
plt.ylabel('durations')
plt.title('Netflix Movie Durations 2011-2020')
plt.show()

# Task 4

netflix_data_set = 'C:/Users/HEZRON WEKESA/Desktop/carl/datasets/netflix_data.csv'
netflix_data_set = pd.read_csv(netflix_data_set)
print(netflix_data_set.head(5))

# Task 5

# Subset the DataFrame to keep only rows where type is "Movie"
netflix_df_movies_only = netflix_data_set[netflix_data_set['type'] == 'Movie']

# List of columns to keep
columns_to_keep = ['title', 'country', 'genre', 'release_year', 'duration']

# Subset the DataFrame to keep only specified columns
netflix_movies_col_subset = netflix_df_movies_only[columns_to_keep]

print(netflix_movies_col_subset.head(5))

# Task 6

# Create a scatter plot
plt.figure(figsize=(10, 6))  # Set the figure size
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'], color='blue', alpha=0.5)
plt.title("Movie Duration by Year of Release")  # Add a title
plt.xlabel("Release Year")  # Label for x-axis
plt.ylabel("Movie Duration (minutes)")  # Label for y-axis
plt.grid(True)  # Add grid lines
plt.show()  # Display the plot

# Task 7

# Subset to create short_movies DataFrame
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]

# Print the first 20 rows of short_movies
print(short_movies.head(20))

# Task 8

# Initialize an empty list called colors
colors = []

# Iterate through the netflix_movies_col_subset DataFrame's rows
for index, row in netflix_movies_col_subset.iterrows():
    # Append colors based on genre conditions
    if row['genre'] == 'Children':
        colors.append('red')
    elif row['genre'] == 'Documentaries':
        colors.append('blue')
    elif row['genre'] == 'Stand-Up':
        colors.append('green')
    else:
        colors.append('black')

# Print the first 10 values of the colors list
print(colors[:10])

# Task 9

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'], c=colors, alpha=0.5)
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release Year")
plt.ylabel("Duration (min)")
plt.grid(True)
plt.show()

# Task 10

print("Yes")
