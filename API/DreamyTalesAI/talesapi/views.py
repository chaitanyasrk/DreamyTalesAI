from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from grpc import Status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai

from .serializers import StorySerializer

@method_decorator(csrf_exempt, name='dispatch')
class StoryAPIView(APIView):
    def post(self, request):
        # Extract necessary data from request...
        data = request.data

        # Configure OpenAI API key and settings
        openai.api_key = 'Your_API_KEY'

        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-0125",  # Updated model name here
                prompt="Your prompt here",
                max_tokens=500
            )
            story = response.choices[0].text.strip()
            return Response({'story': story}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)