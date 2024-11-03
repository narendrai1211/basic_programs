def canMakePairSum(arr):
    # Step 1: Initialize counters for even and odd numbers
    even_numbers = 0
    odd_numbers = 0
    
    # Step 2: Count how many even and odd numbers we have
    for num in arr:
        if num % 2 == 0:    # If number is even (divisible by 2)
            even_numbers += 1
        else:               # If number is odd
            odd_numbers += 1
    
    # Step 3: Check if we have same count of even and odd
    return even_numbers == odd_numbers

# Test cases with explanation
arr = [2,7,4,6,3,1]
print("Numbers:", arr)
print("Can make pairs:", canMakePairSum(arr))


""" 
Let me break down the Python problem statement:

Task:
- Given a set of N integers
- Need to split them into N/2 pairs
- Sum of each pair must be ODD
- Every number must be used exactly once
- N is guaranteed to be even

Requirements:
- Return True if possible to make such pairs
- Return False if impossible

Example:
```python
Input: [2,7,4,6,3,1]
Output: True
Explanation:
- Can form pairs: (2,7), (4,3), (6,1)
- Each pair sums to odd number:
  * 2+7 = 9 (odd)
  * 4+3 = 7 (odd)
  * 6+1 = 7 (odd)
- All numbers used exactly once
```

Why Solution Works:
1. To get odd sum: need one even + one odd number
2. So we count:
   - even_count = numbers of even integers
   - odd_count = numbers of odd integers
3. If even_count equals odd_count:
   - Each even can be paired with an odd
   - All pairs will sum to odd
   - Return True
4. If counts not equal:
   - Can't pair them all to get odd sums
   - Return False

More Examples:
```python
[2,4,6,8] -> False (all even, no odd pairs possible)
[1,3,5,7] -> False (all odd, no odd pairs possible)
[1,4,3,2] -> True (can make (1,4), (3,2))
```



Let me explain WHY in the simplest way possible:

Imagine you need to make pairs of numbers where their sum must be ODD.

1. Let's understand what makes a sum ODD:
```
Even + Even = Even  (2+4=6)   Not what we want
Odd + Odd = Even   (3+5=8)    Not what we want
Even + Odd = Odd   (2+3=5)    This is what we want!
```

2. Think of it like making dance pairs:
```
Each pair needs:
- One boy (even number)
- One girl (odd number)
```

3. Let's look at [2,7,4,6,3,1]:
```
Even numbers (boys): 2,4,6
Odd numbers (girls): 7,3,1

We have 3 boys and 3 girls - Perfect! Everyone gets a partner!
We can make pairs:
(2,7) = 9  ✅ odd sum
(4,3) = 7  ✅ odd sum
(6,1) = 7  ✅ odd sum
```

4. Let's see why it fails with [2,4,6,8]:
```
Even numbers (boys): 2,4,6,8
Odd numbers (girls): none

We have 4 boys and 0 girls!
- No matter how we pair boys together
- We can never get odd sum
- Just like you can't make dance pairs with only boys!
```

So simply:
1. Count boys (even numbers)
2. Count girls (odd numbers)
3. If counts are equal = Everyone can dance! (return True)
4. If counts different = Someone left without partner! (return False)

It's just like pairing dance partners - you need equal numbers of each to make everyone happy!




""" 
