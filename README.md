# Site4Training
교사 연수 추천 사이트

### 기술 스택
- ElasticSearch
  - elasticsearch(PyPI)
  - elasticsearch_dsl
    - 토큰 필터(불용어 필터, 유의어 필터) + 토크나이저(nori_tokenizer) 활용
    - query 생성(document를 검색하는데 활용)
  - django_elasticsearch_dsl
    - document 생성(elasticserach로 indexing 되는 전체 문서 단위)
- Django
  - CreateView, FormView 등 generic View class 활용
  - UserCreationForm, UploadFileForm 등 ModelForm 및 custom form 활용
  - LoginRequiredMixin, @login_required 등 mixin class와 decorator 활용
  - paginator 및 query
- pandas
  - 연수 크롤링 데이터 파싱
  - 연수 데이터 DB 로딩
- django-allauth
  - social login 구현 시도

<br>

### 구동 시연
![2022-10-23 04;13;35](https://user-images.githubusercontent.com/89024993/197358653-3b6a7000-9648-4dbb-9f38-a2d86a007bf6.gif)
![2022-10-23 04;14;52](https://user-images.githubusercontent.com/89024993/197358654-edd9d35d-f9b4-449c-bfd4-de54f1525f5a.gif)
