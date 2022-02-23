from django.shortcuts import render, redirect
from .models import Report
from django.contrib import messages

# Create your views here.


def home2(request):
    reportlist = Report.objects.all()
    # messages.success(request, '¡Reporte Exitoso!')
    return render(request, "gestionreport.html", {"report": reportlist})



def registrarReport(request):
    codigo = request.POST['txtCodigo']
    name = request.POST['txtName']
    description= request.POST['txtDescription']
    text = request.POST['txtText']
    image = request.POST.get('txtImagen', False)


    report = Report.objects.create(
        codigo=codigo, name=name, description=description, text=text, image=image,)
    messages.success(request, '¡Reporte Completado!')
    return redirect('/report')


def edicionReport(request, codigo):
    report = Report.objects.get(codigo=codigo)
    return render(request, "edicionReport.html", {"report": report})


def editarReport(request):
    codigo = request.POST['txtCodigo']
    name = request.POST['txtName']
    description= request.POST['txtDescription']
    text = request.POST['txtText']
    image = request.POST['txtImagen']

    report = Report.objects.get(codigo=codigo)
    report.name = name
    report.description = description
    report.text = text
    report.image = image
    report.save()

    messages.success(request, '¡Reporte actualizado!')

    return redirect('/report')


def eliminarReport(request, codigo):
    report = Report.objects.get(codigo=codigo)
    report.delete()

    messages.success(request, '¡Reporte eliminado!')

    return redirect('/report')

