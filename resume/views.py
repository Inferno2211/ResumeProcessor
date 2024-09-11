from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from pyresparser import ResumeParser
import os
import spacy
import tempfile

def upload_resume(request):
    return render(request, 'upload_resume.html')

class ExtractResumeAPIView(APIView):
    parser_classes = [MultiPartParser]  # To handle file uploads

    def post(self, request, format=None):
        # Check if 'resume' is in the request files
        if 'resume' not in request.FILES:
            return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

        file = request.FILES['resume']
        
        # Ensure the file was successfully uploaded
        try:
            file_name = file.name
            file_extension = os.path.splitext(file_name)[1]
            
            if file_extension not in ['.pdf', '.docx']:
                return Response({"error": "Unsupported file format. Please upload a PDF or DOCX."},
                                status=status.HTTP_400_BAD_REQUEST)

            # Create a temporary file to store the uploaded resume
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
                for chunk in file.chunks():
                    temp_file.write(chunk)

                temp_file_path = temp_file.name

            # Load the spacy language model
            nlp = spacy.load("en_core_web_sm")  # Load the model

            # Parse the resume using pyresparser
            data = ResumeParser(temp_file_path).get_extracted_data()

            # Remove the temporary file after parsing
            os.remove(temp_file_path)

            if not data:
                return Response({"error": "Failed to parse the resume."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Return the extracted data (e.g., name, email, phone)
            return Response({
                "first_name": data.get('name', 'N/A'),
                "email": data.get('email', 'N/A'),
                "mobile_number": data.get('mobile_number', 'N/A'),
            })

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)