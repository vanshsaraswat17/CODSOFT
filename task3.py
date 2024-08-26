
import cv2
import face_recognition

print('''
      

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
''')

# Load known face
known_image = face_recognition.load_image_file("known_person.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

def detect_and_recognize(image_path):
    # Load and process the image
    img = cv2.imread(image_path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Detect faces
    face_locations = face_recognition.face_locations(rgb_img)
    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Recognize faces
        matches = face_recognition.compare_faces([known_encoding], face_encoding)
        label = "Match" if matches[0] else "Unknown"
        
        # Draw rectangle and label
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(img, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow('Face Recognition', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
detect_and_recognize('unknown_person.jpg')
