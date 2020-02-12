from generator import Generator
import pandas as pd

gen = Generator(num_of_records=50)
ints = gen.generate_integer(start_at=0, end_at=1000)
seqs = gen.generate_sequence(start_at=12, step=4)
strings = gen.generate_string(length=12)
chars = gen.generate_char()
floats = gen.generate_float(start_at=0.0, end_at=1234567890.12345)
dts = gen.generate_timestamp(start_at="1981-10-21T12:12:55UTC", end_at="2019-12-12T23:59:59UTC")
bools = gen.generate_boolean()
df = pd.DataFrame({'ints': ints, 'seqs': seqs, 'strs': strings, 'chrs': chars, 'flts': floats, 'dts': dts, 'bls': bools})

print(df)
