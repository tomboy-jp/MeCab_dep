# Mecab Test  
「MeCab」は「めかぶ」と読みます。  
日本語で書かれた文字列から品詞の種類を判定し、バラバラに分解してくれるすごいやつです。  
文字列をバラバラにする処理のことを形態素解析(けいたいそかいせき)と言います。  

## 目的
* MacOS & Python3環境で[MeCab](https://ja.wikipedia.org/wiki/MeCab)をデプロイする。  
* 生のMeCabでは辞書が貧弱で使い物にならないため、[mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd/blob/master/README.ja.md)もセットで落とす。  

## 環境
```
$ sw_vers  
ProductName:    Mac OS X  
ProductVersion: 10.13.3  
BuildVersion:   17D102  

$ python -V  
Python 3.6.3 :: Anaconda custom (64-bit)  

$ brew -v  
Homebrew 1.5.8  
Homebrew/homebrew-core (git revision 695f341; last commit 2018-03-04)  
```
## 導入手順  
基本は[ここ](https://github.com/neologd/mecab-ipadic-neologd)に書いてある通り。  
あとはPython上で動かすために[ここにある](https://qiita.com/piruty/items/5ae2c2ba660796112207)コマンドを入力します。  

リンク先を読めば全部書いてありますが、一応私が打ったコマンドを載せておきます。

```
$ brew install mecab mecab-ipadic git curl xz  

$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git  

$ cd mecab-ipadic-neologd  

$ ./bin/install-mecab-ipadic-neologd -n -a  

$ pip install mecab-python3  
```

## 注意  
コードを書くとき[このバグ(?)](https://qiita.com/piruty/items/ce218090eae53b775b79)に注意しましょう。  
テストコード(mecabtest.pyというのがそれです)置いておきます。
辞書の参照パスが違っている場合は適宜変更してください。  
デプロイできたら読ませるテキストファイルを変えて遊びましょう。  
