from django.shortcuts import render
from django.views import View
from sql_db.models import RoutineEntry, Section
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

class RoutineView(LoginRequiredMixin, View):
    login_url = "/signin/"
    def get(self, request):
        user = request.user
        user_section_name = getattr(user, "section", None)

        if not user_section_name:
            return_context = {
                "error": "NO SECTION SELECTED"
            }
            return render(request, "routine.html", return_context)

        try:
            user_section = Section.objects.get(name=user_section_name)
        except Section.DoesNotExist:
            return_context = {
                "error": "SECTION DOES NOT EXIST"
                }
            return render(request, "routine.html", return_context)

        days = ["SUN", "MON", "TUE", "WED", "THU", "FRI"]
        routines_by_day = []

        # FETCH ROUTINE ENTRY FOR EACH DAY
        for day in days:
            entries = RoutineEntry.objects.filter(
                sections=user_section,
                routine__show_on_website=True,
                day=day
            ).order_by("time_range")
            routines_by_day.append((day, entries))

        today = datetime.now().strftime("%a").upper()[:3]
        return_context = {
            "routines_by_day": routines_by_day,
            "today": today,
            "user_section": user_section.name,
        }
        return render(request, "routine.html", return_context)
