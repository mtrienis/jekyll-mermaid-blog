
def multipliers():
    return [lambda x : i * x for i in range(4)]

print [m(2) for m in multipliers()] # [6, 6, 6, 6]
print range(4) # [0, 1, 2, 3]
print lambda x : i * x # <function <lambda> at 0x109ad8668>
print [lambda x : i * x for i in range(4)] # [<function <lambda> at 0x109ad8668>, <function <lambda> at 0x109adcb90>, <function <lambda> at 0x109adc500>, <function <lambda> at 0x109ae6500>]
print [lambda x : i * x for i in range(4)][0] # <function <lambda> at 0x109ad8668>
print [lambda x : i * x for i in range(4)][0](2) # 6 [3x2]


def multipliers():
    for i in range(4): yield lambda x : i * x


dict = {"key":"value"}
for i in {"key":"value"}:
    print i


def dynamicArguments(*arg, **kwargs):
    print arg
    print kwargs

dynamicArguments(1, first=4, 2, second=5, 3, third=6)



(1, 2, 3)
{'second': 5, 'third': 6, 'first': 4}


