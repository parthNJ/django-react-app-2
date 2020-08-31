from rest_framework import serializers
from .models import Program, UserProgram, PurchasedProgram

class ProgramSerializers(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"

class UserProgramSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProgram
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['program'] = ProgramSerializers(instance.program).data
        return response
    
class PurchasedProgramSerializers(serializers.ModelSerializer):
    class Meta:
        model = PurchasedProgram
        fields = "__all__"
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['program'] = ProgramSerializers(instance.program).data
        return response

   