# Udacity_ND_FS-Project1_Python
## Movie Trailer Website Project for Full Stack Nano Degree at Udacity
Last Update: April 4th 2017

Generate a movie trailer website, where you can find a nice movie library and see trailers for any movie shown there.

## Requirements
Python 2.7.13 installed on your computer.

## Install
Copy “movies”  folder to your computer drive, it must be a place that allows Python to be executed.

## Usage
Go to the movies folder in your computer.
Launch entertainment_center.py from python console or doubleclick it. It depends on how Python is configured on your computer.
A webbrowser is launched where the movie library is shown.

### Adding movies
You can add movies by editing “entertainment_center.py” file.

Make sure you add a movie after the last movie and before the line where it says:
```
# Creates movies Array with the instances created before
```

It’s needed to follow this structure while adding a movie:
```
# Declare Movie instance for <Movie Name> using media class
<movie_name> = media.Movie(“<Movie Name>",
                           “<Storyline for the movie>",
                           “<Movie poster URL>", # NOQA
                           “<YouTube Movie trailer URL>”)
```
Make sure the tabulation is the same as the other movies.

Replace the <> with what it says inside, be aware that <Movie_Name> must be writen using underscores.

Example for Toy Story movie:
```
# Declare Movie instance for Toy Story using media class
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg", # NOQA
                        “https://youtu.be/KYz2wyBy3kc")
```
Then, add the movie in the movies Array declaration, just after the line:
```
# Creates movies Array with the instances created before
```
Adding movie example:
```
# Creates movies Array with the instances created before
movies = [city_of_god, life_of_pi, lord_of_the_rings, star_wars, toy_story, avatar, <movie_name>]
```
Don’t modify anything else.

## Files in folder
Originally the content of the media folder is:

\movies\...
  \entertainment_center.py
  \fresh_tomatoes.py
  \media.py

After executing “entertainment_center.py”, it must generate an HTML file called “fresh_tomatoes.html”, which is the Website showed at the webbrowser while the code is executed.

It also generates Python class files for fresh_tomatoes.py and media.py, with the same name and .pyc extension.

## Author
Marc Codera Campos

Contact
For information, bugs, feature requests, submit patches or other things related to this application:
* e-mail: marc.codera@gmail.com
* e-mail subject: [Movie Trailer Website]YourSubject

