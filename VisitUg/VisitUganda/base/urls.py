from django.urls import path
from . import views

urlpatterns = [
  # Site Manager urls
    path("Admin", views.admin, name="Admin"),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("payments/", views.payments, name="payments"),
    path("packages/", views.viewPackages, name="packages"),
    
    # Client urls
    path("", views.index, name="index"),
    path("registerClient", views.registerClient, name="registerClient"),
    path("login/", views.customerLogin, name="customerLogin"),
    path("services/", views.viewServices, name="services"),
    path("events/", views.viewEvents, name="events"),
    path("about/", views.viewAbout, name="about"),
    path("contact/", views.viewContact, name="contact"),
    path("services/company/<int:id>", views.viewCompany, name="company"),
    path("services/company/<int:id>", views.viewCompany, name="company"),
    path("services/company/package/<int:id>", views.viewPackage, name="package"),
    path("services/company/package/book/<int:id>", views.book, name="book"),
    path("package/book/<int:id>", views.book, name="book"),
    path("package/<int:id>", views.viewPackage, name="package"),
    path("services/company/testimonials/", views.addTestimonial, name="testimonials"),
    path("payment/", views.pay, name="paymentss"),
    path("regCompany", views.regCompany, name="regCompany"),
    path("registerCompany/", views.registerCompany, name="registerCompany"),
    
    path("paymentMode/", views.selectPayMode, name="paymentMode"),
    path("registerPackage/", views.registerPackage, name="registerPackage"),
    path("registerHotel/", views.registerHotel, name="registerHotel"),
    path("registerActivity/", views.registerActivity, name="registerActivity"),
    path("addAccomodation/", views.addAccomodation, name="addAccomodation"),
]
