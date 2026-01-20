{
    "name": "Immobilier",
    "version": "1.0",
    "depends": ["base"],
    "author": "Francois Laurent",
    "summary": "Gestion de biens immobiliers",
    'description': """
        Module permettant de gérer un parc immobilier
    """,
    "category": "Real Estate",
    "data": [
        "security/ir.model.access.csv",
        "views/bien_view.xml",
    ],
    "installable": True,
    "application": True,
}