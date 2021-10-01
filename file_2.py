file=open("pepole-txt","w")
file.write("francis=goa/n")
file.write("riya-francis/n ")
# file=open(\data.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))