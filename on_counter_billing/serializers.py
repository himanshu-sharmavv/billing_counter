from rest_framework import serializers
from .models import CustomUser, Employee, Product, Customer, Bill, BillProduct

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')

class EmployeeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value

class CustomerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        return value

class BillProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillProduct
        fields = ('product', 'quantity')

class BillSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    employee = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    products = BillProductSerializer(many=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Bill
        fields = ('customer', 'employee', 'products', 'total')

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        total = 0
        for product_data in products_data:
            product = product_data['product']
            quantity = product_data['quantity']
            total += product.price * quantity
            product.quantity -= quantity
            product.save()
        validated_data['total'] = total
        bill = Bill.objects.create(**validated_data)
        for product_data in products_data:
            BillProduct.objects.create(bill=bill, **product_data)
        return bill