# Music-BiLSTM-GAN
Composing Melodies with Bidirectional LSTM Generative Adversarial Networks

# Results
[Listen to Generated Song 1](https://vocaroo.com/embed/lMJ34mf5Rqg) <br/>
[Listen to Generated Song 2](https://vocaroo.com/embed/gKi1mFdOTQh)

# Data Representation
There are a lot of ways to represent music data. Soundwaves, Spectograms, etc... <br/>
I am chosing to represent music data using discrete MIDI values. <br/>
![midi](https://www.noterepeat.com/images/other/other_midi_terms_explained_2.png)

# Knowledge Representation
I am using Bidirectional LSTMs for both the generator and the discriminator <br/>
![BiLSTM](https://www.i2tutorials.com/wp-content/uploads/2019/05/Deep-Dive-into-Bidirectional-LSTM-i2tutorials.jpg) <br/>
Bidirectional LSTMs analyze the input sequence both forwards and backwards <br/>

Both the generator and the discriminator are working against each other in an adversarial network. <br/>
The two networks are playing a minimax game, aiming to minimize the loss of the generator while maximizing the loss of the discriminator.



# Generator Architecture
![gen](https://raw.githubusercontent.com/vee-upatising/Music-BiLSTM-GAN/master/generator.JPG)
# Discriminator Architecture
![disc](https://raw.githubusercontent.com/vee-upatising/Music-BiLSTM-GAN/master/discriminator.JPG)
# Training
![epoch](https://raw.githubusercontent.com/vee-upatising/Music-BiLSTM-GAN/master/training.JPG)
<br/>The models were trained for 1000 epochs and achieved this loss
