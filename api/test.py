from api.model import Model

img_processor = Model("data/test.png")

print (f"the license plate number is: {img_processor.get_plate_number()}")