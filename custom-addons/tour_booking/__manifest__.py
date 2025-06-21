# tour_booking/__manifest__.py
{
    "name": "tour booking",
    "version": "1.0",
    "category": "Website",
    "summary": "Módulo para reservas de tours turísticos",
    "description": """
        Permite la venta de tours turísticos desde el sitio web,
        con selección de fecha y cantidad de personas.
    """,
    "depends": [
        "website",
        "website_sale",
        "product",
        "sale_management",
        "payment",
        "account",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_views.xml",
        "views/sale_order_views.xml",
        "views/website_sale_templates.xml",
    ],
    "installable": True,
    "auto_install": False,
}
