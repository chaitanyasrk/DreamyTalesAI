from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
from .serializers import StorySerializer

class StoryAPIView(APIView):
    def post(self, request):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                openai.api_key = 'YOUR_API_KEY'
                prompt = f"Act as a creative storyteller for a {data['age']}-year-old kid named {data['kid_name']} from {data['location']}, who enjoys {', '.join(data['hobbies'])}. Write a story that includes elements of their hobbies, making it readable and simple to understand. Include some simple rhyming paragraphs to make the story more kid-friendly."
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=500
                )
                return Response({'story': response.choices[0].text.strip()}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)