#! python2
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    
states = list(capitals.keys())
    
quizes = 35

for quiz in range(quizes):
    quizFile = open('quizes\\quiz%s.txt' % (quiz + 1), 'w')
    ansFile = open('answers\\quiz%s_answers.txt' % (quiz + 1), 'w')
    
    quizFile.write('Name:'.ljust(30, '_') + '\n' + 'Date:'.ljust(30, '_') + '\n\n' + 'State Capitals Quiz'.center(30) + '\n\n\n')
    
    random.shuffle(states)
    
    for i in range(len(states)):
        quizFile.write('Q%s: %s\n' % (str(i+1), states[i]))
        correct = capitals[states[i]]
        others = list(capitals.values())
        del others[others.index(correct)]
        ans = random.sample(others, 3) + [correct]
        random.shuffle(ans)
        ansFile.write('Q%s: %s\n' % (str(i + 1), 'ABCD'[ans.index(correct)]))
        for j in range(len(ans)):
            quizFile.write('\t%s\t%s\n' % ('ABCD'[j], ans[j]))
        quizFile.write('\n')
    
    quizFile.close()
    ansFile.close()