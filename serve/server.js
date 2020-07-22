let WebSocketServer = require('ws').Server;
wss = new WebSocketServer({ port: 8181 }); 
wss.broadcast = function (msg) {
    wss.clients.forEach(function each(client) {
        client.send(msg);
    });
};
wss.on('connection', function (ws) {
    ws.on('message', function (e) {
        let resData = JSON.parse(e)
        console.log('接收到来自client的消息：' + resData.msg)
        wss.broadcast(JSON.stringify({ msg: resData.msg })); 
    });
    ws.on('close', function (e) {
        console.log('长连接已关闭')
    })
})
console.log('服务器创建成功')