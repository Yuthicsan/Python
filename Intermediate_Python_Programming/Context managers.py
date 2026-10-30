# Context managers


with open('notes.txt', 'w') as f:
    f.write('some todo...')


f = open('notes.txt', 'w')
try:
    f.write('some todo...')
finally:
    f.close()



#context manager as a class


class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename
        
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit')
            
with ManagedFile('notes.txt') as f:
    print('doing stuff...')
    f.write('some todo...')




#context manager as a generator


from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()
        
with open_managed_file('notes.txt') as f:
    f.write('some todo...')