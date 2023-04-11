# Top-100-Billboard-Playlists
Create, by date input, an ordered playlist of the top 100 billboard songs of that day

Needs:
1. Libraries
  - datetime
  - beautifulsoup
  - requests
  - spotipy
2. Create spotify for dev account
  - Go to the developer dashboard and create a new Spotify App: https://developer.spotify.com/dashboard/
  - Client ID and Client Secret into your Python project 
  - Use http://localhost:8080.com/callback as your Redirect URI. Add it to the dashboard 
  - When prompted for url response, it'll redirect to localhost while giving you a code by link
    - grab that localhost link, and parse the code
    - save code as env variable
    - now, you should have authorized your account with selected scopes

Done!
  
