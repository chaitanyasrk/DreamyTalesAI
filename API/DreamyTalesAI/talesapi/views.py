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
        prompt = f"Act as a creative storyteller for a {data['age']}-year-old kid named {data['kid_name']} from {data['location']}, who enjoys {', '.join(data['hobbies'])}. Write a story that includes elements of their hobbies, making it readable and simple to understand. Include some simple rhyming paragraphs to make the story more kid-friendly."

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use an appropriate model like "text-davinci-004"
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            story = response['choices'][0]['message']['content']
            return Response({'story': story}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)