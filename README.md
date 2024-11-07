***GAN  Generative Adversial Network*** :

 its a type of neural network that used in machine learning to generate new data that looks similar to a given data.
 
 it consists of two main components:
 
***Generator***: its a neural network takes random noise(vector of random numbers) as input and tries to generate data that looks realistic enough.

**Discriminator**: its also a neural network , it takes both real data from the dataset and fake data from the generator as input and tries to do a binary classification, if it as real or fake.

These two networks are compeeting to win if we could say, at some point, the generator gets so good at creating realistic data that the discriminator wont descriminate .

applications of GAN :
       
                      -Image to Image translation

                      -Image to Text / Text to Image translation
                      
                      -Deep Fake


***GANs Don’t Work Well for Text ?***

GANs perform well with continuous data, like images, because the generator can create smooth, flowing values ( for example : pixel intensities), but when it comes to text and words; it cant perform good results beacus the input is **discrete valuse**
so thats why reasearchers suggest some solutions

