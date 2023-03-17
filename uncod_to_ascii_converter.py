# Function to convert unicode characters to ascii
import unicodedata
def unicode_to_ascii(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn')

""""
text = "L'Argentine se pr\u00e9pare \u00e0 vibrer. Alors que les doux souvenirs de la coupe du monde sont encore dans toutes les m\u00e9moires, le pays s'appr\u00eate \u00e0 retrouver ses h\u00e9ros. Trois mois apr\u00e8s l'incroyable victoire arrach\u00e9e face au bleu lors de la finale de la coupe du monde, les hommes de Lionel Scaloni ont en effet rendez-vous les 24 et 28 mars prochains pour deux matchs amicaux, respectivement face au Panama et \u00e0 Curacao."
print(unicode_to_ascii(text))