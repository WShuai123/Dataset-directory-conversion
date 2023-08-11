### converted2train&test.py

(Before conversion)转换前：

```
├── your_dataset_name
    ├── class_1
    |   ├── img_1.jpg  # .png
    │   ├── img_2.jpg
    │   ├── ...
    ├── class_2
    |   ├── img_a.jpg
    │   ├── img_b.jpg
    │   ├── ...
    ├── ...
```

(After conversion)转换后：

```
├── your_dataset_name
    ├── training
    |   ├── class_1
    |   |   ├── img_1.jpg  # .png
    |   │   ├── img_2.jpg
    |   │   ├── ...
    |   ├── class_2
    |   |   ├── img_a.jpg
    |   │   ├── img_b.jpg
    |   │   ├── ...
    |   ├── ...
    └── test
```

### converted2train&val&test.py

(Before conversion)转换前：

```
├── your_dataset_name
    ├── class_1
    |   ├── img_1.jpg  # .png
    │   ├── img_2.jpg
    │   ├── ...
    ├── class_2
    |   ├── img_a.jpg
    │   ├── img_b.jpg
    │   ├── ...
    ├── ...
```

(After conversion)转换后：

```
├── your_dataset_name
    ├── training
    |   ├── class_1
    |   |   ├── img_1.jpg  # .png
    |   │   ├── img_2.jpg
    |   │   ├── ...
    |   ├── class_2
    |   |   ├── img_a.jpg
    |   │   ├── img_b.jpg
    |   │   ├── ...
    |   ├── ...
    └── validation
    └── test
```
