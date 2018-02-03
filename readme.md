# @5kdnのtwitterプロフィールを変更する

## 環境構築

python, Node.js環境が必要

### テスト環境

- python  == 3.6.3
- Node.js == 9.4.0

```bash
# python
pyenv virtualenv 3.6.3 TwitterProfileChanger
pyenv local TwitterProfileChanger
pip install -r requirement.txt

# Node.js
yarn install    # SAME TO: npm install
```

### 開発中

開発中は`yarn gulp`することで、pug, cass, jsの編集をwatchできる.
