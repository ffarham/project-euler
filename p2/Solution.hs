module Solution where 

solution :: Int 
solution = fib (0,1) 0 4000000

fib :: (Int,Int) -> Int -> Int -> Int
fib (a,b) sum target | b > target = sum 
                     | otherwise = fib (b, a+b) (if b `mod` 2 == 0 then b+sum else sum) target
