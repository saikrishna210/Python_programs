class shopping:
    mall_name="lulu"
    def shopping_details(self,clothes,slippers,cosmetics):
        self.clothes=clothes
        self.slippers=slippers
        self.cosmetics=cosmetics
    def show_details(self):
        print(f"mall_name:{self.mall_name}")
        print(f"clothes:{self.clothes},slippers:{self.slippers},cosmetics:{self.cosmetics}")
# shopping.mall_name="lexus mall"
c1=shopping()
# shopping.mall_name="lexu mall"
c1.shopping_details("bear house","nike","perfumes")
c1.show_details()
del c1.clothes
print(c1.__dict__)