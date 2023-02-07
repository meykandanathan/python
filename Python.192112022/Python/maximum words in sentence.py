def maxNumOfWords(sentences):
    words = [sentence.split() for sentence in sentences]
    return max(len(word_list) for word_list in words)

sentences1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print("the first sentence has:", maxNumOfWords(sentences1),"words") 

sentences2 = ["please wait", "continue to fight", "continue to win"]
print("the second sentence has:", maxNumOfWords(sentences2),"words") 

sentences3 = ["the heads", "of", "two", "sorted linked lists"]
print("the third sentence has:", maxNumOfWords(sentences3),"words") 
