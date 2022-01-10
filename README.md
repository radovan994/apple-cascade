# apple-cascade
Haar cascade cassifier for apple detection

Apple cascade classifier trained using Cascade trainer GUI from https://amin-ahmadi.com/cascade-trainer-gui/

Download 10 apple images from Bing using crawler. Augmented using the augmentation script to create 1000 positive samples. 
 
Negatives are from https://www.kaggle.com/muhammadkhalid/negative-images. Only a representative portion is in p and n folders.

Use the resizing script to adjust the size of positives and negatives.

Follow the instructions on Cascade trainer website to train the cascade.

Use the resulting cascade as an argurment along with the image for obj_det.py script which detects an apple and makes a rectangle around it.
The result is the result.jpg

![alt text](https://github.com/https://github.com/radovan994/apple-cascade/blob/master/result.jpg?raw=true)
