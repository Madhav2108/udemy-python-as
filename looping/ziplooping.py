questions = ['name', 'age', 'skills'] 
answers = ['Maddy', '20', 'web developer'] 
for question, answer in zip(questions, answers): 
    print('What is your {0}?  I am {1}.'.format(question, answer))