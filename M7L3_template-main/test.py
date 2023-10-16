text = 'Что ты запятая делаешь точка восклицательный знак вопросительный знак'

symbols = ['точка', 'запятая', 'восклицательный знак', 'вопросительный знак']

if 'токча' in text:
    new_text = text.replace('точка', ".")
if 'запятая' in text:
    new_text = text.replace('запятая', ",")
if 'восклицательный знак' in text:
    new_text = text.replace('восклицательный знак', "!")
if 'вопросительный знак' in text:
    new_text = text.replace('вопросительный знак', ".?")


print(new_text)

