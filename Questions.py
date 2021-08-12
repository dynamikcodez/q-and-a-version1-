from collections import OrderedDict

class questions():
    """Main question class, allows for adding and 
    updating questions and answers"""
    # Dict of questions and answers, updated at each (new) instance
    question_dict = OrderedDict()
    # list question_dict to allow for easy indexing
    question_list = list(question_dict.items())
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        questions.question_dict[self.question] = self.answer
        questions.question_list = list(self.question_dict.items())
        # print("Made ", self.question_list)
    
    def __str__(self):
        return str(f"(Question:{self.question}), (Answer:{self.answer})")
    
    def update_question(self, new_question):
        """update current question"""
        # since the questions.question_list is a tuple and i tend to update an index of it
        new_question_list = [] 
        for question in questions.question_list:
    # question[0] is the index of the question of the questions instance while question[1] the answer
            if self.question == question[0]: # targeting the (question)index to be changed
                question = (new_question,question[1])
            new_question_list.append(question)
    # updating questions.question_list and dict 
        questions.question_list = new_question_list
        questions.question_dict = OrderedDict(questions.question_list)
    # actually updating the instance of the question 
        self.question = new_question
        return self.question
        
    def update_answer(self, new_answer):
        """update current answer"""
        # since the questions.question_list is a tuple and i tend to update an index of it
        new_answer_list = [] 
        for answer in questions.question_list:
    # answer[1] is the index of the answer of the questions instance while answer[0] the question
            if self.answer == answer[1]: # targeting the (answer)index to be changed
                answer = (answer[0], new_answer)
            new_answer_list.append(answer)
    # updating questions.question_list and dict 
        questions.question_list = new_answer_list
        questions.question_dict = OrderedDict(questions.question_list)
    # actually updating the instance of the question 
        self.answer = new_answer
        return self.answer
        
    def details(self):
        """View current question and answer of question instance"""
        print(f" Question:{self.question} , {self.answer} ")
    
    
    def view_all():
        print(questions.question_dict)
        
    def delete(self):
        del self 
        

q1 = questions("What is ", "a thing is")

q1.update_question("What is not")
print(q1.question)
q1.update_answer("That which was or never is")
q2 = questions("What is red", "Anything that is not not red")
q1.delete()
questions.view_all()



# make a proper delete method