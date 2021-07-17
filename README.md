# Text-Summarization-using-Audio-Input
The system is divided into two major parts, an input module for the text document to be summarized, a summarizer algorithm and the output module.
In the preprocessing stage, the unstructured text is converted into structured text. The stop words are then removed and the document is parsed to collect all the words along with their frequencies.

**PHASE 1: SPEECH TO TEXT**
1.1 Obtaining input
•	The input audio for processing is obtained by recording using the device’s microphone.
•	The audio recording and processing are done with the help of sound_recorder module. Audio is recorded by continuously appending frames of audio
•	If the speaker halts for more than 5seconds the program gets terminated automatically and text summarization function gets executed and output is displayed.
1.2	Need of partition
•	The audio file recorded needs to be converted into text. This process uses python module Speech_Recognition. This module requires a working internet connection to function as it uses Google’s web-based speech to text engine. The time duration for which the engine accepts input is a maximum of 1 minute. So, if the duration of the audio file increases beyond 1 minute then we need to divide it into chunks of smaller duration .
•	The individual files are then processed further for getting the final text output of the original audio file. This text will then be processed for getting summary.
1.3	 Getting the Test Output
•	The functionssss of generating text from the audio file recorded is aided by the python module Speech Recognition. 
•	The reason for selecting this specific module is due to its simplicity of usage and better efficiency than offline modules. The audio file or chunk of audio file is passed to an instance of the module that takes this wav file as source. The audio file is scanned and rectified for noise.
•	 The module uses Google’s engine to recognize the audio and convert it into text file. This file stores the original text of the speech and is stored for operational purposes. This file is then processed under phase two to get the extractive summary of the text recorded in this file.

**PHASE 2: TEXT SUMMARIZATION**
This phase focuses on generating a text summary as an output for the input text that is generated in phase 1. This phase mentions the major steps taken in the algorithm of summarization. It uses SpaCy which is an open-source software library for advanced Natural Language Processing, written in the programming languages Python

2.1	Tokenization of words and word frequency Generation
•	At this point, the data has to be tokenized by breaking it down into words to generate the frequency of each word occurring in the provided data. 
•	After the list of tokens is generated, iterate through the list and check if the corresponding word is not present in the stop words list and if not, increase its frequency by 1.
2.2	Sentence Tokenization
•	Now there is a need to generate scores of each sentence in the data to generate an optimal summary of the given data. For that first tokenize each sentence in the data.
2.3	Sentence Selection
•	The next stage is to extract the important key-phrases in the text by implementing a new algorithm through which extracting high frequency words. 
•	The system uses the extracted keywords to select the important sentence.
2.4	Sentence Scoring 
•	In this stage the system will generate a score for each sentence by adding the weighted frequencies of the word that occur in a particular sentence.
•	 As it is not interested in a summary, it has to score only those sentences with less than 30 words.
2.5	Output
•	Using the above listed stages the input text is being summarized and the output is display in the form of text which is  in concised form.


