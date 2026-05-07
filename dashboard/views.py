def index(request):
    # Remove 'dashboard/' from the path
    return render(request, 'index.html')
