from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def send_email(request):
    if request.method == "POST":
        # print(f"Request method: {request.method}")
        # print(f"Request content type: {request.content_type}")
        # print(f"Request body: {request.body}")
        # print(f"Request POST data: {request.POST}")

        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        mail = request.POST.get("mail")
        select = request.POST.get("select")
        comment = request.POST.get("comment")

        if (select is None or select == "") and phone_number is None:
            select = 'Клиент выбрал обратный звонок'

        print(
            f"Full Name: {full_name}, Phone Number: {phone_number}, Email: {mail}, Select: {select}, Comment: {comment}")

        subject = "Новая завка с сайта"
        message = f"""
        Контактная информация:
        * ФИО: {full_name}
        * Номер телефона: {phone_number}
        * Email: {mail}

        Выбранная услуга: {select}

        Комментарий:
        {comment}

        """
        from_email = 'mailtrap@demomailtrap.com'  # замените на вашу почту
        recipient_list = ['ir-g-technical@mail.ru']  # замените на почту получателя

        send_mail(subject, message, from_email, recipient_list)

        return HttpResponse(
            f"Received data")
    else:
        return HttpResponse("This view accepts only POST requests")
