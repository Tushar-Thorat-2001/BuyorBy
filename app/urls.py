from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm , MyPasswordChangeForm
urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart,),
    path('minuscart/', views.minus_cart,),
    path('removecart/', views.remove_cart,),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'), 
    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topwearsdata'), 
  
    path('bottom/', views.bottom, name='bottom'),
    path('bottom/<slug:data>', views.bottom , name='bottomdata'), 
  
    path('dress/', views.Dress, name='dress'),
    path('dress/<slug:data>', views.Dress, name='dressdata'), 
    
    path('india/', views.india, name='india'),
    path('india/<slug:data>', views.india, name='indiadata'), 

    path('sup/', views.sup, name='sup'),
    path('sup/<slug:data>', views.sup, name='supdata'),

    path('eq/', views.eq, name='eq'),
    path('eq/<slug:data>', views.eq, name='eqdata'), 
  
  

    
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',
    authentication_form=LoginForm),name='login'),
    path('logout/' , auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class= MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('registration/',views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name="app/passwordchangedone.html"), name='passwordchangedone'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
