let WebSocketServer = require('ws').Server;
let list = [];
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
        wss.broadcast(JSON.stringify({ msg: resData.msg, roomId: resData.roomId })); 
    });
    ws.on('close', function (e) {
        console.log('长连接已关闭')
    })
})
// 创建排队的服务
wss1 = new WebSocketServer({ port: 8282 }); 
wss1.broadcast = function (msg) {
    wss1.clients.forEach(function each(client) {
        client.send(msg);
    });
};
wss1.on('connection', function (ws) {
    ws.on('message', function (e) {
        let resData = JSON.parse(e)
        if (resData.msg === 'open') {
            if (list.indexOf(resData.userId) == -1) {
                list.push(resData.userId);
            }
            wss1.broadcast(JSON.stringify({ index: list.indexOf(resData.userId), userId: resData.userId }));
            wss1.broadcast(JSON.stringify({ type: 'teacher', dataList: list }));
            console.log('进入成功')
        }
        else if (resData.msg === 'start') {
            list.splice(list.indexOf(resData.userId), 1);
            wss1.broadcast(JSON.stringify({ type: 'teacher', msg: 'start', userId: resData.userId, dataList: list }));
        }
        else if (resData.msg === 'openAccess') {
            wss1.broadcast(JSON.stringify({ msg: 'openAccess', userId: resData.userId }));
        }
        else if (resData.msg === 'closeAccess') {
            wss1.broadcast(JSON.stringify({ msg: 'closeAccess', userId: resData.userId }));
        }
        else {
           list.splice(list.indexOf(resData.userId), 1);
           wss1.broadcast(JSON.stringify({ type: 'teacher', dataList: list }));
           console.log('推出成功')
       }
    });
    ws.on('close', function (e) {
        console.log('长连接已关闭')
    })
})
console.log('服务器创建成功')