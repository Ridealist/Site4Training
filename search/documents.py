from elasticsearch_dsl import analyzer, token_filter, tokenizer
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Training

## 토큰 필터

# 불용어 필터
stopfilter = token_filter(
    'stopfilter',
    type="stop",
    ignore_case=True,
    stopwords_path="user_dic/stopwords_trn.txt",
    # stopwords=[
    #     '수업', '학습', '교실', '학급', '강의' ## 전체 문서 countvector화 해서 다 빈도 단어 파일에 정리
    # ]                                     ## 구현 완료!
)

# 유의어 필터
synfilter = token_filter(
    'synfilter',
    type='synonym',
    synonyms=[                             ## 학습 목차 데이터까지 활용해 검색하면 일단은 어느정도는 구현
        '사진, 촬영, 디카, 셀카, 디지털카메라', ##(확장 방안) 강의 리뷰 데이터 긁어와서 키워드 추출해 연관어 파일에 정리
        'ai, 에이아이, 인공지능',
        '주식, 투자, 월급, 재무',
        '학급긍정훈육, 긍정훈육, 학급긍정훈육법, 긍정훈육법 => pdc'
    ],
)

# 품사 필터
posfilter = token_filter(
    'posfilter',
    type='nori_part_of_speech',
    stoptags = [
                "E", #//어미   ## 명사형 품사만 남도록 다른 pos들 제거
                "J", #//조사
                "IC",#//감탄사
                "NNB", #//종속 명사
                "NP", #//대명사
                "VV", #//동사
                "VA", #//형용사
                "MAG", "MAJ", #//부사
                "MM", #//관형사
                "SP", "SSC", "SSO", "SC", "SE",
                "VX", #//조동사
                "XPN", "XSA", "XSN", "XSV", #//보조 명사
                "UNA", "NA", "VSV", "VCP"
            ]
)

# 토큰길이 필터
lenfilter = token_filter(
    'lenfilter',
    type='length', ## 2글자 이상 토큰만 남도록
    min=2
)

# nori_user_dict = tokenizer(   ## user_dict 사용하는 별도 토크나이저 필요성??
#     'nori_user_dict',
#     type='nori_tokenizer',
#     decompound_mode='mixed'
# )

## 토크나이저
# nori_tokenizer
my_analyzer = analyzer(
    'my_analyzer',
    tokenizer='nori_tokenizer',
    decompound_mode='mixed',
    filter=[
        synfilter,
        stopfilter,
        posfilter,
        lenfilter,
    ]
)


@registry.register_document
class TrainDocument(Document):
    class Index:
        name = 'training'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    title = fields.TextField(
        analyzer=my_analyzer
    )

    description = fields.TextField(
        analyzer=my_analyzer
    )

    website = fields.KeywordField()
    type = fields.KeywordField()
    time = fields.KeywordField()

    class Django:
        model = Training
        fields = [
            'price'
        ]
