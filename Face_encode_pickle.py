# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:42:38 2019

@author: swathi
"""


import face_recognition
import os 
import pickle

all_face_encodings = {}

folder = 'face_images'
for filename in os.listdir(folder):
    image_name = face_recognition.load_image_file(filename)
    image_encoding = face_recognition.face_encodings(image_name)[0]
    name = filename[:-4]
    all_face_encodings.update({name:image_encoding})    
    
    
with open('faces_encode_pk.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)