import face_recognition

gigante_image = face_recognition.load_image_file("gigante.jpeg")
gigante_image_encoding = face_recognition.face_encodings(gigante_image)
print(gigante_image_encoding)