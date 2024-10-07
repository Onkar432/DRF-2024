from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def index(request):
    courses = {
        'course_name': 'python',
        'learn': ['flask', 'Django', 'Totnado', 'FastAPi'],
        'course_provider': 'UDEMY'

    }
    if request.method == 'GET':
        print('You hit get method')
        return Response(courses)
    elif request.method == 'POST':
        print('You hit post method')
        return Response(courses)
