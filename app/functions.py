import collections

def get_quiz_scores(supabase, q):
    scores = supabase.table(q).select('*').execute()
    response = {}
    for score in scores.data:
        response[score['name']] = score['score']
    return response

def get_scores(supabase):
    scores_dict = collections.defaultdict(list)

    scores_1 = supabase.table('q1').select('*').execute()
    scores_2 = supabase.table('q2').select('*').execute()
    scores_3 = supabase.table('q3').select('*').execute()
    scores_4 = supabase.table('q4').select('*').execute()

    for scores in [scores_1, scores_2, scores_3, scores_4]:
        add_to_scores(scores_dict, scores)

    response = {}
    for person in scores_dict:
        scores = scores_dict[person]
        new_score = sum(scores)/len(scores)
        response[person] = new_score

    
    return response
  
def add_to_scores(scores_dict, scores):
    scores = scores.data 
    for score in scores:
        scores_dict[score['name']].append(score['score'])
