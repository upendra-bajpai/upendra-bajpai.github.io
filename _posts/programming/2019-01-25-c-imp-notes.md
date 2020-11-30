---
layout: post
title:  "C Importent notes"
author: sal
date: 2020-07-24-03:25:54
categories: [ Jekyll, tutorial ]
image: assets/images/4.jpg
tags: [featured]
---
# C Importent notes
## Pointers
### Size of pointers is fixed.
- Size of an array is number of elements multiplied by the type of element, that is why we get sizeof arri as 12 and sizeof arrc as 3. Size of a pointer is fixed for a compiler. All pointer types take same number of bytes for a compiler. That is why we get 4 for both ptri and ptrc.

- Guess Output
```
#include<stdio.h> 
int main() 
{ 
   int a; 
   char *x; 
   x = (char *) &a; 
   a = 512; 
   x[0] = 1; 
   x[1] = 2; 
   printf("%dn",a);   
   return 0; 
}
```
*Ans. machine dependent*
```
Explanation: 
Output is 513 in a little endian machine. To understand this output, let integers be stored using 16 bits. In a little endian machine, when we do x[0] = 1 and x[1] = 2, the number a is changed to 00000001 00000010 which is representation of 513 in a little endian machine.
```

### Segmenation fault:
Segmentation fault is a specific kind of error caused by accessing memory that “does not belong to you.” It’s a helper mechanism that keeps you from corrupting the memory and introducing hard-to-debug memory bugs. Whenever you get a segfault you know you are doing something wrong with memory – accessing variable that has already been freed, writing to a read-only portion of the memory, etc. Segmentation fault is essentially the same in most languages that let you mess with the memory management, there is no principial difference between segfaults in C and C++.

There are many ways to get a segfault, at least in the lower-level languages such as C(++). A common way to get a segfault is to dereference a null pointer:

```
int *p = NULL;
*p = 1;
```
Another segfault happens when you try to write to a portion of memory that was marked as read-only:
```
char *str = "Foo"; // Compiler marks the constant string as read-only
*str = 'b'; // Which means this is illegal and results in a segfault
```
Dangling pointer points to a thing that does not exist any more, like here:
```
char *p = NULL;
{
    char c;
    p = &c;
}
// Now p is dangling
```
The pointer p dangles because it points to character variable c that ceased to exist after the block ended. And when you try to dereference dangling pointer (like *p='A'), you would probably get a segfault.

- *void * type pointers cannot be de-referenced*
```
#include<stdio.h>
int main()
{
    int a = 12;
    void *ptr = (int *)&a;
    printf("%d", *ptr);
    getchar();
    return 0;
}
```
*Ans. Compiler Error*

- Increment the pointer or value?
```
int arr[] = {1, 2, 3, 4, 5};
    int *p = arr;
    ++*p;
```
```
Explanation: 
The expression ++*p is evaluated as "++(*p)" . So it increments the value of first element of array (doesn't change the pointer p). When p += 2 is done, p is changed to point to third element of array.
```

#### Time Complexity
 
![Array sorting](/assets/images/dssorting.jpg)
![Ds Sorting](/assets/images/sorting.jpg)
![Sementics](https://www.freecodecamp.org/news/semantic-html5-elements/)