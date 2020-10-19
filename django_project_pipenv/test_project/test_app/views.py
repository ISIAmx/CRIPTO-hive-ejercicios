from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'test_app/index.html', {}) # Devuelve el archivo HTML

def words_page(request):
    return render(request, 'test_app/ciclos_index.html', {}) # Devuelve el archivo HTML