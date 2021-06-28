from django.shortcuts import render 
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()    
    return render(request, 'contact/contact.html', {'form':form})












































# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse
# def contact(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			subject = "Website Inquiry" 
# 			body = {
# 			'first_name': form.cleaned_data['first_name'], 
# 			'last_name': form.cleaned_data['last_name'], 
# 			'email': form.cleaned_data['email_address'], 
# 			'message':form.cleaned_data['message'], 
# 			}
# 			message = "\n".join(body.values())

# 			try:
# 				send_mail(subject, message, 'email', ['learndjangobyown@gmail.com'], fail_silently=False) 
# 			except BadHeaderError:
# 				return HttpResponse('Invalid header found.')
# 			return render(request, "contact/contact.html")
      
# 	form = ContactForm()
# 	return render(request, "contact/contact.html", {'form':form})


