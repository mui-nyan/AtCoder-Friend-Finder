def load_atcoder_users():
    with open("./data/users.tsv") as f:
        for s in f:
            if len(s.strip()) == 0 :
                continue
            tmp = s.strip().split("\t")
            if len(tmp) < 2:
                continue
            yield {
                "atcoder_id": tmp[0],
                "twitter_id": tmp[1]
            }
