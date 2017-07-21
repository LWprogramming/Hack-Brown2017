# Sarcasm detector

![I hope this quacks you up...](http://i0.wp.com/www.fowllanguagecomics.com/wp-content/uploads/2015/11/so-sarcastic.jpg?w=300)

<sub>[source](http://www.fowllanguagecomics.com/comic/so-sarcastic/)</sub>

Does *exactly* what its name describes.

## Details

Uses machine learning and the Text Analytics API from Microsoft's Cognitive Services (aka Project Oxford) to determine whether an input statement is sarcastic in nature.

## Usage instructions

~~~~ python3 model.py ~~~~

## Pipeline

Clean data -> Send text to Microsoft Cognitive Services -> use sentiment to evaluate sarcasm