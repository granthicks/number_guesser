# Auto Number Guesser

A simple mess around project that generates a random number (from 1 to 5,000,000) then tries to "guess" the number by randomly generating another number in that range. After each guess there will be a response of either "higher" or "lower" indicating that the originally generated number is either higher or lower than the guess, and the range will be adjusted for the next guess. If the correct number is higher than the guess, then the low range of the next guess will be adjusted to be the previous guess and vice versa.

After a correct guess has been made, the correct number and number of guesses is took to reach the correct number will be stored in a sql database and the number of correct guesses made so far (essentially the number of times the script has been run) and the average number of guesses to reach the correct number (rounded to the nearest whole number) will be displayed.


### Other Info
Just a simple project for messing around when bored and trying some new things out. I'll be trying to make things more interesting as I go along adding some different approaches for practice.