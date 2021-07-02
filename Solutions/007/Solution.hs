module Solution where 

    solution :: Int
    solution = primes 10001
    
    primes :: Int -> Int
    primes n = sieveOfEratosthenes [2..] 1 n where 
        sieveOfEratosthenes (x:xs) c n = if c == n then x else sieveOfEratosthenes (filter (\a -> mod a x /= 0) xs) (c+1) n