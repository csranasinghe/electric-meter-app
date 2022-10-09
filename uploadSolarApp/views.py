# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Solar
from .serializers import solarSerilaizer
from .predict import main

class TodoListApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = solarSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            list_value =[serializer.data['Province'],
                        serializer.data['usage'],
                        serializer.data['rainFallType'],
                        serializer.data['skyType'],
                        serializer.data['windDirection'],
                        serializer.data['windSpeed'],
                        serializer.data['humidity'],
                        serializer.data['Temperature'],
                        serializer.data['elevation'],
                        serializer.data['radiation'],
                        serializer.data['VaporPressure'],
                        serializer.data['surfaceTemperature'],
                        serializer.data['AtmospherePressure'],
                        serializer.data['Bulbs'],
                        serializer.data['Fan'],
                        serializer.data['Iron'],
                        serializer.data['TV'],
                        serializer.data['Refrigerator'],
                        serializer.data['Blender'],
                        serializer.data['airConditioner'],
                        serializer.data['waterHeater'],
                        serializer.data['microwaveOven'],
                        serializer.data['riceCooker'],                      
                        ]
            result_value = main(list_row=list_value)
            return Response(result_value, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, *args, **kwargs):
    #     snippets = sensors.objects.all()
    #     serializer = sensorSerializer(snippets, many=True)
    #     return Response(serializer.data)