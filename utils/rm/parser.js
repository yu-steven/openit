const fs = require('fs');
module.exports={
    read(path){
        let file = fs.readFileSync(path,'utf8');
        let urlList = file.split('\n');
        let returnList = [];
        for(let i=0;i<urlList.length;i++){
            let url = urlList[i];
            switch (url.split('://')[0]){
                case 'vmess':
                    let vmessJSON = JSON.parse(Buffer.from(url.split('://')[1], 'base64').toString('utf-8'));
                    returnList.push({type:'vmess',name:vmessJSON.ps,address:vmessJSON.add,vmessData:vmessJSON,data:vmessJSON,url:url});
                    break
                case 'trojan':
                    let trojanData = url.split('://')[1];
                    let trojanName = decodeURIComponent(trojanData.split('#')[1])
                    let trojanAddress = trojanData.split('@')[1].split('?')[0].split(':')[0];
                    returnList.push({type:'trojan',name:trojanName,address:trojanAddress,data:trojanData.split('#')[0],url:url})
                    break
                case 'ss':
                    let ssData = url.split('://')[1];
                    let ssName = decodeURIComponent(ssData.split('#')[1])
                    let ssAddress = ssData.split('@')[1].split('#')[0].split(':')[0];
                    returnList.push({type:'ss',name:ssName,address:ssAddress,data: ssData.split('#')[0],url:url})
                    break
                case 'ssr':
                    let ssrData = Buffer.from(url.split('://')[1], 'base64').toString('utf-8');
                    let ssNameBase64 = ssrData.split('&')[1].split('=')[1];
                    let ssrName = Buffer.from(ssNameBase64, 'base64').toString('utf-8');
                    let ssrAddress = ssrData.split(':')[0]
                    returnList.push({type:'ssr',name:ssrName,address:ssrAddress,data:ssrData.replace(/remarks=\w+?&/,'remarks={name}&'),url:url});
                    break
                case 'https':
                    let httpsData = url.split('://')[1].split('#')[0];
                    let httpsAddress = Buffer.from(httpsData.split('?')[0],"base64").toString('utf8').split('@')[1].split(':')[0]
                    returnList.push({type: 'https',name:decodeURIComponent(url.split('://')[1].split('#')[1]),address:httpsAddress,data:httpsData,url:url})
                    break
                default:
                    break
            }
        }
        return returnList
    }
}
