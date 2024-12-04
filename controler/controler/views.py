from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Comment

def forum(request):
    return render(request, 'forum.html')

@csrf_exempt
def get_comments(request):
    if request.method == "GET":
        comments = Comment.objects.all().order_by('-date_posted')
        comments_data = [
            {
                "username": comment.username,
                "topic": comment.topic,
                "message": comment.message,
                "date": comment.date_posted.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for comment in comments
        ]
        return JsonResponse({"comments": comments_data})

@csrf_exempt
def add_comment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        topic = data.get("topic")
        message = data.get("message")
        
        # Save to the database
        comment = Comment.objects.create(username=username, topic=topic, message=message)
        comment.save()
        
        return JsonResponse({"message": "Comment added successfully!"})

@csrf_exempt
def add_reply(request, comment_id):
    if request.method == "POST":
        data = json.loads(request.body)
        parent_comment = get_object_or_404(Comment, id=comment_id)
        reply = Comment.objects.create(
            username=data.get("username"),
            topic=parent_comment.topic,  # Inherit topic from parent
            message=data.get("message"),
            parent=parent_comment
        )
        reply.save()
        return JsonResponse({"message": "Reply added successfully!"})

@csrf_exempt
def delete_comment(request, comment_id):
    if request.method == "DELETE":
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return JsonResponse({"message": "Comment deleted successfully!"})