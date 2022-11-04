from fastapi import FastAPI 
from deta import Deta
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
import collections
import time

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

############## for post requests #############
class Quiz(BaseModel):
    name: str 
    score: int 

################### helper functions ##################
def get_quiz_scores(scores):
    response = {}
    for score in scores:
        response[score['name']] = score['score']
    return response

def get_scores(q1, q2, q3, q4):
    scores_dict = collections.defaultdict(list)
    s1 = q1.fetch()
    s2 = q2.fetch()
    s3 = q3.fetch()
    s4 = q4.fetch()
    for score in [s1._items, s2._items, s3._items, s4._items]:
        add_to_scores(scores_dict, score)
    
    for person in scores_dict:
        length = len(scores_dict[person])
        total = sum(scores_dict[person])
        scores_dict[person] = total/length

    return scores_dict
  
def add_to_scores(scores_dict, scores):
    for score in scores:
        scores_dict[score['name']].append(score['score'])

################### gaining access to dbs #################
while True:
    try:
        deta = Deta('b012fbqh_9oJ7mfAusXwewwjaHww2zoQvZJFhqiD7')
        users = deta.Base('users')
        q1 = deta.Base('q1')
        q2 = deta.Base('q2')
        q3 = deta.Base('q3')
        q4 = deta.Base('q4')
        break
    except Exception as error:
        print('failed to connect')
        print('error', error)
        time.sleep(2)
        
################ entry #####################
@app.get('/')
def home_page():
    results = {'endpoints': {'get': ['q1', 'q2', 'q3', 'q4', 'all_scores_average'], 'post': ['q1', 'q2', 'q3', 'q4']}}
    print('loser')
    return results

################ verify user ####################
@app.get('/users')
def verify_user():
    results = users.fetch()
    print('loser')
    return results._items


################## quiz 1 #########################
@app.get('/q1')
def q1_get():
    scores = q1.fetch()
    scores = get_quiz_scores(scores._items)
    return scores

@app.post('/q1')
def q1_post(quiz: Quiz):
    quiz = quiz.dict()
    try:
        q1.insert({'name': quiz['name'], 'score': quiz['score'], 'key': quiz['name']+quiz['name']})
        return 1
    except:
        return 2
 
################## quiz 2 #########################
@app.get('/q2')
def q2_get():
    scores = q2.fetch()
    scores = get_quiz_scores(scores._items)
    return scores

@app.post('/q2')
def q2_post(quiz: Quiz):
    quiz = quiz.dict()
    try:
        q2.insert({'name': quiz['name'], 'score': quiz['score'], 'key': quiz['name']+quiz['name']})
        return 1
    except:
        return 2
        

################## quiz 3 #########################
@app.get('/q3')
def q3_get():
    scores = q3.fetch()
    scores = get_quiz_scores(scores._items)
    return scores

@app.post('/q3')
def q3_post(quiz: Quiz):
    quiz = quiz.dict()
    try:
        q3.insert({'name': quiz['name'], 'score': quiz['score'], 'key': quiz['name']+quiz['name']})
        return 1
    except:
        return 2


################## quiz 4 #########################
@app.get('/q4')
def q4_get():
    scores = q4.fetch()
    scores = get_quiz_scores(scores._items)
    return scores

@app.post('/q4')
def q4_post(quiz: Quiz):
    quiz = quiz.dict()
    try:
        q4.insert({'name': quiz['name'], 'score': quiz['score'], 'key': quiz['name']+quiz['name']})
        return 1
    except:
        return 2


################## user average #########################
@app.get('/all_scores_average')
def all_scores_average():
    return get_scores(q1, q2, q3, q4)

