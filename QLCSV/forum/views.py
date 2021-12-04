from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from authentication.models import Student
from forum.models import Post, Comment
from django.contrib import messages
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def forum(request):
    #Data = {'Posts': Post.objects.all().order_by('-post_date')}

    list = Post.objects.all().order_by('-post_date')
    paginator = Paginator(list, 10)

    pageNumber = request.GET.get('page')

    try:
        post = paginator.page(pageNumber)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    return render(request, 'forum.html', {'Posts': post})


def discussion(request, pk):
    post = Post.objects.get(id=pk)
    if (request.method == "POST"):
        cmt_content = request.POST['newcmt']
        cmt_user = Student.objects.get(MSSV=request.session['MSSV'])
        if request.FILES.get('cmt_image', False):  # Check if user updated image
            cmt_image = request.FILES['cmt_image']
        else:
            cmt_image = ''
        post.post_comment = F('post_comment') + '1'
        post.save()
        Comment(postID=post, cmt_content=cmt_content,
                cmt_user=cmt_user, cmt_image=cmt_image).save()
    post = Post.objects.get(id=pk)
    Cmts = Comment.objects.filter(postID=pk).order_by('-cmt_date')

    paginator = Paginator(Cmts, 10)

    pageNumber = request.GET.get('page')

    try:
        Cmts = paginator.page(pageNumber)
    except PageNotAnInteger:
        Cmts = paginator.page(1)
    except EmptyPage:
        Cmts = paginator.page(paginator.num_pages)

    return render(request, 'discussion.html', {"post": post, "Cmts": Cmts})


def topic(request):
    if (request.method == 'POST'):
        post_user = Student.objects.get(MSSV=request.session['MSSV'])
        print(post_user)
        post_title = request.POST['post_title']
        post_content = request.POST['post_content']
        if request.FILES.get('post_image', False):  # Check if user updated image
            post_image = request.FILES['post_image']
        else:
            post_image = ''
        Post(post_user=post_user, post_content=post_content,
             post_title=post_title, post_image=post_image).save()

        return redirect(f'/forum/')
    return render(request, 'topic.html')


def editpost(request, pk):
    post = Post.objects.get(id=pk)
    if (request.method == 'POST'):
        post.post_title = request.POST['new_title']
        post.post_content = request.POST['new_post_content']
        if request.FILES.get('new_post_image', False):  # Check if user updated image
            post.post_image = request.FILES['new_post_image']
        # else: post.post_image = ''

        post.save()
        #messages.success(request, "ok")
        return redirect(f'/forum/discussion/id={post.id}')
    else:
        return render(request, 'editpost.html', {"post": post})


def editcmt(request, pk):
    cmt = Comment.objects.get(id=pk)
    print('khue')
    if (request.method == 'POST'):
        print('yes')
        cmt.cmt_content = request.POST['new_cmt_content']
        if request.FILES.get('new_cmt_image', False):  # Check if user updated image
            cmt.cmt_image = request.FILES['new_cmt_image']
        # else: post.post_image = ''
        cmt.save()
        #messages.success(request, "ok")
        return redirect(f'/forum/discussion/id={cmt.postID.id}')
    else:
        return render(request, 'editcomment.html', {"cmt": cmt, "post": cmt.postID})


def deletepost(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect(f'/forum/')


def deletecmt(request, pk):
    cmt = Comment.objects.get(id=pk)
    cmt.postID.post_comment = F('post_comment') - '1'
    cmt.postID.save()
    cmt.delete()
    return redirect(f'/forum/discussion/id={cmt.postID.id}')


def likepost(request, pk):
    if (request.method == 'POST'):
        post = Post.objects.get(id=pk)
        post.post_like = F('post_like') + '1'
        post.save()
    return redirect(f'/forum/')
