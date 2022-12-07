from cohorts.models import CohortUser
from commons.redis import performRedisOps
from commons.cost_tracker import track_db_hit

def fetchRankListFromDB(cohort_id):
    """
    Please don't update this method. Use this method to get scoreboard from DB.
    Parameters:
        cohort_id (int): CohortId
  
    Returns:
    list: list of tuple with (email, score) sorted by score desc
        ex: [('user1@example.com', 100), ('user2@example.com', 10)]
    """

    track_db_hit()
    return CohortUser.objects.filter(
        score__gt=0,
        cohort_id=cohort_id
    ).order_by('-score').values_list('user__email', 'score')


def FetchRankList(cohort_id):
    """
    Fetch Rank list of Cohort
    Parameters:
        cohort_id (int): CohortId
  
    Returns:
    list: list of tuple with (email, score) sorted by score desc
        ex: [('user1@example.com', 100), ('user2@example.com', 10)]
    """
    # Complete this function, using given helper functions 'performRedisOps' and 'fetchRankListFromDB'
    pass


def updateUserRank(user_email, cohort_id, new_score):
    """
    Update Rank list in Cache, shouldn't make call to DB.
    Parameters:
        user_email (str): Email for User whose score is updated in DB.
        cohort_id (int): CohortId
        cohort_id (int): Assigned Score
    """
    # Complete this function
    pass
