# Simple Audio Recognition 

Created a simple audio recognition to convert speech to text 
utilizing the ```SpeechRecognition``` python library and the 
```PyAudio``` library.  

```Speech_recognition.py``` allows you to either of these: 
1. convert real time input audio into text 
1. convert real time input audio into a *.wav* file to later 
utilize in ```speech_recognition_1.py```
   
```deep_search.py``` is a portion of a class created by tensorflow
for deep search when working with strings.  These functions tokenize the string
and calculate the difference either of a sentence or words.
1. ```wer(decode, target)``` computes the Word Error Rate (WER) between two provided
sentences after tokenizing to words.
1. ```cer(decode, target)``` computes the Character Error Rate (CER) between
two given strings. 