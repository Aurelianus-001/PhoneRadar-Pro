import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phoneradar_pro.settings')
django.setup()

from games.models import Game

games_data = [
    {
        "name": "The Legend of Zelda: Breath of the Wild",
        "description": "Open-world action-adventure game set in Hyrule. Explore, solve puzzles, and defeat enemies.",
        "release_date": "2017-03-03",
        "rating": 10.0,
        "image_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1t0r.jpg"
    },
    {
        "name": "Super Mario Odyssey",
        "description": "3D platformer where Mario travels to different kingdoms to rescue Princess Peach from Bowser.",
        "release_date": "2017-10-27",
        "rating": 9.8,
        "image_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1x1p.jpg"
    },
    {
        "name": "Red Dead Redemption 2",
        "description": "Epic western action-adventure set in 1899, following outlaw Arthur Morgan.",
        "release_date": "2018-10-26",
        "rating": 9.7,
        "image_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1t4r.jpg"
    },
    {
        "name": "God of War (2018)",
        "description": "Action-adventure game following Kratos and his son Atreus in Norse mythology.",
        "release_date": "2018-04-20",
        "rating": 9.8,
        "image_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1t1r.jpg"
    },
    {
        "name": "Elden Ring",
        "description": "Open-world action RPG by FromSoftware, featuring challenging combat and exploration.",
        "release_date": "2022-02-25",
        "rating": 10.0,
        "image_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co4jni.jpg"
    },
    {
        "name": "Cyberpunk 2077",
        "description": "Open-world RPG set in a dystopian future, with deep character customization.",
        "release_date": "2020-12-10",
        "rating": 8.5,
        "image_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1x1k.jpg"
    },
    {
        "name": "Hollow Knight",
        "description": "Metroidvania with beautiful hand-drawn art and tight combat.",
        "release_date": "2017-02-24",
        "rating": 9.5,
        "image_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1t0o.jpg"
    },
    {
        "name": "Stardew Valley",
        "description": "Farming simulation RPG with crafting, fishing, and relationships.",
        "release_date": "2016-02-26",
        "rating": 9.2,
        "image_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1t0q.jpg"
    }
]

for data in games_data:
    obj, created = Game.objects.get_or_create(
        name=data["name"],
        defaults={
            "description": data["description"],
            "release_date": data["release_date"],
            "rating": data["rating"],
            "image_url": data["image_url"],
        }
    )
    if created:
        print(f"Added: {data['name']}")
    else:
        print(f"Already exists: {data['name']}")

print("Done!")