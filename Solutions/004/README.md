Find the largest palindrome made from the product of two 3-digit numbers.

The solution uses brute force to go through all integers up to 999*999 and checks whether each integer is a pallindrome. Working backwards (999*999 to 100*100) to find the find the first palindrome integer is not more efficient then brute forcing forward as the first palindrome integer calculated working backwards is not guaranteed to be the largest. Therefore it is necessary to calulate all products.

Ans: 906609