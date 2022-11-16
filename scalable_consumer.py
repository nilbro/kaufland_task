from simple_consumer import Consumer

if __name__ == "__main__":
    c0 = Consumer('my-group')
    c1 = Consumer('my-group')
    c2 = Consumer('my-group')
    c3 = Consumer('my-group')
    c4 = Consumer('my-group')
    c5 = Consumer('my-group')
    c6 = Consumer('my-group')
    c7 = Consumer('my-group')
    c8 = Consumer('my-group')
    c9 = Consumer('my-group')
    
    for c in [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]:
        c.consume_message()
