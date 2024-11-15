Project Name: Print Emojis Using Python Programming Language
Emojis are used to express our emotions while writing a message or any piece of text. If you want to learn how to display imojis in the output using python.
Print Emojis using python 
Smiling, thumbs up, and the heart emoji are some of the emojis we often use while texting our friends or collegues.

To print emojis using Python, you need to install the emoji module in your python virtual environment. You can easily install it by using the pip command on your terminal 

pip install emoji 

The emoji.emojize method helps you write the description of any emoji inside "::" While writing a piece of text. Below are examples are of descriptions of some of the popular emojis

1. :thumbs_up:
2. :red_heart:
3. :smiling: 

You can use the descriptions of any emoji inside "::" to print the emoji using Python. You can find the descriptions of all the emojis [Here](https://carpedm20.github.io/emoji/)

Now let's a have a look at an example of how to print emojis using Python.

The Code is Given as Under:
import emoji
print(emoji.emojize("I love reading books:books:"))
print(emoji.emojize("Some people have a very sensitive heart :infinity:, Please be kind with them. :hibiscus:"))
print(emoji.emojize("Weldone, My here you are done a Good Job! :thumbs_up:"))

Output given as under:
I love reading books📚
Some people have a very sensitive heart ♾️, Please be kind with them. 🌺
Weldone, My here you are done a Good Job! 👍

Summary 
Emojis are used to to express our emotions while writing a message or any piece of text. To print any emoji using Python, you need to install the emoji module in your Python virtual environment. I hope you liked this article on displaying the emojis in the output using Python programming language. Feel Free to ask valuable questions.


# Correct Spelling Using Python

Correct spelling is a piece of text is one of the handy features that can be used in any application where users write content. For example, if you want to create a notepad, if should have features to identify, and correct the wrong spellings. So, if you want to learn how to correct spellings using the Python programming languages, this article is for you. This article will introduce a handy tool to correct spelling using Python

# Correct Spellings using Python

The SpellChecker Module in Python is one of the handiest tools that can be used to correct misspelt words in a piece of text. If you have never used this module before, you can easily install it in your Python virtaul environment by running the command mentioned below in your command prompt or terminal:

# pip install pyspellchecker

Now below is how you can use this module to correct any misspelt words using python

from spellchecker import SpellChecker

corrector = SpellChecker()

word = input("Enter a word : ")

if word in corrector:
 print("Correct")
else:
 correct_word = corrector.correction(word)
 print("Correct Spelling is ",correct_word)

 Output of Code is given as under:
 ![Output of the code](image-1.png)

There are many alternatives in Python for the same task, but the spellchecker module is easy to use compare to other [alternatives](https://thecleverprogrammer.com/2020/12/18/spelling-correction-with-python/)

Summary
So this is how you can correct any misspelt word using the Python programming language. Correcting misspelt words in a piece of text is one of the handy features that can be used in any application where user write content. I hope you liked this article on how to correct spellings using python. Feel free to ask valuable questions through my email alisikandarlaghari@gmail.com



# Scraping GitHub Profile using Python

Web Scraping is one of the most valuable skills every coder should have. If you want to learn how to collect data from Github using web scraping techniques, this article is for you. I will take you through a web scrapping tutorial on scraping GitHub profile using Python.

# Scraping GitHub Profile Using Python

When we open any GitHub account, we see a profile picture, the name of the user, and a short description of the user in the profile section. Here you  will learn how to scrape your GitHub profile image. For this task you need some knowledge of HTML and the requests and BeautifulSoup  libraries in Python.

If you have never used the BeautifulSoup library before, use the command mentioned below in your command prompt or terminal to install this library in your python virtual Environment.

# pip install beautifulsoup4

You don't need to install the requests library as it is already present in the Python Standard library. Now below is how to write Python a program to a profile image from any GitHub Profile.

# Git Profile Picture Scraper
This python script  fetches the profile picture URL from a specified GitHub Profile using web scraping. It uses 'requests' to retrieve the HTML content of the profile page and 'BeautifulSoup' to parse and extract the profile image URL.

![alt text](image-2.png)



#Visualize Linear Relationship Using Python

A linear relationship is a statistical term that is nothing but the relationship between two variables. A linear relationship shows how well two variables x and y are related to each other. As a data science professional, you should know how to visualize a linear relationship as it will show the relationship between two numerical features of a dataset. So if you want to learn how to visualize a linear relationship, this article is for you. In this article, I will take you through a tutorial on how to visualize a linear relationship using Python.


# Visualize a Linear Relationship using Python

When the value of variable increases or decreases with the increase or decrease in the value of another variable. then it is nothing but a linear relationship. When we visualize a linear relationship, It shows whether the relationship between two features is linear or not. 


You can use any data visualization library in Python to visualize a linear relationship. I prefer to use  plotly as it provides interactive results. But as so many Python Programmers use matplotlib for data visualization, I will show you how to visualize a linear relationship with Python using plotly and matplotlib

# Visualize Linear Relationships using Python

Here's how to visulize linear relationships by using the plotly library in python.

To  visualize a relationship using matplotlib, you have to use seaborn.regplot method. So here's how to plot linear relationships by using the matplotlib library in Python. 


 Update README File for this project.

# Instagram Data Analysis: Releationship between Likes and Impressions 

This project performs an analysis of the relationship between **Likes** and **Impressions** on Instagram using a dataset. The code visualizes the coorelation between these two variables using **plotly** and **Seaborn** for interactive and static plots, respectively.

# Project Overview:
The analysis demonstrates the linear relationship between the number of **Impressions** and the **Likes** on Instagram posts. We use two type of visualization 

**Plotly Scatter plot** with trendline: An interactive plot that shows the relationship and adds a trendline to visualize the correlation.
**Seaborn Regression plot**: A static plot to observe the regression line between the two variables.

## Requirements 
Before running the code 


## Generate Text Using Python 

Text generation involves generating text using machine learning techniques. The purpose of text generation is to automatically generate text that is indistinguishable from a text written by a human. If you want to learn how to generate text with Python, this article is for you. In this article, I will walk you through how to use the popular GPT-2 text generation model to generate text using python.

# What is GPT-2 Model?
GPT-2 stands for Generative Pretrained Transformer.It is an open source Natural Language Processing model created by OpenAI. It can generate paragraphs of text with the state of the art performance on many language benchmarks. It is also used for machine translation, question anwering, and text summarization. 

To use the GPT-2 model to generate text using python, you need to install the Transformers library in Python. It can be easily installed using the pip command on your command prompt or terminal as mentioned below.

# pip install transformers

I hope you now have have understood what GPT-2 model is and how you can install it in your Python virtual environment. You can read more about this model ['here'](https://openai.com/index/better-language-models/). Now in the section below, I'll explain how you can use this model for generating text using Python.

# Text Generation using Hugging Face Transformers

This project demonstrates text generation using the Hugging Face Transformers library. Specifically, it shows how to use a pre-trained language model (e.g., GPT-2) to generate text based on a given prompt.

## Requirements

- Python 3.7+
- Hugging Face Transformers library
- PyTorch

Install the necessary libraries by running:

```bash
pip install torch transformers


Usage
The following code snippet loads a pre-trained language model and tokenizer from Hugging Face, generates text based on a given prompt, and outputs multiple text variations.

from transformers import pipeline

# Load pre-trained text generation pipeline
model = pipeline("text-generation", model="gpt2")

# Generate text
sentence = model(
    "Hi, My name is Sikandar Ali, I am here",
    do_sample=True,
    top_k=50,
    temperature=0.9,
    max_length=100,
    num_return_sequences=2
)

# Output the generated text
for i in sentence:
    print(i["generated_text"])


Parameters
do_sample: Enables sampling; without it, the model would use greedy decoding.
top_k: Limits sampling to the top k tokens with the highest probabilities.
temperature: Controls the randomness of predictions by scaling the logits.
max_length: Specifies the maximum length of the generated sequence.
num_return_sequences: Specifies the number of generated sequences to return.








