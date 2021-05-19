from django.shortcuts import render

def index(request):
	context = {
		'Title':'Document Management System',
		'heading':'Welcome to Document Management System',
	}
	return render(request,'index.html',context)
