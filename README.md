# Top-100-Billboard-Playlists
Create, by date input, an ordered playlist of the top 100 billboard songs of that day

Needs:
1. Libraries
  a. datetime
  b. beautifulsoup
  c. requests
  d. spotipy
2. Create spotify for dev account
  a. Go to the developer dashboard and create a new Spotify App: https://developer.spotify.com/dashboard/
  b. Client ID and Client Secret into your Python project 
  c. Use http://localhost:8080.com/callback as your Redirect URI. Add it to the dashboard 
  d. When prompted for url response, it'll redirect to localhost while giving you a code by link
    i. grab that localhost link, and parse the code
    ii. save code as env variable
    iii. now, you should have authorized your account with selected scopes

Done!
  
