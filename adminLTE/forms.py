from django import forms
from .models import Video,camera
#DataFlair #File_Upload
class Video_Form(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
        'inputName',
        'initialTime',
        'file'
        ]


# creating a form 
class Camera_Form(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = camera 
  
        # specify fields to be used 
        fields = [ 
            "id",
            "camera_name", 
            "camera_id", 
            "direction_id1", 
            "direction_name1", 
            "direction_coordinates1", 
            "direction_id2", 
            "direction_name2", 
            "direction_coordinates2", 
            "direction_id3", 
            "direction_name3", 
            "direction_coordinates3", 
            "direction_id4", 
            "direction_name4", 
            "direction_coordinates4", 
        ] 