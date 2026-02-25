from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Complaint
from accounts.models import User  # ⚠️ adjust if different
from .serializers import ComplaintSerializer, ComplaintResolveSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import ComplaintSerializer

User = get_user_model()


class CreateComplaintView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")

        # 🔥 find user
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=400)

        serializer = ComplaintSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(reported_by=user)  # ⭐ FIXED
            return Response(serializer.data, status=201)

        print(serializer.errors)
        return Response(serializer.errors, status=400)
    
class ListComplaintsView(APIView):
    def get(self, request):
        complaints = Complaint.objects.all().order_by("-created_at")
        serializer = ComplaintSerializer(complaints, many=True)
        return Response(serializer.data)


class ResolveComplaintView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def patch(self, request, pk):
        complaint = Complaint.objects.get(id=pk)
        serializer = ComplaintResolveSerializer(
            complaint,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save(status="Completed")
            return Response(serializer.data)
        return Response(serializer.errors, status=400)