from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout



from .forms import ContactForm , LoginForm, RegisterForm

def logout_view(request):
    logout(request)
    return redirect('home')

def home_page(request):
	#print(request.session.get('first_name', 'Unknown'))
	context = {
		"title":"Premium Shoes",
		
	}
	if request.user.is_authenticated():
		context["premium_content"] = "You are now logged in"
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title":"About Page"
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title":"Contact Page",
		"form": contact_form 
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	return render(request, "contact/view.html", context)
def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	print("User logged in")
	print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			print(request.user.is_authenticated())
			login(request, user)
			#context['form'] = LoginForm()
			return redirect("/")
		else:
			print("Error")
	return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

# def register_page(request):
# 	form = RegisterForm(request.POST or None)
# 	context = {
# 		"form": form
# 	}
# 	if form.is_valid():
# 		print(form.cleaned_data)
# 	return render(request, "auth/register.html", context)


def home_page_old(request):
	return HttpResponse("<h1>Hello World</h1>")