# SpamMailDetection
The Project Spam mail detection using naïve bayes is a classification problem that uses the  Bayesian network to predict whether are mail belongs to spam or ham class. The spam mails are classified as “spam” 
and the important/ relevant mails are classified as “ham”. The naive  bayes algorithm is a probability-based classifier based on bayes theorem. To create a model 
that detects the relationship between a mail being spam or not from the given dataset, we need  to the train the model with a test dataset that contains the relevant attributes (word frequency, 
presence of specific words, use of respective phrases). 
The Bayesian model calculates the probability of each attribute being associated with the spam  or ham labels using the training dataset. To detect the label of the new mail i.e. spam or ham it 
uses the already calculated posterior probability of a mail being spam based on the data attributes(features). The mail can be then classified into a category (spam or ham) with the 
highest probability. 
The project can be used to filter the unwanted spam mail by using the naive bayes model that is simple and effective. The naive bayes assumes the features are conditionally independent, 
making the model computationally efficient. The Bayesian model observes the text patterns in the mail and classifies it as spam or ham based on the probabilities of features. 
