def get_msg(request):
    if request.method == 'POST':
        sms_from = request.POST.get('From')
        body = request.POST['Body']
        msg = Message(body=body, sms_from=sms_from)
        msg.save()
        return HttpResponse('<h1>SMS sent to Email</h1>')

    else:
        return HttpResponse('<h1>You will get Email once you have sms in twilio</h1>')

