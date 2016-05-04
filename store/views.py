from django.shortcuts import get_object_or_404,render
from .models import RegStore,Comments,Category
from .forms import CommentsForm
from django.db.models import Q
import operator
from functools import reduce
from senticomment.views import review

# Create your views here.
def store_view(request):
    stores=RegStore.objects.all()
    return render(request,'store/view_store.html',{'stores':stores})

def store_home(request,slug):
    store=get_object_or_404(RegStore,storeslug=slug)
    comment_view=Comments.objects.filter(store__storeslug=slug)
    if request.method=='POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            save_it=form.save(commit=False)
            save_it.store=store
            save_it.user=request.user
            comment_sentiment=review(store,data['comment'],data['ratings'])
            save_it.pos_score_comment=comment_sentiment[0]
            save_it.neg_score_comment=comment_sentiment[1]
            save_it.polarity_comment=comment_sentiment[2]
            save_it.save()
            form=CommentsForm()
        else:
            form=CommentsForm(request.POST)
    else:
        form=CommentsForm()
    
    return render(request,'store/store_home.html',{'store':store,'comments':comment_view,'form':form,'range_ten':range(1,11)})

def store_category(request,slug):
    
    stores=RegStore.objects.filter(category__slug=slug)
    #cat_in=Category.objects.get(slug=slug)
    #parent=RegStore.objects.filter(category__parent_category=cat_in.slug)
    return render(request,'store/view_store.html',{'stores':stores})


def searchResults(request):
    srch_key = request.GET.get('srch_key')
    city = request.GET.get('city')
    #stores = RegStore.objects.filter(name__icontains=srch_key)
    
    if srch_key:
        query_list=srch_key.split()
        result = RegStore.objects.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(desc__icontains=q) for q in query_list))
            )
        result=result.filter(city=city)
        #search_var = getVariables(request)
        #search_var={}
        #search_var['store'] = store
    
    return render(request,'store/search.html',{'stores':result})

