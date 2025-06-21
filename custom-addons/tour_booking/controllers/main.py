from odoo import http
from odoo.http import request

class WebsiteSaleTour(http.Controller):
    """Controladores para manejar la reserva de tours."""

    @http.route(['/shop/product/<model("product.template"):product>'], type='http', auth='public', website=True)
    def product(self, product, **kwargs):
        """Muestra la ficha de producto en el sitio web."""
        return request.render('website_sale.product', {'product': product})

    @http.route(['/shop/cart/update'], type='http', auth='public', website=True, methods=['POST'])
    def cart_update(self, product_id, fecha_reserva=None, cantidad_personas=1, **kw):
        """Agrega tours al carrito validando fecha y personas."""
        product = request.env['product.product'].browse(int(product_id))
        if product.product_tmpl_id.es_tour:
            if not fecha_reserva or int(cantidad_personas) < 1:
                return request.redirect("/shop/cart?error=invalid_input")
            sale_order = request.website.sale_get_order(force=True)
            sale_order._cart_update(
                product_id=int(product_id),
                add_qty=int(cantidad_personas),
                set_qty=0,
                product_custom_attributes={
                    'fecha_reserva': fecha_reserva,
                    'cantidad_personas': int(cantidad_personas),
                }
            )
        else:
            sale_order = request.website.sale_get_order(force=True)
            sale_order._cart_update(
                product_id=int(product_id),
                add_qty=int(kw.get('add_qty', 1)),
                set_qty=0,
            )
        return request.redirect("/shop/cart")
