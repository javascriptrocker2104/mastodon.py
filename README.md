git clone https://github.com/javascriptrocker2104/mastodon.py.git
cd mastodon.py

sudo apt-get install ./python3-module-mastodon-2.2.2-alt1.noarch.rpm

#Проверка
python3 -c "import mastodon; print('ok')"

# Подробная инфа об установленном пакете
rpm -qi python3-module-mastodon

# Список файлов, установленных пакетом
rpm -ql python3-module-mastodon




#Зависимости (если через rpm -ivh и нет зависимостей)
sudo apt-get install python3-module-requests python3-module-dateutil python3-module-decorator python3-module-magic
