from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormDates, FormSalesByProduct, FormSalesType, FormDateView, FormProveedor, FormStock
from .models import Venta, Compra
from .util.dates import dates_from_form, format_date_df
from pandas import DataFrame, merge
from plotly.express import bar

# Create your views here.
def home (request):
    return render(request, "gestion_tienda/Home.html")

def ventas(request):
    form = FormDates()
    if request.method=='POST':
        form = FormDates(request.POST)
        if form.is_valid():
            dates = dates_from_form(request)
            dt_type = request.POST.get('dt_type')

            sales = Venta.objects.filter(fecha__gte=dates[0], fecha__lte=dates[1]).values() 
            df_sales = DataFrame(sales) 
            df_sales = format_date_df(df_sales, dt_type)
            df_sales['Venta'] = df_sales['cantidad'] * df_sales['precio']
            df_sales = df_sales.pivot_table(index='fecha',aggfunc='sum', values='Venta')
            fig = bar(df_sales, x=df_sales.index, y='Venta', title=f'Ventas {dt_type} del {dates[0].date()} al {dates[1].date()}', text_auto=True)
            return HttpResponse (fig.to_html())

    return render(request, "gestion_tienda/ventas.html",{"formu":form, "name":"Resumen Ventas"})

def venta_by_product(request):
    form =FormSalesByProduct()
    if request.method=='POST':
        form = FormSalesByProduct(request.POST)
        if form.is_valid():
            dates = dates_from_form(request)
            dt_type = request.POST.get('dt_type')
            view_type= request.POST.get('view_type')
            product = request.POST.getlist('product')
            df_sales = format_date_df(DataFrame(Venta.objects.filter(fecha__gte=dates[0], fecha__lte=dates[1]).values() ), dt_type)

            if not product:
                pass
            else:
                products = DataFrame(product, columns=['producto_id'])
                df_sales = merge(products, df_sales, on='producto_id', how='left')

            if view_type == 'venta':
                df_sales["cantidad"] = df_sales["cantidad"] * df_sales['precio']

            df_sales = df_sales.pivot_table( index=['producto_id','fecha'],values='cantidad', aggfunc='sum').reset_index()
            fig = bar(df_sales, x='fecha',y='cantidad',color='producto_id', text_auto=True, title=f'Ventas por productos {dt_type} del {dates[0].date()} al {dates[1].date()}')

            return HttpResponse(fig.to_html())

    return render(request, "gestion_tienda/ventas.html",{"formu":form, "name":"Resumen Ventas por Producto"})

def venta_by_region(request):
    form = FormSalesType()
    if request.method=='POST':
        form = FormSalesType(request.POST)
        if form.is_valid():
            dates = dates_from_form(request)
            view_type= request.POST.get('view_type')
            df_sales = DataFrame(Venta.objects.filter(fecha__gte=dates[0], fecha__lte=dates[1]).values() )
            
            if view_type == 'venta':
                df_sales["cantidad"] = df_sales["cantidad"] * df_sales['precio']

            df_pivot = df_sales.pivot_table(index=['region_id','producto_id'], values='cantidad', aggfunc='sum').fillna(0).reset_index()
            fig = bar(df_pivot, x="region_id", y="cantidad", color="producto_id", text_auto=True, title=f'Ventas por región del {dates[0].date()} al {dates[1].date()}')
            return HttpResponse (fig.to_html())
    return render(request, "gestion_tienda/ventas.html",{"formu":form, "name":"Resumen Ventas por Región"})

def compras(request):
    form = FormDateView()
    if request.method=='POST':
        form = FormDateView(request.POST)
        if form.is_valid():
            dates = dates_from_form(request)
            dt_type = request.POST.get('dt_type')
            view_type= request.POST.get('view_type')

            df_buy = format_date_df(DataFrame(Compra.objects.filter(fecha__gte=dates[0], fecha__lte=dates[1]).values()), dt_type)

            if view_type=='dinero':
                df_buy['cantidad'] = df_buy['cantidad'] * df_buy['precio']

            df_buy = df_buy.pivot_table(index=['fecha','producto_id'],values=['cantidad'], aggfunc={'cantidad':'sum'}).reset_index()
            fig = bar(df_buy, x='fecha', y='cantidad', color='producto_id', text_auto=True)
            return HttpResponse(fig.to_html())
    return render(request, "gestion_tienda/compras.html",{"formu":form, "name":"Resumen Compras"})

def compra_by_proveedor(request):
    form = FormProveedor()
    if request.method=='POST':
        form = FormProveedor(request.POST)
        if form.is_valid():
            dates = dates_from_form(request)
            view_type= request.POST.get('view_type')
            provedors = request.POST.getlist('proveedor')
            df_buy = DataFrame(Compra.objects.filter(fecha__gte=dates[0], fecha__lte=dates[1]).values())

            if view_type =='dinero':
                df_buy['cantidad'] = df_buy['cantidad'] * df_buy['precio']

    return render(request, "gestion_tienda/compras.html",{"formu":form, "name":"Resumen Compras Proveedores"})


def inventario(request):
    form = FormStock()
    if request.method=='POST':
        form = FormStock(request.POST)
        if form.is_valid():
            df_sale= DataFrame(list( Venta.objects.values('fecha','cantidad','precio','producto_id')))
            df_buys= DataFrame(list( Compra.objects.values('fecha','cantidad','precio','producto_id'))) 
            df_buys = df_buys.groupby('producto_id').agg({'cantidad': 'sum'})
            df_sale = df_sale.groupby('producto_id').agg({'cantidad': 'sum'})
            stock = df_buys.merge(df_sale, on='producto_id', suffixes=('_compras', '_ventas'))
            stock['disponible'] = stock['cantidad_compras'] - stock['cantidad_ventas']
            #TODO hacer filtro por productos
            fig = bar(stock, x=stock.index, y='disponible', text='disponible')
            return HttpResponse(fig.to_html())
            

    return render(request, "gestion_tienda/compras.html",{"formu":form, "name":"Inventario"})