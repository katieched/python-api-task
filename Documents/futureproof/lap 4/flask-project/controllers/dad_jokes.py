# from werkzeug.exceptions import BadRequest

dad_jokes = [
    {'id': 1, 'joke': "Why do fathers take an extra pair of socks when they go golfing?", 'punchline': "In case they get a hole in one!"},
    {'id': 2, 'joke': "What do you call a fish wearing a bowtie?", 'punchline': "Sofishticated."},
    {'id': 3, 'joke': "What did the ocean say to the beach?", 'punchline': "Nothing, it just waved."},
    # {'id': 4, 'joke': "", 'punchline': ""},
    # {'id': 5, 'joke': "", 'punchline': ""},
    # {'id': 6, 'joke': "", 'punchline': ""},
    # {'id': 7, 'joke': "", 'punchline': ""}
]

def index(req):
    return [joke for joke in dad_jokes], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_joke = req.get_json()
    new_joke['id'] = sorted([dad_joke['id'] for dad_joke in dad_jokes])[-1] + 1
    dad_jokes.append(new_joke)
    return new_joke, 201


def find_by_uid(uid):
    try: 
        return next(dad_joke for dad_joke in dad_jokes if dad_joke['id'] == uid)
    except:       
        raise (f"We don't have a joke with id {uid}!")

