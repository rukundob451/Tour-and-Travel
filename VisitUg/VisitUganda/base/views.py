from email import message
from .models import Accomodation, Activity, Company, Package, PackageAccomodation, City, Testimonial
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CompanyRegistrationForm, RegistrationForm
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.views.generic import TemplateView
from django.db.models import Q
# Create your views here.

# Customer views

# Customer Registration View
def registerClient(request):
  form = RegistrationForm()
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      
      if User.objects.filter(username=user.username).exists():
        messages.error(request, "Username Taken!")
        return redirect('registerClient')
      #check email
      elif User.objects.filter(email=user.email).exists():
        messages.error(request, "Email Taken!")
        return redirect('registerClient')
      else:
        email = user.email
        html_template='html_template.html'
        html_message = render_to_string(html_template)
        subject='Welcome to Travel'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        message = EmailMessage(subject, html_message, email_from, recipient_list) 
        message.content_subtype='html'
        message.send()
        
        
        user.save()
        return redirect('customerLogin') 
    else:
      messages.error(request, "Form Invalid!")
      return redirect('registerClient')
  else:
    context = {'form': form}
    return render(request, "customer_registration.html", context)


# Customer login view
def customerLogin(request):
  if request.method == 'POST':
    username = request.POST['username'].lower()
    password = request.POST['password']
    
    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, "User doesn't exist!")
      return redirect('customerLogin')
      
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      if user.is_superuser:
        return redirect('Admin')
      else:
        return redirect('index')
    else:
      messages.error(request, "Invalid Credentials!")
      return redirect('customerLogin')
  else:
    context = {}
    return render(request, "customer_login.html", context)

# Index page view
def index(request):
  if 'q' in request.GET:
    q = request.GET['q']
    multiple_q = Q(Q(name__icontains=q)|Q(description__icontains=q))
    packages = Package.objects.filter(multiple_q)
  else:
     packages = Package.objects.all()
  activities = Activity.objects.all()
  hotels = PackageAccomodation.objects.all()
  
  context = {
    'packages': packages,
    'activities': activities,
    'hotels': hotels,
  }
  return render(request, "index.html", context)

# Viewing services page
def viewServices(request):
  companies = Company.objects.all()
  cities = City.objects.all()
  
  context = {
    'companies': companies,
    'cities': cities,
  }
  return render(request, "services.html", context)

# Viewing events page
def viewEvents(request):
  return render(request, "events.html")

# Viewing the About us Page
def viewAbout(request):
  return render(request, "about_us.html")

# Viewing the contacts
def viewContact(request):
  return render(request, "contact.html")

# View company details
def viewCompany(request, id):
  company = Company.objects.get(id=id)
  packages = Package.objects.filter(company=id)
  activities = Activity.objects.all()
  hotels = PackageAccomodation.objects.all()
  numOfPackages = Package.objects.filter(company=id).count()
  numOfHotels = PackageAccomodation.objects.all().count()
  numOfActivities = Activity.objects.all().count()
  testimonials = Testimonial.objects.filter(company=id)
  
  context = {
    'company': company,
    'packages': packages,
    'activities': activities,
    'hotels': hotels,
    'numOfPackages': numOfPackages,
    'numOfHotels': numOfHotels,
    'numOfActivities': numOfActivities,
    'testimonials': testimonials,
  }
  return render(request, "company_info.html", context)

# Renders package details
def viewPackage(request, id):
  package = Package.objects.get(id=id)
  activities = Activity.objects.filter(package=id)
  hotels = PackageAccomodation.objects.filter(package=id)
  
  context = {
    'package': package,
    'activities': activities,
    'hotels': hotels,
  }
  return render(request, "package_info.html", context)

@login_required(login_url='customerLogin')
def book(request, id):
  if request.method == "POST":
    return redirect('paymentss')
  
  context = {
    'packageId': id,
  }
  return render(request, "book.html", context)

def addTestimonial(request):
  companyId=request.GET['companyId']
  company = Company.objects.get(id=(request.GET['companyId']))
  if request.method == 'POST':
    testimonial = Testimonial(
      username=request.user,
      company=company,
      img=request.FILES['image'],
      message=request.POST['message'],
    )
    
    testimonial.save()
    company = Company.objects.get(id=id)
    packages = Package.objects.filter(company=id)
    activities = Activity.objects.all()
    hotels = PackageAccomodation.objects.all()
    numOfPackages = Package.objects.filter(company=id).count()
    numOfHotels = PackageAccomodation.objects.all().count()
    numOfActivities = Activity.objects.all().count()
    testimonials = Testimonial.objects.filter(company=id)
    
    context = {
      'company': company,
      'packages': packages,
      'activities': activities,
      'hotels': hotels,
      'numOfPackages': numOfPackages,
      'numOfHotels': numOfHotels,
      'numOfActivities': numOfActivities,
      'testimonials': testimonials,
    }
    return render(request, "company_info.html", context)
  
  context = {
    'companyId': companyId,
  }
  return render(request, "testimonial.html", context)

# Site manager views
def admin(request):
  companies = Company.objects.all()
  numOfCompanies = Company.objects.all().count()
  numOfPackages = Package.objects.all().count()
  numOfCustomers = User.objects.filter(is_superuser=False).count()
  numOfActivities = Activity.objects.all().count()
  hotels = Accomodation.objects.all().count()
  
  context = {
    'companies': companies,
    'numOfCompanies': numOfCompanies,
    'numOfPackages': numOfPackages,
    'numOfCustomers': numOfCustomers,
    'hotels': hotels,
    'numOfActivities': numOfActivities,
  }
  return render(request, "Admin.html", context)

def loginPage(request):
  if request.user.is_authenticated:
    return redirect('Admin')
  
  if request.method == 'POST':
    username = request.POST['username'].lower()
    password = request.POST['password']
    
    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, "User doesn't exist!")
      return redirect('login')
      
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      return redirect('Admin')
    else:
      messages.error(request, "Invalid Credentials!")
      return redirect('login')
  else:
    context = {}
    return render(request, "login.html", context)
  
# Logout View
def logoutUser(request):
  det = None
  if request.user.is_superuser:
    det = True
  else:
    det = False
  logout(request)
  
  if det:
    return redirect('Admin')
  else:
    return redirect('index')

# View to show payments
def payments(request):
  customers = User.objects.filter(is_superuser=False)
  
  context = {
    'customers': customers
  }
  return render(request, "payments.html", context)

def viewPackages(request):
  packages = Package.objects.all()
  
  context = {
    'packages': packages,
  }
  return render(request, "packages.html", context)

def regCompany(request):
    return render(request,'register_company.html')
  
# Register Company
def registerCompany(request):
  
  if request.method == 'POST':
    company = Company(
      name=request.POST['name'],
      location=request.POST['location'],
      email=request.POST['email'],
      account=request.POST['account'],
      img=request.FILES['image'],
      mission=request.POST['mission'],
    )
    company.save()
    companies = Company.objects.all()
    numOfCompanies = Company.objects.all().count()
    numOfPackages = Package.objects.all().count()
    numOfCustomers = User.objects.filter(is_superuser=False).count()
    numOfActivities = Activity.objects.all().count()
    hotels = Accomodation.objects.all().count()
  
    context = {
      'companies': companies,
      'numOfCompanies': numOfCompanies,
      'numOfPackages': numOfPackages,
      'numOfCustomers': numOfCustomers,
      'numOfActivities': numOfActivities,
      'hotels': hotels,
    }
    
    return render(request,"Admin.html",context)
  else:
    return render(request, "register_company.html")

def pay(request):
  
  return render(request, "payment.html")

def selectPayMode(request):
  packageId = request.POST['packageid']
  
  package = Package.objects.get(id=packageId)
  amount = int(request.POST['guests'])* int(package.price)
  
  context = {
    'package': package,
    'amount': amount
  }
  return render(request, "amount.html", context)


# Register package view
def registerPackage(request):
  companies=Company.objects.all()
  if request.method == 'POST':
    company=request.POST['company']
    companyId=Company.objects.get(name=company)
    package = Package(
      name=request.POST['name'],
      company=companyId,
      price=request.POST['price'],
      img=request.FILES['image'],
      description=request.POST['desc'],
    )
    
    package.save()
    companies = Company.objects.all()
    numOfCompanies = Company.objects.all().count()
    numOfPackages = Package.objects.all().count()
    numOfCustomers = User.objects.filter(is_superuser=False).count()
    numOfActivities = Activity.objects.all().count()
    hotels = Accomodation.objects.all().count()
  
    context = {
      'companies': companies,
      'numOfCompanies': numOfCompanies,
      'numOfPackages': numOfPackages,
      'numOfCustomers': numOfCustomers,
      'numOfActivities': numOfActivities,
      'hotels': hotels,
    }
    
    return render(request,"Admin.html",context)
  
  context={
    "companies": companies,
  }
  return render(request, "register_package.html", context)

def registerHotel(request):
  cities = City.objects.all()
  if request.method == 'POST':
    hotel = Accomodation(
      name=request.POST['name'],
      img=request.FILES['image'],
      location=request.POST['location'],
    )
    
    hotel.save()
    companies = Company.objects.all()
    numOfCompanies = Company.objects.all().count()
    numOfPackages = Package.objects.all().count()
    numOfCustomers = User.objects.filter(is_superuser=False).count()
    numOfActivities = Activity.objects.all().count()
    hotels = Accomodation.objects.all().count()
  
    context = {
      'companies': companies,
      'numOfCompanies': numOfCompanies,
      'numOfPackages': numOfPackages,
      'numOfCustomers': numOfCustomers,
      'numOfActivities': numOfActivities,
      'hotels': hotels,
    }
    
    return render(request,"Admin.html",context)
  
  context={
    'cities': cities
  }
  return render(request, "register_hotel.html", context)

def registerActivity(request):
  packages = Package.objects.all()
  if request.method == 'POST':
    package=request.POST['package']
    packageId=Package.objects.get(name=package)
    activty = Activity(
      name=request.POST['name'],
      package=packageId,
      img=request.FILES['image'],
      description=request.POST['desc'],
    )
    
    activty.save()
    companies = Company.objects.all()
    numOfCompanies = Company.objects.all().count()
    numOfPackages = Package.objects.all().count()
    numOfCustomers = User.objects.filter(is_superuser=False).count()
    numOfActivities = Activity.objects.all().count()
    hotels = Accomodation.objects.all().count()
  
    context = {
      'companies': companies,
      'numOfCompanies': numOfCompanies,
      'numOfPackages': numOfPackages,
      'numOfCustomers': numOfCustomers,
      'numOfActivities': numOfActivities,
      'hotels': hotels,
    }
    
    return render(request,"Admin.html",context)
  
  context = {
    'packages': packages
  }
  return render(request, "register_activity.html", context)

def addAccomodation(request):
  hotels = Accomodation.objects.all()
  packages = Package.objects.all()
  
  if request.method == "POST":
    hotel=Accomodation.objects.get(name=request.POST['hotel'])
    package=Package.objects.get(name=request.POST['package'])
    
    acc = PackageAccomodation(
      package=package,
      accomodation=hotel
    )
    acc.save()
    
    companies = Company.objects.all()
    numOfCompanies = Company.objects.all().count()
    numOfPackages = Package.objects.all().count()
    numOfCustomers = User.objects.filter(is_superuser=False).count()
    numOfActivities = Activity.objects.all().count()
    hotels = Accomodation.objects.all().count()
    
    context = {
      'companies': companies,
      'numOfCompanies': numOfCompanies,
      'numOfPackages': numOfPackages,
      'numOfCustomers': numOfCustomers,
      'numOfActivities': numOfActivities,
      'hotels': hotels,
    }
    
    return render(request,"Admin.html",context)
  
  context = {
    'hotels': hotels,
    'packages': packages 
  }
  return render(request, "add_accomodation.html", context)