text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'
text = list(filter(lambda el: 'абв' not in el.lower() , text.split()))
print(' '.join(text))
