# Organization:

* Find a pair for yourself.
* Work on this assignment together with your pair. Both students should clone the repository and create your local repository 'development'.
If one student creates it, let the other student work on the same upstream remote.
Any information exchange between students should be done only through GIT this time.
Call the file "Solution_Pandas_hw1.ipynb". Only work commonly on this same file.

* The formatting should be such that before every code cell, you have a Markdown cell that describes what sub-step you are solving.
Every time you start working on this assignment, first GIT pull the changes from remote and merge them. If you agree with your pair's work, retain them, otherwise change.
Good way can be to use [Jupyter over Pycharm](https://www.jetbrains.com/help/pycharm/editing-jupyter-notebook-files.html) because Pycharm integrates natively with GIT and it is very good for resolving `Merge` conflicts.
If you get there, explore `Resolve conflicts` tab under `VCS` in Pycharm.
* What to do : First Complete these mini-tasks outlined here with your pair communicating your code only through GIT pull/Git merge.
* What to do (2): Write 5 things what you found useful from the Kaggle Kernel
https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python
* What to do (3): Describe in 15 sentences what can be done in Pandas (exclude trivial statements like "read in data" etc, please be specific).
This part you can write together (no GIT merge-pull needed)
* If you are ready, please send your assignment to the group on the pair paper that comes after your group. The last group should send the assignment to the first group.
Please only send the link to your GITHUB repository.


## Basic info

Read the data-file (a 10 000 row subset of most rated IMDB-movies) into Pandas DataFrame and name the DataFrame-variable to `df` (use tab-character (`\t`) as the separator)

1. Use the following column-names: `ID, title, year, rating, votes, duration, genres`
2. Index the `df` with `ID`-column (either on reading the file or after it.)
3. Display first 5 rows of the `df`
4. Display last 11 rows of the `df`
5. Display the `df`-info


## Cleaning

1. Drop all the missing rows which contain _any_ column with missing data
2. Convert the `duration` column to numerical representation of seconds
3. Remove the year from `title` column


## Concatenating

1. Read `crew_data.tsv.gz` to DataFrame named `movie_crew_df` with columns `ID, director_ids` indexed by `ID` (forget the rest of the columns)
2. Read `person_data.tsv.gz` to DataFrame named `person_df` with columns `person_ID, name` indexed by `person_ID` (forget the rest of the columns)
3. Merge `movie_crew_df` into `df` with `ID`s and drop the columns without necessary data (hint `outer`-join)
4. Remove movies with more than one director and rename `director_ids` => `director_id`
5. Merge `df` with `person_df` on `director_id`, remove `director_id` and `person_ID` columns, rename `name` => `director`

## Exploration

1. Find ten most longest movies
2. Find Best rated movies ordered by rating DESC and Title ASC
3. What is the average duration (in minutes) of a movie?
4. Get ten most productive directors
5. How many movie has been made in the 2000's?
6. Get all the movies directed by Akira Kurosawa ordered by year DESC
