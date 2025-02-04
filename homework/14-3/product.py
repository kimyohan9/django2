# class Product:
#     def __init__(self,cart):
#         self.cart = cart
       
#     def add_item(self,name,price):
#         item = {"name": name, "price":price}
#         self.cart.append(item)
#         print(f"상품 '{name}'이(가) 추가되었습니다.")
    
#     def add_item(self,name,price):
#         for item in self.cart:
#             if item["name"] == name:
#                 self.cart.remover(item)
#                 print(f"상품 '{name}'이(가) 제거 되었습니다")
#                 return
#         print(f"상품'{name}'을(를) 찾을 수 없습니다.")

#     def totla_price(self):
#         total = sum(item["price"] for item in self.cart)
#         return total
    
#     def show_cart(self):
#         if self.cart:
#             print("현재 쇼핑카트에 담긴 상품들:")
#             for item in self.cart:
#                 print(f"{item['name']} - {item['price']}원")
#         else:
#             print("쇼핑카트가 비어 있습니다.")

class shooppingcart:
    def __init__(self):
        self.cart = []

    def add_item(self,name,price):
        self.cart.append({"이름": name, "가격": price})
        print(f"✅ {name}(￦{price})원이 장바구니에 추가되었습니다.")

    def remove_item(self,name):
        for item in self.cart:
            if item["이름"] == name:
                self.cart.remove(item)
                print(f"❌ {name}이 장바구니에서 삭제되었습니다")
                return
        print(f"⚠️ {name}은(는) 장바구니에 없습니다.")

    def calculate_total(self):
        total = sum(item["가격"] for item in self.cart)
        return total
    
    def show_cart(self):
        if not self.cart:
            print("🛒 장바구니가 비어 있습니다.")
        else:
            print("\n🛍️ 현재 장바구니:")
            for item in self.cart:
                print(f"-{item['이름']}: ￦{item['가격']}")
            print(f"💰 총 금액: ￦{self.calculate_total()}\n")

cart = shooppingcart()
cart.add_item("참치", 5000)
cart.show_cart()





# class ShoppingCart:
#     def __init__(self):
#         """장바구니를 초기화 (빈 리스트)"""
#         self.cart = []

#     def add_item(self, name, price):
#         """상품 추가 (이름과 가격을 가진 딕셔너리로 저장)"""
#         self.cart.append({"이름": name, "가격": price})
#         print(f"✅ {name} (₩{price})이(가) 장바구니에 추가되었습니다.")

#     def remove_item(self, name):
#         """상품 제거 (이름 기준)"""
#         for item in self.cart:
#             if item["이름"] == name:
#                 self.cart.remove(item)
#                 print(f"❌ {name}이(가) 장바구니에서 제거되었습니다.")
#                 return
#         print(f"⚠️ {name}은(는) 장바구니에 없습니다.")

#     def calculate_total(self):
#         """총 금액 계산"""
#         total = sum(item["가격"] for item in self.cart)
#         return total

#     def show_cart(self):
#         """현재 장바구니에 담긴 상품 목록 출력"""
#         if not self.cart:
#             print("🛒 장바구니가 비어 있습니다.")
#         else:
#             print("\n🛍️ 현재 장바구니 목록:")
#             for item in self.cart:
#                 print(f"- {item['이름']}: ₩{item['가격']}")
#             print(f"💰 총 금액: ₩{self.calculate_total()}\n")