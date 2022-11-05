from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer
from base.models import Question, OperationType
from rest_framework import status


@api_view(['GET'])
def getData(request):
    # person = {'slackUsername' : 'Destiny', 'backend': True, 'age' : 17, 'bio' : 'My name is John Destiny. I am a Web Developer as well as a Mechatronics Engineering student. I am very passionate about Technology and Engineering. I am a very creative person and also a problem solver'}

    questions = Question.objects.all()

    serializer = QuestionSerializer(questions, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    x = request.data['x']
    y = request.data['y']
    operation_type = request.data['operation_type']

  
    if operation_type == OperationType.AD.value:
      result = int(x) + int(y)

    if operation_type == OperationType.SU.value:
      result = int(x) - int(y)

    if operation_type == OperationType.MU.value:
      result = int(x) * int(y)

  

    data = {'operation_type': operation_type, 'x': x, 'y': y, 'result': result}

    serializer = QuestionSerializer(data=data)

    if serializer.is_valid():

      serializer.save()
      return Response(serializer.data)

    else:
      return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
 
