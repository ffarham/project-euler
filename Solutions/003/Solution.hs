module Solution where

    solution :: Int
    solution = primeFactor 0 600851475143 

    primeFactor :: Int -> Int -> Int
    primeFactor p n | n == 1    = p
                    | otherwise = if s > p then primeFactor s m   
                                  else primeFactor p n
                        where s            = smallestPF n
                              m            = div n s
                              smallestPF n = head [a | a <- [2..], mod n a == 0]