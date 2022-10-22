from django.shortcuts import render
from .models import Training
from django.core.paginator import Paginator
from .query import query_elastic


def Search(request):
    training_list = Training.objects.order_by('title')

    paginator = Paginator(training_list, 10)

    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    context = {'training_list': page_obj}
    return render(request, 'search/find.html', context)


def SearchResult(request):
    if not request.GET.get('kw'):
        keyword = None
        queryset_search = query_elastic(keyword, request)
    else:
        keyword = request.GET.get('kw')
        queryset_search = query_elastic(keyword, request)

    context = {'training_list': queryset_search, 'query': keyword}
    return render(request, 'search/find.html', context)


    # all_query = Training.objects.all()
    # queryset_site = Training.objects.none()
    #
    # # ## 사이트 필터링
    # # if 'site_all' in request.GET:
    # #     queryset_site = all_query
    # # if 'choice_site1' in request.GET:
    # #     queryset_site = queryset_site.union(all_query.filter(
    # #         Q(website__icontains='아이스크림')
    # #     ))
    # # if 'choice_site2' in request.GET:
    # #     queryset_site = queryset_site.union(all_query.filter(
    # #         Q(website__icontains='티처빌')
    # #     ))
    #
    # # 선택 필터링
    # ## 강좌종류 필터링
    # queryset_type = Training.objects.none()
    #
    # # if 'type_all' in request.GET:
    # #     queryset_type = all_query
    # if 'choice_type1' in request.GET:
    #     queryset_type = queryset_type.union(all_query.filter(
    #         Q(type__icontains='생활지도')
    #     ))
    # if 'choice_type2' in request.GET:
    #     queryset_type = queryset_type.union(all_query.filter(
    #         Q(type__icontains='학습지도')
    #     ))
    # if 'choice_type3' in request.GET:
    #     queryset_type = queryset_type.union(all_query.filter(
    #         Q(type__icontains='어학')
    #     ))
    # if 'choice_type4' in request.GET:
    #     queryset_type = queryset_type.union(all_query.filter(
    #         Q(type__icontains='자기계발')
    #     ))
    # if 'choice_type5' in request.GET:
    #     queryset_type = queryset_type.union(all_query.filter(
    #         Q(type__icontains='인문·교양')
    #     ))
    # if 'choice_type6' in request.GET:
    #     queryset_type = queryset_type.union(all_query.filter(
    #         Q(type__icontains='교과지도')
    #     ))
    # if 'choice_type7' in request.GET:
    #     queryset_type = queryset_type.union(all_query.filter(
    #         Q(type__icontains='ICT·스마트')
    #     ))
    # if 'choice_type8' in request.GET:
    #     queryset_type = queryset_type.union(all_query.filter(
    #         Q(type__icontains='학급경영')
    #     ))
    # if 'choice_type9' in request.GET:
    #     queryset_type = queryset_type.union(all_query.filter(
    #         Q(type__icontains='진로·인성')
    #     ))
    #
    # if 'choice_type1' not in request.GET and 'choice_type2' not in request.GET and 'choice_type3' not in request.GET and 'choice_type4' not in request.GET and 'choice_type5' not in request.GET and 'choice_type6' not in request.GET and 'choice_type7' not in request.GET and 'choice_type8' not in request.GET and 'choice_type9' not in request.GET:
    #     queryset_type = all_query
    #
    # ## 강의시간 필터링
    # queryset_time = Training.objects.none()
    #
    # # if 'time_all' in request.GET:
    # #     queryset_time = all_query
    # if 'choice_time1' in request.GET:
    #     queryset_time = queryset_time.union(all_query.filter(
    #         Q(time__icontains='5시간') |
    #         Q(time__icontains='7시간') |
    #         Q(time__icontains='8시간') |
    #         Q(time__icontains='10시간')
    #     ))
    # if 'choice_time2' in request.GET:
    #     queryset_time = queryset_time.union(all_query.filter(
    #         Q(time__icontains='15시간')
    #     ))
    # if 'choice_time3' in request.GET:
    #     queryset_time = queryset_time.union(all_query.filter(
    #         Q(time__icontains='30시간')
    #     ))
    # if 'choice_time4' in request.GET:
    #     queryset_time = queryset_time.union(all_query.filter(
    #         Q(time__icontains='45시간')
    #     ))
    # if 'choice_time5' in request.GET:
    #     queryset_time = queryset_time.union(all_query.filter(
    #         Q(time__icontains='60시간')
    #     ))
    #
    # if 'choice_time1' not in request.GET and 'choice_time2' not in request.GET and 'choice_time3' not in request.GET and 'choice_time4' not in request.GET and 'choice_time5' not in request.GET:
    #     queryset_time = all_query
    #
    # ## 연수가격 필터링
    # queryset_price = Training.objects.none()
    #
    # # if 'price_all' in request.GET:
    # #     queryset_site = all_query
    # if 'choice_price1' in request.GET:
    #     queryset_price = queryset_price.union(all_query.filter(
    #         Q(price__lte=0)
    #     ))
    # if 'choice_price2' in request.GET:
    #     queryset_price = queryset_price.union(all_query.filter(
    #         Q(price__gt=0) &
    #         Q(price__lte=50000)
    #     ))
    # if 'choice_price3' in request.GET:
    #     queryset_price = queryset_price.union(all_query.filter(
    #         Q(price__gt=50000) &
    #         Q(price__lte=100000)
    #     ))
    # if 'choice_price4' in request.GET:
    #     queryset_price = queryset_price.union(all_query.filter(
    #         Q(price__gt=100000)
    #     ))
    #
    # if 'choice_price1' not in request.GET and 'choice_price2' not in request.GET and 'choice_price3' not in request.GET and 'choice_price4' not in request.GET:
    #     queryset_price = all_query
    #
    # queryset_check = queryset_site.intersection(queryset_type, queryset_time, queryset_price)
    #
    # ## 검색어 필터링
    #
    # if not request.GET.get('kw'):
    #     keyword = None
    #     queryset_search = query_elastic(keyword, request)
    # else:
    #     keyword = request.GET.get('kw')
    #     queryset_search = query_elastic(keyword, request)