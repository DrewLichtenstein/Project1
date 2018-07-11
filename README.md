# Project 1

Overall, working on this project was really rewarding; I really struggled at first, but I eventually got things to work after many hours
of practice -- programming can be quite rewarding!

One requirement I couldn't quite figure out how to successfully implement the %LIKE% operator in SQL with variables -- I tried several
different iteration but can't seem to get the syntax to work. I left my last attempt in as a comment (it's in the search_location
function) and any suggestions on how to get it to work would be appreciated! As a result, my search result requires a specific location
to work.

Another thing I had some issue with was requiring users to be logged in; I have sessions set correctly (I think) so I know if someone is
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




