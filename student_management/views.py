from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentImportAPIView(APIView):

    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response(
                {"error": "CSV file is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {"message": "Students imported successfully."},
            status=status.HTTP_201_CREATED
        )