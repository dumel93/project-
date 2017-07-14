from django.contrib import admin

from .models import FootballType, User


@admin.register(FootballType)
class FootBallTypeAdmin(admin.ModelAdmin):
    fields = ['first_team', 'second_team', 'date_game', 'retired',
              'draw', 'league','bet', 'course',  'is_ended', 'comments']
    list_display = ['__str__', 'date_game', 'is_ended', 'id']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
