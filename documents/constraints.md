PIDファイルの機能要件は以下の通りである。



mydaemon\_tが親ディレクトリ内を通過および探索する。

mydaemon\_tが親ディレクトリに対して書き込みを行う。

mydaemon\_tが親ディレクトリに新しいファイル名を追加する。

mydaemon\_tが親ディレクトリからファイル名を削除する。

mydaemon\_tが親ディレクトリ内にファイルを作成する際、そのラベルを自動的にPIDファイルのタイプに遷移させる。

mydaemon\_tがPIDファイルを新規作成する。

mydaemon\_tがPIDファイルを開く。

mydaemon\_tがPIDファイルへデータを書き込む。

mydaemon\_tがPIDファイルの属性情報を参照する。

mydaemon\_tがPIDファイルをロックする。

mydaemon\_tがPIDファイルを削除する。



上記のPIDファイル制御に関する要件を、論理制約 $\\phi\_{pid}$ として以下のように定義する。



$\\phi\_{pid}$ = $ (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_run\\\_t}, \\texttt{dir}, \\texttt{search}) = \\mathrm{True}) $

&nbsp;              $ \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_run\\\_t}, \\texttt{dir}, \\texttt{write}) = \\mathrm{True}) \\\\

&nbsp;              $ \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_run\\\_t}, \\texttt{dir}, \\texttt{add\\\_name}) = \\mathrm{True}) \\\\

&nbsp;              $ \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_run\\\_t}, \\texttt{dir}, \\texttt{remove\\\_name}) = \\mathrm{True})

&nbsp;              $ \\land (type\\\_transition(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_run\\\_t}, \\texttt{file}, \\\\

&nbsp;              $ \\qquad \\qquad \\texttt{mydaemon\\\_var\\\_run\\\_t}) = \\mathrm{True}) \\\\

&nbsp;              $ \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{create}) = \\mathrm{True}) \\\\

&nbsp;              $ \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{open}) = \\mathrm{True}) \\\\

&nbsp;              $ \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{write}) = \\mathrm{True}) \\\\

&nbsp;              $ \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{getattr}) = \\mathrm{True}) \\\\

&nbsp;              $ \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{lock}) = \\mathrm{True}) \\\\

&nbsp;              $ \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_var\\\_run\\\_t}, \\texttt{file}, \\texttt{unlink}) = \\mathrm{True})

&nbsp;              

&nbsp;\\end{split}

\\end{equation}

\\end{small}







設定ファイルの機能要件は以下の通りである。



mydaemon\_tが親ディレクトリ内を通過および探索する。

mydaemon\_tが親ディレクトリの属性情報を参照する。

mydaemon\_tが設定ファイルを開く。

mydaemon\_tが設定ファイルの内容を読み取る。

mydaemon\_tが設定ファイルの属性情報を参照する。



上記の設定ファイル読み込みに関する要件を、論理制約 $\\phi\_{conf}$ として以下のように定義する。



\\begin{small}

\\begin{equation}

&nbsp;\\begin{split}

&nbsp; \\phi\_{conf} = \& (allow(\\texttt{mydaemon\\\_t}, \\texttt{etc\\\_t}, \\texttt{dir}, \\texttt{search}) = \\mathrm{True}) \\\\

&nbsp;               \& \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{etc\\\_t}, \\texttt{dir}, \\texttt{getattr}) = \\mathrm{True}) \\\\

&nbsp;               \& \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_conf\\\_t}, \\texttt{file}, \\texttt{open}) = \\mathrm{True}) \\\\

&nbsp;               \& \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_conf\\\_t}, \\texttt{file}, \\texttt{read}) = \\mathrm{True}) \\\\

&nbsp;               \& \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_conf\\\_t}, \\texttt{file}, \\texttt{getattr}) = \\mathrm{True})

&nbsp;\\end{split}

\\end{equation}

\\end{small}







ログファイルの機能要件は以下の通りである。



mydaemon\_tが親ディレクトリ内を通過および探索する。

mydaemon\_tが親ディレクトリに対して書き込みを行う。

mydaemon\_tが親ディレクトリに新しいログファイル名を追加する。

mydaemon\_tが親ディレクトリ内にファイルを作成する際、そのラベルを自動的にログファイルのタイプに遷移させる。

mydaemon\_tがログファイルを新規作成する。

mydaemon\_tがログファイルを開く。

mydaemon\_tがログファイルの属性情報を参照する。

mydaemon\_tがログファイルの末尾にデータを追加する。



上記のログファイル記録に関する要件を、論理制約 $\\phi\_{log}$ として以下のように定義する。



\\begin{small}

\\begin{equation}

&nbsp;\\begin{split}

&nbsp; \\phi\_{log} = \& (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_log\\\_t}, \\texttt{dir}, \\texttt{search}) = \\mathrm{True}) \\\\

&nbsp;              \& \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_log\\\_t}, \\texttt{dir}, \\texttt{write}) = \\mathrm{True}) \\\\

&nbsp;              \& \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_log\\\_t}, \\texttt{dir}, \\texttt{add\\\_name}) = \\mathrm{True}) \\\\

&nbsp;              \& \\land (type\\\_transition(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_log\\\_t}, \\texttt{file}, \\\\

&nbsp;              \& \\qquad \\qquad \\texttt{mydaemon\\\_log\\\_t}) = \\mathrm{True}) \\\\

&nbsp;              \& \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_log\\\_t}, \\texttt{file}, \\texttt{create}) = \\mathrm{True}) \\\\

&nbsp;              \& \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_log\\\_t}, \\texttt{file}, \\texttt{open}) = \\mathrm{True}) \\\\

&nbsp;              \& \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_log\\\_t}, \\texttt{file}, \\texttt{getattr}) = \\mathrm{True}) \\\\

&nbsp;              \& \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_log\\\_t}, \\texttt{file}, \\texttt{append}) = \\mathrm{True})

&nbsp;\\end{split}

\\end{equation}

\\end{small}







ログファイルおよびPIDファイルへ到達するための共通要件は以下の通りである。



mydaemon\_tが上位ディレクトリ内を通過および探索する。

mydaemon\_tが上位ディレクトリの属性情報を参照する。



上記の共通要件を、論理制約 $\\phi\_{common}$ として以下のように定義する。



\\begin{small}

\\begin{equation}

&nbsp;\\begin{split}

&nbsp; \\phi\_{common} = \& (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_t}, \\texttt{dir}, \\texttt{search}) = \\mathrm{True}) \\\\

&nbsp;                 \& \\land (allow(\\texttt{mydaemon\\\_t}, \\texttt{var\\\_t}, \\texttt{dir}, \\texttt{getattr}) = \\mathrm{True})

&nbsp;\\end{split}

\\end{equation}

\\end{small}







ネットワーク待ち受けの機能要件は以下の通りである。



mydaemon\_tがTCPソケットを作成する。

mydaemon\_tがソケットの設定を変更する。

mydaemon\_tがソケットにポートを紐付ける。

mydaemon\_tが、ポートタイプ \\texttt{http\\\_cache\\\_port\\\_t} を使用する。

mydaemon\_tがノードタイプ \\texttt{node\\\_t} を使用する。

mydaemon\_tが接続待ち状態にする。



上記のネットワーク待ち受けに関する要件を、制約 $\\phi\_{net}$ として定義する。



$\\phi\_{net}$ = $(allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_t}, \\texttt{tcp\\\_socket}, \\texttt{create}) = \\mathrm{True}) $

&nbsp;              $\\land$ $(allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_t}, \\texttt{tcp\\\_socket}, \\texttt{setopt}) = \\mathrm{True}) $

&nbsp;              $\\land$ $(allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_t}, \\texttt{tcp\\\_socket}, \\texttt{bind}) = \\mathrm{True}) $

&nbsp;              $\\land$ $(allow(\\texttt{mydaemon\\\_t}, \\texttt{http\\\_cache\\\_port\\\_t}, \\texttt{tcp\\\_socket}, \\texttt{name\\\_bind}) = \\mathrm{True}) $

&nbsp;              $\\land$ $(allow(\\texttt{mydaemon\\\_t}, \\texttt{node\\\_t}, \\texttt{tcp\\\_socket}, \\texttt{node\\\_bind}) = \\mathrm{True}) $

&nbsp;              $\\land$ $(allow(\\texttt{mydaemon\\\_t}, \\texttt{mydaemon\\\_t}, \\texttt{tcp\\\_socket}, \\texttt{listen}) = \\mathrm{True}) $

