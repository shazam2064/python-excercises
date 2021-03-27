from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from restapi import models, serializers


# Create your views here.
class ExpenseListCreate(APIView):
    def get(self, request):
        expenses = models.Expense.object.all()
        serializer = serializers.Expense(expenses, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = serializers.Expense(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)
