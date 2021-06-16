module Solution where 

-- returns the sum of all even fibonacci terms that are below 4 million
solution :: Int 
solution = fib (0,1) 0 4000000

-- The recursive function takes a pair of integers (where b represents the fibonacci value in question), a sum and target value. 
-- The target value remains constant but the sum value gets updated by even finonacci values. The base case returns the accumulated 
-- sum when a fibonacci value exceeding 4 million is reached.
fib :: (Int,Int) -> Int -> Int -> Int
fib (a,b) s t | b > t = s 
              | otherwise = fib (b, a + b) (if b `mod` 2 == 0 then b + s else s) t
