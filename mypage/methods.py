import pandas as pd
from .models import Training_List

# pip install openpyxl -> 설치해야 xlsx 파일 읽기 가능

def mk_mytraining(xlsx_file):

    df = pd.read_excel(xlsx_file)
    df.drop(columns=['순번', '연수\n성적', '직무\n관련성', '평점\n학점', '학년도별\n연수시간누계', '교육형태'], axis=1, inplace=True)

    def strip_start(a):
        ind = a.index('~')
        start = a[0:ind].strip()
        return start.replace('.', '-')

    def strip_end(a):
        ind = a.index('~')
        end = a[ind+1:].strip()
        return end.replace('.', '-')

    df['연수시작'] = df['연수기간'].apply(lambda x: strip_start(x))
    df['연수끝'] = df['연수기간'].apply(lambda x: strip_end(x))

    df.drop('연수기간', axis=1, inplace=True)
    df.columns = ['number', 'name', 'auth', 'time', 'type', 'period_st', 'period_end']

    def duration(b):
        from datetime import timedelta
        h = b[:b.index('시간')]
        m = b[b.index('분')-2 : b.index('분')].strip()
        t = timedelta(hours=int(h), minutes=int(m))
        # t = t.days*24 + t.seconds/60/60
        return t

    df['time'] = df['time'].apply(lambda x: duration(x))

    return df


def mk_db(df):
    Training_List.objects.all().delete()

    # own = request.user
    # for r in df.itertuples():
    #     My_Training(owner=own, number=r.number, name=r.name, auth=r.auth, period_st=r.period_st,
    #                 period_end=r.period_end, time=r.time, type=r.type).save()

    for i in range(len(df)):
        Training_List.objects.create(
            owner=request.user,
            number=df.iloc[i]['number'],
            name=df.iloc[i]['name'],
            auth=df.iloc[i]['auth'],
            period_st=df.iloc[i]['period_st'],
            period_end=df.iloc[i]['period_end'],
            time=df.iloc[i]['time'],
            type=df.iloc[i]['type']
        )