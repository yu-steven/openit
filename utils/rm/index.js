const fs = require('fs');
let urls = fs.readFileSync('./rm2','utf8');

let urlList = urls.split('\n');
let resList = [];
let stringList = [];
let finalList = [];
let finalURLs = [];

for(let i=0;i<urlList.length;i++){
    let url = urlList[i];
    switch (url.split('://')[0]) {
        case 'vmess':
            let vmessJSON = JSON.parse(Buffer.from(url.split('://')[1], 'base64').toString('utf-8'));
            vmessJSON.ps = null
            resList.push({type: 'vmess', data: vmessJSON});
            break
        case 'trojan':
            let trojanData = url.split('://')[1];
            resList.push({type: 'trojan', data: trojanData.split('#')[0]})
            break
        case 'ss':
            let ssData = url.split('://')[1];
            resList.push({type: 'ss', data: ssData.split('#')[0]})
            break
        case 'ssr':
            let ssrData = Buffer.from(url.split('://')[1], 'base64').toString('utf-8');
            resList.push({type: 'ssr', data:ssrData.replace(/remarks=\w+?&/,'remarks={name}&')});
            break
        default:
            break
    }
}
for(let i=0;i<resList.length;i++){
    stringList.push(JSON.stringify(resList[i]))
}
let afterList = Array.from(new Set(stringList))
for(let i=0;i<afterList.length;i++){
    finalList.push(JSON.parse(afterList[i]))
}

for(let i=0;i<finalList.length;i++){
    let item = finalList[i];
    switch (item.type){
        case 'vmess':
            item.data.ps = (i+1).toString();
            finalURLs.push('vmess://'+Buffer.from(JSON.stringify(item.data),'utf8').toString('base64'));
            break
        case 'trojan':
            finalURLs.push('trojan://'+item.data+'#'+(i+1).toString())
            break
        case 'ss':
            finalURLs.push('ss://'+item.data+'#'+(i+1).toString())
            break
        case 'ssr':
            finalURLs.push('ssr://'+Buffer.from(item.data.replace('{name}',Buffer.from((i+1).toString(),'utf8').toString('base64')),'utf8').toString('base64'));
            break
        default:
            break
    }
}
console.log(`去重完成，总共${urlList.length}个节点，去重${urlList.length-finalURLs.length}个节点，剩余${finalURLs.length}个节点。`)
fs.writeFileSync('./url',finalURLs.join('\n'))
