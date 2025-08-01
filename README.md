# Text complexity and sentiment analysis with python
## Complexity analysis and score
#### Using the SpaCy libray, with models for english (en_core_web_lg), spanish (es_core_news_lg) and german (de_core_news_lg) language, the results show: 
#### - Average sentence lenght
#### - Average word lenght
#### - POS label variety
#### - Sintactic dependencies variety
#### - Number of entities used
#### Depending on these scores, using Pandas and NumPy libraries and a specific formula, the complexity score is determined

## Emotion analysis and dominance
#### using transformers.pipeline with the j-hartmann/emotion-english-distilroberta-base model, a translated text (translated with deep-translator) is analysed considering the multilabel list with a 0 to 1 scale for the following emotions: sadness, joy, anger, fear, disgust, surprise or neutral. 
#### The score is converted to a percentage and compared in order to find dominance
## Tone analysis
#### To find the tone difference (analytic vs emotional), both TextBlob and transformers libraries were used. TextBlob gives subjectivty level, combined with the main emotion, given by transformers, the result is a tone analysis with the analytic and emotional percentage.
## Sentiment analysis
#### Using the transformers.pipeline("sentiment-analysis") and translated with deep-translator, the text content can be labeled as NEU (neutral), POS (positive) or NEG (negavie) with a percentage for each.

