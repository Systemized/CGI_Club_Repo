from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    # COMMETTED OUT BECAUSE LEAVING WILL CAUSE "NotImplementedError; This backend doesn't support absolute paths."
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    

# POSSIBLE REPLACEMENT FOR THE PROFILE CLASS TO SAVE RESIZED IMAGES INTO 
# AZURE BLOB STORAGE, BUT NOT TRUSTWORTHY BECAUSE WAS GENERATED WITH SOME AI
# 
# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image
# from io import BytesIO
# from django.core.files.storage import default_storage

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self, *args, **kwargs):
#         # Open the image from Azure Storage
#         image_file = default_storage.open(self.image.name, 'rb')
#         img = Image.open(image_file)

#         # Resize image if it exceeds 300px in width or height
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
            
#             # Save the resized image back to Azure Storage
#             img_io = BytesIO()
#             img.save(img_io, img.format)
#             img_io.seek(0)

#             # Save the resized image to the image field
#             self.image.save(self.image.name, img_io, save=False)

#         # Call the superclass save method to save the object
#         super().save(*args, **kwargs)