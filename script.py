# Follow instructions mentioned on following page:

# https://stackoverflow.com/questions/60370799/google-image-download-with-python-cannot-download-images
# https://stackoverflow.com/a/60556289/13163828


# importing google_images_download module 
from google_images_download import google_images_download  
  
# creating object 
response = google_images_download.googleimagesdownload()

search_queries = [
    'Red-collared dove', 
    'Indian Roller', 
    'Little Green Bee Eater', 
    'Blue Throat', 
    'Rosy starling', 
    'Blue Rock Pigeon', 
    'Grey Headed Canary Flycatcher', 
    'Rufous fronted prinia', 
    'Long tailed shrike juvenile', 
    'Laughing Dove', 
    'Red-wattled lapwing juvenile', 
    'Black-Rumped Flameback', 
    'Great grey shrike', 
    'Indian Grey HornBill', 
    'Eurasian Collared Dove', 
    'Yellow wattled lapwing', 
    'White cheeked bulbul', 
    'Indian Robin Female', 
    'Desert Wheatear', 
    'Common Stonechat', 
    'Cattle Egret', 
    'Zitting cisticola', 
    'Red vented bulbul', 
    'Rufous treepie', 
    'Common Babler', 
    'Rufous tailed lark', 
    'Plain prinia', 
    'Yellow footed green pigeon', 
    'Brown RockChat', 
    'Pied bushchat', 
    'Grey Frankolin', 
    'Bay Backed Shrike', 
    'Indian Bushlark', 
    'White browed wagtail', 
    'Black Eared Kite'
] 
  
def downloadimages(query): 
    # keywords is the search query 
    # format is the image file format 
    # limit is the number of images to be downloaded 
    # print urs is to print the image file url 
    # size is the image size which can 
    # be specified manually ("large, medium, icon") 
    # aspect ratio denotes the height width ratio 
    # of images to download. ("tall, square, wide, panoramic") 
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit":100} 
    response.download(arguments) 
      
  
# Driver Code 
for query in search_queries: 
    downloadimages(query)  
    print()  
