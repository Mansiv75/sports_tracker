import redis

redis_client=redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

LEADERBOARD_KEY="leaderboard"

def update_leaderboard(team_name,score):
    redis_client.zincrby(LEADERBOARD_KEY,score,team_name)

def get_top_teams(limit=5):
    top_teams=redis_client.zrevrange(LEADERBOARD_KEY, 0, limit-1, withscores=True)
    return [{"team":team.decode(),"score":int(score)} for team, score in top_teams]