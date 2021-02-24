import sys
import re


#This function is O(nlogn) it has to sort all the tokens first
#alphabetically then it sorts all of the tokens by frequency
def print_data(tokens):
    for k,val in sorted(sorted(tokens.items(),key = lambda x: x[0]),key = lambda x: x[1],reverse = True):
        print("{0}\t{1}").format(k, val)

def removeLinks(line):
    newLine = re.sub("(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?","",line)
    return newLine

#This function runs in O(n) it only reads through the line once when it
#splits the line into individual words
def tokenize(fn):
    tokens = dict()
    for line in fn:
        line  = removeLinks(line)
        words = re.split('[^a-z0-9]', line.lower())
        for word in words:
            if word not in tokens and word != '' and len(word)>2:
                tokens[word] = 1
            elif word != '' and len(word)>2:
                tokens[word] += 1
    return tokens


#This function runs in O(n) the tokenize function runs in O(n)
#time complexity.
def read_file(file_name):
    fn = open(file_name, 'r')
    tokens = tokenize(fn)
    fn.close()
    return tokens


#This function runs in O(1) time complexity all it is doing is assigning
#a string to a variable
def get_file_name(sav):
    return "{0}".format(sav[1])
    


#This function runs in O(n) time complexity of the read_file function call
#inside of that read_file function the tokenize function is called.
def main():
    #sys.argv python command line agrument
    file_name = get_file_name(sys.argv)
    tokens = read_file(file_name)
    print_data(tokens)

if __name__=="__main__":
    main()
