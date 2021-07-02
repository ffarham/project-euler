What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

The problem requires us to work out the lowest common multiple (lcm) of the set {1,2,..,20}. The implementation is super inefficient using an imperitive approach as it uses brute force. To slightly optimise the solution, x is implemented by 20 as it is the largest number in the set.
The solution is best implemented in Haskell as we can make use of the built in lcm function.

ANS: 232792560