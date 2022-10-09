from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
from .predict import main

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            result = main([{
                "noOfMembers": file_serializer.data['noOfMembers'],
                "noOofTimesUsingTheIron": file_serializer.data['noOofTimesUsingTheIron'],
                "noOfTimesUsingTheWashingMachine": file_serializer.data['noOfTimesUsingTheWashingMachine'],
                "firstmonthUnits": file_serializer.data['firstmonthUnits'],
                "secondMonthUnits": file_serializer.data['secondMonthUnits'],
                "thirdMonthUnits": file_serializer.data['thirdMonthUnits'],
                "firstMonthCost": file_serializer.data['firstMonthCost'],
                "secondMonthCost": file_serializer.data['secondMonthCost'],
                "thirdMonthCost": file_serializer.data['thirdMonthCost'],
                "averageUnits" : file_serializer.data['averageUnits'],
                "microwave_Yes": file_serializer.data['microwave_Yes'],
                "hairDryer_Yes": file_serializer.data['hairDryer_Yes'],
                "electricOven_Yes": file_serializer.data['electricOven_Yes'],
                "windowType_Yes": file_serializer.data['windowType_Yes'],
                "waterGeyser_Yes": file_serializer.data['waterGeyser_Yes'],
                "electricWaterHeater_Yes": file_serializer.data['electricWaterHeater_Yes'],
                "cielingFan_Yes": file_serializer.data['cielingFan_Yes'],
                "standFan_Yes" : file_serializer.data['standFan_Yes'],
                "tableFan_Yes" : file_serializer.data['tableFan_Yes'],
                "exhaustFan_Yes": file_serializer.data['exhaustFan_Yes']
                }])
            resultValue = {"Reason": result[0],
                            "Units": result[1][0]}
            return Response(resultValue, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
