from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.core.mail import EmailMessage
from django.conf import settings
# import os
# from mst.settings import STATIC_DIR

from .models import *

# Create your views here.


# def home_page(request):
#     return render(request, 'index.html', )

def tq_page(request):
    return render(request, 'Thanks.html', )

def fail_page(request):
    return render(request, 'fail.html', )

def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def informals_page(request):
    return render(request, 'informal.html')

def schedule_page(request):
    return render(request, 'schedule.html')

# def gallery_page(request):
#     nums = []
#     for i in range(30):
#         nums.append(i+1)
#     return render(request, 'gallery.html', {'num' : nums})

def team_page(request):
    return render(request, 'team.html')

def register_page(request):
    if request.method == 'GET':
        response = {
            'msg': 'Regiser Here',
            'method': 'GET'
        }
        return render(request, 'index.html', response)
    elif request.method == 'POST':
        mailBody = ''
        mem = Member()
        mem.name = request.POST['name']
        mem.college = request.POST['college']
        mem.city = request.POST['city']
        mem.role = request.POST['designation']
        mem.email_id = request.POST['email']
        mem.mobile = request.POST['contact']
        # print('----------',int(request.POST['bad_check']))
        mailBody = mailBody + 'Name : '+mem.name+'\nCollege : '+mem.college+'\nCity : '+mem.city+'\n'
        try:
            if int(request.POST['bad_check']) == 1:
                # print("bad")
                bad = Badminton()
                mailBody = mailBody+'Badminton : \n '
                try:
                    if int(request.POST['bad_male_check']) == 1:
                        # print("bad male",request.POST['bad_male_no'],int(request.POST['bad_male_no']))
                        bad.men = int(request.POST['bad_male_no'])
                        mailBody = mailBody + '\tMen : ' + str(bad.men) + '\n'
                        # print("added")
                except:
                    pass
                try:
                    if int(request.POST['bad_female_check']) == 1:
                        bad.women = int(request.POST['bad_female_no'])
                        mailBody = mailBody + '\tWomen : ' + str(bad.women) + '\n'
                except:
                    pass
                bad.college = mem.college
                bad.save()
                # print("------------",bad)
                mem.bad = bad
        except:
            # print("err")
            pass
        try:
            if int(request.POST['cri_check']) == 1:
                mailBody = mailBody + 'Cricket : \n '
                cri = Cricket()
                try:
                    if int(request.POST['cri_male_check']) == 1:
                        cri.men = int(request.POST['cri_male_no'])
                        mailBody = mailBody + '\tMen : ' + str(cri.men) + '\n'
                    cri.college = mem.college
                    cri.save()
                    mem.cri = cri
                except:
                    pass
        except:
            pass
        try:
            if int(request.POST['tab_check']) == 1:
                mailBody = mailBody + 'Table Tennis : \n '
                tab = TableTennis()
                try:
                    if int(request.POST['tab_male_check']) == 1:
                        tab.men = int(request.POST['tab_male_no'])
                        mailBody = mailBody + '\tMen : ' + str(tab.men) + '\n'
                except:
                    pass
                try:
                    if int(request.POST['tab_female_check']) == 1:
                        tab.women = int(request.POST['tab_female_no'])
                        mailBody = mailBody + '\tWomen : ' + str(tab.women) + '\n'
                except:
                    pass
                tab.college = mem.college
                tab.save()
                mem.tab = tab
        except:
            pass
        try:
            if int(request.POST['vol_check']) == 1:
                mailBody = mailBody + 'Volleyball : \n '
                vol = Volleyball()
                try:
                    if int(request.POST['vol_male_check']) == 1:
                        vol.men = int(request.POST['vol_male_no'])
                        mailBody = mailBody + '\tMen : ' + str(vol.men) + '\n'
                except:
                    pass
                try:
                    if int(request.POST['vol_female_check']) == 1:
                        vol.women = int(request.POST['vol_female_no'])
                        mailBody = mailBody + '\tWomen : ' + str(vol.women) + '\n'
                except:
                    pass
                vol.college = mem.college
                vol.save()
                mem.vol = vol
        except:
            pass
        try:
            if int(request.POST['bas_check']) == 1:
                mailBody = mailBody + 'Basketball : \n '
                bas = BasketBall()
                try:
                    if int(request.POST['bas_male_check']) == 1:
                        bas.men = int(request.POST['bas_male_no'])
                        mailBody = mailBody + '\tMen : ' + str(bas.men) + '\n'
                except:
                    pass
                try:
                    if int(request.POST['bas_female_check']) == 1:
                        bas.women = int(request.POST['bas_female_no'])
                        mailBody = mailBody + '\tWomen : ' + str(bas.women) + '\n'
                except:
                    pass
                bas.college = mem.college
                bas.save()
                mem.bas = bas
        except:
            pass
        try:
            if int(request.POST['foo_check']) == 1:
                foo = Football()
                mailBody = mailBody + 'Football : \n '
                try:
                    if int(request.POST['foo_male_check']) == 1:
                        foo.men = int(request.POST['foo_male_no'])
                        mailBody = mailBody + '\tMen : ' + str(foo.men) + '\n'
                except:
                    pass
                foo.college = mem.college
                foo.save()
                mem.foo = foo
        except:
            pass
        try:
            if int(request.POST['ten_check']) == 1:
                ten = Tennis()
                mailBody = mailBody + 'Tennis : \n '
                try:
                    if int(request.POST['ten_male_check']) == 1:
                        ten.men = int(request.POST['ten_male_no'])
                        mailBody = mailBody + '\tMen : ' + str(ten.men) + '\n'
                except:
                    pass
                try:
                    if int(request.POST['ten_female_check']) == 1:
                        ten.women = int(request.POST['ten_female_no'])
                        mailBody = mailBody + '\tWomen : ' + str(ten.women) + '\n'
                except:
                    pass
                ten.college = mem.college
                ten.save()
                mem.ten = ten
        except:
            pass
        try:
            if int(request.POST['che_check']) == 1:
                che = Chess()
                mailBody = mailBody + 'Chess : \n '
                try:
                    if int(request.POST['che_male_check']) == 1:
                        che.men = int(request.POST['che_male_no'])
                        mailBody = mailBody + '\tMen : ' + str(che.men) + '\n'
                except:
                    pass
                try:
                    if int(request.POST['che_female_check']) == 1:
                        che.women = int(request.POST['che_female_no'])
                        mailBody = mailBody + '\tWomen : ' + str(che.women) + '\n'
                except:
                    pass
                che.college = mem.college
                che.save()
                mem.che = che
        except:
            pass
        try:
            if int(request.POST['kab_check']) == 1:
                kab = Kabaddi()
                mailBody = mailBody + 'Kabaddi : \n '
                try:
                    if int(request.POST['kab_female_check']) == 1:
                        kab.women = int(request.POST['kab_male_no'])
                        mailBody = mailBody + '\tWomen : ' + str(kab.women) + '\n'
                except:
                    pass
                kab.save()
                mem.kab = kab
        except:
            pass
        try:
            if int(request.POST['gym_check']) == 1:
                gym = Gym()
                mailBody = mailBody + 'Gym : \n '
                try:
                    if int(request.POST['gym_wei_check']) == 1:
                        gym.weightLifting = int(request.POST['gym_wei_no'])
                        mailBody = mailBody + '\tWeight Lifting : ' + str(gym.weightLifting) + '\n'
                except:
                    pass
                try:
                    if int(request.POST['gym_pow_check']) == 1:
                        gym.powerLifting = int(request.POST['gym_pow_no'])
                        mailBody = mailBody + '\tPower Lifting : ' + str(gym.powerLifting) + '\n'
                except:
                    pass
                try:
                    if int(request.POST['gym_bes_check']) == 1:
                        gym.bestPhysique = int(request.POST['gym_bes_no'])
                        mailBody = mailBody + '\tBest Physique : ' + str(gym.bestPhysique) + '\n'
                except:
                    pass
                gym.college = mem.college
                gym.save()
                mem.gym = gym
        except:
            pass
        mem.save()
        mailBody = mailBody + '\nMobile : '+mem.mobile
        email = EmailMessage(
            'MST Registration',
            'Hi '+mem.name+ '\n\nYour registration in MST\'18 has been successful\n\nThe registration form will be soon sent to you. Please fill out the form and submit it on your arrival at the registration desk\n\nThank You',
            settings.EMAIL_HOST_USER,
            [mem.email_id]
        )
        email1 = EmailMessage(
            'MST Online Registration',
            mailBody,
            settings.EMAIL_HOST_USER,
            ['manishgnote69@gmail.com','2015ucp1752@mnit.ac.in','2015uch1763@mnit.ac.in']
        )
        # pdf = os.path.join(STATIC_DIR, 'registrationForm.pdf')
        # email.attach_file(pdf)
        try:
            email.send()
            email1.send()
            print("YEs")
            return redirect('/thankyou/')
        except:
            return redirect('/failure/')
