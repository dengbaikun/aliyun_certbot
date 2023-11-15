import dns.resolver


def bytetostring(bv):
    sv = bv.decode()
    return sv


def getSPFKey(domain):
    spf = 'spf' + "." + domain
    return spf


def getSPFValue(domain):
    answersSPF = dns.resolver(getSPFKey(domain), 'TXT')
    for rdata in answersSPF:
        for txt_string in rdata.strings:
            txt_string = bytetostring(txt_string)
            return txt_string


def getTvalue(domain):
    answersTXT = dns.resolver(domain, 'TXT')
    for tdata in answersTXT:
        for txt_string in tdata.strings:
            txt_string = bytetostring(txt_string)
            return txt_string


def getMXvalue(domain):
    resultMX = dns.resolver(domain, 'MX')
    for exdata in resultMX:
        res = exdata.to_text()
        av = res.split(' ')
        return av[1]


def getAvalue(domain):
    resultA = dns.resolver(domain, 'A')
    for ip in resultA:
        return ip.to_text()
