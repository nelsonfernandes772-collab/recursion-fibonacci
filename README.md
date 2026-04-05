# Fibonacci Sequence (Recursion vs Iteration)

## Base Case
F(0) = 0  
F(1) = 1  

## Recursive Case
F(n) = F(n-1) + F(n-2)

## Example (n = 5)
F(5) = F(4) + F(3)  
F(4) = F(3) + F(2)  
F(3) = F(2) + F(1)  
F(2) = F(1) + F(0)  

Result: 5

## Comparison
- Recursive: simple but slower (repeats calculations)
- Iterative: faster and uses less memory

## Limitation
- Recursive: limited by stack depth (~1000 calls)
- Iterative: limited by memory and integer size
