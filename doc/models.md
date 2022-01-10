# Models

## Project

 - Each project has a name, a baseline and bonus number of blocks, and
   a number of rows to use for displaying the blocks in a grid.

 - Each project belongs to a user.


## Block

 - Each block belongs to a single project.
 
 - Each block has a start time and duration.


## Settings

 - Settings are used as a key-value store for user options.
 
 - The keys are taken from a fixed collection of choices.
 
 - The values are all stored as text, but represent different Python
   types, depending on the key, so a custom manager will be needed to
   deal with the conversions.
