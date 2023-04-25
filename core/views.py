from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from core.models import Churn
from core.models import Reviews
from core.serializers import ChurnSerializer
from core.serializers import ReviewSerializer
from django.http.response import JsonResponse

# Create your views here.
#GET, POST, PUSH, DELETE methods defined
@csrf_exempt
def churnApi(request,id=0):
    if request.method=='GET':
        churns = Churn.objects.all()
        churns_serializer = ChurnSerializer(churns, many=True)
        return JsonResponse(churns_serializer.data, safe=False)
    elif request.method=='POST':
        churn_data=JSONParser().parse(request)
        churns_serializer = ChurnSerializer(data=churn_data)
        if churns_serializer.is_valid():
            churns_serializer.save()
            return JsonResponse("Added Successfully!", safe = False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        churn_data = JSONParser().parse(request)
        churn=churns.objects.get(ModelPred=churn_data['ModelPred'])
        churns_serializer=ChurnSerializer(churn,data=churn_data)
        if churns_serializer.is_valid():
            churns_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        churn=Churn.objects.get(ModelPred=id)
        churn.delete()
        return JsonResponse("Deleted successfully", safe=False)

@csrf_exempt
def ReviewApi(request,id=0):
    if request.method=='GET':
        reviews = Reviews.objects.all()
        reviews_serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(reviews_serializer.data, safe=False)
    elif request.method=='POST':
        review_data=JSONParser().parse(request)
        reviews_serializer = ReviewSerializer(data=review_data)
        if reviews_serializer.is_valid():
            reviews_serializer.save()
            return JsonResponse("Added Successfully!", safe = False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        review_data = JSONParser().parse(request)
        review=reviews.objects.get(ModelPred=review_data['ModelPred'])
        reviews_serializer=ReviewSerializer(review,data=review_data)
        if reviews_serializer.is_valid():
            reviews_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        review=Reviews.objects.get(ModelPred=id)
        review.delete()
        return JsonResponse("Deleted successfully", safe=False)

        
#Render frontend from folder
def front(request):
    context = { }
    return render(request, "index.html", context)

