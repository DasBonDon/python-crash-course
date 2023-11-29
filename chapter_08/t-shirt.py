# 8-3 T-Shirt
def make_shirt(size, text):
    text = (
        f'The size of this t-shirt is {size} ' 
        f'and it has the text "{text.title()}" on it.'
    )
    print(text)

make_shirt('large', 'hello world')
make_shirt(size='small', text='i love donuts')