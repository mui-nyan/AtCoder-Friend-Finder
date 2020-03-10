
def matching(twitter_users, atcoder_users):
    len_twitter_users = len(twitter_users)
    len_atcoder_users = len(atcoder_users)

    left = 0
    right = 0

    ret = []

    while left < len_twitter_users and right < len_atcoder_users:
        if twitter_users[left]["id"] == atcoder_users[right]["twitter_id"]:
            ret.append({
                "atcoder_id": atcoder_users[right]["atcoder_id"],
                "twitter_id": twitter_users[left]["id"],
                "twitter_name": twitter_users[left]["name"],
            })
            left += 1
            right += 1
        elif twitter_users[left]["id"] < atcoder_users[right]["twitter_id"]:
            left += 1
        else:
            right += 1

    return ret
