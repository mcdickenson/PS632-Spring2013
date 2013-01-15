Make sure everyone already has:

1. Python installed
1. A Github account

Make sure everyone understands:

1. How to start Python interactively
1. How to `print` to the screen
1. How to run a Python script
1. How to write a comment `#`
1. How to define a function with `def`
1. `if`
1. `else`
1. `for`
1. `while`
1. `return`
1. `str`
1. `+-*/%=`
1. lists `[]`

Then go through `binarify` - basic function to convert integer to base 2:
1. how does the `while num` line work? 
1. what about those built-in method calls?
1. can you find input to break it? 
1. what input could you give that would break this? (e.g. negative)

Could you make that function more generic, where it could convert to any base? That's what we do with `int_to_base`. 

What if we want to add two of our new binary numbers? Well, they aren't really numbers--they're strings--so it doesn't work. We need a function `back_to_int` where we give a string and its base, and convert it back to an int. Can you do that? 

Now for some more string play. Let's write a function to turn ints into Roman numerals (`roman_numify`) and back. (Consider also doing this with regular expressions - http://www.diveintopython.net/regular_expressions/n_m_syntax.html.)

Testing: come up with some tests that my functions *don't* pass. Then, make them pass those tests. 
