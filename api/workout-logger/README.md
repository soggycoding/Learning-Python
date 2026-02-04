Markdowns to remember: 
'#' For headings 
'-' for bullet points 
'code' for inline code 
'''code block''' for code blocks 
'[x]' for completed checkboxes 
'[]' for incomplete checkboxes

# WORKOUT-LOGGER DATABASE
First database API project, this will track your workouts and which body part it targets. It will also track how many sets and reps for each workout, and have a status if it is pending or completed.

## THINGS TO CONSIDER
- the sets and reps should be in one column and should present it as "15x2" where 15 is the repetition and 2 is the sets. (So probably a string is needed?)
- should have an ID for each muscle part it targets and each workouts. So it can be presented as a workout plan whenever you need a targeted body workout.
-  
## FEATURES
- Takes the workout and which bodypart it targets, creates a unique ID for both to quickly identify their purpose later on
- Will work as a workout plan if the user wants to check specific category that target that muscle group
- 
## PROJECT OVERVIEW
First API DATABASE project that will also be useful for me since I need to workout again. This will serve as my log and workout guide when its done
# ENDPOINTS

### WORKOUTS
- POST /workouts Create a new workout
- GET /workouts Retrieves all workouts
- PUT /workouts/<int:id> Updates a specific workout
- GET /workouts/<int:id> Retrieves a specific workout
- DELETE /workouts/<int:id> Delete a specific workout

### CATEGORIES
- POST /categories Create a new category
- GET /categories Retrives all categories
- PUT /categories/<int:id> Updates a specific Category
- GET /categories/<int:id> Retrieves a specific Category
- DELETE /categories/<int:id> Delete a specific Category

# PROJECT STATUS
- [x] PHASE 1: Create a CRUD for workouts and categories
- [x] PHASE 2: Have a validator for workouts and categories
- [] PHASE 3: Use a mapper so it filters specific workouts per category
- [] PHASE 4: Create a workout plan per category