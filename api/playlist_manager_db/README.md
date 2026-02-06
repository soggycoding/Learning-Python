Markdowns to remember: 
'#' For headings 
'-' for bullet points 
'code' for inline code 
'''code block''' for code blocks 
'[x]' for completed checkboxes 
'[]' for incomplete checkboxes

# PLAYLIST MANAGER DATABASE
2nd API database project, this project will use many-to-many relationship since one artist can be in more than one playlist.

## THINGS TO CONSIDER
- Song and playlist should have a playlist
- Should have a third table that is suppose to be a junction table
- 
## FEATURES
- Should have a display for each playlist
- 
## PROJECT OVERVIEW
- This project should teach me about many-to-many, how a junction table works, how db.Table() differ from db.Model and how to remove items in many-to-many
# ENDPOINTS

## SONGS
- POST /songs Creates a new song that includes the artist
- GET /songs Retrieves all the songs
- PUT /songs/<int:id> Updates a specific song's details
- GET /songs/<int:id> Retrieves a specific song
- DELETE /songs/<int:id> Delete a specific song

## PLAYLISTS
- POST /playlists Creates a new playlist category
- GET /playlists Retrieves all the playlist
- PUT /playlists/<int:id> Updates a specific playlist
- GET /playlists/<int:id> Retrieves a specific playlist
- DELETE /playlist/<int:id> Delete a specific playlist

## JUNCTION TABLE
- ???

# PROJECT STATUS
- [x] PHASE 1: Create a CRUD for both songs and playlists
- [x] PHASE 2: Create a validator for both songs and playlists
- [x] PHASE 3: Figure out how Junction table works
- [] PHASE 4: Connect the junction table with the songs and playlists 