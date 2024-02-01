from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# views.py

from django.shortcuts import render, redirect

def registration(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        experience = request.POST.get('experience')
        designation = request.POST.get('designation')

        # Process the form data (you can add additional logic here)
        
        # Redirect to a success page
        return render(request, 'home.html')

    return render(request, 'register.html')



from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Simulate user authentication without a database
        if email == 'test@example.com' and password == 'password':
            # For simplicity, hardcoding a single user for demonstration
            # In a real-world scenario, you might implement a more secure mechanism
            user = {
                'email': email,
                'username': 'testuser',
            }

            # Store user information in session
            request.session['user'] = user

            # Redirect to a success page or dashboard
            return render(request, 'home.html', {'user': user})
        else:
            # Display an error message (you can customize this part)
            error_message = "Invalid email or password. Please try again."

    return render(request, 'login.html', {'error_message': error_message if 'error_message' in locals() else None})




