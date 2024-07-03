def area(h,b):
    area=0.5*h*b
    return area


height=int(input("Enter the height of triangle: "))
base=int(input("Enter the base of triangle: "))

result=area(height,base)
print("Area of Triangle is ",result)