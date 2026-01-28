\# 機能要件と論理制約の詳細定義



本ドキュメントでは、論文内において紙面の都合上省略した機能要件および論理制約の全容を記述する。



\## 1. PIDファイル制御に関する要件



\### 機能要件

\* mydaemon\_tが親ディレクトリ内を通過および探索する。

\* mydaemon\_tが親ディレクトリに対して書き込みを行う。

\* mydaemon\_tが親ディレクトリに新しいファイル名を追加する。

\* mydaemon\_tが親ディレクトリからファイル名を削除する。

\* mydaemon\_tが親ディレクトリ内にファイルを作成する際、そのラベルを自動的にPIDファイルのタイプに遷移させる。

\* mydaemon\_tがPIDファイルを新規作成する。

\* mydaemon\_tがPIDファイルを開く。

\* mydaemon\_tがPIDファイルへデータを書き込む。

\* mydaemon\_tがPIDファイルの属性情報を参照する。

\* mydaemon\_tがPIDファイルをロックする。

\* mydaemon\_tがPIDファイルを削除する。



\### 論理制約 $\\phi\_{pid}$



$$

\\begin{aligned}

\\phi\_{pid} \&= (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_run\\\_t}, \\texttt{dir}, \\texttt{search}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_run\\\_t}, \\texttt{dir}, \\texttt{write}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_run\\\_t}, \\texttt{dir}, \\texttt{add\\\_name}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_run\\\_t}, \\texttt{dir}, \\texttt{remove\\\_name}) = \\mathrm{True}) \\\\

\&\\land (type\\\_transition(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_run\\\_t}, \\texttt{file}, \\texttt{mydaemon\\\_var\\\_run\\\_t}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{create}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{open}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{write}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{getattr}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{lock}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{unlink}) = \\mathrm{True})

\\end{aligned}

$$



---



\## 2. 設定ファイル読み込みに関する要件



\### 機能要件

\* mydaemon\_tが親ディレクトリ内を通過および探索する。

\* mydaemon\_tが親ディレクトリの属性情報を参照する。

\* mydaemon\_tが設定ファイルを開く。

\* mydaemon\_tが設定ファイルの内容を読み取る。

\* mydaemon\_tが設定ファイルの属性情報を参照する。



\### 論理制約 $\\phi\_{conf}$



$$

\\begin{aligned}

\\phi\_{conf} \&= (allow(\\texttt{mydaemon\\\_t}, \\texttt{etc\\\_t}, \\texttt{dir}, \\texttt{search}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{etc\\\_t}, \\texttt{dir}, \\texttt{getattr}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_conf\\\_t}, \\texttt{file}, \\texttt{open}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_conf\\\_t}, \\texttt{file}, \\texttt{read}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_conf\\\_t}, \\texttt{file}, \\texttt{getattr}) = \\mathrm{True})

\\end{aligned}

$$



---



\## 3. ログファイル記録に関する要件



\### 機能要件

\* mydaemon\_tが親ディレクトリ内を通過および探索する。

\* mydaemon\_tが親ディレクトリに対して書き込みを行う。

\* mydaemon\_tが親ディレクトリに新しいログファイル名を追加する。

\* mydaemon\_tが親ディレクトリ内にファイルを作成する際、そのラベルを自動的にログファイルのタイプに遷移させる。

\* mydaemon\_tがログファイルを新規作成する。

\* mydaemon\_tがログファイルを開く。

\* mydaemon\_tがログファイルの属性情報を参照する。

\* mydaemon\_tがログファイルの末尾にデータを追加する。



\### 論理制約 $\\phi\_{log}$



$$

\\begin{aligned}

\\phi\_{log} \&= (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_log\\\_t}, \\texttt{dir}, \\texttt{search}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_log\\\_t}, \\texttt{dir}, \\texttt{write}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_log\\\_t}, \\texttt{dir}, \\texttt{add\\\_name}) = \\mathrm{True}) \\\\

\&\\land (type\\\_transition(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_log\\\_t}, \\texttt{file}, \\texttt{mydaemon\\\_log\\\_t}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_log\\\_t}, \\texttt{file}, \\texttt{create}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_log\\\_t}, \\texttt{file}, \\texttt{open}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_log\\\_t}, \\texttt{file}, \\texttt{getattr}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_log\\\_t}, \\texttt{file}, \\texttt{append}) = \\mathrm{True})

\\end{aligned}

$$



---



\## 4. 共通要件



\### 機能要件

\* mydaemon\_tが上位ディレクトリ内を通過および探索する。

\* mydaemon\_tが上位ディレクトリの属性情報を参照する。



\### 論理制約 $\\phi\_{common}$



$$

\\begin{aligned}

\\phi\_{common} \&= (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_t}, \\texttt{dir}, \\texttt{search}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_t}, \\texttt{dir}, \\texttt{getattr}) = \\mathrm{True})

\\end{aligned}

$$



---



\## 5. ネットワーク待ち受けに関する要件



\### 機能要件

\* mydaemon\_tがTCPソケットを作成する。

\* mydaemon\_tがソケットの設定を変更する。

\* mydaemon\_tがソケットにポートを紐付ける。

\* mydaemon\_tが、ポートタイプ `http\_cache\_port\_t` を使用する。

\* mydaemon\_tがノードタイプ `node\_t` を使用する。

\* mydaemon\_tが接続待ち状態にする。



\### 論理制約 $\\phi\_{net}$



$$

\\begin{aligned}

\\phi\_{net} \&= (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_t}, \\texttt{tcp\\\_socket}, \\texttt{create}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_t}, \\texttt{tcp\\\_socket}, \\texttt{setopt}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_t}, \\texttt{tcp\\\_socket}, \\texttt{bind}) = \\mathrm{True}) \\\\

\&\\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{http\\\_cache\\\_port\\\_t}, \\texttt{tcp\\\_socket}, \\

