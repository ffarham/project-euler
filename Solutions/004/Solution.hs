module Solution where 

    solution :: Int
    solution = maximum [ x*y | x <- [100..999], y <- [100..999], isPalindrome $ x*y]
        where isPalindrome n = let a = show n in a == reverse a

    
