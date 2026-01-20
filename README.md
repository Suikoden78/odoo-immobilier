# Module Odoo – Immobilier

## Description
Module Odoo personnalisé permettant la gestion simple de biens immobiliers.

Ce module a été développé dans le cadre d’un test technique Odoo.

## Fonctionnalités
- Gestion des biens immobiliers
- Champs : nom, prix, surface, disponibilité
- Vue liste et vue formulaire
- Menu dédié "Immobilier"
- Droits d’accès configurés

## Structure du module

immobilier/
- __init__.py
- __manifest__.py
- models/
    - __init__.py
    - bien.py
- views/
    - bien_view.xml
- security/
    - ir.model.access.csv
- static
    - description
        - icon.png

## Compatibilité
- Odoo 19.0

## Auteur
Francois Laurent