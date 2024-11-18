from django.shortcuts import render ,redirect
from django.http import HttpResponse

from .models import *

# Create your views here.
def receipes(request):  # sourcery skip: extract-method
    if request.method == "POST":
      
     #   data = request.POST
        Book_name =request.POST.get('Book_name')
        Book_description = request.POST.get('Book_description')
        Book_image =request.FILES.get('Book_image')



        #for storing data

        Receipe.objects.create(
            Book_name=Book_name,
            Book_description=Book_description, 
            Book_image=Book_image,
        )

        return redirect('receipes')

    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(Book_name__icontains = request.GET.get('search'))

        
    recipes_with_safe_images =[]
    for recipe in queryset:
        try:
            # This will raise an exception if the image file doesn't exist
            if recipe.Book_image:
                recipe.Book_image.url
            recipes_with_safe_images.append(recipe)
        except Exception as e:
            print(f"Error with recipe {recipe.id}: {str(e)}")
    
    

    context = {'receipes':recipes_with_safe_images}
    return render(request,'receipes.html',context)


def delete_receipe(request,id):
  queryset=Receipe.objects.get(id=id)
  queryset.delete()
  return redirect('receipes')


def update_receipe(request, id):
  queryset=Receipe.objects.get( id =id)

  if request.method == 'POST':
    Book_name =request.POST.get('Book_name')
    Book_description = request.POST.get('Book_description')
    Book_image =request.FILES.get('Book_image')


    queryset.Book_name =Book_name
    queryset.Book_description = Book_description
    if Book_image:
        queryset.Book_image= Book_image

    queryset.save()
    return redirect('receipes')

  context={'receipe':queryset}
  return render(request,'update_receipes.html', context)



def calculator(request):
    c = ''
    if request.method == 'POST':
        try:
            n1 = float(request.POST.get('num1', 0))
            n2 = float(request.POST.get('num2', 0))
            opr = request.POST.get('opr', '+')
            
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "*":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2 if n2 != 0 else "Cannot divide by zero"
        except ValueError:
            c = "Invalid input. Please enter numbers only."

        print(c)
    
    return render(request, 'calculator.html', {'c': c})