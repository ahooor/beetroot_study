# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):
    def decorator(func):
        def inner(name):
            str = func(name)
            for word in str.split():
                word = word.strip(" ,.?!-")
                if word in words:
                    str = str.replace(word, "*")
            print(str)
            return str
        return inner
    return decorator
        

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan("Steve")

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"