from django.shortcuts import render, redirect
from PC.forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'PC/home.html')

def services(request):
    return render(request, 'PC/services.html')

def about(request):
    return render(request, 'PC/about.html')

def contact(request):
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        data = {
            'fullName': fullName,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message,
        }

        email_message = '''
        New message from contact form:

        Full Name: {fullName}
        Email: {email}
        Phone: {phone}
        Subject: {subject}
        Message: {message}
        '''.format(
            fullName=data['fullName'],
            email=data['email'],
            phone=data['phone'],
            subject=data['subject'],
            message=data['message']
        )

        try:
            send_mail(
                data['subject'],
                email_message,
                'your-email@gmail.com',  # Replace with your email address
                ['warragambasilverdalepc@gmail.com'],  # Replace with the recipient email address
                fail_silently=False,
            )
            return redirect('success')
        except Exception as e:
            print(f"Error sending email: {e}")
            return HttpResponse('Error sending email', status=500)

    else:
        form = ContactForm()
    return render(request, 'PC/contact.html', {'form': form})

def success(request):
    return render(request, 'PC/success.html')