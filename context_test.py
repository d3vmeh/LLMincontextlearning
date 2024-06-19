from openai import OpenAI

count = 1
while True:
    question = input("Please enter a prompt: ")
    if question.lower() == "exit":
        break
    
    file = open("context.txt",'r',encoding="utf8")
    context = file.read()
    file.close()


    client = OpenAI()

    f = open("response.txt",'w')


    # completion = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    # messages=[
    #     {"role": "system", 
    #      "content": """Use only the context below and the conversation with the user to answer this question, 
    #      do not use your prior knowledge under any circumstance. If you do not know the answer, say I do not know, do not guess. Context weight 
    #      is the number that appears before the words User Question. The greater the Context Weight, the more relevant that question and the response following it are to the response you will create.
        
    #      Context is below:
    #      =======
    #      {context}
         
    #      """},
        
    #     {"role": "user", "content": question}
    # ]
    # )

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Use only the context below and the conversation with the user to answer this question, "+
         "do not use your prior knowledge under any circumstance. If you do not know the answer, say I do not know, do not guess. Context weight "+
         "is the number that appears before the words User Question. The greater the Context Weight, the more relevant that question and the response following it are to the response you will create." + 
         "Context: " + context},
        {"role": "user", "content": question}
    ]
    )


    response = completion.choices[0].message.content
    f.write(response+'\n')
    print(response)
    f.close()

    c = open("context.txt",'a',encoding="utf8")
    c.write('\n')
    c.write("Context Weight: " + str(count)+"\nUser Question: " + question)
    c.write("\nYour answer to the question: "+response)
    c.write("\n\n")
    c.close()
    
    count += 1


