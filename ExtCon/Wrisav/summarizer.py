import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

# text = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
# A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
# Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
# In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
# Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
# 2010 marriage license application, according to court documents.
# Prosecutors said the marriages were part of an immigration scam.
# On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
# After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
# Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
# All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
# Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
# Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
# The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
# Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
# Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
# If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
# """
# text = There are times when the night sky glows with bands of color. The bands may begin as cloud shapes and then spread into a great arc across the entire sky. They may fall in folds like a curtain drawn across the heavens. The lights usually grow brighter, then suddenly dim. During this time the sky glows with pale yellow, pink, green, violet, blue, and red. These lights are called the Aurora Borealis. Some people call them the Northern Lights. Scientists have been watching them for hundreds of years. They are not quite sure what causes them. In ancient times people were afraid of the Lights. They imagined that they saw fiery dragons in thesky. Some even concluded that the heavens were on fire.

text = " Hi! This is Arpan. Hi! This is Subhodeep. Hi! This is Srikanta. Hi! This is Wrishav."

# Tokenizing the text 
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 

# Frequency table to keep score of each word 
freqTable = dict() 
for word in words: 
	word = word.lower() 
	if word in stopWords: 
		continue
	if word in freqTable: 
		freqTable[word] += 1
	else: 
		freqTable[word] = 1

# Dictionary to keep score of each sentence 
sentences = sent_tokenize(text) 
sentenceValue = dict() 

for sentence in sentences: 
	for word, freq in freqTable.items(): 
		if word in sentence.lower(): 
			if sentence in sentenceValue: 
				sentenceValue[sentence] += freq 
			else: 
				sentenceValue[sentence] = freq 


sumValues = 0
for sentence in sentenceValue: 
	sumValues += sentenceValue[sentence] 

# Average value of a sentence from the original text 
average = int(sumValues / len(sentenceValue)) 

# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
		summary += " " + sentence 
print(summary) 
