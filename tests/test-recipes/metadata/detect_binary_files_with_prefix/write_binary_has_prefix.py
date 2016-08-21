import os

prefix = os.environ['PREFIX']
fn = '%s/binary-has-prefix' % prefix

if not os.path.isdir(prefix):
    os.makedirs(prefix)

with open(fn, 'wb') as f:
    f.write(prefix.encode('utf-8') + b'\x00')
