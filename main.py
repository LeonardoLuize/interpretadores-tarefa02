import re

def readFile(filename: str):
    with open(filename, "r") as newFile:
        return newFile.readlines()

def verifyStrings(filename: str):
  file = readFile(filename)
  
  file.pop(0)
  print(f"{filename.replace('.txt', '').capitalize()}")

  for line in file:
    verify(line)
    print("\n")

def verifyFormula(sentence, index):
  try:
    if sentence[index + 1] == "OperadorBinario":
      if sentence[index + 2] == "Proposicao" and sentence[index + 3] == "Proposicao" and sentence[index + 4] == "FechaParen":
        return True
        
    if sentence[index + 1] == "OperadorUnario":
      if sentence[index + 2] == "Proposicao" and sentence[index + 3] == "FechaParen":
        return True
  
      return False  
  except:
    return False
      

def verify(line):
  sentence = []
  operator = ""
  prop = ""
  operations = ["\\neg", "\\wedge", "\\vee", "\\rightarrow", "\\leftrightarrow"]
  
  for letter in line:
    if letter == "T" or letter == "F":
      sentence.append("Constante")
      continue
    if letter == "(":
      sentence.append("AbreParen")
    elif letter == ")":
      sentence.append("FechaParen")
    elif letter == "\\":
      operator = "\\"
    elif re.match("[a-z0-9]+", letter):
      if re.match("\\\\", operator):
        operator = operator + letter
        continue

      sentence.append("Proposicao")

    for operation in operations:
      if "\\neg" == operator:
        sentence.append("OperadorUnario")
        operator = ""
      elif operation == operator:
        sentence.append("OperadorBinario")
        operator = ""


  isValid = True

  if operator != "":
    isValid = False

  sentenceIndex = 0
  for string in sentence:
    if string == "AbreParen":
      if not verifyFormula(sentence, sentenceIndex):
        isValid = False
        break
      else:
        break
    else:
      if len(sentence) != 1:
        if string != "Constante" or string != "Proposicao":
          isValid = False
          break
      
    

    sentenceIndex += 1
  
  print(f"{line}: {'valido' if isValid else 'inválido'}")
      
      
verifyStrings("entrada.txt")
verifyStrings("entrada2.txt")
verifyStrings("entrada3.txt")
