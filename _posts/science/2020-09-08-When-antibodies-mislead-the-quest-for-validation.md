---
layout: post
title: "When antibodies mislead the quest for validation"
author: jane 
date: 08-09-2020 10:36:34 
categories: [ SCIENCE ] 
image: assets/images/08-09-2020__10/d41586-020-02549-1_18344760.jpg
---
Research antibodies are designed to recognize and bind to specific proteins according to their shape and chemical properties.Credit: Adapted from Molekuul/SPL

Commercial antibodies are commonplace in biology laboratories. Researchers use these giant Y-shaped proteins to detect specific molecules in cells, tissues and test tubes. But sometimes the proteins detect other molecules, too — or even instead. When that happens, confusion can snowball.

Consider the gene CR9ORF72. It’s often mutated in people with the neurodegenerative diseases amyotrophic lateral sclerosis and familial frontotemporal dementia. But what it actually does has been hard to pin down, partly because the widely varying locations of the protein in the cell offer more confusion than clarity.

Peter McPherson, a neuroscientist at McGill University in Montreal, Canada, suspects that the multiple locations arise from what is often seen as a trivial decision for detecting the protein: the choice of antibody. Antibodies work by binding to specific parts of a protein, according to the protein’s shape and chemical properties, but an antibody produced to bind to one protein can often bind to another, and sometimes with better affinity.

That’s borne out in McPherson’s work. He and his team bought 16 antibodies marketed to detect CR9ORF72. Then they took a cell line that produces the protein at high levels and used the genome-editing tool CRISPR–Cas9 to make a line in which CR9ORF72 was knocked out, so the protein would not be present. They then assessed how the antibodies performed in the two lines in a series of common tests and found that the antibody that had been used in the most publications (and cited most often) found the protein even when it wasn’t there. Those that worked best for each assay had not appeared in the literature at all1.

Others have reported comparable experiences. Cecilia Williams, a cancer researcher at the KTH Royal Institute of Technology in Stockholm, tested 13 antibodies to try to untangle conflicting data about estrogen receptor β, a protein discovered in 1996 that is a potential anticancer target. Twelve of the antibodies, including the two most popular, gave either false positives or false negatives, or both, she and her team reported2. “Don’t take either the literature or the antibody for granted,” she warns.

Antibody anarchy: a call to order

Researchers often buy antibodies according to the number of times the product has been cited in the literature, but that strategy can overlook newer products that have been put through more rigorous tests. They also tend to assume that others who used the antibody before them checked that it worked as intended, and that it will therefore work in their own experiments, opening the door for self-perpetuating artefacts.

“When I look at papers in general, I get depressed by the quality of the antibody characterization,” says Simon Goodman, a science consultant at the Antibody Society, a not-for-profit professional association. Goodman is based in Darmstadt, Germany, and has organized a series of educational webinars on appropriate techniques for the society3. “If you ask ‘how did you validate the antibody?’, researchers will say, ‘well we bought it and the producer says that it behaves like this.’”

Often, the data that companies provide to show an antibody works come from a cell line that has been engineered to express the protein at levels substantially higher than under physiological conditions. Researchers would do better to check that an antibody can detect the protein at physiological levels, in the technique and tissue type they plan to use and, ideally, that the signal fades or disappears when levels of the protein do.

Validation drive

There has been a steady drumbeat of efforts to make researchers more careful. In 2016, the US National Institutes of Health (NIH) began requiring grant applicants to describe how they would authenticate antibodies and other key resources. Validation road maps have been printed, summits held and web portals established — Antibodypedia, Antibodies-online, Antibody Resource, Biocompare, CiteAb and Labome, to name a few.

“The true game-changer has been CRISPR,” says Aled Edwards, who leads the Structural Genomics Consortium from Toronto, Canada, a public–private partnership devoted to doing basic science that can promote drug discovery. That’s because the technique makes it easy to perform useful control experiments, just as McPherson and his team did. Earlier this year, the antibody vendor Abcam in Cambridge, UK, introduced a suite of knockout cell lines and preparations that researchers can buy alongside its antibodies to test positive and negative cells under specific conditions in their own labs. The company now has more than 1,600 cell lines and 2,400 cell lysates available.

An antibody signal in wild-type cells (top) should disappear in tissue in which the target protein has been knocked out (bottom).Credit: K. J. Rhodes and J. S. Trimmer/J. Neurosci. (2006, Society for Neuroscience)

Edwards and McPherson helped to set up a Toronto-based charity called YCharOS (pronounced Ikaros), to put commercial antibodies to the test. They plan to use McPherson’s strategy to assess more antibodies against other targets, gauging performance across three common assays: immunoblot, immunoprecipitation and immunofluorescence. They are also working with several antibody suppliers and pharmaceutical companies to develop standard operating protocols. As well as some in-kind corporate contributions, the NIH and the Parkinson’s disease charity the Michael J. Fox Foundation in New York City are providing initial funding of about US$300,000 to test a suite of antibodies used in neuroscience.

Not every antibody can be tested using knockout controls, Edwards admits. About 10% of genes are essential to life, so a knockout cell line is not viable for them. Also, an antibody that performs well in one cell line could fall short in another. Still, these simple experiments can help to identify those antibodies that aren’t binding with their target protein. There are other methods researchers can try, too, such as coupling immunoprecipitation to mass spectrometry to see what proteins the antibody binds to4. Ultimately, says Edwards, “the onus is on the experimenter”.

That said, it takes more than just the right antibody to yield informative experiments, says James Trimmer, who directs the NeuroMab lab at the University of California, Davis, an effort to produce high-quality antibodies for neuroscience. An antibody that works reliably when a protein is in its folded (‘native’) state inside a cell can perform differently when proteins are chemically altered in preserved tissue or unfolded in cell mixtures, and even small changes in sample preparation can have a large impact.

Researchers need to know how their own methods compare with those used in validation experiments, and should avoid antibodies if the validation details are unavailable. “If you use them for the wrong purpose, they won’t be a good fit,” Trimmer says.

Reproducibility crisis: Blame it on the antibodies

It is not uncommon for labs to buy several antibodies and select the one that works best. But many developers license their antibodies to multiple distributors, who do not always disclose the antibodies’ origins. When setting out to test antibodies for C9ORF72, McPherson’s postdoc Carl Laflamme used CiteAb and the research literature to identify more than 100 antibody products. He then sent enquiries to vendors and scoured data sheets to rule out duplicates. Even so, the team realized later that 2 of the 16 antibodies they purchased from different companies were the same, so they had run a whole set of experiments unnecessarily. “We wasted our money and our time and effort,” McPherson says.

Identity crisis

Sometimes it’s not even clear which antibody researchers have used, especially in older studies. Only about 11% of the antibodies used in papers published in 1997 are identifiable, according to an analysis5 led by researchers at the University of California, San Diego (UCSD), and the data-sharing platform SciCrunch in La Jolla, California; nowadays, that figure has risen to 43%.

NatureTech hub

Anita Bandrowski, head of SciCrunch and a bioinformatician at UCSD, is spearheading an effort to assign every antibody a unique identifier, called an RRID, and include it in publications. Researchers can find or request an RRID on the Antibody Registry’s website, and the identifiers would remain the same even if the vendor supplying an antibody changes its catalogue or goes out of business. Antibodies are much easier to find when journals mandate RRIDs, says Bandrowski. The journal Cell, for instance, asks authors for RRIDs, and 97% of its antibodies are findable5. Both Nature and Nature Research journals encourage the use of RRIDs to track key biological resources, including antibodies, cell lines, model organisms and tools.

RRIDs can alleviate, but not solve, the problem of the same antibody being sold by many vendors: if the original source is clearly disclosed, all the antibodies can be assigned the same RRID. Bandrowski guesstimates that the 2.5 million antibodies with RRIDs represent perhaps 700,000 unique molecules. But RRIDs do not distinguish between different batches of the same product, which can be particularly problematic for polyclonal antibodies, which are purified from the blood of immunized animals and are therefore more of a mixture than those made from cultured cells.

The bottom line is: however an antibody-driven experiment comes out, researchers would be wise to be sceptical. When experiments fail, researchers often question their own technique, says Goodman. “Of course you blame yourself as a young scientist.” But the scientific community should be equally sceptical of antibodies that seem to work, says Edwards, and demand evidence that they do before relying on them. “We buy antibodies, we don’t test them, and then we publish articles that send the field sideways.”