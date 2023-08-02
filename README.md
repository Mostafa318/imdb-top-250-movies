# imdb-top-250-movies

  In this exercise, we are going to extract the information of the top 250 movies on the imdb website based on their titles. 
  See the titles of these movies from this [link](https://www.imdb.com/chart/top/).
  
This exercise has three different phases, which are:
  
   #### 1- Extracting the required information from the imdb site.
   #### 2- Creating a database and storing information in it using the Python interface.
   #### 3- Create a dashboard to display the required analysis using streamlit.

## First Section 

### After entering the page of each video, you must extract the following information:

    1. Name or title of the movie (title).
    2. Year of release of the movie (year)
    3. Movie age rating (parental_guide)
    4. Duration of the movie in minutes (runtime)
    5. film genre or genres
    6. full name of the director or directors
    7. full name of the author or authors (writer)
    8. full name of the actor or actors (star)
    9. Description of the movie or summary of the movie (storyline)
    10. The amount of movie sales in America and Canada (gross_us_canada)

## Second Section 

  In this section, store the information collected in the previous step after cleaning according to the needs of this section in the form of 6 tables in a database.
  Be careful for this step, you must use sql interfaces in Python and you are not allowed to use sql commands directly.
  The descriptions of each table and its columns are given below:

  #### Movie Table
    This table contains the general information of each movie and includes the following columns:

    1. ID: For movies, you must use the id available on the imdb site.
    2. title
    3. Year of release of the movie (year)
    4. Duration of the movie in minutes (runtime)
    5. The age rating of the movie (parental_guide). You should replace null, blank and Not Rated with the value Unrated.
    6. The amount of movie sales in America and Canada (gross_us_canada). Your output must be stored as a number and must not contain $ and , characters.

  #### Storyline Table
    This table contains summary information for each movie. and includes the following columns:

    1. ID: It is the same ID in the movie table.
    2. Content: The summary of each movie is placed in this column.

  #### Person Table
    This table contains information about all actors, directors and writers and includes the following columns:

    1. ID: It is similar to the ID of movies and should be based on the ID of each person on the imdb site.
    2. Full name of all actors, directors and writers
      *Please note that to fill this table, you do not need to extract all the people on the site and only extract the people who were in the top 250 movies. (as a director, writer or actor)
 
  #### Cast Table
    This table contains information about the actors of each movie and includes the following columns:

    1. ID: This ID should be AUTO_INCREMENT and its initial value should be 1.
    2. Movie ID (movie_id): It is the ID in the movie table.
    3. Person ID (person_id): The ID in the person table.

  #### Crew Table
    This table contains the information of the directors and writers of each film and includes the following columns:

    1. ID: This ID should be AUTO_INCREMENT and its initial value should be 1.
    2. Movie ID (movie_id): It is the ID in the movie table.
    3. Person ID (person_id): The ID in the person table.
    4. Role: This column has Director or Writer values.
  #### Genre Table
    This table stores the genres of each movie and contains the following columns:

    1. ID: This ID should be AUTO_INCREMENT and its initial value should be 1.
    2. Movie ID (movie_id): It is the ID in the movie table.
    3. Genre: Get the genres obtained from the site for each movie. Each movie genre should be stored in a separate line.
  In addition to the above information, you can get help from the following diagram to create a database and connections between tables.
  ![Image of Tables](https://quera.org/qbox/download/dI4ROOnIr5/4.PNG)


## Third Section
  ### First subcategory; Filtering tables

    In this subsection, it is necessary to receive information from the user and place tables on the page based on his interests and wishes.
    Use st.dataframe or st.table to create these tables.
    #### It is mandatory to implement all the things you read below.

    1. The table of movies that have been produced in the time period desired by the user. For example, a table of movies made between 1997 and 2021. The years 1997 and 2021 are entered by the user as desired.
    2. The table of movies whose duration is in the range desired by the user. For example, the table of movies that last between 80 and 120 minutes. The numbers 80 and 120 are chosen by the user.
    3. The table of movies in which the user's favorite actor or actors are present. For example, the table of movies in which Leonardo DiCaprio or Matthew McConaughey played a role.
       Leonardo DiCaprio and Matthew McConaughey don't have to be in the same movie; Simply put the table of movies starring either Leonardo DiCaprio or Matthew McConaughey on the page. User can choose any number of actors.
    4. Table of movies that have a specific genre. The user is only allowed to select one genre (he cannot view movies belonging to different genres in one table.
       There are only movies of one genre in this table. If the user wants to view the table of movies of another genre, it is necessary to select the genre previously had chosen to change, for example,
       the table of movies with the Crime genre, where the user has chosen the Crime genre.

 ### The second subcategory; Static charts

    These types of charts are more analytical and we are not going to take special input from users to display them.

    #### It is mandatory to implement all the things you read below.
    
    1. Bar chart (column chart) of 10 best-selling movies
    2. Bar chart (column chart) of 5 most active actors (number of appearances in all 250 films)
    2. A pie chart of the number of different genres
    3. Pie chart (pie chart) of the number of age ratings of movies
    4. Graph of the number of occurrences of each age grade in each genre. For example,
       different age levels have been seen several times each in the Crime genre (for guidance and ideas, you can look at st.barchart in the presentation files on May 8).

 ### The third subcategory; Interactive charts
    In the third subcategory, we are going to draw a diagram that matches the user's wishes.

    #### It is necessary to implement what you read below.

    1. Place a bar graph (column) of the best-selling movies in the user's chosen genre on the page. For this purpose,
      input the desired genre from the user (only one genre, he cannot choose multiple genres)
      and show him the best-selling movies of that genre in the form of a bar graph.

    
