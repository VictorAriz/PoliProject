from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.


def home(request):
    userlist = User.objects.all()
    # messages.success(request, '¡Usuarios listados!')
    return render(request, "gestionuser.html", {"users": userlist})



def registrarUser(request):
    codigo = request.POST['txtCodigo']
    name = request.POST['txtName']
    last_name= request.POST['txtLast_name']
    mail = request.POST['txtMail']
    user_name = request.POST['txtUser_name']
    document = request.POST['numDocument']

    user = User.objects.create(
        codigo=codigo, name=name, last_name=last_name, mail=mail, user_name=user_name, document=document)
    messages.success(request, '¡Usuario registrado!')
    return redirect('/user')


def edicionUser(request, codigo):
    user = User.objects.get(codigo=codigo)
    return render(request, "edicionUser.html", {"user": user})


def editarUser(request):
    codigo = request.POST['txtCodigo']
    name = request.POST['txtName']
    last_name= request.POST['txtLast_name']
    mail = request.POST['txtMail']
    user_name = request.POST['txtUser_name']
    document = request.POST['numDocument']

    user = User.objects.get(codigo=codigo)
    user.name = name
    user.last_name = last_name
    user.mail = mail
    user.user_name = user_name
    user.document = document
    user.save()

    messages.success(request, '¡Usuario actualizado!')

    return redirect('/user')


def eliminarUser(request, codigo):
    user = User.objects.get(codigo=codigo)
    user.delete()

    messages.success(request, '¡Usuario eliminado!')

    return redirect('/user')



def user_create(request):
    if request.method == 'POST':
        form = userForm(request.POST, instance=request.user)
        form2 = profileForm(request.POST, instance=request.user.profile)
        if form.is_valid() and form2.is_valid():
            #form.groups.add(form.cleaned_data['group'])
            user = form.save()
            user.groups.add(form.cleaned_data['group'])
            #profile = form2.save(commit=False)
            form2.save()
            #profile.User = form.save()
            #profile.save()
            return redirect('users:user_list')
    else:
        form = userForm()
        form2 = profileForm()
    return render(request, 'users_form.html', {'form': form, 'form2': form2})