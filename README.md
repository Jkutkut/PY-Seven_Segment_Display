# Seven Segments Display logic:

Logic to codify information into a collection of Seven segment displays. Code written in Python3 and developed for StarVault by [Brandom Moore](https://github.com/Brandommoore).

```python
d = Display("1234567")
print(d)

d.update("0000000")
print(d)
```

```
      ──   ──        ──   ──   ──  
   │    │    │ │  │ │    │       │ 
      ──   ──   ──   ──   ──       
   │ │       │    │    │ │  │    │ 
      ──   ──        ──   ──       
 ──   ──   ──   ──   ──   ──   ──  
│  │ │  │ │  │ │  │ │  │ │  │ │  │ 
                                   
│  │ │  │ │  │ │  │ │  │ │  │ │  │ 
 ──   ──   ──   ──   ──   ──   ──  
```