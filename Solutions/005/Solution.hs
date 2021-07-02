module Solution where

    solution :: Int
    solution = foldr lcm 1 [2..20]