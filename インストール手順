#################################################
# Mac 向け Pepper Tablet Emulator セットアップ手順  
#################################################

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
NAOqi Python SDK をインストール
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

□ ダウンロード

NAOqi Python SDK (Python 2.7 SDK 2.4.2 Mac 64) を次よりダウンロード 

https://community.aldebaran.com/en/resources/software/pepper-sdks-and-documentation-242

(リソースにアクセスするには Aldebara デベロッパープログラムに登録しておく必要があります。
まず https://store.aldebaran.com/default/customer/account/create/ でユーザー登録、次に
https://community.aldebaran.com/en/developerprogram#section3 でデベロッパープログラムに登録します）

□ ダウンロードしたファイルを展開

□ 展開したファイルを特定の場所にファイルを保存 例えば ユーザーディレクトリの naoqi ディレクトリ配下に保存 

例：
mkdir -p ~/naoqi
cp -r pynaoqi-python2.7-2.4.2.26-mac64  ~/naoqi
　  

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
nginx インストール、セットアップ
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
□ インストール

brew install nginx

(※ brew をまだセットアップしていない場合、まず http://brew.sh/index_ja.html を参考に homebrew をインストールします)

□ エミュレータ用セットアップ

mkdir -p ~/.local/share/PackageManager/apps
  
ln -s ~/.local/share/PackageManager/apps /usr/local/var/www/


＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
libqi-js のセットアップ
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
□ https://github.com/aldebaran/libqi-js/ ページの [Download ZIP] ボタンを押して libqi-js のアーカイブを入手

□ ファイルを展開、展開したフォルダーの中に入って次を実行

cp -r libs /usr/local/var/www/

□ qimessaging-json を /usr/local/bin に保存

cp qimessaging-json  /usr/local/bin 

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
tornadoのインストール
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

□ sudo pip install tornado

(※ pip をまだ設定していない場合、次のコマンドを実行してまず pip をインストールします 
sudo easy_install pip 
)

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
tornadio2 のインストール
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
□ https://github.com/MrJoes/tornadio2 右下 [Downlad ZIP]ボタンを押して、tornadio2 アーカイブファイルを入手

□ ファイルを展開して、展開したフォルダーの中に入って次を実行

sudo ./setup.py install

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
Pepper Tablet Emulatorのセットアップ
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

□ 作業用ディレクトリを作成、移動

□ 次のコマンドを実行

git clone https://github.com/tkawata1025/PepperTabletEmulator.git

cd PepperTabletEmulator

cp install_files/PepperTabletEmulator.py /usr/local/bin/

cp install_files/nginx/nginx.conf /usr/local/etc/nginx/

□ Choregraphe2.4_te.sh　をテキストエディタで開き３行目を変更を環境に合わせて任意に変更

-----
NAOQISDK="$HOME/naoqi/pynaoqi-python2.7-2.4.2.26-mac64" # <--- NAOqi Python SDK を保存した場所で書き換える
-----

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
Mac OS X El Capitan の場合 - SDK へのパッチ
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

Mac OS X El Capitan を使っている場合、次を参考に Python SDK にパッチを当てます

http://qiita.com/tkawata1025/items/31dd49bcef04c85b3047





