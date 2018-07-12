# Project 1

File summary: Appliation.py handles all of the functions as follows:
-- def index() renders the login.html

-- def registration renders the registration.html

-- def /on_registration checks to see if the registered username is taken and, if not, stores registration information to the user_login table

-- def Logged_in checks to see if username and password match and, if so, renders main.html

-- def search_location is the main function for main.html; it searchers the zip_data table for a location or zipcode (and should throw an error if
you are not logged in, but I haven't quite figured out how to do that...)

-- search_location/location_id renders either location_info.html or location_info_noform.html (depenidng on if a user has checked-in to a location before);
both those html pages include location information from the zip_data table and also current weather information from the Dark Sky API. Location_info.html
has a way to check-in and make comments, while location_info_noform.html removes that form.

-- def location_api(lookup_zipcode) provides a JSON version of the zip_data table based on a location's ID

-- def logout logs the user out

-- def main let's anyone search for a location without being logged in.

import.py is a simple CSV-to-SQL importer for zip code data, and all the various html templates are in the main template folder (all extended from
layout.html, which includes the Bootstrap CSS and header). The database templates are in the weather_database sql file.

Overall, working on this project was really rewarding; I really struggled at first, but I eventually got things to work after many hours
of practice -- programming can be quite rewarding!

One requirement I had some issue with was requiring users to be logged in; I have sessions set correctly (I think) so I know if someone is
logged in and logging out works. What I am not quite clear on is how to track that someone is not logged in -- I tried to cover it
with a try/except clause (see the search_location function), but no success and seeing if the session['user'] varialbe is set to false
also didn't work. Thoughts on how I should implement this functionality?

I like my solution for only letting them comment one: I render different HTML pages (one with the check-in form and one without) if their
Username and Location ID match in the comments database!

I did a bit of CSS styling (imported Bootstrap and customized error messages), but since I was a bit time crunched working on this project I
didn't make it look too "pretty" -- definitely could improve more on that.

Also, small thing, but I called my API address ("/api/zipcode/<lookup_zipcode>") instead of the required ("/api/zipcode/<lzip>")
because "zip" seems to have a specific meaning in Python and I didn't want to accidentally cause any errors.

All comments deeply appreciated -- I am taking this course to learn! :)




