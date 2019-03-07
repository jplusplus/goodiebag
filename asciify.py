"""
 ASCII är den teckenuppsättning som användes i datorernas barndom,
 och som fortfarande är en vanlig begränsning i e-postadresser
 och webbadresser
 https://en.wikipedia.org/wiki/ASCII

 För en utförligare lista över latinska tecken, se
 https://en.wikipedia.org/wiki/List_of_Latin-script_letters
"""
import unicodedata


def asciify(string):
    """
     Ersätt vanliga latiska tecken med visuellt liknande ascii-
     tecken, som ofta används som ersättare i e-postadresser
     och liknande.
    """
    # Some additional replacements, not handled by Unicode normalization
    replacements = [
        ("ʻ", "'"),  # Polynesian/Hawaiian okina
        ("ł", "l"), ("Ł", "L"),
    ]
    for replacement in replacements:
        string = string.replace(replacement[0], replacement[1])
    # Use Unicode normalization for the rest
    string = unicodedata.normalize('NFD', string).encode('ascii', 'ignore')
    # Return ASCII string, crash on invalid input
    return string.decode("ascii")


def emailify(string):
    """
     Ersätt latinska tecken med de motsvarigheter som ofta
     används i e-postadresser
    """
    string = string.lower().replace(" ", ".")
    string = asciify(string)
    return string


print(asciify("Erdoğan på besök i Łódź"))
print(emailify("Örjan de-Vriis"))
