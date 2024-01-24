# WordSearch Puzzle Generator

Max's attempt to create a word search puzzle game.

This is the puzzle generating algorithm wrapped as an API server. (The file trial_code contains a testcase for the puzzle algorithm and a sample tkinter menu, which has been abandoned by myself).
Includes a lot of features like selecting our own grid size, having inverted words, empty spaces and random charecters in the grid, and including mixed case words to add some spice to the game :fire:, or if you are tired you can just get the answer for a puzzle instead of silving it yourself :skull:.

### Required libraries:
 - random (mostly comes preinstalled with python)
 - numpy 
 - flask (for the API wrap)
  
## How to get this started :thumbsup::
1. Download the files `api_flask.py` and `wordSearchGen.py` from this repo.
2. Run the api_flask.py file on your machine after making sure you have all the required libraries mentioned above.
3. Connect to localhost (the port is specified in the code itself). 

## Making an API call:
- Make sure you pass all the parameteres in the call (rows,cols,words,inv,spaces,chars,mixCase,answers). All the parametres would be explained below.
- Example: `https://localhost:7853/get-puzzle/?rows=10&cols=10&words='apple,orange,papaya,grapes'&inv=true&spaces=false&chars=false&mixCase=false&answers=true`

  - words: should be a string of words seperated by commas
  - rows,cols: should be integers
  - inv,spaces,chars,mixCase,answers: should be boolean(true or false)

## Different parametres:
- rows,cols : specifies the dimentions of the wordsearch grid
- words: specifies the words that are hidden in the puzzle
- inv: Specifies if the words can be inverted before being hidden in the puzzle (for example, when finding the word "apple" horizontally you might see "elppa")
- spaces: Specifies if there can be empty spaces left in the puzzle after completing it.
- chars: Includes random charecters in the puzzle when filling the empty spaces (makes it a real challenge to find anything :rofl:)
- mixCase: Includes a mix of lower and uppercase letters inside the puzzle grid.
- answers: Dosen't fill the empty spaces in the puzzle (you basically get just the answer to the puzzle)

## Note:
To make this api server publicly available you can either host it in an online service or using something like [ngrok](https://ngrok.com/) to host a public server in your own hardware (do be aware of the [risks](https://security.stackexchange.com/questions/41983/what-risks-are-involved-in-exposing-our-home-computers-over-the-public-internet) when going with the 2nd option).
