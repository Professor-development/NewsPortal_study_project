from django import template

register = template.Library()

CENSOR_WORDS = {'хребет', 'дроны', 'массы', 'тибет'}


@register.filter()
def censor(value):
    final_text = ""
    value = str(value)
    if isinstance(value, str):
        counter = 0
        while counter < len(value):
            i = counter
            temp_word = ''
            if value[i] != ' ':
                while i < len(value) and value[i] != ' ':
                    temp_word += value[i]
                    i += 1
                if temp_word.lower() in CENSOR_WORDS:
                    temp_word = temp_word[0] + ('*' * (len(temp_word)-1))
                final_text += temp_word + " "
            counter = i + 1
        return final_text
    else:
        raise ValueError("Невозможно применить фильтр к не строковому типу данных")


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()