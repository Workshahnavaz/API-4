from rest_framework import serializers
from.models import *

class sqlserializers(serializers.ModelSerializer):
    class Meta:
        model = sqldatabase
        fields = "__all__"