# Leetcode-Problem-1780__Check-if-Number-is-a-Sum-of-Powers-of-Three__Python3

## Description

Given an integer _n_, return true if it is possible to represent _n_ as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y = 3^x.

Example 1:

    Input: n = 12
    Output: true
    Explanation: 12 = 3^1 + 3^2

Example 2:

    Input: n = 91
    Output: true
    Explanation: 91 = 3^0 + 3^2 + 3^4

Example 3:

    Input: n = 21
    Output: false

 

## Constraints:

    1 <= n <= 107


## Solution strategy:

    -Get the ternary representation of the given number n
    -Check if there is 2 in the ternary representation
          -if yes, return false
          -else, return true
