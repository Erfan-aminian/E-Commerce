

CART_SESsION_ID = 'cart'
class cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESsION_ID)
        if not cart:
            cart = self.session[CART_SESsION_ID] = {}
        self.cart =cart

