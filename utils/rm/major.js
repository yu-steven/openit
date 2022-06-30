const Clash = require('clash-proxy');
const axios = require('axios');
const cp = require('child_process');
const path = require("path");
const fs = require("fs");
const parser = require('./parser')
const http = require("http");
const ProgressBar = require('./process-bar')
const config = require("./config");
const os = require("os");

let file = null;
let list = null;
let resList = [];
let finalList = [];
let clash;

async function startClash(){
    return new Promise((res,rej)=>{
        let subProgress = cp.spawn(getPath('clash'),['-f','./config.yml'],{cwd:path.join(process.cwd())})
        subProgress.stdout.on('data',(d)=>{
            let dataAfter = Buffer.from(d).toString('utf8')
            if(dataAfter.includes('level=info msg="RESTful API listening at: [::]:38888"')){
                res()
            }
        })
    })
}

async function convert(){
    const base64 = Buffer.from(file, 'utf-8').toString('base64');
    http.createServer(((req, res) => {
        res.writeHead(200);
        res.end(base64)
    })).listen(7867);
    let result = await axios('http://127.0.0.1:25500/sub?target=clash&remove_emoji=false&url=http%3A%2F%2F127.0.0.1%3A7867%2F');
    fs.writeFileSync('config.yml',result.data.replace('7890','6688').replace('7891','6699').replace('9090','38888'))
}

async function startSub(){
    return new Promise((res,rej)=>{
        let subProgress = cp.spawn(getPath('subconverter'),[],{cwd:path.join(process.cwd(),'./subconverter/'),shell:true})
        subProgress.stderr.on('data',(d)=>{
            let dataAfter = Buffer.from(d).toString('utf8')
            if(dataAfter.includes('Startup completed. Serving HTTP @ http://0.0.0.0:25500')){
                res()
            }
        })
    })
}

async function start(){
    file = fs.readFileSync('out',"utf-8")
    list = parser.read('out')
    await startSub();
    console.log('Subconverter start ok!!!');
    await convert();
    console.log('Convert ok!!!');
    await startClash();
    console.log('Clash ok!!!');
    clash = Clash({
        secret: '',
        api: 'http://127.0.0.1:38888'
    });
    await axios.patch('http://127.0.0.1:38888/configs',{"mode":"Global"});
    await test();
    await finish();
    process.exit(0);
}
async function test(){
    let pb = new ProgressBar('Progressing...', 50);
    let num = 0, total = list.length;
    for(let i=0;i<list.length;i++){
        let proxy = list[i];
        proxy.media = {netflix:'',bilibili:'',disney:''}
        await axios.put('http://127.0.0.1:38888/proxies/'+encodeURIComponent('🔰 节点选择'),{"name":proxy.name})
        //bilibili 港澳台
        try{
            let res = await axios.get('https://api.bilibili.com/pgc/player/web/playurl?avid=18281381&cid=29892777&qn=0&type=&otype=json&ep_id=183799&fourk=1&fnver=0&fnval=16&session=${randsession}&module=bangumi',{proxy: {
                    protocol: 'http',
                    host: '127.0.0.1',
                    port: 6688,
                }});
            if(res.data.code === 0){
                try{
                    let res2 = await axios.get('https://api.bilibili.com/pgc/player/web/playurl?avid=50762638&cid=100279344&qn=0&type=&otype=json&ep_id=268176&fourk=1&fnver=0&fnval=16&session=${randsession}&module=bangumi',{proxy: {
                            protocol: 'http',
                            host: '127.0.0.1',
                            port: 6688,
                        }});
                    if(res2.data.code === 0 ){
                        proxy.media.bilibili = 'B(T)'
                    }else{
                        proxy.media.bilibili = 'B'
                    }
                }catch(e){
                    proxy.media.bilibili = 'B'
                }
            }else{
                proxy.media.bilibili = ''
            }
        }catch(e){
            proxy.media.bilibili = ''
        }
        //netflix
        try{
            let res = await axios.get('https://www.netflix.com/title/81215567',{proxy: {
                protocol: 'http',
                    host: '127.0.0.1',
                    port: 6688,
            }})
            if(res.status === 200 || res.status === 301){
                proxy.media.netflix = 'N'
            }else{
                proxy.media.netflix = 'N(-)'
            }
        }catch (e){
            if(e.response){
                if(e.response.status === 404){
                    proxy.media.netflix = 'N(-)'
                }else{
                    proxy.media.netflix = ''
                }
            }
        }
        //disney
        try{
            let res = await axios.get('https://www.disneyplus.com',{proxy: {
                    protocol: 'http',
                    host: '127.0.0.1',
                    port: 6688,
                }})
            if(res.status === 200){
                proxy.media.disney = 'D'
            }else{
                proxy.media.disney = ''
            }
        }catch (e){
            proxy.media.disney = ''
        }
        resList.push(proxy)
        pb.render({ completed: i, total: total });
    }
    pb.render({ completed: total, total: total });
}

async function finish(){
    for(let i=0;i<resList.length;i++){
        let item = resList[i];
        let name = item.name.replace('{{result}}',item.media.netflix+item.media.bilibili+item.media.disney)
        switch (item.type){
            case 'vmess':
                item.data.ps = (name).toString();
                finalList.push('vmess://'+Buffer.from(JSON.stringify(item.data),'utf8').toString('base64'));
                break
            case 'trojan':
                finalList.push('trojan://'+item.data+'#'+(name).toString())
                break
            case 'ss':
                finalList.push('ss://'+item.data+'#'+(name).toString())
                break
            case 'ssr':
                finalList.push('ssr://'+Buffer.from(item.data.replace('{name}',Buffer.from((name).toString(),'utf8').toString('base64')),'utf8').toString('base64'));
                break
            case 'https':
                finalList.push('https://'+item.data+'#'+encodeURIComponent(name.toString()))
                break
            default:
                break
        }
    }
    fs.writeFileSync('output',finalList.join('\n'))
}

module.exports = {async start(){
        file = fs.readFileSync('out',"utf-8")
        list = parser.read('out')
        await startSub();
        console.log('Subconverter start ok!!!');
        await convert();
        console.log('Convert ok!!!');
        await startClash();
        console.log('Clash ok!!!');
        clash = Clash({
            secret: '',
            api: 'http://127.0.0.1:38888'
        });
        await axios.patch('http://127.0.0.1:38888/configs',{"mode":"Global"});
        await test();
        await finish();
        console.log(' ');
        console.log('Successfully finished.Output file:./output');
        process.exit(0);
    }}

function getPath(i){
    switch (i){
        case 'clash':
            if(os.platform() === 'win32'){
                if(os.arch() === 'ia32'){
                    return './clash/clash-windows-386'
                }else if(os.arch() === 'x64'){
                    return './clash/clash-windows-amd64'
                }else{
                    throw 'Your arch is not supported.Only support x86 and x64.'
                }
            }else if(os.platform() === 'linux'){
                if(os.arch() === 'ia32'){
                    return path.join(process.cwd()+'/clash/clash-linux-386')
                }else if(os.arch() === 'x64'){
                    return path.join(process.cwd()+'/clash/clash-linux-amd64')
                }else{
                    throw 'Your arch is not supported.Only support x86 and x64.'
                }
            }else{
                throw 'Your OS is not supported.Only support linux and windows.'
            }
        case 'subconverter':
            if(os.platform() === 'win32'){
                if(os.arch() === 'ia32'){
                    return './subconverter/subconverter-ia32.exe'
                }else if(os.arch() === 'x64'){
                    return './subconverter/subconverter-amd64.exe'
                }else{
                    throw 'Your arch is not supported.Only support x86 and x64.'
                }
            }else if(os.platform() === 'linux'){
                if(os.arch() === 'ia32'){
                    return path.join(process.cwd()+'/subconverter/subconverter-linux32')
                }else if(os.arch() === 'x64'){
                    return path.join(process.cwd()+'/subconverter/subconverter-linux64')
                }else{
                    throw 'Your arch is not supported.Only support x86 and x64.'
                }
            }else{
                throw 'Your OS is not supported.Only support linux and windows.'
            }
        default:
            return null
    }
}
