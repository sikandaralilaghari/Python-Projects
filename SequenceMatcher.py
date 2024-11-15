from difflib import SequenceMatcher

text1 = "My Name is Sikandar Ali Laghari"
text2 = "Hi, My Name is Sikandar Ali Laghari"

# Calculate similarity ratio
sequence_score = SequenceMatcher(None, text1, text2).ratio()

# Convert to percentage
similarity_percentage = sequence_score * 100

# Print the result
print(f"Both are {similarity_percentage:.2f}% Similar")


# Dissimilarity 

text3= "My name is Sikandar Ali Laghari"
text4 = "I am the founder of KaiSik Coding Club"
#calculate the similarity ratio 
sequence_score = SequenceMatcher(None, text3, text4).ratio()
# Convert to Percentage 
similarity_percentage = sequence_score * 100
#print the result
print(f"Both are{similarity_percentage:.2f} % similar")
