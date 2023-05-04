from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import requests
import json
from django.http import JsonResponse

# Create your views here.


@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def getchatresponse(request):
    openai_api_key = "sk-..."
    if request.body:
        try:
            data = json.loads(request.body)
            chat_prompt = data.get("prompt", "")

            url = "https://api.openai.com/v1/completions"

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {openai_api_key}"
            }

            data = {
                "model": "text-davinci-003",
                "prompt": chat_prompt,
                "max_tokens": 200,
                "temperature": 0
            }

            response = requests.post(url, headers=headers, json=data)

            response = response.json()

            return JsonResponse(response)

        except:
            return JsonResponse({"error": "Invalid JSON Response"}, status=400)
    else:
        return JsonResponse({"error": "Empty request Bosy"}, status=400)
