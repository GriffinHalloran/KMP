#Get input from users. Must be in quotations
string = input("Enter a string of characters: ")
sub = input("Enter a word to see if it is a substring of the provided string: ")

j = 0
i = 0
posList = []

pos = 1
cnd = 0

T = []

#set up prefix / suffix table
for i in range(len(sub)):
    if i == 0:
        T.append(-1)
    else:
        T.append(0)

#Create the table
while pos < len(sub):
    if sub[pos] == sub[cnd]:
        T[pos] = T[cnd]
    else:
        T[pos] = cnd
        cnd = T[cnd]
        while cnd >= 0 and sub[pos] is not sub[cnd]:
            cnd = T[cnd]
    pos += 1
    cnd += 1

T.append(cnd)


#Tell if the word is a substring in O(n) time
while j < len(string):
    if sub[i] == string[j]:
       j += 1
       i += 1
       if i == len(sub):
          posList.append(j - i)
          i = T[i]
    else:
          i = T[i]
          if i < 0:
             j += 1
             i += 1

#Print if substring was found
if len(posList) > 0:
    print("Substring Found at the following position(s)!")
    print(posList)
else:
    print("The word is not a substring")

print(sub)
print(string)
            
            
