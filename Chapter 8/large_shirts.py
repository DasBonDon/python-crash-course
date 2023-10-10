# 8-4 Large Shirts
def make_shirt(size = 'large', text = 'i love python'):
    text = (
        f'The size of this t-shirt is {size} ' 
        f'and it has the text "{text.title()}" on it.'
    )
    print(text)

make_shirt()
make_shirt(size = 'medium')
make_shirt(size = 'extra large', text = 'i love ice cream')