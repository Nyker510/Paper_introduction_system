# Paper_introduction_system
Paper and Book introduction system powered by Django.

本システムは論文や参考書の輪読を研究室の複数人で行うときに，他の人の担当範囲を効率よく把握するために作成しました．

具体的には，

・先生のオススメや読みたい論文の一覧を作成<br>
・研究室内の他の構成員が取り組んでいる論文をハイライト表示
・論文を読んだ感想，報告の保存
・ソーティングや一括登録などのデータベース管理
を容易に実現するシステムとなっています．

作者の必要性に応じて特有の表示やデータベース構造を作成しているため，利用者の必要に応じて変更を施してください．

実行環境はPython3 + Django on Ubuntu16.04
実行方法は「python3 runserver manage.py」と入力した後に，ブラウザから「localhost:8000」にアクセスしてください．
