# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)

str = "Mr Johnson"

def urlify(str):
  
  for i in range (len(str)):
    if str[i] == " ":
      str = str.replace(str[i], "%20")
  
  return str
  
print(urlify(str))
