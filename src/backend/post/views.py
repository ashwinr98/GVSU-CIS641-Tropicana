from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import requests
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
# Create your views here.

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Predict(APIView):
    def get(self,request, *args, **kwargs):
        # a=request.query_params
        # print(a['q'])
        base_dir='D:/Coding/react/img_upl/react-form-data/backend'
        r = requests.get('http://127.0.0.1:8000/api/posts')
        req_json = r.json()
        imgurl = req_json[-1]['image']
        print(base_dir+imgurl)
        ins_model = tf.keras.models.load_model('D:/Coding/react/img_upl/react-form-data/backend/post/saved_model/insect_model1')
        batch_size = 32
        img_height = 180
        img_width = 180
        class_names=['Amara_anthobia', 'Bembidion_lampros', 'Bembidion_tetracolum', 'Carabus_problematicus', 'Loricera_pilicornis']
        #insect_path = "D:/Coding/opencv/insec_test/Carabus_problematicus.jpg"
        insect_path = base_dir+imgurl
        img = tf.keras.utils.load_img(
            
            insect_path, target_size=(img_height, img_width)
        )
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) # Create a batch
        predictions = ins_model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        pred_str=(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
        )
        return Response(pred_str)