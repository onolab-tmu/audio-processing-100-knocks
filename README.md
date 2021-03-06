音響信号処理100本ノック
-----------------------

## 前付け

Python のインストールは[Anaconda](https://www.anaconda.com/distribution/)をオススメする。

インストール出来たら、`environment.yml`を使って必要なパッケージをインストールする。

    conda env create -f environment.yml

その後、新しい環境をアクティベートする。

    conda activate onkyo100pon

## 第1章：オーディオファイルの読み込み・サンプリングレート・ビットレート・録音・再生・サンプリングレート変換

1. `wav`ファイルを読み込んで、サンプリングレートとビットレートをチェックする、波形をプロットする
2. 440ヘルツ波を再生する、周波数を変換など
3. `wav` ファイルを読み込んで、再生する
4. 音を録音し、`wav`ファイルに落とす
5. 音を録音し、そのまま再生する（パススルー）
6. 16ビット`wav`ファイルを`float`に変換
7. ...
8. ...
9. ...
10. ...

## 第2章：線形代数・プロジェクション・最小二乗推定量・固有値分解

1. 信号を配列で表す
2. 線形
3. 逆行列・線形方程式を解く
4. 線形代数の基本定理（零空間/Nullspace・像空間/Range space）
5. 射影（プロジェクション）
6. 最小二乗問題
7.
8.
9.
10.

## 第3章：FFT・スペクトル・窓関数・畳み込み・フィルター・サンプリング定理

1. 離散フーリエ変換と高速フーリエ変換で計算時間・振幅スペクトルの形状を比較する
2. 窓関数をHann、Hamming、矩形窓と変えながら正弦波のスペクトルをプロット、比較する
3. サンプリング定理を満たさない場合，エイリアシングが生じることを確認する．
4.
5.
6.
7.
8.
9.
10.

## 第4章：STFT・スペクトラム・時間周波数領域プロセッシング

1. STFT してみる
2.
3.
4.
5.
6.
7.
8.
9.
10.

## 第5章：確率・共分散行列・相互相関・ウィーナーフイルター・LPC

1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

## 第6章：シングルチャンネルノイズ除去・スペクトルサブトラクション

1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

## 第7章：アレー信号処理・区間共分散行列・ビームフォーミング

1. Delay and Sum beamforming してみる
2. 時不変な Minimum variance distortionless response beamforming してみる
3. アダプティブ MVDR beamforming してみる
4.
5.
6.
7.
8.
9. IVA を実装する
10. ILRMA を実装する

## 第8章：主成分分析・MUSIC・スペクトル推定・到来方向推定

1. 時間差を計算してみる．それを角度に直してみる
2.
3.
4.
5.
6.
7.
8.
9.
10.

## 第9章：

1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

## 第10章：

1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
