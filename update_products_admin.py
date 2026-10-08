with open('create_admin_pages.py', 'r') as f:
    c = f.read()

# Replace products fields to include price
old_prod = """    'products': {
        'title': 'Məhsullar',
        'table': 'products',
        'fields': [
            {'name': 'title', 'label': 'Başlıq', 'type': 'text'},
            {'name': 'description', 'label': 'Məzmun / Açıqlama', 'type': 'textarea'},
            {'name': 'image_url', 'label': 'Şəkil', 'type': 'image'}
        ]
    },"""

new_prod = """    'products': {
        'title': 'Məhsullar',
        'table': 'products',
        'fields': [
            {'name': 'title', 'label': 'Başlıq', 'type': 'text'},
            {'name': 'price', 'label': 'Qiymət (məs: 120 ₼)', 'type': 'text'},
            {'name': 'description', 'label': 'Məzmun / Açıqlama', 'type': 'textarea'},
            {'name': 'image_url', 'label': 'Şəkil', 'type': 'image'}
        ]
    },"""

c = c.replace(old_prod, new_prod)
with open('create_admin_pages.py', 'w') as f:
    f.write(c)
