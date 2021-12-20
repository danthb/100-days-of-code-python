
punctuations = '\'!()-[]{};:\'\"\,<>./?@#$%^&*_~\''
    
file_contents = '''Thank you. Thank you, thank you,-[]{};: thank you. It’s good to be back. As Mitch and Chuck will understand, it’s good to be almost home, down the hall. Anyway, thank you all. Madam Speaker, Madam Vice President. No president has ever said those words from this podium. No president has ever said those words. And it’s about time. The first lady, I’m her husband. Second gentleman. Chief justice. Members of the United States Congress and the cabinet, distinguished guests. My fellow Americans. While the setting tonight is familiar, this gathering is just a little bit different. A reminder of the extraordinary times we’re in. Throughout our history, presidents have come to this chamber to speak to Congress, to the nation and to the world. To declare war, to celebrate peace, to announce new plans and possibilities. '''
    
uninteresting_words = ["the", "a", "[]{}", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "our", "our", "ours", "you", "your", "your", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
# LEARNER CODE START HERE

#cleaning string
punctuations_list = list(punctuations)
list_file_contents = file_contents.split(' ')
str_words0 = ' '.join(char for char in list_file_contents if (char.isalnum() and char not in punctuations_list))
str_words = str_words0.split(' ')
str_words_join = (' '.join(char0 for char0 in str_words if char0 not in uninteresting_words)).lower()
words = str_words_join.split(' ')

#Counting and adding to dict
wordCount = {}
for word in words:
    if (word in wordCount):
        continue;
    else:
        counter = words.count(word)
        wordCount[word] = counter;

""" print(wordCount) """

# Sort dictionary 
wordCount1 = {}
sort_orders = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
	wordCount1[i[0]] = i[1]

print(wordCount1)


#Transform dict to array
""" temp = []
dictList = []

for key, value in wordCount.items():
    temp = [key,value]
    dictList.append(temp)

print(dictList) """