from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
import cv2
import pytesseract as tess


def func2(self, p):
    x = p.get("file")
    x = x.split('/')
    img = cv2.imread("media/"+x[-1], cv2.IMREAD_COLOR)
    roi = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    erd = cv2.erode(roi, None, iterations=2)
    text = tess.image_to_string(roi, config="--psm 6")    
    return text


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            result = file_serializer.data
            result = func2(self, result)

            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
