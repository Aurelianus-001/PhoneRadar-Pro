import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phoneradar_pro.settings')
django.setup()

from PhoneReview.models import Brand, PhoneModel, Review
from django.contrib.auth.models import User
from django.utils.text import slugify

# 获取 admin 用户
admin_user, _ = User.objects.get_or_create(username='admin')
if admin_user.password == '':
    admin_user.set_password('woc7014admin')
    admin_user.save()
print(f"Using author: {admin_user.username}")

# 确保品牌存在（如果不存在则创建）
brands_to_create = [
    {'name': 'Samsung', 'origin': 'South Korea', 'since': 1938},
    {'name': 'OnePlus', 'origin': 'China', 'since': 2013},
    {'name': 'Google', 'origin': 'USA', 'since': 1998},
]
for data in brands_to_create:
    brand, created = Brand.objects.get_or_create(
        name=data['name'],
        defaults={
            'origin': data['origin'],
            'manufacturing_since': data['since'],
            'logo_url': f'/static/images/brands/{data["name"].lower()}.png'
        }
    )
    if created:
        print(f"Created brand: {brand.name}")
    else:
        print(f"Brand already exists: {brand.name}")

# 定义型号和测评数据
models_data = [
    # Samsung
    {'brand': 'Samsung', 'model': 'Galaxy S23 Ultra', 'launch': '2023-02-17', 'platform': 'Android',
     'review_title': 'Samsung Galaxy S23 Ultra Review: The Ultimate Android Powerhouse',
     'review_content': 'The Galaxy S23 Ultra features a 200MP main camera, Snapdragon 8 Gen 2, and an integrated S Pen. The display is stunning, battery life is excellent, and the performance is top-tier. A true competitor to the iPhone.',
     'rating': 5},
    {'brand': 'Samsung', 'model': 'Galaxy Z Fold 5', 'launch': '2023-08-11', 'platform': 'Android',
     'review_title': 'Samsung Galaxy Z Fold 5 Review: Foldable Maturity',
     'review_content': 'The Z Fold 5 refines the foldable experience with a gapless hinge, IPX8 water resistance, and improved multitasking. The inner screen is gorgeous, and the Snapdragon 8 Gen 2 handles everything with ease. Still expensive, but the best foldable on the market.',
     'rating': 4},
    # OnePlus
    {'brand': 'OnePlus', 'model': 'OnePlus 11', 'launch': '2023-02-07', 'platform': 'Android',
     'review_title': 'OnePlus 11 Review: Flagship Killer Returns?',
     'review_content': 'The OnePlus 11 brings back the bang-for-buck value with Snapdragon 8 Gen 2, 100W charging, and a Hasselblad-tuned camera system. The design is refined, the display is fluid, and OxygenOS is clean. A great alternative to pricier flagships.',
     'rating': 4},
    {'brand': 'OnePlus', 'model': 'OnePlus Open', 'launch': '2023-10-19', 'platform': 'Android',
     'review_title': 'OnePlus Open Review: A Promising First Foldable',
     'review_content': 'The OnePlus Open impresses with a lightweight design, minimal crease, and excellent multitasking features. The cameras are solid, and the battery life is decent. It competes well with the Galaxy Z Fold series.',
     'rating': 4},
    # Google
    {'brand': 'Google', 'model': 'Pixel 8 Pro', 'launch': '2023-10-12', 'platform': 'Android',
     'review_title': 'Google Pixel 8 Pro Review: The AI-Powered Camera King',
     'review_content': 'The Pixel 8 Pro excels with its Tensor G3 chip, amazing computational photography features like Best Take and Magic Editor, and a clean Android experience. The display is bright, and the seven years of updates are a standout. A top pick for photography lovers.',
     'rating': 5},
    {'brand': 'Google', 'model': 'Pixel Fold', 'launch': '2023-06-27', 'platform': 'Android',
     'review_title': 'Google Pixel Fold Review: The Best Foldable Camera?',
     'review_content': 'The Pixel Fold offers a unique landscape-oriented inner screen, excellent cameras for a foldable, and pure Android. The hinge is smooth, and the form factor is more usable when closed. Battery life is average, but the software experience is great.',
     'rating': 4},
]

for data in models_data:
    brand = Brand.objects.get(name=data['brand'])
    # 创建或获取手机型号
    phone_model, created = PhoneModel.objects.get_or_create(
        brand=brand,
        model_name=data['model'],
        defaults={
            'launch_date': data['launch'],
            'platform': data['platform'],
            'newslink': f"https://www.gsmarena.com/results.php3?sSearch={data['brand']}+{data['model'].replace(' ', '+')}",
            'image_url': f'/static/images/brands/{data["brand"].lower()}.png',
        }
    )
    if created:
        print(f"Created phone model: {phone_model}")
    else:
        print(f"Phone model already exists: {phone_model}")

    # 创建测评（如果不存在）
    review, rev_created = Review.objects.get_or_create(
        title=data['review_title'],
        defaults={
            'author': admin_user,
            'content': data['review_content'],
            'rating': data['rating'],
        }
    )
    if rev_created:
        review.phone_models.add(phone_model)
        # 生成唯一 slug
        base_slug = slugify(review.title)
        slug = base_slug
        counter = 1
        while Review.objects.filter(slug=slug).exclude(id=review.id).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        review.slug = slug
        review.save()
        print(f"  -> Added review: {review.title}")
    else:
        # 如果测评已存在，确保关联到该型号
        if phone_model not in review.phone_models.all():
            review.phone_models.add(phone_model)
            print(f"  -> Linked existing review '{review.title}' to {phone_model}")
        else:
            print(f"  -> Review already exists and linked: {review.title}")

print("\n✅ All missing phone models and reviews have been added.")