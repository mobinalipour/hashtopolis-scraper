# hashtopolis-scraper
a tool for scraping hashtopolis tasks and send log to telegram


### how this tool works ?
this tool will login to your hashtopolis server and gets task names and the progress in % and cracks number and send them to telegram with a bot

### prerequisites
u have to install this libraries :
`pip install requests`
`pip install beautifulsoup4`

### Usage
by running the program it will get some information:
1. Enter your hashtopolis server ip so the scraper can login to hashtopolis server
2. Enter the number of tasks u wanna see their log in telegram for example if enter '3' scraper will send first 3 tasks!
3. Enter your hashtopolis username
4. Enter your password
5. Enter the bot token (you should create a bot in `@BotFather` bot in telegram in it will give a token)
6. Enter your Chat id ( you can get your chat id from `@raw_data_bot` in telegram
7. Enter a number for example if enter 20, the scraper will send logs to telegram every 20 second.


### Donate
my BTC address : bc1qa447uc04kumc27x5zefkgpnmk6g60uzcuawtv7
