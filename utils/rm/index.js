const fs = require('fs')
const location = require('./location')
const config = require('./config')
const major = require('./major')

let urls = fs.readFileSync('./rm2','utf8');
let flags = JSON.parse(fs.readFileSync('./flags.json','utf8'))

let urlList = urls.split('\n');
let resList = [];
let stringList = [];
let finalList = [];
let finalURLs = [];
let countryList = ['unknown'];
let emojiList =[''];
let countryCount = {unknown:0};
let urlCountryList = {unknown:[]}

async function run(){
    //处理flags
    for(let i=0;i<flags.length;i++){
        countryList.push(flags[i].code);
        emojiList.push(flags[i].emoji);
        countryCount[flags[i].code] = 0;
        urlCountryList[flags[i].code] = [];
    }

    //解析URL
    for(let i=0;i<urlList.length;i++){
        let url = urlList[i];
        switch (url.split('://')[0]) {
            case 'vmess':
                let vmessJSON = JSON.parse(Buffer.from(url.split('://')[1], 'base64').toString('utf-8'));
                vmessJSON.ps = null
                resList.push({type: 'vmess', data: vmessJSON,address:vmessJSON.add});
                break
            case 'trojan':
                let trojanData = url.split('://')[1];
                let trojanAddress = trojanData.split('@')[1].split('?')[0].split(':')[0];
                resList.push({type: 'trojan', data: trojanData.split('#')[0],address:trojanAddress})
                break
            case 'ss':
                let ssData = url.split('://')[1];
                let ssAddress = ssData.split('@')[1].split('#')[0].split(':')[0];
                resList.push({type: 'ss', data: ssData.split('#')[0],address:ssAddress})
                break
            case 'ssr':
                let ssrData = Buffer.from(url.split('://')[1], 'base64').toString('utf-8');
                let ssrAddress = ssrData.split(':')[0];
                resList.push({type: 'ssr', data:ssrData.replace(/remarks=\w+?&/,'remarks={name}&'),address:ssrAddress});
                break
            case 'https':
                let httpsData = url.split('://')[1].split('#')[0];
                let httpsAddress = Buffer.from(httpsData.split('?')[0],"base64").toString('utf8').split('@')[1].split(':')[0]
                resList.push({type: 'https',data:httpsData,address:httpsAddress})
                break
            default:
                break
        }
    }

    //去重时要先将对象转为字符串
    for(let i=0;i<resList.length;i++){
        stringList.push(JSON.stringify(resList[i]))
    }

    //去重
    let afterList = Array.from(new Set(stringList))

    //转回来
    for(let i=0;i<afterList.length;i++){
        finalList.push(JSON.parse(afterList[i]))
    }

    //批量测试国家
    for(let i=0;i<finalList.length;i++){
        finalList[i].country = await location.get(finalList[i].address)
    }

    //变回链接
    for(let i=0;i<finalList.length;i++){
        let item = finalList[i];
        let name;
        countryCount[finalList[i].country]++
        if(config.enableMediaUnlockTest === true){
            name = emojiList[countryList.indexOf(finalList[i].country)]+finalList[i].country+' '+countryCount[finalList[i].country]+' | {{result}}'+config.nodeAddName
        }else{
            name = emojiList[countryList.indexOf(finalList[i].country)]+finalList[i].country+' '+countryCount[finalList[i].country]+config.nodeAddName
        }
        switch (item.type){
            case 'vmess':
                item.data.ps = (name).toString();
                urlCountryList[finalList[i].country].push('vmess://'+Buffer.from(JSON.stringify(item.data),'utf8').toString('base64'));
                break
            case 'trojan':
                try{
                urlCountryList[finalList[i].country].push('trojan://'+item.data+'#'+(name).toString())}catch(e){
                    console.log('err')
                }
                break
            case 'ss':
                urlCountryList[finalList[i].country].push('ss://'+item.data+'#'+(name).toString())
                break
            case 'ssr':
                urlCountryList[finalList[i].country].push('ssr://'+Buffer.from(item.data.replace('{name}',Buffer.from((name).toString(),'utf8').toString('base64')),'utf8').toString('base64'));
                break
            case 'https':
                urlCountryList[finalList[i].country].push('https://'+item.data+'#'+encodeURIComponent(name.toString()))
                break
            default:
                break
        }
    }
    for(const i in urlCountryList){
        if(urlCountryList[i].length === 0 ){
        }else{
            for (let a=0;a<urlCountryList[i].length;a++){
                finalURLs.push(urlCountryList[i][a])
            }
        }
    }
    console.log(`去重完成，总共${urlList.length}个节点，去重${urlList.length-finalURLs.length}个节点，剩余${finalURLs.length}个节点。`)
    fs.writeFileSync('./out',finalURLs.join('\n'))
}

run().then(async ()=>{
    if(config.enableMediaUnlockTest){
        console.log('即将开始流媒体测试...')
        await major.start()
    }
})
