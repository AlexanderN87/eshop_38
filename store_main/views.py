from django.shortcuts import render, redirect
from .import models

from telebot import TeleBot

bot = TeleBot('6244918183:AAHhiN_MdOlYPZZqmML4smDSYaPTiC1xa2U', parse_mode="HTML")
# Функция для главной страницы
def home(request):
    # Получить все продукты из базы
    all_products = models.Products.objects.all() # Select * FROM products

    # Получить все названия категорий
    all_categories = models.Category.objects.all() # Select * FROM category

    # и передать на Фрон часть
    context = {'products': all_products, 'categories': all_categories}

    return render(request, 'index.html', context)

# Функция для отображения информации о конкретном продукте
def about_product(request, pk):
    # Получить конкретный продукт/данные из базы
    current_product = models.Products.objects.get(product_name=pk)

    context = {'product': current_product}

    return render(request, 'about.html', context)

# Продукты из конкретной категории
def category_products(request, pk):
    category = models.Category.objects.get(category_name=pk)
    products_from_category = models.Products.objects.filter(product_category=category)

    context = {'products': products_from_category}

    return render(request, 'index.html', context)


# Поиск продуктов
def search_for_product(request):
    product_from_front = request.GET.get('search')
    find_product_from_db = models.Products.objects.filter(product_name__contains=product_from_front)

    context = {'products': find_product_from_db}
    return render(request, 'index.html', context)

# Добавить продукт в корзину
def add_product_to_cart(request, pk):
    # Получим сам продукт
    current_product = models.Products.objects.get(id=pk)

    # Добавим в корзину
    checker = models.UserCart.objects.filter(user_id=request.user.id, user_product=current_product)

    # Проверка
    if checker:
        # Если продукт уже добавлен
        checker[0].quantity = int(request.POST.get('pr_count'))
        checker[0].total_for_product = current_product.product_price * checker[0].quantity

        # Сохраним изменения
        # models.UserCart().save()



    else:
        # Если нет в корзине, то добавим
        models.UserCart.objects.create(user_id=request.user.id,
                                       user_product=current_product,
                                       quantity=request.POST.get('pr_count'),
                                       total_for_product=current_product.product_price * int(request.POST.get('pr_count')))

    return redirect(f'/product-detail/{current_product.product_name}')

# Страница корзины пользователя
def get_user_cart(request):
    user_cart = models.UserCart.objects.filter(user_id=request.user.id)

    context = {'user_cart': user_cart}

    return render(request, 'cart.html', context)

# Удаление товара из корзины
def delete_pr_from_cart(request, pk):
    prod_to_delete = models.UserCart.objects.get(id=pk)
    prod_to_delete.delete()
    return redirect('/cart')

# Оформление заказа и отправка в тг
def order_zakaz(request):
    # Получить корзину пользователя
    user_cart = models.UserCart.objects.filter(user_id=request.user.id)

    # Получить введные данные(имя, номер телефона, адрес
    username = request.POST.get('username')
    phone_number = request.POST.get('phone_number')
    address = request.POST.get('address')

    # Посчитать итог
    result = sum(i.total_for_product for i in user_cart)

    # Формирует сообщение для тг(инфойс)
    invoice_message = f'<b>Новый заказ</b>\n\n<b>Имя:</b> {username}\n<b>Номер:</b> {phone_number}\n<b>Адрес доставки</b> {address}\n---------\n'

    for i in user_cart:
        invoice_message += f'<b>{i.user_product}</b> X <b>{i.quantity}</b> = <b>{i.total_for_product}, </b>'

    invoice_message += f'\n----------\n<b>Итог</b> {result} сум'

    # Отправим сообщение в бот где есть админ
    bot.send_message(746988763, invoice_message)

    return redirect('/')