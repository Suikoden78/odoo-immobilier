{
    'name': 'Immobilier',
    'version': '1.0',
    'summary': 'Gestion de biens immobiliers',
    'description': 'Module permettant de gérer les annonces de biens immobiliers.',
    'author': 'Francois Laurent',
    'category': 'Real Estate',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/bien_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}