"""
SAPネットの実装開始
並列化を考えず、活性値を持たせて実装
動作検証を重視してプログラミング
重みをもたせた状態で活性化
隣接行列・接続行列などを用いて実装予定
活性値をランダム、重みをランダムで実装
動作のリアルタイム表示を実現する
"""

#隣接行列→https://qiita.com/tanaka_benkyo/items/3a242e0ca7724973dcd9

#フルメッシュなSAPネットワークの可視化における幾何学的矛盾の解決
"""
直線表現を行うと、表現方法として幾何学的に矛盾が起こる
解決方法を２つ提案
1->大きい重みを持つノードを曲線として表現することで実質無限大になる（煩雑になる可能性）
2->大きい重み（太く）、小さい重み（細く）表現することで、他のノードに干渉せずに表現
結果として、他ノードに影響を与えるが少なそうな２の案を採択する
"""


import numpy
import pandas

