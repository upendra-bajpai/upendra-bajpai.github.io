---
layout: post
title:  "Network Importent notes"
author: sal
date: 2020-07-24-03:25:54
categories: [ Jekyll, tutorial ]
image: assets/images/4.jpg
---
# Computer Network
Range of Private IP 
-  10.0.0.0 - 10.255.255.255
-  172.16.0.0 - 172.31.255.255
-  192.168.0.0 - 192.168.255.255 

- In multi-programmed systems, it is advantageous if some programs such as editors and compilers can be shared by several users. Which of the following must be true of multi-programmed systems in order that a single copy of a program can be shared by several users? I. The program is a macro II. The program is recursive III. The program is reentran.
#####Question 34 Explanation:

Reentrant code is commonly required in operating systems and in applications intended to be shared in multi-use systems. A programmer writes a reentrant program by making sure that no instructions modify the contents of variable values in other instructions within the program. Each time the program is entered for a user, a data area is obtained which keep all the variable values for that user. The data area is in another part of memory from the program itself. When the program is interrupted to give another user a turn to use the program, information about the data area associated with that user is saved. When the interrupted user of the program is once again given control of the program, information in the saved data area is recovered and the program can be reentered without concern that the previous user has changed some instruction within the program. The program is recursive is correct.
- Which of the following comment about peep-hole optimization is true?
It is applied to small part of the code and applied repeatedly,[Peep-hole optimization](https://www.geeksforgeeks.org/peephole-optimization-in-compiler-design/) is a type of optimization technique which is applied to small part of the code called as 'peep' and Peephole optimization involves the changing in small set of instructions to an equivalent set of instruction that gives the better performance compare to other optimization technique and applied repeatedly.
- Consider the code segment
```
int i, j, x, y, m, n;
 n=20;
 for (i = 0, i < n; i++)
  {
    for (j = 0; j < n; j++)
     {
        if (i % 2)
        {
         x + = ((4*j) + 5*i);
         y += (7 + 4*j);
        }
     }
  }
  m = x + y;
  ```
  - The code contains loop invariant computation
- There is scope of common sub-expression elimination in this code
- There is scope of strength reduction in this code
- There is scope of dead code elimination in this code
##### Answer:
  There is scope of dead code elimination in this code
  . in dead code elimination technique it removes the dead code as name suggested. The statements of code is called dead code in which code is either never executes or unreachable or their output is never used are eliminated but here is not such type of statements or code. Here we reduce the strength reduction as replacing the " 4 * j with 4 << j " and code has common sub-expression as well as loop invariant computations.

- Peephole optimization is form of Local optimization.
##### Answer:
```
In the optimisation technique, we optimise the code during compilation which reduces the space complexity as well as time complexity and eliminate the redundant code.Peephole optimization one of the optimisation technique which performed on a small set of compiler-generated instructions and the small set is known as the peephole or window. [Peephole optimization](https://www.geeksforgeeks.org/peephole-optimization-in-compiler-design/) does change the small set of instructions to the other an equivalent set which has better performance.:- For example :-

1.  Peephole optimization technique would remove both instructions push and pop operation on stack instead of pushing register A onto the stack and then immediately popping the value back into register A
2.  Peephole optimization technique might do an arithmetic shift left Instead of adding A to A.
3.  Peephole optimization technique might scale the floating point register’s exponent by 3 Instead of multiplying a floating point register by 8.

The main objective of peephole optimization is:

-   To improve performance
-   To reduce memory footprint
-   To reduce code size
``` 
- In compiler terminology reduction in strength means
#### replacing a costly operation by a relatively cheaper one.
- The use of multiple register windows with overlap causes a reduction in the number of memory accesses for I. Function locals and parameters II. Register saves and restores III. Instruction fetches
#### needed study

- The expression _(a*b)* c_ op........ where 'op' is one of '**+**', '*****' and '**↑**' (exponentiation) can be evaluated on a CPU with a single register without storing the value of _(a * b)_ if
#### Given expression is :-

(a*b)* c op  

Here op is one of the ‘+’, ‘*’ and ‘↑’ (exponentiation). (a* b)* having high precedence so it will evaluate first in CPU register. But we have given one single register as we cannot store any value from reg to memory. Now ( a * b ) is evaluated in register R and precedence order is ( ↑ , * or / , + or – ). If we put op as (a*b)* c op ‘ ↑ ‘ then expression becomes as (a*b)* c ↑ d here c ↑ d will evaluate first. But we have not extra register to evaluate ( a * b ). Therefore we cannot put any operator having precedence greater than ” * ”. Hence, Operator is either ” + ” or “- ” .

- ### [Introduction of Assembler](https://www.geeksforgeeks.org/introduction-of-assembler/)
- -   **Pass-1:**
    1.  Define symbols and literals and remember them in symbol table and literal table respectively.
    2.  Keep track of location counter
    3.  Process pseudo-operations
-   **Pass-2:**
    1.  Generate object code by converting symbolic op-code into respective numeric op-code
    2.  Generate data for literals and look for values of symbols.
    
  - lexical analyser uses finite autometa so it uses regular grammer. whose expression will be for example letter(letter + digit )* , where as syntax tree uses context free grammer which uses pda.
  - In operator grammar production rules which have two adjacent non-terminals on right hand side are not allowed. Additionally empty production rules are also not allowed. So, A → BC and A → ε are not allowed.
  - YACC is the standard parser generator for Unix operating system. It is used as a parser in C programming language. It stands for Yet Another Compiler Compiler.
  -  Which of the following productions eliminate left recursion in the productions given below: S → Aa | b A → Ac | Sd | ε

A

S → Aa | b A → bdA' A' → A'c | A'ba | A | ε

S → Aa | b A → A' | bdA', A' → cA' | adA' | ε

C

S → Aa | b A → A'c | A'd A' → bdA' | cA | ε

D

S → Aa | b A → cA' | adA' | bdA' A' → A | ε

**[Parsing and Syntax directed translation](https://www.geeksforgeeks.org/parsing-and-syntax-directed-translation-gq/)** **[ISRO CS 2013](https://www.geeksforgeeks.org/isro-cs-2013/)**  
**[Discuss it](https://www.geeksforgeeks.org/isro-isro-cs-2013-question-6/)**  
  
  

Question 67 Explanation:

To remove left recursion from the grammar of the
form :  A → Aα | β
We rewrite the production rules as:
           A → βA'
           A'→ αA'| ε

Given Grammar: S → Aa | b
               A → Ac | Sd | ε

after finding indirect left recursion, grammar:

               S → Aa | b
               A → Ac | Aad | bd | ε

here, α = c, ad, β = bd

So, Grammar after removing left recursion = 
               S → Aa | b
               A → A' | bdA'
               A'→ CA'| ada'| ε 

So, option (B) is correct.
- Operator stack is used for converting infix to postfix expression such that operators like as +, *, (, ), / are pushed in stack where as operand stack is used for converting Postfix to Prefix evaluation such that operands are 7,2,1,2 etc.
- A lexical analyzer uses the following patterns to recognize three tokens T1, T2, and T3 over the alphabet {a,b,c}. T1: a?(b∣c)*a T2: b?(a∣c)*b T3: c?(b∣a)*c Note that ‘x?’ means 0 or 1 occurrence of the symbol x. Note also that the analyzer outputs the token that matches the longest possible prefix. If the string _bbaacabc_ is processes by the analyzer, which one of the following is the sequence of tokens it outputs?
- 
A: T1T2T3
B: T1T1T3
C: T2T1T3
D:T3T3
#### Explanation:

0 or 1 occurrence of the symbol x. T1 : (b+c)* a + a(b+c)* a T2 : (a+c)* b + b(a+c)* b T3 : (b+a)* c + c(b+a)* c Given String : bbaacabc Longest matching prefix is " **bbaac** " _(Which can be generated by **T3**)_ The remaining part (after Prefix) "abc" _(Can be generated by **T3**)_ So, the answer is **T3T3**
