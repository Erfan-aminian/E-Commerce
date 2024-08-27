

CART_SESsION_ID = 'cart'
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESsION_ID)
        if not cart:
            cart = self.session[CART_SESsION_ID] = {}
        self.cart =cart

    def add(self,product,quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}
        self.cart[product_id][quantity] += quantity
        self.save()

    def save(self):
        self.session.modified = True


