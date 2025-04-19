# prefect match
from nltk.translate.bleu_score import sentence_bleu
reference = [['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']]
candidate = ['the','the', 'the', 'the', 'the', 'over', 'the', 'lazy', 'dog']
score = sentence_bleu(reference, candidate)
print(score)
print(4/9)