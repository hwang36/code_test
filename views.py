
import datetime
from django.db.models import Avg, Max, Min

@csrf_exempt
def view_data(request):
    days = 3
    today = datetime.datetime.today()

    all_device_ids = View_data.objects.all().distinct()
    one_day_summary = {}
    devices_summary = {}
    for x in range(0, days):
        day = today + x
        all_device_one_day = View_data.objects.all().filter(excel_data = day)
        for device_id in all_device_ids:
            one_device_data = all_device_one_day.filter(device_id = device_id)
            one_device_summary = {}
            one_device_summary['max_kwh'] = one_device_data.aggregate(Max('kwh'))
            one_device_summary['min_kwh'] = one_device_data.aggregate(Min('kwh'))
            one_device_summary['ave_kwh'] = one_device_data.aggregate(Avg('kwh'))
            one_device_summary['graphNm'] = device_id + day
            devices_summary[device_id] = one_device_summary

        one_day_summary[day] = devices_summary

    return_json = {}
    return_json['summary'] = one_day_summary

    return render_to_response('agglobal/summary.html', return_json, context_instance=RequestContext(request))

