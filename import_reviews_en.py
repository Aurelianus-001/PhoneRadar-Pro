import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phoneradar_pro.settings')
django.setup()

from django.contrib.auth.models import User
from PhoneReview.models import Brand, PhoneModel, Review

# ---------- 1. 默认用户 ----------
author, created = User.objects.get_or_create(
    username='review_author',
    defaults={'email': 'review@example.com'}
)
if created:
    author.set_password('123456')
    author.save()
    print(f"Created default user: {author.username} (password: 123456)")

# ---------- 2. 品牌 ----------
brand_apple, _ = Brand.objects.get_or_create(
    name='Apple',
    defaults={'origin': 'USA', 'manufacturing_since': 1976}
)
brand_xiaomi, _ = Brand.objects.get_or_create(
    name='Xiaomi',
    defaults={'origin': 'China', 'manufacturing_since': 2010}
)
brand_huawei, _ = Brand.objects.get_or_create(
    name='Huawei',
    defaults={'origin': 'China', 'manufacturing_since': 1987}
)
print("Brands ready")

# ---------- 3. 手机型号 ----------
phones_data = [
    (brand_apple, 'iPhone X', '2017-11-03', 'iOS'),
    (brand_apple, 'iPhone XS', '2018-09-21', 'iOS'),
    (brand_apple, 'iPhone 11 Pro', '2019-09-20', 'iOS'),
    (brand_apple, 'iPhone 12', '2020-10-23', 'iOS'),
    (brand_apple, 'iPhone 12 Pro', '2020-10-23', 'iOS'),
    (brand_apple, 'iPhone 13 Pro', '2021-09-24', 'iOS'),
    (brand_apple, 'iPhone 14 Pro', '2022-09-16', 'iOS'),
    (brand_apple, 'iPhone 15 Pro', '2023-09-22', 'iOS'),
    (brand_apple, 'iPhone 16 Pro Max', '2024-09-20', 'iOS'),
    (brand_xiaomi, 'Mi 10 Pro', '2020-02-13', 'Android'),
    (brand_xiaomi, 'Mi 11 Pro', '2021-03-29', 'Android'),
    (brand_xiaomi, 'Xiaomi 12 Pro', '2021-12-28', 'Android'),
    (brand_xiaomi, 'Xiaomi 13 Pro', '2022-12-11', 'Android'),
    (brand_xiaomi, 'Xiaomi 14 Pro', '2023-10-26', 'Android'),
    (brand_huawei, 'P40 Pro', '2020-03-26', 'Android'),
    (brand_huawei, 'Mate 40 Pro', '2020-10-22', 'Android'),
    (brand_huawei, 'P50 Pro', '2021-07-29', 'Android'),
    (brand_huawei, 'Mate 60 Pro', '2023-08-29', 'Android'),
]

phone_models = {}
for brand, name, launch_date, platform in phones_data:
    obj, created = PhoneModel.objects.get_or_create(
        brand=brand,
        model_name=name,
        defaults={'launch_date': launch_date, 'platform': platform}
    )
    phone_models[name] = obj
    if created:
        print(f"Created phone: {brand.name} {name}")

# ---------- 4. 英文测评 ----------
reviews_data = [
    # Apple
    {
        'title': 'iPhone X Review: A True Game Changer with Face ID',
        'content': 'The iPhone X marked Apple\'s 10th anniversary with a radical redesign. The edge-to-edge Super Retina display, removal of the home button, and introduction of Face ID set a new standard. The glass back and stainless steel frame feel premium, and the dual cameras with Portrait mode are excellent. Although the notch was controversial, it enabled advanced facial recognition. The A11 Bionic chip remains snappy for everyday tasks. A true milestone in smartphone history.',
        'rating': 5,
        'phone_models': ['iPhone X'],
    },
    {
        'title': 'iPhone XS Review: Powerful but Battery Letdown',
        'content': 'The iPhone XS brings the A12 Bionic chip, which is still capable for gaming and multitasking. The OLED display is gorgeous, and the camera improvements are noticeable, especially Smart HDR. However, battery life is mediocre, and it lacks dual SIM in many regions. If you value performance and compact design, it\'s a good choice, but the battery might frustrate heavy users.',
        'rating': 4,
        'phone_models': ['iPhone XS'],
    },
    {
        'title': 'iPhone 11 Pro: The Ultimate Powerhouse with Triple Cameras',
        'content': 'The iPhone 11 Pro introduces a triple-camera system (ultra-wide, wide, telephoto) that delivers stunning photos and Night mode. The A13 Bionic chip focuses on machine learning and efficiency, giving 4 more hours of battery life than the XS. The matte glass back and stainless steel feel luxurious, and the new Midnight Green color is elegant. It\'s expensive but worth it for photography enthusiasts and power users.',
        'rating': 5,
        'phone_models': ['iPhone 11 Pro'],
    },
    {
        'title': 'iPhone 12 / 12 Pro Review: Flat Edges and 5G Arrive',
        'content': 'The iPhone 12 series brings back the flat-edged design of the iPhone 4, feels thinner and lighter. 5G support is the biggest upgrade, offering fast downloads while intelligently switching to 4G to save battery. The Ceramic Shield front cover improves drop durability by 4x. No charger or EarPods in the box is a downside, but MagSafe accessories add convenience. A solid upgrade for those on older iPhones.',
        'rating': 4,
        'phone_models': ['iPhone 12', 'iPhone 12 Pro'],
    },
    {
        'title': 'iPhone 13 Pro Review: ProMotion and Stellar Battery',
        'content': 'The iPhone 13 Pro finally introduces ProMotion with adaptive refresh rate from 10Hz to 120Hz, making scrolling incredibly smooth while preserving battery life. The A15 Bionic is overkill for most tasks. The new Sierra Blue color looks fantastic. The main drawback is that some apps aren\'t fully optimized for high refresh rates, and the PWM dimming may bother sensitive users. Still, it\'s one of the best iPhones ever.',
        'rating': 5,
        'phone_models': ['iPhone 13 Pro'],
    },
    {
        'title': 'iPhone 14 Pro Review: Dynamic Island – A Clever Gimmick',
        'content': 'The Dynamic Island transforms the pill-shaped cutout into an interactive hub for alerts, live activities, and music controls. It\'s a smart software solution to a hardware limitation. The 48MP main camera enables ProRAW shots with incredible detail. Always-on display is finally here. However, the Dynamic Island still cuts into video content, and third-party app support is limited. A creative but imperfect innovation.',
        'rating': 4,
        'phone_models': ['iPhone 14 Pro'],
    },
    {
        'title': 'iPhone 15 Pro Review: Titanium, USB-C, and A17 Pro',
        'content': 'The iPhone 15 Pro is a major leap with aerospace-grade titanium, making it noticeably lighter. The A17 Pro chip delivers console-level gaming with hardware ray tracing. USB-C finally replaces Lightning, supporting USB 3 speeds for fast file transfers. The camera system includes a 48MP main sensor and 3x telephoto. It\'s a true "Pro" device, though the price is steep.',
        'rating': 5,
        'phone_models': ['iPhone 15 Pro'],
    },
    {
        'title': 'iPhone 16 Pro Max Review: Bigger Screen, Better Battery',
        'content': 'The iPhone 16 Pro Max features a 6.9-inch display with ultra-thin bezels, offering an immersive viewing experience. The new Camera Control button lets you adjust zoom and exposure like a DSLR. The ultra-wide camera is upgraded to 48MP, and the A18 Pro chip is blazing fast. Battery life is class-leading. If you want the biggest iPhone and longest battery, this is it.',
        'rating': 5,
        'phone_models': ['iPhone 16 Pro Max'],
    },
    # Xiaomi
    {
        'title': 'Xiaomi Mi 10 Pro Review: A True Flagship Killer?',
        'content': 'The Mi 10 Pro packs a Snapdragon 865, 90Hz AMOLED display, and a 108MP main camera. The 50W wired and 30W wireless charging are impressive. Stereo speakers sound great. It\'s a well-rounded device with no major weakness, though MIUI can be heavy. Excellent value for the specs.',
        'rating': 4,
        'phone_models': ['Mi 10 Pro'],
    },
    {
        'title': 'Xiaomi Mi 11 Pro Review: King of Displays',
        'content': 'The Mi 11 Pro features a 2K 120Hz E4 AMOLED panel, rated A+ by DisplayMate. The Snapdragon 888 is powerful but runs hot. IP68 water resistance is a first for Xiaomi. The GN2 sensor captures amazing low-light photos. If you can tolerate some heat, it\'s a flagship beast.',
        'rating': 4,
        'phone_models': ['Mi 11 Pro'],
    },
    {
        'title': 'Xiaomi 12 Pro Review: Triple 50MP Cameras',
        'content': 'The Xiaomi 12 Pro targets the iPhone with a Snapdragon 8 Gen 1, a 2K LTPO 2.0 display (1-120Hz), and three 50MP cameras covering wide, ultra-wide, and portrait. Night mode is fast and impressive. The design is more refined. A strong all-rounder, though the chip still heats up under load.',
        'rating': 5,
        'phone_models': ['Xiaomi 12 Pro'],
    },
    {
        'title': 'Xiaomi 13 Pro Review: 1-Inch Sensor and Leica Magic',
        'content': 'The Xiaomi 13 Pro is a photography dream. It packs a 1-inch Sony IMX989 sensor with Leica tuning, producing stunning colors and natural bokeh. All three 50MP lenses are Leica-certified. The ceramic back feels premium, and the Snapdragon 8 Gen 2 runs cool. One of the best camera phones of its generation.',
        'rating': 5,
        'phone_models': ['Xiaomi 13 Pro'],
    },
    {
        'title': 'Xiaomi 14 Pro Titanium Review: Premium Materials, Great Cameras',
        'content': 'The Xiaomi 14 Pro Titanium edition uses a titanium frame for a unique, fingerprint-resistant finish. The Leica triple 50MP cameras with Light Fusion 900 sensor deliver excellent dynamic range. The 6.73-inch quad-curved screen combines curve aesthetics with flat-screen usability. A refined flagship for those who want something different.',
        'rating': 5,
        'phone_models': ['Xiaomi 14 Pro'],
    },
    # Huawei
    {
        'title': 'Huawei P40 Pro Review: DxOMark Champion',
        'content': 'The P40 Pro topped DxOMark with its Leica quad-camera system: 50MP RYYB main, 40MP ultra-wide, 5x periscope telephoto, and ToF. Zoom and night shots are unbeatable. The 90Hz quad-curve display looks stunning. However, no Google services is a dealbreaker for many. For photography lovers willing to sideload apps, it\'s amazing.',
        'rating': 5,
        'phone_models': ['P40 Pro'],
    },
    {
        'title': 'Huawei Mate 40 Pro Review: The Last Kirin Legend',
        'content': 'The Mate 40 Pro features the Kirin 9000, a 5nm chip that still performs well today. The 88° curved screen and dual speakers make gaming immersive. The camera system is top-tier. It\'s a legendary device as the last Huawei phone with Kirin and Google services (via workarounds). A collector\'s item.',
        'rating': 5,
        'phone_models': ['Mate 40 Pro'],
    },
    {
        'title': 'Huawei P50 Pro Review: Computational Photography Master',
        'content': 'Despite sanctions, the P50 Pro impresses with computational optics and XD Fusion Pro. The 64MP periscope zoom delivers crisp shots. Colors are accurate and dynamic range is excellent. No 5G and no Google services, but HarmonyOS is smooth. A testament to Huawei\'s engineering.',
        'rating': 4,
        'phone_models': ['P50 Pro'],
    },
    {
        'title': 'Huawei Mate 60 Pro Review: Kirin 5G Returns',
        'content': 'The Mate 60 Pro marks the return of Kirin chips and 5G. The Kirin 9000s is surprisingly capable, and the phone supports satellite calling. The design is rugged with second-gen Kunlun glass. It\'s not about raw specs but about resilience. A symbolic and functional flagship.',
        'rating': 5,
        'phone_models': ['Mate 60 Pro'],
    },
]

# ---------- 5. 导入测评 ----------
for rev_data in reviews_data:
    title = rev_data['title']
    content = rev_data['content']
    rating = rev_data['rating']
    model_names = rev_data['phone_models']

    # 获取关联的手机型号对象列表
    related_models = [phone_models[name] for name in model_names if name in phone_models]

    if not related_models:
        print(f"Warning: No phone models found for {title}, skipping.")
        continue

    # 创建或获取测评（避免重复）
    review, created = Review.objects.get_or_create(
        title=title,
        defaults={
            'author': author,
            'content': content,
            'rating': rating,
        }
    )
    if created:
        # 设置多对多关系
        review.phone_models.set(related_models)
        review.save()
        print(f"Added review: {title}")
    else:
        print(f"Review already exists: {title}")

print("\n✅ All reviews imported successfully!")