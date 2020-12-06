---
layout: post
title:  "OS Importent notes"
author: sal
date: 2020-07-24-03:25:54
categories: [ Jekyll, tutorial ]
image: assets/images/4.jpg
---

# OS

> read about **polled I/O** or **software-driven I/O**.

- We describe a protocol of input device communication below. a. Each device has a distinct address b. The bus controller scans each device in sequence of increasing address value to determine if the entity wishes to communicate. c. The device ready to communicate leaves it data in IO register. d. The data is picked up and the controller moves to step-a above. Identify the form of communication best describes the IO mode amongst the following?
##### answer: polling

- Consider a hard disk with 16 recording surfaces (0-15) having 16384 cylinders (0-16383) and each cylinder contains 64 sectors (0-63). Data storage capacity in each sector is 512 bytes. Data are organized cylinder-wise and the addressing format is
##### Explain
 First convert ⟨1200,9,40⟩ into sector address.  
  
(1200×16×64)+(9×64)+40=1229416  
  
Number of sectors to store file =(42797  KB)/512=85594  
  
Last sector to store file =1229416+85594=1315010  
  
Now, do reverse engineering,  
  
1315010/(16×64)=1284.189453 (1284 will be cylinder number and remaining sectors =194)  
  
194/64=3.03125 (3 is surface number and remaining sectors are 2)  
  
∴⟨1284,3,1⟩ is last sector address.
[Concept](https://gateoverflow.in/1337/gate2009-51)
- A file system with 300 GByte disk uses a file descriptor with 8 direct block addresses, 1 indirect block address and 1 doubly indirect block address. The size of each disk block is 128 Bytes and the size of each disk block address is 8 Bytes. The maximum possible file size in this file system is?
##### Expain:
**The question in simple words**- A 300GB disk has indexing in which 8 direct block addresses are present, 1 single indirect block(means it points to the address of a disk block in which 128/8=16 more addresses are stored which further stores data ), and 1 doubly indirect address is present. so using this file decryptor what is the max. possible size of a file possible that can be supported by this file system.

Direct block addressing will point to 8 disk blocks =8×128  B=1  KB  
  
Singly Indirect block addressing will point to 1 disk block which has 128/8 disc block addresses =(128/8)×128  B=2  KB  
  
Doubly indirect block addressing will point to 1 disk block which has 128/8 addresses to disk blocks which in turn has 128/8 addresses to disk blocks =16×16×128  B=32  KB  
  
Total =35  KB
- An application loads 100 libraries at startup. Loading each library requires exactly one disk access. The seek time of the disk to a random location is given as 10 ms. Rotational speed of disk is 6000 rpm. If all 100 libraries are loaded from random locations on the disk, how long does it take to load all libraries? (The time to transfer data from the disk block once the head has been positioned at the start of the block may be neglected.)

> average rotation latency = (1/2)× rotation time Disk access time=Seek
> time+Rotational latency+Transfer time (given that transfer time is
> neglected)

 ##### explain:
Seek time=10 ms  
Rotational speed=6000 rpm

-   60s→6000 rotations

-   1 rotation→60/6000s

-   Rotational latency=1/2×60/6000s=5 ms

Total time to transfer one library =10+5=15 ms

  
∴ Total time to transfer 100 libraries =100×15 ms=1.5s

- The data blocks of a very large file in the Unix file system are allocated using?
##### The Unix file system uses an extension of indexed allocation. It uses direct blocks, single indirect blocks, double indirect blocks and triple indirect blocks. Following diagram shows implementation of Unix file system. The diagram is taken from [Operating System Concept](http://codex.cs.yale.edu/avi/os-book/OS8/os8j/slide-dir/index.html) book
![GFG Unix large file](https://contribute.geeksforgeeks.org/wp-content/uploads/gate20.jpg)
- Which of the following statements about synchronous and asynchronous I/O is NOT true?
A. An ISR is invoked on completion of I/O in synchronous I/O but not in asynchronous I/O
B. In both synchronous and asynchronous I/O, an ISR (Interrupt Service Routine) is invoked after completion of the I/O
C. A process making a synchronous I/O call waits until I/O is complete, but a process making an asynchronous I/O call does not wait for completion of the I/O
D. In the case of synchronous I/O, the process waiting for the completion of I/O is woken up by the ISR that is invoked after the completion of I/O
**B is false.**


