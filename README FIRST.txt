# info-retriever-chatbot

EXTRACT THE 'INFORMATIONNLTK' FOLDER TO C:/ DRIVE IN WINDOWS SYSTEMS!
INSTALL THESE ON YOUR SYSTEM FIRST:
-> go to python scripts folder in CMD.
-> pip install nltk
-> pip install numpy
-> pip install pyspellchecker
-> pip install sklearn

Part of an internship at Hindustan Petroleum Corporation Ltd Datacenter, Hyderabad during the month of December, 2018.

This is a Python program that uses Machine Learning to extract relevant information depending on the user's question. The chatbot also has the ability to greet users/exchange pleasantries and ask for more questions.

It has a spellchecker function, so it can correct minor typing errors in the user input and give the required information on the topic.

The input is converted to lowercase, and then tokenized and lemmatized.

This program uses TF-IDF vectorizer to find out the chances of the text being relevant to the question.

The bot then prints the top 4 sentences which it deems relevant.

If it does not understand the question asked, it will give you an option to add your answer to that specific question for future use, or to ask another question.

When it asks you whether you want to give more questions, the program can either be used again by obliging or it can be ended by typing 'bye', 'thanks' or 'thank you'.


