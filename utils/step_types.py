"""Type personnalisé : accepte aussi une chaine vide entre guillemets."""
import parse
from behave import register_type

@parse.with_pattern(r'[^"]*')
def parse_text(text):
    return text

register_type(Text=parse_text)