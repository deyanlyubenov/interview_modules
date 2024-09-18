{
    'name': 'Contact Validation',
    'version': '16.0.0.0',
    'depends': ['base', 'account', 'sale', 'purchase'],
    'category': 'Customizations',
    'author': 'Deyan Lyubenov',
    'summary': 'Add validation process for contacts',
    'data': [
        'security/contact_validation_security.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'post_init_hook': 'post_init_hook',
}
