
#capitalized string
string = "python is awesome."

capitalized_string = string.capitalize()

print('old string: ', string)
print('capitalized sting:',capitalized_string)
print()

#centered string
new_string = string.center(24)

print("centered string: ", new_string)
print()
#lower case string using casefold
string2 = "PYTHON IS AWESOME"

print("Lowercase string:",string2.casefold())
print()
#String count
string3 = "Python is awesome, isn't it?"

substring = "is"

count = string3.count(substring)
print("the count is:", count)
print()

#string endswith.
text = "python is easy to learn."

result = text.endswith("to learn")
#output is Faulse
print(result)

result = text.endswith("to learn.")
#output is True
print(result)
print()

#string Expandtabs
str = 'xyz\t12345\tabc'

result=str.expandtabs()

print(result)
print()

#string encode
string4 = 'pythön!'
print('The string is:', string4)
# default encoding to utf-8
string_utf = string4.encode()
# result
print('The encoded version is:', string_utf)
print()

#string Find
quote = 'Let it be, let it be, let it be'

result = quote.find('let it')
print("Substring 'let it':", result)

result = quote.find('small')
print("Substring 'small ':", result)

if  (quote.find('be,') != -1):
  print("Contains substring 'be,'")
else:
  print("Doesn't contain substring")
  print()

#string format
  # default arguments
print("Hello {}, your balance is {}.".format("Sir Rauf", 222445))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Sir Rauf", 222445))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Sir Rauf", blc=222445))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Sir Rauf", blc=222445))
print()

#string index
sentence = 'Python programming is fun.'

result = sentence.index('is fun')
print("Substring 'is fun':", result)
print()

# string inalnum
name = "ajh343h5jh"
print(name.isalnum())


name2 = "Ahh2285 jhcn "
print(name.isalnum())

name3 = "AUhurwu2yrwy9222"
print(name.isalnum())

name4 = "133"
print(name.isalnum())
print()

#string alpha
name = "SirRauf"
print(name.isalpha())


name = "kingkong"
print(name.isalpha())

# contains number
name = "jhonwhick3"
print(name.isalpha())
print()

#string is Decimal
s = "28212"
print(s.isdecimal())

# contains alphabets
s = "32ladk3"
print(s.isdecimal())
print()

#string is digits
s = "2728"
print(s.isdigit())

# contains alphabets
s = "fast5"
print(s.isdigit())
print()

#isidentifier
str = 'Python'
print(str.isidentifier())

str = 'Py thon'
print(str.isidentifier())

str = '22Python'
print(str.isidentifier())

str = ''
print(str.isidentifier())
print()

# lowercase
s = 'PYTHON IS EASY'
print(s.lower())
print()

# Title
s = 'python is easy'
print(s.title())
print()


string = "python is easy!"
print(string.upper());
print()

# Join method
numList = ['1', '2', '3', '4']
seperator = ', '
print(seperator.join(numList))

numTuple = ('5', '6', '7', '8')
print(seperator.join(numTuple))
print()

#Lower case
# example string
string = "THIS SHOULD BE LOWERCASE!"
print(string.lower())

# string with numbers
# all alphabets whould be lowercase
string = "Th!s Sh0uLd B3 L0w3rCas3!"
print(string.lower())
print()

#Upper case
# example string
string = "this should be uppercase!"
print(string.upper())

# string with numbers
# all alphabets whould be lowercase
string = "Th!s Sh0uLd B3 uPp3rCas3!"
print(string.upper())
print()

#swapcase
# example string
string = "THIS SHOULD ALL BE LOWERCASE."
print(string.swapcase())

string = "this should all be uppercase."
print(string.swapcase())

string = "ThIs ShOuLd Be MiXeD cAsEd."
print(string.swapcase())
print()

#Partition
string = "Python is fun"

# 'is' separator is found
print(string.partition('is '))

# 'not' separator is not found
print(string.partition('not '))

string = "Python is fun, isn't it"

# splits at first occurence of 'is'
print(string.partition('is'))
print()

#Replace
song = 'cold, cold heart'
print (song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'

'''only two occurences of 'let' is replaced'''
print(song.replace('let', "don't let", 2))
print()

#zFill
text = "program is fun"
print(text.zfill(15))
print(text.zfill(20))
print(text.zfill(10))
print()

#Format map
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))
print()


# get input from user
inputString = input()
print('The inputted string is:', inputString)
print()


# integer
print("int(123) is:", int(123))

# float
print("int(123.23) is:", int(123.23))

# string
print("int('123') is:", int('123'))
print()

#Iterator
# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

vowelsIter = iter(vowels)

# prints 'a'
print(next(vowelsIter))

# prints 'e'
print(next(vowelsIter))

# prints 'i'
print(next(vowelsIter))

# prints 'o'
print(next(vowelsIter))

# prints 'u'
print(next(vowelsIter))
print()

#Length
testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))
print()

#Maximum
# using max(arg1, arg2, *args)
print('Maximum is:', max(1, 3, 2, 5, 4))

# using max(iterable)
num = [1, 3, 2, 8, 5, 10, 6]
print('Maximum is:', max(num))
print()


#Minimum
# using min(arg1, arg2, *args)
print('Minimum is:', min(1, 3, 2, 5, 4))

# using min(iterable)
num = [3, 2, 8, 5, 10, 6]
print('Minimum is:', min(num))
print()

#Reversed
# for string
seqString = 'Python'
print(list(reversed(seqString)))

# for tuple
seqTuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seqTuple)))

# for range
seqRange = range(5, 9)
print(list(reversed(seqRange)))

# for list
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))
print()

#sorted
# vowels list
pyList = ['e', 'a', 'u', 'o', 'i']
print(sorted(pyList))

# string 
pyString = 'Python'
print(sorted(pyString))
print()

# sum
numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbersSum = sum(numbers)
print(numbersSum)

# start = 10
numbersSum = sum(numbers, 10)
print(numbersSum)
print()"# Assingment-" 
