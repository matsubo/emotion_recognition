# 感情分析

## 概要

引数に与えられた動画ファイルの感情分析を行います。


Setup
```
% docker compose build
```

実行
```
% docker compose run app python main.py archive.mp4
[
    {
        "time": 0.0,
        "emotion": "neutral"
    },
    {
        "time": 0.0,
        "emotion": "sad"
    },
    {
        "time": 0.0,
        "emotion": "neutral"
    },
    {
        "time": 0.0,
        "emotion": "sad"
    },
    {
        "time": 0.2,
        "emotion": "neutral"
    },
    {
        "time": 0.2,
        "emotion": "angry"
    },
    ...
```


