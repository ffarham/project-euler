module Solution where

-- uses list comprehension to produce a list of all positive integers below 1000 that are either a multiple of 3 or 5 and sums 
-- integers in the list
solution = sum [n | n <- [1..999], mod n 5 == 0 || mod n 3 == 0]
