# Poetry_Annotator

In this project, I had to write code that could be used to help poets confirm that their work meets pronunciation stress pattern rules and rhyme scheme rules.

We represent English & French language data using an n-gram language model (experimented with unigram, bigram, and trigram models), and measure the probability distribution over our language by using MLE with add-delta smoothing (extended form of Laplace smoothing) - and experimented with several delta values (analysis of impact of varying delta in Task3.txt)
We implement the IBM-1 algorithm to learn word alignments between English and French words (thereby allowing us to translate from one to the other)
We use the IBM BlueMix service to obtain reference translations, and implement the BLEU-metric algorithm to measure the performance of our translation algorithm.
Developed by:

Chidi Nwaka

Refer to handout.pdf <a href="https://github.com/ChidiNwaka/Poetry_Annotator/blob/master/handout.pdf"> for a more detailed explanation of this projects tasks.


