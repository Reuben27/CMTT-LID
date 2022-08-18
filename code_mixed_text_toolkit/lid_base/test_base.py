from getLanguage import langIdentify
import os
os.system("echo x")

os.environ["MALLET_HOME"] = "D:\Projects\Web-Development-Projects\Code-Mixed-Text-Toolkit\code_mixed_text_toolkit\lid\mallet-2.0.8\\"

# inputText is a list of input sentences
# classifier is the name of the mallet classifier to be used

def bitch():
  print(langIdentify("""han voh bhi baat hai""", "classifiers/HiEn.classifier"))
  return "hi"