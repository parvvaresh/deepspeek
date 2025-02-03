import ollama  


class deepseek:
    def __init__(self):
        self.model = 'deepseek-r1:1.5b'  
    
    def get_message(self, input):

        response = ollama.chat(model=self.model, messages=[  
            {  
                'role': 'user',  
                'content': input,  
            },  
        ])  

        ollama_response = response['message']['content']  
        return ollama_response


# just for test
# model = deepseek()
# while True:
    # q = input("please enter : \n")
    # print(model.get_message(q))
