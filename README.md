# 非言語 一問一答（白黒・片手操作・LaTeX）

就活で受けるwebテストの非言語問題の対策を行うwebアプリです。
PCでもスマホでも簡単に勉強できるようにしました。
非言語問題の公式を暗記するのに使ってください。

Flask + MathJax。WSL2 で開発、Render or Fly.io に公開可能。

## 0. 前提
- Windows 11 + **WSL2 (Ubuntu)** + **VS Code Remote-WSL**  
- Git/GitHub アカウント

## 1. WSL2 でプロジェクトを開く
```bash
cd ~
git clone https://github.com/<yourname>/nonverbal-flashcards.git
cd nonverbal-flashcards
code .