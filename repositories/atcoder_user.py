

cache = None

def load_twitter_id_atcoder_user_dict():
    global cache
    if cache is not None:
        return cache

    users = {}

    with open("./data/users.tsv") as f:
        for s in f:
            if len(s.strip()) == 0 :
                continue
            tmp = s.strip().split("\t")
            if len(tmp) < 2:
                continue
            users[tmp[1]] = {
                "atcoder_id": tmp[0],
                "twitter_id": tmp[1],
                "rating": int(tmp[2]),
                "profile_img": tmp[3],
            }
    
    cache = users
    return users
