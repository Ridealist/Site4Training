from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .methods import mk_mytraining, mk_db
from .models import Training_List, Excel_File

from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.paginator import Paginator

class MyPageView(LoginRequiredMixin, FormView):
    login_url = 'account:login'
    form_class = UploadFileForm
    template_name = 'mypage/mypage.html'
    success_url = '/mypage/'


    def get_context_data(self, **kwargs):
        # context 얻기 위해 먼저 기본 구현을 호출
        context = super().get_context_data(**kwargs)
        training_list = Training_List.objects.filter(owner_id=self.request.user.id)
        paginator = Paginator(training_list, 10)
        page = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page)
        context['training_list'] = page_obj

        return context

    # def form_valid(self, form):
    #     owner = self.request.user
    #     word = form.cleaned_data.get('word')
    #     keyword, created = Keyword.objects.get_or_create(word=word)
    #     keyword.owner.add(owner)
    #     return super().form_valid(form)

@login_required(login_url='account:test')
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel = form.save(commit=False)
            excel.owner = request.user
            excel.save()
            xlsx = request.FILES['upload']
            df = mk_mytraining(xlsx)
            Training_List.objects.all().delete()
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
            return HttpResponseRedirect('success/')
    else:
        form = UploadFileForm()

    return render(request, 'mypage/mypage.html', {'form': form})


@login_required(login_url='account:test')
def upload_success(request):
    training_list = Training_List.objects.filter(owner=request.user)
    form = UploadFileForm()

    paginator = Paginator(training_list, 10)

    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    context = {'training_list': page_obj, 'form': form}

    return render(request, 'mypage/mypage.html', context)