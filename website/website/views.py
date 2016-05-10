from django.shortcuts import render_to_response

def about(request):
    template_name = 'about.html'
    return render_to_response(template_name)