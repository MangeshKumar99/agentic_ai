import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hey there, I am Mangesh"
tokens = enc.encode(text)
# [25216, 1354, 11, 357, 939, 391, 8273, 71]
print(tokens)
text = enc.decode(tokens)
# Hey there, I am Mangesh
print(text)