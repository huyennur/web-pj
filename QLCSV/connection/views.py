from django.shortcuts import render, redirect
from connection.models import Group, Group_post, Group_comment
from authentication.models import Student
from django.contrib import messages
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def connect(request):
    list = Group.objects.all()
    paginator = Paginator(list, 9)

    pageNumber = request.GET.get('page')

    try:
        gr = paginator.page(pageNumber)
    except PageNotAnInteger:
        gr = paginator.page(1)
    except EmptyPage:
        gr = paginator.page(paginator.num_pages)

    Data = {'Groups': gr}
    return render(request, "connect.html", Data)


def group(request, pk):
    list = Group_post.objects.filter(groupID=pk).order_by('-g_post_date')
    paginator = Paginator(list, 10)

    pageNumber = request.GET.get('page')

    try:
        post = paginator.page(pageNumber)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    Data = {'Posts': post, 'Group': Group.objects.get(id=pk)}

    return render(request, 'g_forum.html', Data)


def g_discussion(request, pk1, pk2):
    gr = Group.objects.get(id=pk2)
    post = Group_post.objects.get(id=pk1)
    if (request.method == "POST"):
        cmt_content = request.POST['g_newcmt']
        cmt_user = Student.objects.get(MSSV=request.session['MSSV'])
        if request.FILES.get('g_cmt_image', False):  # Check if user updated image
            cmt_image = request.FILES['g_cmt_image']
        else:
            cmt_image = ''
        post.g_post_comment = F('g_post_comment') + '1'
        post.save()
        Group_comment(g_postID=post, g_cmt_content=cmt_content,
                      g_cmt_user=cmt_user, g_cmt_image=cmt_image).save()
    post = Group_post.objects.get(id=pk1)
    Cmts = Group_comment.objects.filter(g_postID=pk1).order_by('-g_cmt_date')

    paginator = Paginator(Cmts, 10)

    pageNumber = request.GET.get('page')

    try:
        Cmts = paginator.page(pageNumber)
    except PageNotAnInteger:
        Cmts = paginator.page(1)
    except EmptyPage:
        Cmts = paginator.page(paginator.num_pages)

    return render(request, 'g_discussion.html', {"post": post, "Cmts": Cmts, 'Group': gr})


def g_topic(request, pk):
    if (request.method == 'POST'):
        post_user = Student.objects.get(MSSV=request.session['MSSV'])
        post_title = request.POST['g_post_title']
        post_content = request.POST['g_post_content']
        groupID = Group.objects.get(id=pk)
        if request.FILES.get('g_post_image', False):  # Check if user updated image
            post_image = request.FILES['g_post_image']
        else:
            post_image = ''
        Group_post(g_post_user=post_user, g_post_content=post_content,
                   g_post_title=post_title, g_post_image=post_image, groupID=groupID).save()

        return redirect(f'/connection/group/{pk}')
    return render(request, 'g_topic.html')


def g_editpost(request, pk1, pk2):
    post = Group_post.objects.get(id=pk1)
    if (request.method == 'POST'):
        post.g_post_title = request.POST['g_new_title']
        post.g_post_content = request.POST['g_new_post_content']
        if request.FILES.get('g_new_post_image', False):  # Check if user updated image
            post.g_post_image = request.FILES['g_new_post_image']
        # else: post.post_image = ''

        post.save()
        #messages.success(request, "ok")
        return redirect(f'/connection/discussion/{post.id}/{pk2}')
    else:
        return render(request, 'g_editpost.html', {"post": post, 'Group': Group.objects.get(id=pk2)})


def g_editcmt(request, pk1, pk2):
    cmt = Group_comment.objects.get(id=pk1)
    if (request.method == 'POST'):
        cmt.g_cmt_content = request.POST['g_new_cmt_content']
        if request.FILES.get('g_new_cmt_image', False):  # Check if user updated image
            cmt.g_cmt_image = request.FILES['g_new_cmt_image']
        cmt.save()
        return redirect(f'/connection/discussion/{cmt.g_postID.id}/{pk2}')
    else:
        return render(request, 'g_editcomment.html', {"cmt": cmt, "post": cmt.g_postID, 'Group': Group.objects.get(id=pk2)})


def g_deletepost(request, pk1, pk2):
    post = Group_post.objects.get(id=pk1)
    post.delete()
    return redirect(f'/connection/group/{pk2}')


def g_deletecmt(request, pk1, pk2):
    cmt = Group_comment.objects.get(id=pk1)
    post = cmt.g_postID.id
    cmt.g_postID.g_post_comment = F('g_post_comment') - '1'
    cmt.g_postID.save()
    cmt.delete()
    return redirect(f'/connection/discussion/{post}/{pk2}')
