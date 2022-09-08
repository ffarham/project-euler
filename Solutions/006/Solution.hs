module Solution where 

    solution :: Int
    solution = squareOfSum - sumOfSquares
        where squareOfSum  = let s = sum [1..100] in s*s
              sumOfSquares = sum $ (\x -> x*x) <$> [1..100]