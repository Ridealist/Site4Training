# python manage.py shell 실행
# 아래 내용 실행

from search.models import Training
import pandas as pd
import re

def load_data():
    Training.objects.all().delete()

    path = 'C://Users/Junbo Koh/PycharmProjects/pythonProject/jbksite/search/dataset/class_list.csv'
    cl = pd.read_csv(path, encoding='utf-8')
    cl['desc'] = cl['purpose']+cl['summary']
    try:
        cl['desc'] = cl['desc'].apply(lambda x: re.sub('[^가-힣]', ' ', x))
        cl['desc'] = cl['desc'].apply(lambda x: x.strip())
    except:
        pass
    Training.objects.bulk_create([
        Training(
            title=cl.iloc[i]['title'],
            website=cl.iloc[i]['website'],
            type=cl.iloc[i]['lesson_type'],
            description=cl.iloc[i]['desc'],
            time=cl.iloc[i]['learning_time'],
            price=cl.iloc[i]['price'],
            url=cl.iloc[i]['url'],
            image='/static/img/' + cl.iloc[i]['image']
        )
        for i in range(len(cl))
    ])


# https://dev-yakuza.posstree.com/ko/django/data-seed/
# json 형식으로 테스트(마스터) 데이터 넣는 방법

# def sort_value(column):
#     queryset = Training.objects.all()
#     query_list = [tr for tr in queryset]
#     query_list
#
#     for i in range(n_rec):
#         v_s.append(Training.objects.all()[i].col)
#     value_array = pd.Series(v_s).unique()
#
#     return value_array

