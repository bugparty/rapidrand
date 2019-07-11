import rapidrand

assert rapidrand.__version__ == '0.0.1'

assert len(rapidrand.genstr(12345)) == 12345
assert len(rapidrand.entropy(12345)) == 12345
assert len(rapidrand.entropy2(12345)) == 12345