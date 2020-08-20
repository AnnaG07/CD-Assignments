from django.shortcuts import render, redirect
from .models import *
from log_reg_app.models import *

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'all_messages': Wall_Message.objects.all(),
        'all_comments': Wall_Comment.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'wall.html', context)

def post_message(request):
    if request.method == 'POST':
        print(request.POST)
        Wall_Message.objects.create(m_content=request.POST['m_content'], poster=User.objects.get(id=request.session['user_id']))
        return redirect('/wall')

def post_comment(request, id):
    if request.method == 'POST':
        print(request.POST)
        poster = User.objects.get(id=request.session['user_id'])
        message = Wall_Message.objects.get(id=id)
        Wall_Comment.objects.create(c_content=request.POST['c_content'], poster=poster, message=message)
        return redirect('/wall')

def edit_message(request, id):
    context = {
        'message': Wall_Message.objects.get(id=id)
    }
    return render(request, 'edit_message.html', context)

def update_message(request, id):
    if request.method == 'POST':
        print(request.POST)
        edit_message = Wall_Message.objects.get(id=id)
        edit_message.m_content = request.POST['m_content']
        edit_message.save()
        return redirect('/wall')

def edit_comment(request, id):
    context = {
        'comment': Wall_Comment.objects.get(id=id)
    }
    return render(request, 'edit_comment.html', context)

def update_comment(request, id):
    if request.method == 'POST':
        edit_comment = Wall_Comment.objects.get(id=id)
        edit_comment.c_content = request.POST['c_content']
        edit_comment.save()
        return redirect('/wall')

def delete_message(request, id):
    Wall_Message.objects.get(id=id).delete()
    return redirect('/wall')

def delete_comment(request, id):
    Wall_Comment.objects.get(id=id).delete()
    return redirect('/wall')