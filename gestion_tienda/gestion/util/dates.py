from datetime import datetime
from pandas import to_datetime
def dates_from_form(request):
    date_1 = datetime(int(request.POST.get('date_1_year')), int(request.POST.get('date_1_month')), int(request.POST.get('date_1_day')))
    date_2 = datetime(int(request.POST.get('date_2_year')), int(request.POST.get('date_2_month')), int(request.POST.get('date_2_day')))
    return [date_1, date_2]

def  format_date_df(df, type):
    df['fecha'] = to_datetime(df['fecha'], errors='coerce')
    if type == 'Anuales':
        df['fecha'] = to_datetime((df['fecha']).dt.strftime('%Y'))
    elif type == 'Mensuales':
        df['fecha'] = to_datetime((df['fecha']).dt.strftime('%Y-%m'))
    elif type == 'Diarias':
        pass
    return df