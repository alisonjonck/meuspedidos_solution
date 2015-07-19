from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from questionnaire.forms import CandidateForm
from django.core.mail import send_mail

message_front_end = "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Front-End entraremos em contato."
message_back_end = "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Back-End entraremos em contato."
message_mobile = "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Mobile entraremos em contato."
message_generic =  "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador entraremos em contato."
email_subject = "Obrigado por se candidatar"
email_host_name = "alisonjonck@gmail.com"

def index(request):
	if request.method == 'POST':
		form = CandidateForm(request.POST)

		if form.is_valid():
			newCandidate = form.save()
			isSpecificOpportunity = False

			if int(newCandidate.html or 0) >= 7 and int(newCandidate.css or 0) >= 7 and int(newCandidate.javascript or 0) >= 7:
				send_mail(email_subject, message_front_end, email_host_name, [newCandidate.email])
				isSpecificOpportunity = True
			if int(newCandidate.python or 0) >= 7 and int(newCandidate.django or 0) >=7:
				send_mail(email_subject, message_back_end, email_host_name, [newCandidate.email])
				isSpecificOpportunity = True
			if int(newCandidate.ios or 0) >= 7 or int(newCandidate.android or 0) >= 7:
				send_mail(email_subject, message_mobile, email_host_name, [newCandidate.email])
				isSpecificOpportunity = True
			if not isSpecificOpportunity:
				send_mail(email_subject, message_generic, email_host_name, [newCandidate.email])

			return HttpResponseRedirect('thanks/')
	else:
		form = CandidateForm()

	return render(request, "index.html", { 
		"form": form,
		})

def thanks(request):
	return HttpResponse("Obrigado por se registrar. Entraremos em contato através do email que você cadastrou.")