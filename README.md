# WhatIs package

Gives a concise summary of any object's structure and avoids accidentally printing a huge object to stdout.

Works with various libraries (NumPy, PyTorch etc.) via duck typing.

## Examples
`whatis` is useful for inspecting large objects quickly:
```python
>> x = list(enumerate(range(7,4129,3)))
>> x
# ... (veeery large output) ...
>> whatis(x)
list len=1374
  ├ tuple len=2
  │  ├ 0: int
  │  └ 7: int
  │
  ├ tuple len=2
  │  ├ 1: int
  │  └ 10: int
  │
  ├ tuple len=2
  │  ├ 2: int
  │  └ 13: int
  │
  ├ tuple len=2
  │  ├ 3: int
  │  └ 16: int
  │
  └ ...
>>
```
And makes it easy to view the format of objects like this
```python
>>> x = np.ones((5, 5))
>>> out = np.linalg.eig(x)
>>> out
# A lot of information...
(array([5.00000000e+00, 5.65333918e-49, 0.00000000e+00, 0.00000000e+00,
       1.73014109e-64]), array([[-4.47213595e-01,  1.13586253e-16,  1.13586253e-16,
         1.38161505e-31, -1.11062157e-16],
       [-4.47213595e-01,  8.66025404e-01,  8.66025404e-01,
         1.05339661e-15, -8.46780726e-01],
       [-4.47213595e-01, -2.88675135e-01, -2.88675135e-01,
        -2.39769783e-16,  1.11088069e-01],
       [-4.47213595e-01, -2.88675135e-01, -2.88675135e-01,
        -7.07106781e-01,  3.67846328e-01],
       [-4.47213595e-01, -2.88675135e-01, -2.88675135e-01,
         7.07106781e-01,  3.67846328e-01]]))

>> whatis(out)
tuple len=2
  ├ ndarray shape=(5,) dtype=float64
  └ ndarray shape=(5, 5) dtype=float64
>>
```
or this
```python
>> x = torch.randn((103, 75))
>> out = torch.topk(x, 5)
# what's the format of the output again..?
>> out
# ... (very large output) ...
>> whatis(out)
topk len=2
  ├ Tensor shape=torch.Size([103, 5]) dtype=torch.float32 device=cpu
  └ Tensor shape=torch.Size([103, 5]) dtype=torch.int64 device=cpu
>>
```

## Usage
```python
from whatis import whatis
```

## Setup
```pip install whatis```