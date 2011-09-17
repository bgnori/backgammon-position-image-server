
もやはreadmeではない。ただの開発メモ

Started from  sample from http://www.void.in/wiki/Python/Werkzeug


エーと、まずはurlの再設計が必要。
  * 後方互換性
    アプリでやるか、reverse proxyでやるか？
    とりあえずアプリでやる。




それからエラーが起きたときに画像を返したい。

reverse proxyがやることと、imageserverがやることを分離すること。

 http://ja.wikipedia.org/wiki/HTTP%E3%82%B9%E3%83%86%E3%83%BC%E3%82%BF%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%89
 http://www.studyinghttp.net/cgi-bin/rfc.cgi?2616#Sec6.1


まずは気の利いたものではなく、ただ数字とメッセージを印刷した画像を表示する。
# 結構大変。 404でやられるお遊びのレベルだと大変。
# "No enter found. U are closed out" とかか？
手作りするか、PILでon the flyで生成するか。
サイズがあるので、生成が好ましいが上限が必要。

HTTPExceptionの子クラスとmixinするクラス(ImageMixin)を作る。
BadRequestなどとImageMixinを継承した具象クラスをraise時に使う。

5xxはhandler側で対処。
スタックトレースをimageに書き込めるとうれしい。

imageのformatはpngとjpegをサポートしたい。


get_headersは子クラス側のものをよんで、そこのcontent typeを書き換える。

textのlayout結構複雑。
だらだらしてしまうのでfont sizeくらい使えるようにしたいが・・・。
=> やった。

user guideが必要だ。


1xx Infomatonal => イラネ

2xx Success => 生成したデータを返すので考えない。

3xx Redirection => 見えないはず。2xxを返すものに飛ばされる筈。

4xx 
  400 Bad Request => 必要
  401 Unauthorized => reverse proxyで必要
  402 Payment Required => 不要
  403 Forbidden => 不要
  404 Not Found => 必要
  405 Method Not Allowed => 必要
  406 Not Acceptable => 必要
  407 Proxy Authentication Required => 不要
  408 Request Timeout => 必要, ブラウザで挙動が違う。FireFoxはBodyを無視する。
  409 Conflict => 不要
  410 Gone => 不要
  411 Length Required => 不要
  412 Precondition Failed => 必要
  413 Request Entity Too Large => 必要
  414 Request-URI Too Long => 必要
  415 Unsupported Media Type => 必要
  416 Requested Range Not Satisfiable => 不要 Range requestには対応しない。(417を返す？)
  417 Expectation Failed => 必要
  418 I'm a teapot => I'm a python
  422 Unprocessable Entity => 不要
  423 Locked => 不要
  424 Failed Dependency => 不要
  426 Upgrade Required => 不要


5xxx Server Error
  500 Internal Server Error => 必要
  501 Not Implemented => 必要
  502 Bad Gateway => 不要
  503 Service Unavailable => たぶんreverse proxyのお仕事
  504 Gateway Timeout => 不要
  505 HTTP Version Not Supported => 必要？
  506 Variant Also Negotiates => 不要
  507 Insufficient Storage => 不要
  509 Bandwidth Limit Exceeded => 必要？ たぶんreverse proxyのお仕事
  510 Not Extended => 不要



from http://www.studyinghttp.net/cgi-bin/rfc.cgi?2616#Sec7
リクエストやレスポンスでのメッセージは、リクエストメソッドやレスポンスステータスコードによって規制されていなければ、エンティティを転送する事ができる。エンティティは、エンティティヘッダフィールドとエンティティボディから成るが、エンティティヘッダのみを含むレスポンスもある。


http://werkzeug.pocoo.org/docs/exceptions/

