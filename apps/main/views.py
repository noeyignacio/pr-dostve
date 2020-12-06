import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


# Models
from .models import *

# Form
from .forms import VisitorAttendanceForm, SurveyForm

# Decorators
from .decorators import unauthenticated_user, allowed_users, admin_only


# Error Handling
def handler404(request, exception):
    return render(
        request,
        "main/pages/handlers/404Page.html",
    )


"""
Exhibit Pages
Exhibit Methods
"""

# PAGES
def home(request):
    return render(
        request,
        "main/pages/LandingPage.html",
    )


def exhibit(request):
    return render(
        request,
        "main/pages/exhibit/ExhibitPage.html",
    )


def guide(request):
    return render(
        request,
        "main/pages/GuidePage.html",
    )


def bataanProjects(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/BataanPage.html",
    )


def bulacanProjects(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/BulacanPage.html",
    )


def tarlacProjects(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/TarlacPage.html",
    )


def pampangaProjects(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/PampangaPage.html",
    )


def otherProjects(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/OtherPage.html",
    )


def kaayusan(request):
    return render(
        request,
        "main/pages/exhibit/pages/kaayusan/KaayusanPage.html",
    )


def kalusugan(request):
    return render(
        request,
        "main/pages/exhibit/pages/kalusugan/KalusuganPage.html",
    )


def cest(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/Kabuhayan.html",
    )


# EQUIPMENTS


def filamentWinder(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/FilamentWinder.html",
    )


def microwaveFurnace(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/MicrowaveFurnace.html",
    )


def creatorPro(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/CreatorPro.html",
    )


def formLab(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/FormLabForm2.html",
    )


def microscope(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/Microscope.html",
    )


def shimadzuAgs(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/ShimadzuAgx.html",
    )


def injectionModeling(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/InjectionModeling.html",
    )


def impactTester(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/ImpactTester.html",
    )


def uvCuring(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/UVCuring.html",
    )


def shining3d(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/Shining3D.html",
    )


def filamentExtruder(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/FilamentExtruder.html",
    )


def shimadzuRockwell(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/ShimadzuRockwell.html",
    )


def zortrax(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/ZortraxM200.html",
    )


def viscometer(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/Viscometer.html",
    )


def ultimaker(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/Ultimaker3.html",
    )


def sonicBath(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/equipments/SonicBath.html",
    )


# KABUHAYAN
def cashew(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/CashewIndustry.html",
    )


def double(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/DoubleMulching.html",
    )


def hydro(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/HydroPonicsPage.html",
    )


def zambelena(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Zambelena.html",
    )


def women(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Women.html",
    )


def carra(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Carrageenan.html",
    )


def pump(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/SolarPump.html",
    )


def books(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/StarBooks.html",
    )


def mushroom(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Mushroom.html",
    )


def transplant(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Transplanting.html",
    )


def feeding(request):
    return render(
        request,
        "main/pages/exhibit/pages/kalusugan/pages/FeedingPage.html",
    )


def policy(request):
    return render(
        request,
        "main/pages/handlers/PolicyPage.html",
    )


def ecest(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/ECestPage.html",
    )


def florida(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/FloridaBlanca.html",
    )


def snt(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/S&T.html",
    )


def article1(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Article1.html",
    )


def article2(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Article2.html",
    )


def article3(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Article3.html",
    )


def article4(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Article4.html",
    )


def article5(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Article5.html",
    )


def article6(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Article6.html",
    )


def article7(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Article7.html",
    )


def rxbox(request):
    return render(
        request,
        "main/pages/exhibit/pages/kalusugan/pages/RxboxPage.html",
    )


def clhrdc(request):
    return render(
        request,
        "main/pages/exhibit/pages/kalusugan/pages/CLHRDCPage.html",
    )


def duck(request):
    return render(
        request,
        "main/pages/exhibit/pages/kaayusan/pages/DUCKPage.html",
    )


def clock(request):
    return render(
        request,
        "main/pages/exhibit/pages/kaayusan/pages/JuanTimePage.html",
    )


def swan(request):
    return render(
        request,
        "main/pages/exhibit/pages/kaayusan/pages/SWANPage.html",
    )


def sewing(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Sewing.html",
    )


def sntservice(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/S&TServices.html",
    )


def setup(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Setup.html",
    )


def stories(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/SuccessStory.html",
    )


def products(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Products.html",
    )


def story(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Story.html",
    )


def smart(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/SmartHybrid.html",
    )


def live(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Livelihood.html",
    )


def tech(request):
    return render(
        request,
        "main/pages/exhibit/pages/kabuhayan/pages/Tech.html",
    )


def amrel(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/AdditiveManufacturing.html",
    )


def automated(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/AutomatedGuide.html",
    )


def adoption(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/Adoption.html",
    )


def innovative(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/Innovative.html",
    )


def food(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/FoodInnovation.html",
    )


def agri(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/ImprovingAgricultural.html",
    )


def tbi(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/TBI.html",
    )


def tamarind(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/Tamarind.html",
    )


def sweet(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/SweetPotato.html",
    )


def mist(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/Mist.html",
    )


def safety(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/FoodSafety.html",
    )


def development(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/DesignAndDevelopment.html",
    )


def support(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/Support.html",
    )


def kinabukasan(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/KinabuhasanPage.html",
    )


def starbooks(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/StarBooks.html",
    )


def far(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/FAR.html",
    )


def teach(request):
    return render(
        request,
        "main/pages/exhibit/pages/kinabukasan/Teaching.html",
    )


# METHODS
def registerAttendance(request):

    form = VisitorAttendanceForm()

    # Saving Form
    if request.method == "POST":

        form = VisitorAttendanceForm(request.POST)

        # Province Validator
        province_value = request.POST["province"]
        province_value_regex = re.search(r"^[a-zA-Z]*$", province_value)
        if not province_value_regex:
            messages.error(request, "Province is Invalid")

        # Form Validation
        if form.is_valid():
            print("IS_VALID")
            form.save()
            return redirect("/guide")
        else:
            print("AN_ERROR_OCCURED")

    context = {
        "form": form,
    }

    return render(
        request,
        "main/pages/RegistrationPage.html",
        context,
    )


def survey(request):

    form = SurveyForm()

    # Saving Form
    if request.method == "POST":

        form = SurveyForm(request.POST)

        # Email Validation
        try:
            validate_email(request.POST["email"])
        except ValidationError:
            messages.warning(request, "Email is Invalid.")

        # Phone Number Valdiation
        phone_number_value = request.POST["phone_number"]
        phone_number_regex = re.search(r"^(09|\+639)\d{9}$", phone_number_value)
        if not phone_number_regex:
            messages.warning(request, "Phone Number is Invalid")

        # Form Validation
        else:
            if form.is_valid():
                print("IS_VALID")
                messages.success(request, "Feedback Successfully Sent.")
                form.save()
                form = SurveyForm()
            else:
                print("AN_ERROR_OCCURED")

    context = {
        "form": form,
    }

    return render(
        request,
        "main/pages/SurveyPage.html",
        context,
    )


"""
Admin Pages
Admin Methods
"""

# PAGES
def admin(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dostr3admindahsboard")
        else:
            messages.error(request, "You are not Authorized.")

    context = {}
    return render(
        request,
        "main/pages/panel/AdminLoginPage.html",
        context,
    )


# METHODS


@login_required(login_url="dostr3adminpanellogin")
@admin_only
def panel(request):

    visitors = Visitor.objects.all()
    surveys = Survey.objects.all()

    total_visitors = visitors.count()
    total_surveys = surveys.count()

    context = {
        "total_visitors": total_visitors,
        "total_surveys": total_surveys,
    }

    return render(
        request,
        "main/pages/panel/AdminDashboardPage.html",
        context,
    )


@login_required(login_url="dostr3adminpanellogin")
@admin_only
def visitorTable(request):

    visitors = Visitor.objects.all()
    context = {
        "visitors": visitors,
    }

    return render(
        request,
        "main/pages/panel/containers/VisitorTable.html",
        context,
    )


@login_required(login_url="dostr3adminpanellogin")
@admin_only
def surveyTable(request):

    surveys = Survey.objects.all()

    context = {
        "surveys": surveys,
    }

    return render(
        request,
        "main/pages/panel/containers/SurveyTable.html",
        context,
    )


def logoutAdmin(request):
    logout(request)
    return redirect("dostr3adminpanellogin")
