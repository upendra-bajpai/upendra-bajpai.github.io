---
layout: post
title:  "DLD Importent notes"
author: sal
date: 2020-07-24-03:25:54
categories: [ Jekyll, tutorial ]
image: assets/images/4.jpg
tags: [featured]
---
# DLD Imp notes
##### According to Amdahl's law speed up for infinite number of process:

```
 S = 1 / (1-P) 
```

where p is parallel part of program Given, sequential part of program is 5%. So parallel part of the program (P)

= 1 - sequential part
= 1 - 0.05 (or 5%)
= 0.95 (or 95%)

Now S = 1 / (1-P)
ie  S = 1 / (1-0.95)
    S = 1 / 0.05
    S = 20 

##### A CPU has a 32 KB direct mapped cache with 128 byte block size. Suppose A is a 2 dimensional array of size 512×512 with elements that occupy 8 bytes each. Consider the code segment
```
for (i =0; i < 512; i++) {
  for (j =0; j < 512; j++) {
    x += A[i][j];
  }
} 
```
### Ans: ![cacheimage](/assets/images/cache.jpg)

##### For a pipelined CPU with a single ALU, consider the following situations
```
1. The j + 1-st instruction uses the result of the j-th instruction
    as an operand
2. The execution of a conditional jump instruction
3. The j-th and j + 1-st instructions require the ALU at the same 
   time
   ```

Which of the above can cause a hazard ?
(A) 1 and 2 only
(B) 2 and 3 only
(C) 3 only
(D) All of above

### Answer: (D)

Explanation: Case 1: Is of data dependency .this can’t be safe with single ALU so read after write.

Case 2:Conditional jumps are always hazardous they create conditional dependency in pipeline.

Case 3:This is write after read problem or concurrency dependency so hazardous

All the three are hazardous

##### A micro-instruction format has micro-ops field which is divided into three subfields F1, F2, F3 each having seven distinct micro-operations, condition field CD for four status bits, branch field BR having four options used in conjunction with address field ADF. The address space is of 128 memory locations. The size of micro-instruction is?
The size of micro-instruction is:
a.17
b.20
C.24
D.32
Microprocessor instruction format, which is divided into three subfields F1, F2, F3 each having seven distinct micro-operations, condition field CD for four status bits, branch field BR having four options used in conjunction with address field ADF. The address space is of 128 memory locations.ie: q8 F1,F2,F3 each having seven distinct micro-operation. So, 3 bits are required for each. Condition field have four status, it needs 2 bits for four different condition. Branch field have four option so,it needs 2 bits for four option. Now there are 128 different memory location, So, there 7 bits atre required for 128 diffeent location. Instruction Field: q8 (1) Total bits are 20. So, option (B) is correct.

Main components of memory tube display are:

    Flood gun
    Primary gun
    Writing Beam
    Collector
    Storage grid
    Screen
    Focussing & deflection system
    Flood electron
    Ground or base

Only Liquid crystal is not enlisted here and it is not the display component in memory tube

##### A 32 - bit wide main memory unit with a capacity of 1 GB is built using 256M X 4-bit DRAM chips. The number of rows of memory cells in the DRAM chip is 214. The time taken to perform one refresh operation is 50 nanoseconds. The refresh period is 2 milliseconds. The percentage (rounded to the closet integer) of the time available for performing the memory read/write operations in the main memory unit is _______ 

Given, total number of rows is 214 and time taken to perform one refresh operation is 50 nanoseconds. So, total time taken to perform refresh operation = 214*50 nanoseconds = 819200 nanoseconds = 0.819200 milliseconds. But refresh period is 2 milliseconds. So, time spent in refresh period in percentage = (0.819200 milliseconds) / (2 milliseconds) = 0.4096 = 40.96% Hence, time spent in read/write operation = 100% - 40.96% = 59.04% = 59 (in percentage and rounded to the closet integer). So, answer is 59. 

##### 

    The RISC design philosophy generally incorporates a larger number of registers to prevent in large amounts of interactions with memory.
    The decision of RISC processor designers to provide simple addressing modes leads to uniform length instructions, so RISC instruction is of uniform fixed length.
    In the hardwired control unit, the control units use fixed logic circuits to interpret instructions and generate control signals from them. It is significantly faster than its counterpart but is rather inflexible. Most of the RISC processors are based on the hardwired control unit design approach.


##### A processor has 16 integer registers (R0, R1, … , R15) and 64 floating point registers (F0, F1, … , F63). It uses a 2-byte instruction format. There are four categories of instructions: Type-1, Type-2, Type-3, and Type 4. Type-1 category consists of four instructions, each with 3 integer register operands (3Rs). Type-2 category consists of eight instructions, each with 2 floating point register operands (2Fs). Type-3 category consists of fourteen instructions, each with one integer register operand and one floating point register operand (1R+1F). Type-4 category consists of N instructions, each with a floating point register operand (1F). The maximum value of N is _______ . Note -This was Numerical Type question


##### In Distributed system, the capacity of a system to adapt the increased service load is called __________ .
Scalability
till  page no 14 
https://www.geeksforgeeks.org/computer-organization-and-architecture-gq/