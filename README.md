# Telegram bot style transfer
------  
The final project of the deep learning school from MIPT (1 sem, fall 2022)
------
# Что умеет данный бот
Бот умеет переносить стиль картин на исходную фотографию с применением сверточных нейросетей (CNN).
------
# Пример работы
![](https://github.com/s1lver29/tg_bot_gan/blob/main/gif/example_style_photo.gif)
------
Инициализация бота:  
```bash  
echo API_TOKEN=<YOUR_TELEGRAM:TOKEN> > .env
```
------
Запуск бота:
```bash  
docker-compose up --build
```
------
# Origin  
[A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)
