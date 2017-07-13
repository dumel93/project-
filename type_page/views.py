from datetime import *
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from .forms import UserLoginForm, UserCreateForm
from django.contrib.auth import authenticate, login, logout
from .models import User, FootballType


class TyperBaseView(View):
    def get(self, request):
        return render(request, 'type_page/base.html')


class TyperIndexView(View):


    def get(self, request):
        form = UserLoginForm()
        users = User.objects.count() - 1

        this_year = datetime.now().year
        this_month = datetime.now().month
        today = datetime.now()
        month=today.strftime("%B")
        start = date(this_year, this_month, 1)
        end = date(this_year, this_month, 30)

        prev_month_nb=this_month-1
        prev_month = datetime.strptime(str(prev_month_nb), '%m')
        prev_month_name=datetime.strftime(prev_month, '%B')
        draws_ok_t=len(FootballType.objects.filter(date_game__range=[start, end], draw=True))
        draws_t=len(FootballType.objects.filter(date_game__range=[start, end]))
        sum_t=0
        for types in FootballType.objects.filter(date_game__range=[start, end]).all():
            sum_t += types.total

        draws_ok_y = len(FootballType.objects.filter(date_game__year=this_year, draw=True))
        draws_y = len(FootballType.objects.filter(date_game__year=this_year))
        sum_y=0
        for types_y in FootballType.objects.filter(date_game__year=this_year).all():
            sum_y += types_y.total

        draws_ok_p = len(FootballType.objects.filter(date_game__range=[date(this_year, this_month-1, 1),
                                                                       date(this_year, this_month-1, 30)], draw=True))
        draws_p = len(FootballType.objects.filter(date_game__range=[date(this_year, this_month-1, 1),
                                                                       date(this_year, this_month-1, 30)]))
        sum_p = 0
        for types in FootballType.objects.filter(date_game__range=[date(this_year, this_month-1, 1),
                                                                       date(this_year, this_month-1, 30)]).all():
            sum_p += types.total

        try:
            accuracy= round(100*draws_ok_t/draws_t)
        except ZeroDivisionError:
            accuracy = 0

        try:
            accuracy_y=round(100*draws_ok_y/draws_y)
        except ZeroDivisionError:
            accuracy_y = 0
        try:
            accuracy_p=round(100*draws_ok_p/draws_p)
        except ZeroDivisionError:
            accuracy_p=0


        ctx = {'form': form,
               "users": users,
               "this_year": this_year,
               "this_month": this_month,
               "draws_ok_t": draws_ok_t,
               "draws_ok_y": draws_ok_y,
               "draws_ok_p": draws_ok_p,
               "draws_t": draws_t,
               "draws_y": draws_y,
               "draws_p": draws_p,
               "sum_t": sum_t,
               "sum_y": sum_y,
               "sum_p": sum_p,
               "month": month,
               "accuracy": accuracy,
               "accuracy_y": accuracy_y,
               "accuracy_p": accuracy_p,
               "prev_month": prev_month,
               "prev_month_name": prev_month_name
               }

        return render(request, 'type_page/index.html', ctx)


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        ctx = {'form': form}
        return render(
            request,
            'type_page/index.html',
            ctx
        )

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('index/')
        else:
            return render(
                request,
                'type_page/index.html',
                {'form': form}
            )


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "type_page/user_form.html"
    success_url = 'typer/'


class UserLogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('index')
        else:
            return redirect('login')


class DrawHistoryView(View):
    def get(self, request):
        today = date.today()
        yesterday = today - timedelta(1)
        type = FootballType.objects.filter(date_game__icontains=today).filter(is_ended=True)

        sum = 0
        for bet_day in type:
            sum += bet_day.bet
        total = 0
        for total_day in type:
            total += total_day.total
        try:
            yields = round((total / sum) * 100, 2)

        except ZeroDivisionError:
            yields = 0



        ctx = {'type': type,
               'sum': sum,
               "total": total,
               "yields": yields,
               "today": today,
               "yesterday": yesterday
               }

        return render(request, 'type_page/football_type_list.html', ctx)


class DrawHistoryDayView(View):

    def get(self, request, date_url):
        today = date.today()
        date_page = datetime.strptime(date_url, '%Y-%m-%d')
        prev = date_page - timedelta(1)
        next = date_page + timedelta(1)

        type = FootballType.objects.filter(date_game__icontains=date_url).filter(is_ended=True)

        sum = 0
        for bet_day in type:
            sum += bet_day.bet
        total = 0
        for total_day in type:
            total += total_day.total
        try:
            yields = round((total / sum) * 100, 2)

        except ZeroDivisionError:
            yields = 0

        if date_page.date() == today:
            return redirect('draw-history')

        ctx = {'type': type,
               'sum': sum,
               "total": total,
               "yields": yields,
               "date_page": date_page.date(),
               "prev": prev.date(),
               "next": next.date(),
               "today": today
               }

        return render(request, 'type_page/football_type_day_list.html', ctx)

class DrawLastTypesView(View):

    def get(self,request):
        now = datetime.now()
        last_types=FootballType.objects.order_by('-id').filter(is_ended=False).filter(date_game__gte=now)

        try:
            last_type=last_types[0]
            ctx = {"last_type": last_type}
            return render(request, 'type_page/last_added.html', ctx)
        except Exception:
            return render(request, 'type_page/exception.html')

class DrawCurrentlyTypesView(View):

    def get(self,request):
        currently_types=FootballType.objects.filter(is_ended=False).all()
        now=datetime.now()
        unresolved_types=FootballType.objects.filter(date_game__lte=now).filter(is_ended=False)

        return render(request, 'type_page/currently.html', {"currently_types":currently_types})

class DrawUnresolvedTypesView(View):

    def get(self,request):
        now = datetime.now()
        unresolved_types = FootballType.objects.filter(date_game__gte=now).filter(is_ended=False)
        return render(request, 'type_page/unresolved.html', {"unresolved_types": unresolved_types})