一文带你搞懂HTTP和RPC协议的异同:https://blog.csdn.net/Mr_YanMingXin/article/details/124653945
rpc和http的区别是什么 各自的优缺点有哪些：https://www.cnblogs.com/fuyuanming/p/16155255.html


主要来阐述HTTP和RPC的异同，让大家更容易根据自己的实际情况选择更适合的方案。

 

传输协议

RPC:可以基于TCP协议，也可以基于HTTP协议

HTTP:基于HTTP协议

 

传输效率

RPC:使用自定义的TCP协议，可以让请求报文体积更小，或者使用HTTP2协议，也可以很好的减少报文的体积，提高传输效率

HTTP:如果是基于HTTP1.1的协议，请求中会包含很多无用的内容，如果是基于HTTP2.0，那么简单的封装以下是可以作为一个RPC来使用的，这时标准RPC框架更多的是服务治理

 

性能消耗

RPC:可以基于thrift实现高效的二进制传输
HTTP:大部分是通过json来实现的，字节大小和序列化耗时都比thrift要更消耗性能

负载均衡

RPC：基本都自带了负载均衡策略
HTTP：需要配置Nginx，HAProxy来实现

服务治理

RPC：能做到自动通知，不影响上游
HTTP:需要事先通知，修改Nginx/HAProxy配置

总结

RPC主要用于公司内部的服务调用，性能消耗低，传输效率高，服务治理方便。
HTTP主要用于对外的异构环境，浏览器接口调用，APP接口调用，第三方接口调用等。