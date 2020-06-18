from rest_framework import serializers

from loccate_api.models import Institution, Equipment, Company, Electrician



class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'industry', 'contact_person')

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        # fields = ('name', 'quantity', 'created_by', 'institution')
        fields = '__all__'



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'licence_class', 'licence_number', 'location')


class ElectricianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electrician
        # fields = ('name', 'quantity', 'created_by', 'institution')
        fields = '__all__'

