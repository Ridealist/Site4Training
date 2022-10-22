from elasticsearch_dsl.query import Q
from .documents import TrainDocument

def query_elastic(phrase, request):
    # 검색어
    if phrase is None:
        search = Q("match_all")
    else:
        search = Q(
            "multi_match",
            query=phrase,
            fields=['title^2', 'description']  ## title 필드 boosting 2배 가중치
        )

    # 사이트 선택
    if 'choice_site1' not in request.GET and 'choice_site2' not in request.GET :
        q_site = Q("match_all")
    else:
        if 'choice_site1' in request.GET:
            q1 = Q('term', website='아이스크림')
        else:
            q1 = Q("match_none")
        if 'choice_site2' in request.GET:
            q2 = Q('term', website='티처빌')
        else:
            q2 = Q("match_none")
        q_site = Q('bool', should = [q1, q2])

    # 강좌 종류
    if 'choice_type1' not in request.GET and 'choice_type2' not in request.GET and 'choice_type3' not in request.GET and 'choice_type4' not in request.GET and 'choice_type5' not in request.GET and 'choice_type6' not in request.GET and 'choice_type7' not in request.GET and 'choice_type8' not in request.GET and 'choice_type9' not in request.GET:
        q_type = Q("match_all")
    else:
        if 'choice_type1' in request.GET:
            q1 = Q('term', type='생활지도')
        else:
            q1 = Q("match_none")
        if 'choice_type2' in request.GET:
            q2 = Q('term', type='학습지도')
        else:
            q2 = Q("match_none")
        if 'choice_type3' in request.GET:
            q3 = Q('term', type='어학')
        else:
            q3 = Q("match_none")
        if 'choice_type4' in request.GET:
            q4 = Q('term', type='자기계발')
        else:
            q4 = Q("match_none")
        if 'choice_type5' in request.GET:
            q5 = Q('term', type='인문·교양')
        else:
            q5 = Q("match_none")
        if 'choice_type6' in request.GET:
            q6 = Q('term', type='교과지도')
        else:
            q6 = Q("match_none")
        if 'choice_type7' in request.GET:
            q7 = Q('term', type='ICT·스마트')
        else:
            q7 = Q("match_none")
        if 'choice_type8' in request.GET:
            q8 = Q('term', type='학급경영')
        else:
            q8 = Q("match_none")
        if 'choice_type9' in request.GET:
            q9 = Q('term', type='진로·인성')
        else:
            q9 = Q("match_none")
        q_type = Q('bool', should = [q1, q2, q3, q4, q5, q6, q7, q8, q9])

    # 연수 시간(학점)
    if 'choice_time1' not in request.GET and 'choice_time2' not in request.GET and 'choice_time3' not in request.GET and 'choice_time4' not in request.GET and 'choice_time5' not in request.GET:
        q_time = Q("match_all")
    else:
        if 'choice_time1' in request.GET:
            q1 = Q('term', time='5시간') | Q('term', time='7시간') | Q('term', time='8시간') | Q('term', time='10시간')
        else:
            q1 = Q("match_none")
        if 'choice_time2' in request.GET:
            q2 = Q('term', time='15시간')
        else:
            q2 = Q("match_none")
        if 'choice_time3' in request.GET:
            q3 = Q('term', time='30시간')
        else:
            q3 = Q("match_none")
        if 'choice_time4' in request.GET:
            q4 = Q('term', time='45시간')
        else:
            q4 = Q("match_none")
        if 'choice_time5' in request.GET:
            q5 = Q('term', time='60시간')
        else:
            q5 = Q("match_none")
        q_time = Q('bool', should = [q1, q2, q3, q4, q5])

    # 연수 가격
    if 'choice_price1' not in request.GET and 'choice_price2' not in request.GET and 'choice_price3' not in request.GET and 'choice_price4' not in request.GET:
        q_price = Q("match_all")
    else:
        if 'choice_price1' in request.GET:
            q1 = Q('range', price={'lte':0})
        else:
            q1 = Q("match_none")
        if 'choice_price2' in request.GET:
            q2 = Q('range', price={'gt':0, 'lte':50000})
        else:
            q2 = Q("match_none")
        if 'choice_price3' in request.GET:
            q3 = Q('range', price={'gt':50000, 'lte':100000})
        else:
            q3 = Q("match_none")
        if 'choice_price4' in request.GET:
            q4 = Q('range', price={'gt':100000})
        else:
            q4 = Q("match_none")
        q_price = Q('bool', should = [q1, q2, q3, q4])

    q_fin = Q('bool', must = [search, q_site, q_type, q_time, q_price])

    query = TrainDocument.search().query(q_fin) #.extra(min_score=11.0)
    return query.to_queryset()