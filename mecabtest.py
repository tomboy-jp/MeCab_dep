import MeCab

# ipadic-NEologd辞書を読み込みつつTaggerを配置。
# 引数は使用する辞書のパスを指定している。
# 違う場合は適宜修正を。
# 辞書を使わないなら、引数は空で良い。
tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

# Python3特有のsurfaceが使えないバグを回避。
tagger.parse(' ')

# テキストファイルの読み込み
f = open('txt/text1.txt','r')
text = f.read()
f.close()

# Taggerを使ってテキストを形態素解析。出来上がったnodeはイテレータであることに注意。
node = tagger.parseToNode(text)

# イテレートが終わるまでsurfaseとfeatureを出力。
while node:
    feature = node.feature.split(",")
    print(str(node.surface) + '\t' + str(feature))
    node = node.next

# 分かち書きされた単語を格納するならnode.surfaceを配列にappendすればいい。
# 品詞で条件分けをするなら、
# if feature[0] == '名詞':
#　のように書くと良い。
