# WhatIs package

Gives a summary of any object, avoiding the risk of printing huge amounts to stdout.

Works with various libraries (NumPy, PyTorch etc.) via duck typing.

## Examples
```python
```

```python
>> x = torch.randn((103, 75))
>> out = torch.topk(x, 5)
>> out
... (very large output) ...
>> whatis(out)

topk len=2
  ├ Tensor shape=torch.Size([103, 5]) dtype=torch.float32 device=cpu
  └ Tensor shape=torch.Size([103, 5]) dtype=torch.int64 device=cpu
```

```python
>> x = np.ones((8, 8))
>> out = np.linalg.eig(x)
>> whatis(out)

tuple len=2
  ├ ndarray shape=(8,) dtype=float64
  └ ndarray shape=(8, 8) dtype=float64
```