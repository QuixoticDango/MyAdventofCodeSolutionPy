

# class Cookie():
#     properties = ['cap', 'dur', 'fla', 'tex', 'cal']
#     def __init__(self, *ingredients):
#         self.ingredients = ingredients
#         self.score = 0
    
#     def getScore(self):
#         for ingredient in self.ingredients:
#             for property in self.properties:
#                 if property != 'cal':
#                     self.score += ingredient.getProp(property) * ingredient.getProp()
#         return self.score

#     def getProp(self, string = 'tea'):
#         property = 0
#         for ingredient in self.ingredients:
#             property += ingredient.getProp(string)

# class Ingredient():
#     def __init__(self, cap, dur, fla, tex, cal, tea = 1):
#         self.capacity = cap
#         self.durability = dur
#         self.flavor = fla
#         self.texture = tex
#         self.calories = cal
#         self.teaspoons = tea
    
#     def addTeaspoon(self, num):
#         self.teaspoons += num
    
#     def getProp(self, string='tea'):
#         if string == 'cap':
#             return self.capacity
#         if string == 'dur':
#             return self.durability
#         if string == 'fla':
#             return self.flavor
#         if string == 'tex':
#             return self.texture
#         if string == 'cal':
#             return self.calories
#         if string == 'tea':
#             return self.teaspoons

# frosting = Ingredient       (4,-2,0,0,5)
# candy = Ingredient          (0,5,-1,0,8)
# butterscotch = Ingredient   (-1,0,5,0,6)
# sugar = Ingredient          (0,0,-2,2,1)

# frosting.addTeaspoon(3)
# cookie = Cookie(frosting)
# print(cookie.getScore())
# import sys

score = max(((4*a - c) * (-2*a + 5*b) * (-b + 5*c - 2*d) * (2*d)) 
            for a in range(100)
            for b in range(100)
            for c in range(100)
            for d in range(100)
            if 4*a - c >= 0 and (-2*a + 5*b) >= 0 \
                and (-b + 5*c - 2*d) >= 0 and 2*d >= 0 and a+b+c+d == 100 and 5*a+8*b+6*c+d == 500)
print(score)