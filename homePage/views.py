from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponse
from usefulModels.forms import CommentForm, PostForm
from usefulModels.models import Comment, Post, ReadingBook, QuesModel, Vocabulary

#Tạo render cho HOME
def homePage(request):
    object_list = ReadingBook.objects.all()
    return render(
        request,
        'homePage.html',
        {'object_list':object_list,}
        )

#Tạo render cho READING    
def readingSite(request):
    object_view = ReadingBook.objects.all()
    object_view1 = ReadingBook.objects.filter(category__name = 'Funny Story')
    object_view2 = ReadingBook.objects.filter(category__name = 'Jokes')
    object_view3 = ReadingBook.objects.filter(category__name = 'Children Story')
    return render (
        request,
        'readingSite.html',{
        'object_view': object_view,
        'object_view1' : object_view1,
        'object_view2' :object_view2,
        'object_view3' :object_view3,
        }
    ) 

#Tạo render cho READPAGE
def readPageSite(request, id):
    if request.method == 'POST':
        if request.POST.get('note'):
            object_views = ReadingBook.objects.get(id = id)
            create_notes = Post.objects.create(
                author=request.user,
                name_read=object_views,
                note=request.POST.get('note'),
            )
            post = Post.objects.filter(author=request.user)
            return render(
                request,
                'note-book.html',
                {'post':post,}
                )
        else:
            print(request.POST)
            questions=QuesModel.objects.filter(name_read_id = id)
            score=0
            wrong=0
            correct=0
            total=0
            for q in questions:
                total+=1
                print(request.POST.get(q.question))
                print(q.ans)
                print()
                if q.ans ==  request.POST.get(q.question):
                    score+=10
                    correct+=1
                else:
                    wrong+=1
            percent = score/(total*10) *100
            context = {
                'score':score,
                'time': request.POST.get('timer'),
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total
            }
            return render(request,'kq.html', context)
    else:
        object_views = ReadingBook.objects.get(id = id)
        questions= QuesModel.objects.filter(name_read_id = id)
        vocabulary= Vocabulary.objects.filter(name_read_id = id)
        object_views.views += 1
        object_views.save()

        context = {
            'questions':questions,
            'object_views': object_views,
            'vocabulary': vocabulary,
        }
        return render(request,'readPageSite.html', context)

def post(request):
    postt = Comment.objects.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "post.html", {"postt": postt, "form": form})

def notebook(request):
    post = Post.objects.filter(author=request.user)
    return render(
        request,
        'note-book.html',
        {'post':post,}
        )