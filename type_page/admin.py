

from django.contrib import admin

from .models import FootballType, User



@admin.register(FootballType)
class FootBallTypeAdmin(admin.ModelAdmin):


    fields = ['first_team','second_team','date_game','draw','league','course','bet','is_ended']



@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ['username']