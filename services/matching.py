
def matching(twitter_users, atcoder_users):

    ret = []

    for twitter_user in twitter_users:
        atcoder_user = atcoder_users.get(twitter_user["id"], None)

        if atcoder_user is None:
            continue

        ret.append({
                "atcoder_id": atcoder_user["atcoder_id"],
                "twitter_id": twitter_user["id"],
                "twitter_name": twitter_user["name"],
            })

    return ret
