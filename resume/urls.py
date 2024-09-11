from django.urls import path
from .views import upload_resume, ExtractResumeAPIView

urlpatterns = [
    path('', upload_resume, name='upload_resume'),  # Root URL to render the HTML form
    path('api/extract_resume/', ExtractResumeAPIView.as_view(), name='extract_resume'),  # API endpoint
]