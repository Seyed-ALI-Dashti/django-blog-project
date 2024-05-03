from datetime import date

from django.shortcuts import render

# Create your views here.


all_posts = [
    {
        'post_slug': 'django-blog',
        'title': 'Django Blog',
        'author': '<NAME>',
        'image': 'django.jpg',
        'date': date(2024, 5, 3),
        'short_description': 'this is django blog',
        'body': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aperiam autem eius eveniet magnam odio vero. Aliquid, aperiam dolor eligendi facere fugit ipsam laudantium libero magnam officiis porro quaerat quidem quo quod quos recusandae reprehenderit saepe, soluta vel velit, voluptate.
        """,
    },
    {
        'post_slug': 'python-blog',
        'title': 'Python Blog',
        'author': '<NAME>',
        'image': 'python.jpg',
        'date': date(2024, 4, 10),
        'short_description': 'this is python blog',
        'body': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aperiam autem eius eveniet magnam odio vero. Aliquid, aperiam dolor eligendi facere fugit ipsam laudantium libero magnam officiis porro quaerat quidem quo quod quos recusandae reprehenderit saepe, soluta vel velit, voluptate.
        """,
    },
    {
        'post_slug': 'machin-learning-blog',
        'title': 'Machin Learning Blog',
        'author': '<NAME>',
        'image': 'ml1.jpg',
        'date': date(2024, 4, 12),
        'short_description': 'this is Machin Learning blog',
        'body': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aperiam autem eius eveniet magnam odio vero. Aliquid, aperiam dolor eligendi facere fugit ipsam laudantium libero magnam officiis porro quaerat quidem quo quod quos recusandae reprehenderit saepe, soluta vel velit, voluptate.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aperiam autem eius eveniet magnam odio vero. Aliquid, aperiam dolor eligendi facere fugit ipsam laudantium libero magnam officiis porro quaerat quidem quo quod quos recusandae reprehenderit saepe, soluta vel velit, voluptate.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aperiam autem eius eveniet magnam odio vero. Aliquid, aperiam dolor eligendi facere fugit ipsam laudantium libero magnam officiis porro quaerat quidem quo quod quos recusandae reprehenderit saepe, soluta vel velit, voluptate.
            
            Lorem ipsum dmagnam odio vero. Aliquid, aperiam dolor eligendi facere fugit ipsam laudantium libero magnam officiis porro quaerat quidem quo quod quos recusandae reprehenderit saepe, soluta vel velit, voluptate.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aperiam autem eius eveniet magnam odio vero. Aliquid, aperiam dolor eligendi facere fugit ipsam laudantium libero magnam officiis porro quaerat quidem quo quod quos recusandae reprehenderit saepe, soluta vel velit, voluptate.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aperiam autem eius eveniet magnam odio vero. Aliquid, aperiam dolor eligendi facere fugit ipsam laudantium libero magnam officiis porro quaerat quidem quo quod quos recusandae reprehenderit saepe, soluta vel velit, voluptate.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aperiam autem eius eveniet magnam odio vero. Aliquid, aperiam dolor eligendi facere fugit ipsam laudantium libero magnam officiis porro quaerat quidem quo quod quos recusandae reprehenderit saepe, soluta vel velit, voluptate.
        """,
    },
]


def get_date(post):
    return post['date']


def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', {
        'latest_post': latest_posts
    })


def posts(request):
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog/all-posts.html', context)


def single_post(request, slug):
    post = next(post for post in all_posts if post['post_slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': post
    })
