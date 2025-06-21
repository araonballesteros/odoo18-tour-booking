# tour_booking/__manifest__.py
{
    "name": "tour booking",
    "version": "1.0",
    "category": "website",
    "summary": "modulo para reservas de tours turisticos",
    "description": """
        permite la venta de tours turisticos desde el sitio web,
        con seleccion de fecha y cantidad de personas.
    """,
    "depends": ["website", "website_sale", "product", "sale_management", "payment", "account"],
    "data": [
        "views/product_template_views.xml",
        "views/sale_order_views.xml",
        "views/website_sale_templates.xml",
    ],
    "installable": True,
    "auto_install": False,
}