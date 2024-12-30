import re

def preprocessing(str):
    text = re.sub('[-=+,#/\?:^$.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', '', str)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text

message1 = "WOW!! ThIs mOvIe...    was @@aMAZING@@!!     I couldn't BELIEVE how **good** the actors were.  The plot was    so~~ thrilling."
message2 = "Worst movie EVER!!!    I can't believe I spent $15 on this...    the acting was horrIBle, and the plot? non-existent!! :(  do NOT recommend.   :("

text1 = preprocessing(message1)
text2 = preprocessing(message2)

print(text1)

print(text2)

