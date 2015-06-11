#extra exercise
print "see, I have finished the extra assignment."

# week 1 exercise
# the code below almost works
print "hello world"

# week 2 exercise 1
# The code below almost works

name = raw_input("Enter your name")
print "Hello",name

# week 2 exercise 2
# This first line is provided for you

hrs = raw_input("Enter Hours:")
fhrs = float(hrs)
rate = raw_input("Enter rate:")
frate = float(rate)
pay = fhrs*frate
print pay

# week 3 exercise 1
hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
if h <= 40:
    pay = h*r
if h > 40:
    pay = 40*r+(h-40)*r*1.5
print pay

# week 3 exercise 2
score = raw_input("Enter a score:")
fscore = float(score)
if 1.0>=fscore>=0.9: 
        print "A"
if 0.9>fscore>=0.8:
        print "B"
if 0.8>fscore>=0.7:
        print "C"
if 0.7>fscore>=0.6:
        print "D"
if 0.0<=fscore<0.6:
        print "F"
elif fscore>=1.0|fscore<=0.0:
    print "Error"

# week 4 exercise
def computepay(h,r):
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    r = 10.50
    if h<=40:
        pay = h*r
    if h>40:
        pay = 40*r+(h-40)*r*1.5
    else: 
        print "Error."
    return pay
p = computepay(45,10.5)
print p

# week 5 exercise
largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        inum = int(num)
    except:
        print "Invalid input"
        continue
    for i in [inum]:
        if largest is None:
            largest = i
        elif i > largest:
            largest = i
    for i in [inum]:
        if smallest is None:
            smallest = i
        elif i < smallest:
            smallest = i
print "Maximum is", largest
print "Minimum is", smallest


# week 6 exercise
text = "X-DSPAM-Confidence:    0.8475";
a=text.find('0')
b=text.find('5')
r=text[a:b+1];
result=float(r)
print result

# week 7 exercise
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
	line=line.rstrip()
	print line.upper()

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
x=0
for line in fh:    
    if line.startswith("X-DSPAM-Confidence:") : 
        extract=str(line)
        fextract=float(extract[20:])
        x=x+fextract
        count=count+1
print "Average spam confidence:",float(x)/float(count)

# week 8 exercise

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words=line.split()    
    for word in words:
		if word in lst:continue
		else:
			lst.append(word)
lst.sort()
print lst

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
		count = count + 1
		words = line.split()
		print words[1]
print "There were", count, "lines in the file with From as the first word"

# week 9 exercise

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
senders=[]
for line in handle:
    line=line.rstrip()
    if line.startswith('From '):
        words = line.split()
        senders.append(words[1])
        
counts=dict()
for sender in senders:
    counts[sender]=counts.get(sender,0)+1
    
bigcount=None
bigsender=None
for sender,count in counts.items():
    if bigcount is None or count>bigcount:
        bigsender=sender
        bigcount=count

#or bigcount=max((count.values()))
#or bigsender=list(count.keys())[list(count.values().index(bigcount))]
        
print bigsender,bigcount
    

