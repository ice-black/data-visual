## Project Instructions per Task

### Task 1

To create a dictionary using our friend's data, follow these steps:

1. Generate a list of years spanning from 2011 to 2020 and another list containing the average movie lengths provided (103, 101, 99, 100, 100, 95, 95, 96, 93, and 90).

2. Construct a dictionary named `movie_dict` with keys "years" and "durations," assigning your lists of years and durations respectively.

3. Verify the correctness of the dictionary by printing and inspecting its contents.

### Task 2

1. Import the pandas library using its common alias, `pd`.

2. Create a DataFrame named `durations_df` utilizing the `movie_dict` dictionary that you created in the previous step.

3. Print the entire DataFrame for review.

### Task 3

1. Import the `matplotlib.pyplot` library under the alias `plt`.

2. Generate a line plot representing the data. Place the "years" column of the `durations_df` DataFrame on the x-axis and the "durations" column on the y-axis.

3. Enhance the plot by adding a title: "Netflix Movie Durations 2011-2020."

### Task 4

1. Create another DataFrame named `netflix_df` by loading the CSV file provided by our friend. This file is accessible at the path "datasets/netflix_data.csv."

2. Display the first five rows of the DataFrame to confirm successful data loading.

### Task 5

1. Filter the `netflix_df` DataFrame to retain only rows with the type "Movie." Assign the result to a new DataFrame named `netflix_df_movies_only`.

2. Further refine the `netflix_df_movies_only` DataFrame by preserving only the columns: title, country, genre, release_year, and duration. Save this subset as `netflix_movies_col_subset`.

3. Display the initial five rows of `netflix_movies_col_subset`.

### Task 6

1. Utilizing the `netflix_movies_col_subset` DataFrame, construct a scatter plot. Set the release_year on the x-axis and the movie duration on the y-axis.

2. Enhance the scatter plot by including a title: "Movie Duration by Year of Release."

### Task 7

1. From the `netflix_movies_col_subset` DataFrame, create a new DataFrame called `short_movies` by filtering for movies with a duration of fewer than 60 minutes.

2. Display the initial 20 rows of `short_movies` to gain an understanding of the characteristics of movies with shorter durations.

### Task 8

1. Initialize an empty list named `colors` to store different color values.

2. Employ a for loop to iterate through the rows of the `netflix_movies_col_subset` DataFrame. Based on the specified conditions, append colors to the `colors` list as follows:
   - If the genre is "Children," append "red."
   - If the genre is "Documentaries," append "blue."
   - If the genre is "Stand-Up," append "green."
   - For any other genre, append "black."

3. Print the initial 10 values of the `colors` list to review the results.

### Task 9

1. Utilize the data within `netflix_movies_col_subset` to recreate the scatter plot from Task 6. Make the following modifications:
   - Color the scatter plot points using the `colors` list defined in the previous step.
   - Include a title: "Movie Duration by Year of Release."
   - Label the x-axis as "Release year" and the y-axis as "Duration (min)."

2. Display the modified scatter plot.

Feel free to ask if you have any questions or require further assistance with these project instructions.
