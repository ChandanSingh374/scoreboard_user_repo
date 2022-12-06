from cohorts.models import CohortUser
from commons.redis import performRedisOps
from commons.cost_tracker import track_db_hit

def fetchRankListFromDB(cohort_id):
    track_db_hit()
    return CohortUser.objects.filter(
        score__gt=0,
        cohort_id=cohort_id
    ).order_by('-score').values_list('user__email', 'score')

def FetchRankList(cohort_id):
    return fetchRankListFromDB(cohort_id)

def updateUserRank(user_email, cohort_id, new_score):
    pass
