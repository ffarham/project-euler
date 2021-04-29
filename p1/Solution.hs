module Solution where

solution = sum [n | n <- [1..1000-1], mod n 5 == 0 || mod n 3 == 0]
