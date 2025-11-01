# 非言語 一問一答（白黒・片手操作・LaTeX）

就活で受けるwebテストの非言語問題の対策を行うwebアプリです。
PCでもスマホでも簡単に勉強できるようにしました。
非言語問題の公式を暗記するのに使ってください。

Flask + MathJax。WSL2 で開発、Render or Fly.io に公開可能。

- まず、下記のコマンドを実行してください。
- ls
- 次に下記のコマンドを実行してください。
- source .venv/bin/activate
- その後、下記のコマンドを実行してください。
- python3 app.py
- そうすれば、httpのリンクが出るので、それをクリックするとwebアプリを開けます。

origin/mainを選び、＋アイコンをクリックしてstageを上げ、コメントを書いてからCommitすればGitHubリポジトリに反映できます。

## 0. 前提
- Windows 11 + **WSL2 (Ubuntu)** + **VS Code Remote-WSL**  
- Git/GitHub アカウント

## 1. WSL2 でプロジェクトを開く
```bash
cd ~
git clone https://github.com/<yourname>/nonverbal-flashcards.git
cd nonverbal-flashcards
code .