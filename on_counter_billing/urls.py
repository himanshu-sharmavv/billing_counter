from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListCreate.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDestroy.as_view(), name='employee-detail'),
    path('products/', views.ProductListCreate.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
    path('customers/', views.CustomerListCreate.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroy.as_view(), name='customer-detail'),
    path('billing/', views.Billing.as_view(), name='billing'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
