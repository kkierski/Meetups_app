from django.shortcuts import render

# Create your views here.


def index(request):
    meetups = [
        {
            'title': 'A first meetup',
            'location': 'New York',
            'slug': 'a-first-meetup'
        },

        {
            'title': 'A second meetup',
            'location': 'Paris',
            'slug': 'a-second-meetup'
        }
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups   #1 way to pass
    })

def meetups_details(request, meetup_slug):
    selected_meetup = {
        'title': 'A First Meetup!',
        'description': 'This is a first meetup!'
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],   #2 way to pass
        'meetup_description': selected_meetup['description']
    })
