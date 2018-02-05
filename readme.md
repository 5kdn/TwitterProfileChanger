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

### 実行環境

```bash
git clone https://git.5kdn.red/git/skdn/TwitterProfileChanger.git /var/www/TwitterProfileChanger
cd /var/www
sudo chmod -R 775 TwitterProfileChanger
sudo chown -R skdn. TwitterProfileChanger
cd TwitterProfileChanger
sudo mv TwitterProfileChanger.service /etc/systemd/system/
sudo chmod 755 /etc/systemd/system/TwitterProfileChanger.service
sudo chown root. /etc/systemd/system/TwitterProfileChanger.service
sudo systemctl enable TwitterProfileChanger
sudo systemctl start TwitterProfileChanger
```

```nginx|default.conf
# server {
    location /twitter/ {
      include uwsgi_params;
      uwsgi_pass unix:/var/www/TwitterProfileChanger/webroot/uwsgi.sock;
    }
# }
```
