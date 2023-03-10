# Welcome to C3PO!
---
## The Goal
This is a short program in response to a code question with the following description:
> Given an integer between 0-1000, return the verbal equivalent as a String
>

## How it works
C3PO uses modulo logic and integer division to isolate individual digits in a number. In the context of the program, this allows us to identify what numbers are in the 1s, 10s, 100s, and 1000s place, where we can then act accordingly. This generally is some form of dictionary lookup and string addition for any necessary "and" or "-".

## Testing
The unit tests are to quickly and accurately display the translator performance relative to a dataset of known integer-string pairs. This was useful for adjusting minor logic changes after having completed a majority of the program, and could be easily extended into larger number ranges in the future.

## Conclusion
While this is a simple program for a small range of numbers, the DRYness of the code allows for any necessary number range expansion to just be a matter of using previously established methods.

