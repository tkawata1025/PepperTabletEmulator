#!/bin/bash

NAOQISDK="$HOME/naoqi/pynaoqi-python2.7-2.4.2.26-mac64" # <--- NAOqi Python SDK を保存した場所で書き換える

CHOREGRAPHEDIR="/Applications/Aldebaran/Choregraphe Suite 2.4" # <-- Choregraphe のインストールディレクトリ

cd "$CHOREGRAPHEDIR"

DYLD_FRAMEWORK_PATH=Choregraphe.app/Contents/Resources \
DYLD_LIBRARY_PATH=Choregraphe.app/Contents/Resources/lib \
Choregraphe.app/Contents/Resources/bin/naoqi-bin &

sleep 5

export DYLD_LIBRARY_PATH="$NAOQISDK":$DYLD_LIBRARY_PATH
export PYTHONPATH="$NAOQISDK":$PYTHONPATH 

/usr/bin/python /usr/local/bin/qimessaging-json &
/usr/bin/python /usr/local/bin/PepperTabletEmulator.py &

open --wait-apps ./Choregraphe.app --args -p 9559 

kill %1
kill %2
kill %3

sleep 5

echo ""
echo "終了しました！"
echo "まれにバックグラウンドプロセスが残っている場合があります"
echo "プロセスが残っていると次回の Choregraphe の起動時"
echo "バーチャルロボットがうまく機能しないことがあります"
echo "おかしいなと思ったら、一旦 Choregrape を停止"
echo "ps -ef コマンドで naoqi-bin と qimessaging-json "
echo "というプロセスが動いていないか確認、動いていたら kill "
echo "コマンドで停止させてください"
echo ""





