const dns = require('dns').promises;
const geoip = require('geoip-lite');
const config = require('./config')

Resolver = dns.Resolver;
resolver = new Resolver();
resolver.setServers(config.dnsServers);

module.exports={
    async get(name){
        let domainReg = /[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+.?/g
        let ipReg = /((25[0-5])|(2[0-4]\d)|(1\d\d)|([1-9]\d)|\d)(\.((25[0-5])|(2[0-4]\d)|(1\d\d)|([1-9]\d)|\d)){3}/
        if(ipReg.test(name)){
            let geo = geoip.lookup(name);
            if(geo == null){
                        return 'UN'
                    }else{
                        return geo.country
                    }
        }else if(domainReg.test(name)){
            try{
                let address = await resolver.resolve4(name);
                if(address !== null){
                    let geo = geoip.lookup(address[0])
                    if(geo == null){
                        return 'UN'
                    }else{
                        return geo.country
                    }
                }else{
                    return 'UN'
                }
            }catch(e){
                return 'UN'
            }
        }else{
            return 'UN'
        }
    }
}
