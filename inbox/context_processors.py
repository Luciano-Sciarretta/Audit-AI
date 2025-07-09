from .models import Message

def inbox_unread_count(request):
    if request.user.is_authenticated:
        count = Message.objects.filter(recipient = request.user, is_read = False).count()
    else:
        count = 0
    context = {'inbox_unread_count': count}
    return context