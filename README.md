<h1>タスク管理アプリケーション</h1>
djangoとデータベースにpostgresを用いたタスク管理アプリケーションです。
<p>実際の環境は、<a link href="https://porty5974-habit-record.herokuapp.com/workrecord/habit/">https://porty5974-habit-record.herokuapp.com/workrecord/habit/</a></p>
toppageで取り組んでいるタスクを一覧が見えるようになっていて、
記録ボタンを押すと画面が遷移し、タスクを取り組んだ日にちなどの情報が見れるようになっている。

docker-composeで環境を構築して、テストはまだ実装していないが後学としてCI/CDパイプラインも導入した。
<p>docker内でDjangoサーバー起動する際は、 </p>
<p><b>python manage.py 0.0.0.0:8000</b> を入力。</p>

