# Chia-Fake-Primes
An example 1024 bit pseudoprime to the primality test found in Chia. This particular example has 4 factors and took ~1min to generate.
Should we throw more core-time at the problem, we could easily produce say, an 8 factored example.

Simply a proof of concept to fool the test seen in Chia at https://github.com/Chia-Network/vdf-competition/blob/master/inkfish/primes.py#L16 motivated by Antonia Sanso.

This example is by no means unique or particularly special. The test performs fixed base Miller-Rabin on bases 3 and 5. To fool the test one simply needs a composite with both 3 and 5 as non-witnesses.

Full work at https://eprint.iacr.org/2018/749
