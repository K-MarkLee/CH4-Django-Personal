from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


# Create your views here.

# index 페이지의 view 함수
def index(request):
    
    # 로그인한 유저는 main 페이지로 이동
    if request.user.is_authenticated:
        return render(request, 'products/main.html')

    # sign up 폼을 form 변수에 저장
    form = AuthenticationForm()
    context = {"form" : form}
    return render(request, 'products/index.html', context)


@login_required
def main(request):
    products = Product.objects.all().order_by('-created_at')  # 최신 글 순으로 정렬
    context = {'products': products}
    return render(request, 'products/main.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user  # 현재 로그인된 사용자를 작성자로 설정
            product.save()
            return redirect('products:detail', pk=product.pk)   # 작성한 글의 detail 페이지로 이동
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'products/product_create.html', context)




@login_required
def detail(request, pk):
    product = Product.objects.get(pk=pk)
    liked = product.likes.filter(id=request.user.id).exists() # 좋아요를 눌렀는지 확인
    from_liked_products = request.GET.get('from') == 'liked_products'  # 좋아요 누른 글에서 왔는지 확인
    context = {
        'product': product, 
        'liked': liked, 
        'from_liked_products': from_liked_products
    }
    return render(request, 'products/product_detail.html', context)



@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.author or request.user.is_staff or request.user.is_superuser:
        product.delete()
        return redirect('products:main')
    return redirect('products:detail', pk=pk)


@login_required
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user != product.author and not request.user.is_staff or request.user.is_superuser:
        return redirect('products:detail', pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:detail', pk=pk)
    else:
        form = ProductForm(instance=product)

    context = {'form': form, 'product': product}
    return render(request, 'products/product_update.html', context)


@login_required
def like(request, pk):
    # 작성자는 좋아요를 누를 수 없음
    product = get_object_or_404(Product, pk=pk)
    if request.user != product.author.username:

        if request.user in product.likes.all():
            product.likes.remove(request.user) # 좋아요 취소
        else:
            product.likes.add(request.user) # 좋아요
        return redirect('products:detail', pk=pk)
    return redirect('products:detail', pk=pk)


@login_required
def liked_products(request):
    liked_products = request.user.liked_products.all()
    context = {'products': liked_products} # 좋아요 누른 글만 필터링
    return render(request, 'products/product_liked.html', context)