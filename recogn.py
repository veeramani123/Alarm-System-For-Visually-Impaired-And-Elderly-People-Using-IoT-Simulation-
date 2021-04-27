import face_recognition
known_image = face_recognition.load_image_file("sam.jpg")
unknown_image = face_recognition.load_image_file("sam2.jpg")

sam_encoding = face_recognition.face_encodings(known_image)[0]
sam2_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([sam_encoding], sam2_encoding)

print(results)