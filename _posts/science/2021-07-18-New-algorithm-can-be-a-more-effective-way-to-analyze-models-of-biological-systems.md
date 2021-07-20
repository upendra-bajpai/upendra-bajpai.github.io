---
layout: post
title: "New algorithm can be a more effective way to analyze models of biological systems"
author: jane 
date: 18-07-2021 17:01:50 +05:30 
categories: [ SCIENCE ] 
image: assets/images/18-07-2021/174318220-620x480.jpg
---
From biochemical reactions that produce cancers, to the latest memes virally spreading across social media, simple actions can generate complex behaviors. For researchers trying to understand these emergent behaviors, however, the complexity can tax current computational methods.

Now, a team of researchers has developed a new algorithm that can serve as a more effective way to analyze models of biological systems, which in turn allows a new path to understanding the decision-making circuits that make up these systems. The researchers add that the algorithm will help scientists study how relatively simple actions lead to complex behaviors, such as cancer growth and voting patterns.

The modeling framework used consists of Boolean networks, which are a collection of nodes that are either on or off, said Jordan Rozum, doctoral candidate in physics at Penn State. For example, a Boolean network could be a network of interacting genes that are either turned on -- expressed -- or off in a cell.

Boolean networks are a good way to capture the essence of a system. It's interesting that these very rich behaviors can emerge out of just coupling little on and off switches together -- one switch is toggled and then it toggles another switch and that can lead to a big cascade of effects that then feeds back into the original switch. And we can get really interesting complex behaviors out of just the simple couplings." Jordan Rozum, doctoral candidate in physics at Penn State

"Boolean models describe how information propagates through the network," said Réka Albert, distinguished professor of physics and biology in the Penn State Eberly College of Science and an affiliate of the Institute for Computational and Data Sciences. Eventually, the on/off states of the nodes fall into repeating patterns, called attractors, which correspond to the stable long-term behaviors of the system, according to the researchers, who report their findings in the current issue of Science Advances.

Even though these systems are based on simple actions, the complexity can scale up dramatically as nodes are added to the system, especially in the case when events in the system are not synchronous. A typical Boolean network model of a biological process with a few dozen nodes, for example, has tens of billions of states, according to the researchers. In the case of a genome, these models can have thousands of nodes, resulting in more states than there are atoms in the observable universe.

The researchers use two transformations -- parity and time reversal -- to make the analysis of Boolean networks more efficient. The parity transformation offers a mirror image of the network, switching nodes that are on to off and vice versa, which helps identify which subnetworks have combinations of on and off values that can sustain themselves over time. Time reversal runs the dynamics of the network backward, probing which states can precede an initial input state.

The team tested their methods on a collection of synthetic Boolean networks called random Boolean networks, which have been used for than 50 years as a way to model how gene regulation determines the fate of a cell. The technique allowed the team to find the number of attractors in these networks for more than 16,000 genes, which, according to the researchers, are sizes larger than ever before analyzed in such detail.

According to the team, the technique could help medical researchers.

"For example, you might want a cancer cell to undergo apoptosis (programmed cell death), and so you want to be able to make the system pick the decisions that lead towards that desired outcome," said Rozum. "So, by studying where in the network these decisions are made, you can figure out what you need to do to make the system choose those options."

Other possibilities exist for using the methods to study issues in the social sciences and information technology.

"The propagation of information would also make an interesting application," said Albert. "For example, there are models that describe a society in which people have binary opinions on a matter. In the model people interact with each other, forming a local consensus. Our methods could be used to map the repertoire of consensus groups that are possible, including a global consensus."

She added that uses could extend to any area where researchers are trying to find ways to eliminate pathological behaviors, or drive the system into more normal behaviors.

"To do this, the theory existed, methodologies existed, but the computational expense was a limiting factor," said Albert. "With this algorithm, that has to a large part been eliminated."

The researchers have developed a publicly available software library and the algorithms have already been used in studies carried out by her group, according to Albert.

Computations for the study were performed using Penn State's Roar supercomputer.

Albert and Rozum worked with Jorge Gómez Tejeda Zañudo, postdoctoral associate at Broad Institute and Dana-Farber Cancer Institute; Xiao Gan, postdoctoral researcher at the Center for Complex Network Research; and Dávid Deritei, graduate research fellow at Semmelweis University.