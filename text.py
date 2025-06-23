#text = "How are you" 
text = input("Give me the text: ")

#Print the sentence in uppercase and lowercase.
a = text.upper()
b = text.capitalize()
c = text.split()
#d = "the nummber of letter are :", len(text)----> ('the nummber of letter are :', nummber)
e = text.split()
e = e[::-1]
f =  text.capitalize()
f = text.replace(",", "")
f = text.replace(" ", "")
f = text.replace(".", "")
f = text.replace("!", "")
f = text.replace("?", "")
g = text.replace(" ","-")

print(f"The sentence in uppercase and lowercase:\n{a}\n{b}")

#Count how many words are in the sentence.
print("the nummber of letter are :", len(text))#----> the nummber of letter are : nummber

#Print the sentence in reverse order.
print("The sentence in reverse order:")
print(e)
for i in e:
    print (i + " ")
    
#Check if the sentence is a palindrome (ignore spaces and case)
print(f)
if f == f[::-1]:
    print("this is a palindrome")
elif f != f[::-1]:
    print("It isn't a palindrome") 
#Replace all spaces with dashes -.
print("Replaced all spaces with dashes -:")
print(g)
