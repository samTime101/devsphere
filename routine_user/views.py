from django.shortcuts import render
from django.views import View
from sql_db.models import Routine
from django.contrib.auth.mixins import LoginRequiredMixin
from collections import defaultdict

class RoutineUserView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request):
        user_section = request.user.section
        routines = Routine.objects.filter(show_on_website=True)
        routine_data = []
        days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

        for routine in routines:
            entries_by_day = defaultdict(list) # INITIALIZE DICTIONARY TO HOLD ENTRIES BY DAY
            all_entries = routine.entries.filter(sections__name=user_section).distinct().order_by('day', 'time_range')
            
            for entry in all_entries:
                entry.section_names = [section.name for section in entry.sections.all()]
                entries_by_day[entry.day].append(entry) 
                # GROUP ENTRIES BY DAY

            daily_data = []
            for day in days:
                daily_data.append({
                    'day': day,
                    'entries': entries_by_day[day] 
                    # GET ENTRIES FOR THE DAY (EMPTY IF NONE)
                })

            if all_entries.exists():
                routine_data.append({
                    'routine': routine,
                    'daily_data': daily_data 
                    # ADD DAILY DATA TO ROUTINE
                })
        return_data = {
            'routine_data': routine_data,
            'days': days
        }
        return render(request, 'routine.html', return_data)
