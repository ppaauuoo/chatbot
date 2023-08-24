from gpt4all import GPT4All
model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")
# output = model.generate("what is the biggest country?", max_tokens=100)
# print(output)

def chat(message: str):
    return model.generate(message, max_tokens=100)
