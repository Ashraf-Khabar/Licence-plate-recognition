from model import Model

img_processor = Model("data/test5.jpg")

print (f"the license plate number is: {img_processor.get_plate_number()}")

# C:\Users\pc\workspace\Licence-plate-recognition\api\model.py