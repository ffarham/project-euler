module Solution where 

solution :: Int 
solution = fib (0,1) 0 
    where fib (a,b) s | b > 4000000 = s 
                      | otherwise = fib (b, a + b) (if b `mod` 2 == 0 then b + s else s) 


