# WebApplication for Event Registration

## AIM:
To create a UX design and develop a web application for event registration.
## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a webpage.
### Step 9:
Publish the website in the given URL.
### Step 10:
create a UX design for the web application.
### Step 11:
Choosing the suitable color scheme
### Step 12:
Creating artboards for individual pages
### Step 13:
Designing layout for individual pages
### Step 14:
Creating links and linking it with artboards
### Step 15:
Preview the prototype.


## DESIGN SCREENS:
![output](./static/img/design.png)

## WIREFRAME:
![output](./static/img/wireframe.png)

## PROTOTYPE:
![output](./static/img/preview1.png)
![output](./static/img/preview2.png)
![output](./static/img/preview3.png)
![output](./static/img/preview4.png)
![output](./static/img/preview5.png)

## PROGRAM:

### home.html
~~~
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <div class="jumbotron">
        <div class="cotainer">
            <h1 class="display-4">Working on IOT</h1>
            <p class="lead">It fulfills the need of people in storing important data. </p>
            <hr class="my-4">
            <p class="lead">
            <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
            </p>
        </div>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-12 text-center">
                <h1>One day workshop on internet of thing</h1>
            </div>
        </div>
        <div class="row">
            <div class="col-12 text-center">
                <a href="/register/" class="btn btn-primary btn-lg" role="button">Register</a>
            </div>
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
~~~

### register.html
~~~
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags --> 
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

     <title>Event Register</title>
  </head>
  <body>
      
      
      <div class="jumbotron jumbotron-fluid" style="background-color:orange;">
        <div class="container  text-center">
            
            <img class="card-img" src="/static/img/sec.jpg" style="width: 100px; height: 100px;" alt="Card image cap">
            <h1>Saveetha Engineering college</h1>
        </div>
      </div>

    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1>Application</h1>
            </div>
        </div> 
       <form action="/register/" method="POST">
        {% csrf_token %}
        <div class="container display-4 text-center" style=color:green >
        <div class="form-group">
            <label for="username">NAME</label>
            <input type="text" class="form-control" id="username" name="username" placeholder="Enter your name">
        </div>
        <div class="form-group">
            <label for="phone">MOBILE</label>
            <input type="text" class="form-control" id="phone" name="phone" placeholder="Enter your Phone.no">
        </div>
        <div class="form-group">
            <label for="email">EMAIL</label>
            <input type="email" class="form-control" id="email" name="email" placeholder="name@example.com">
        </div>
        <div class="form-group">
            <label for="institution">institution</label>
            <input type="text" class="form-control" id="institution" name="institution" placeholder="Institution name">
        </div>
        <div class="col-12 text-center">
              
              <input type="submit" class="btn btn-primary btn-lg"  aria-pressed="true"></a>
              
        </div>
    </div>
    </form>

    </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>

</html>
~~~

### listofparticipants.html
~~~
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags --> 
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

     <title>Event Register</title>
  </head>
  <body>
      
      
      <div class="jumbotron jumbotron-fluid" style="background-color:orange;">
        <div class="container  text-center">
            
            <img class="card-img" src="/static/img/sec.jpg" style="width: 100px; height: 100px;" alt="Card image cap">
            <h1>Saveetha Engineering college</h1>
        </div>
      </div>

    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1>Application</h1>
            </div>
        </div> 
       <form action="/register/" method="POST">
        {% csrf_token %}
        <div class="container display-4 text-center" style=color:green >
        <div class="form-group">
            <label for="username">NAME</label>
            <input type="text" class="form-control" id="username" name="username" placeholder="Enter your name">
        </div>
        <div class="form-group">
            <label for="phone">MOBILE</label>
            <input type="text" class="form-control" id="phone" name="phone" placeholder="Enter your Phone.no">
        </div>
        <div class="form-group">
            <label for="email">EMAIL</label>
            <input type="email" class="form-control" id="email" name="email" placeholder="name@example.com">
        </div>
        <div class="form-group">
            <label for="institution">institution</label>
            <input type="text" class="form-control" id="institution" name="institution" placeholder="Institution name">
        </div>
        <div class="col-12 text-center">
              
              <input type="submit" class="btn btn-primary btn-lg"  aria-pressed="true"></a>
              
        </div>
    </div>
    </form>

    </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>

</html>
~~~

### views.py
~~~
from django.shortcuts import render
from .models import participant

# Create your views here.
def home(request):
    context = {}
    return render(request, 'events/home.html', context)

def register(request):
    context = {}
    if request.method == 'POST':
       p1 = participant()
       p1.username = request.POST.get('username', '-')
       p1.email = request.POST.get('email', '-')
       p1.phone = request.POST.get('phone', '000')
       p1.institution = request.POST.get('institution', '-')

       if len(participant.objects.all()) >= 5:
           return render(request,'events/failed.html', context)
       else:
            p1.save()
            return render(request,'events/success.html', context)

    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['institution'] = ''
    return render(request, 'events/register.html', context)

def listofparticipants(request):
    context = {}

    context['participant'] = participant.objects.all()
    return render(request, 'events/listofparticipants.html', context)

~~~


## OUTPUT:
![output](./static/img/home.png)
![output](./static/img/register.png)
![output](./static/img/success.png)
![output](./static/img/failed.png)
![output](./static/img/list of participants.png)
![output](./static/img/admin.png)


## RESULT:
Thus, a UX design and web application for event registration has been developed and is hoisted in the URL http://adityajv.student.saveetha.in:8000/home/ and http://adityajv.student.saveetha.in:8000/listofparticipants/ . GitHub Repo URL is https://github.com/adityajv2310/eventregistration .