# Chia-Fake-Primes
An example 1024 bit composite that is *guaranteed* to be declared prime by the primality test found in Chia. This particular example has 4 factors and took ~1min to generate.
Should we throw more core-time at the problem, we could easily produce say, an 8 factored example.

Simply a proof of concept to fool the test seen in Chia at https://github.com/Chia-Network/vdf-competition/blob/master/inkfish/primes.py#L16 motivated by Antonio Sanso.

This example is by no means unique or particularly special. The test performs fixed base Miller-Rabin on bases 3 and 5. To fool the test one simply needs a composite with both 3 and 5 as non-witnesses.

Simply run 
``` 
python Chia-Primality-Test.py
```
to see for yourself.

Full work at https://eprint.iacr.org/2018/749

# 1024 bit Example

p1 = 17316868081892944814245898804781344373625169673277941408549866301660022650691

p2 = 51950604245678834442737696414344033120875509019833824225649598904980067952071

p3 = 190485548900822392956704886852594788109876866406057355494048529318260249157591

p4 = 571456646702467178870114660557784364329630599218172066482145587954780747472771

n = p1 p2 p3 p4 = 97927636747136748257175200169244424312330490602805343672262360168392666071192663148024680581580906755437635743922113122607597192280550539814882052171802724590431103798434953953098295310858804382941936857074710329271190942925268047368591040457157204472528462550426797995477408897796121010466997522929625225321
