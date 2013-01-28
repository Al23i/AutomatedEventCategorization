import sys
import operator
import re
import math
class CatInfo:
    def __init__(self):
        self.hash = {}
        self.total = 0
        self.wordcount = 0.0
def makeHash(filename, wordcount):
	f = open(filename, 'rU')
	Livetext = f.read()
    	f.close()
    	info = CatInfo()
    	info.wordcount = wordcount
	matches = re.findall('([\d]+)[\s]+([A-Za-z]+).*?\n', Livetext)
    	i = 0
        for match in matches:
            info.hash[match[1]] = [match[0], i,]
            info.total +=1
            i+=1
    	print  'the number of matches is ' + str(info.total)
	return info
def tfIdf(categoryHash, opponentInfo, opponentInfo2):
	#music is
	results = {}
	for key in categoryHash.hash.keys():
        	count = 1
		if opponentInfo.hash.has_key(key):
            		rank = float(opponentInfo.hash[key][1])
            		rank = rank/float(opponentInfo.total)
            		if(rank < 0.25):    
                		count +=1
            		if(rank < 0.50):
                		count +=1
            		if(rank < 0.75):
                		count+=1
            		count+=1
        	if opponentInfo2.hash.has_key(key):
            		rank = float(opponentInfo2.hash[key][1])
            		rank = rank/float(opponentInfo2.total)
            		if(rank < 0.25):    
                		count +=1
            		if(rank < 0.50):
                		count +=1
            		if(rank < 0.75):
                		count+=1
            		count+=1
        	idf = math.log(9/count)
		tf = float(categoryHash.hash[key][0])
        	multiple = float(435928)
        	multiple = multiple/categoryHash.wordcount
		total = tf*idf
        	categoryHash.hash[key].append(total)
	for key, value in categoryHash.hash.items():
		results[key] = value[2]	
	sorted_x = sorted(results.iteritems(), key=operator.itemgetter(1), reverse=True)
	f = open('sportsTfIdf.txt', 'w')
	j =1
	for tuple in sorted_x:
		f.write(str(j)+ ': ' + tuple[0] + ' ' +  str(tuple[1])+ '\n')
		j +=1
	f.close()		
    	return
def main():
	musicTotal = float(198741)
	musicInfo= makeHash('musicwords.txt', musicTotal)
	sportsTotal = float(61771)
    	sportsInfo = makeHash('Sportingwords.txt', sportsTotal)
    	learningInfo = makeHash('lecturewords.txt', float(435928))
    	tfIdf(sportsInfo, musicInfo, learningInfo)

if __name__ == '__main__':
  main()

