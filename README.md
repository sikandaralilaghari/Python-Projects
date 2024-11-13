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



















