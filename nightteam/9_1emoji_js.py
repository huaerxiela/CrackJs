#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 11:30
# @Author  : qizai
# @File    : emoji_js.py
# @Software: PyCharm
"""desc: 考点是考验颜文字对JavaScript的混淆还原

解决方案：
    1、直接通过查看xhr断点，查看那个接口的堆栈调用来源，直接查看最后一个，发现是属于颜文字加密；
        那么继续往下一个堆栈调用点进行查看，这回发现是没有加密的代码，然后直接扣出来即可.
    2、直接复制颜文字加密混淆代码，在控制台粘贴，然后删除最后一个表情 “('_');” 然后回车，即可。
        或者直接删除这个表情后，使用 “toString()” 方法，就可以看到代码转换为明文字符串了。

9-1请问：
这一页帖子的总阅读量（列表页右侧的数字）是多少？

9-2请问：
第7个帖子（以1为起始）的HTML中id为content的部分中一共有多少个img标签？
"""

import requests
import execjs
import json
from scrapy import Selector

from nightteam.pwd import l_data


js_code = """
//定义navigator、window全局变量
navigator = {
    appCodeName: "Mozilla",
    appMinorVersion: "0",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    browserLanguage: "zh-CN",
    cookieEnabled: true,
    cpuClass: "x86",
    language: "zh-CN",
    maxTouchPoints: 0,
    msManipulationViewsEnabled: true,
    msMaxTouchPoints: 0,
    msPointerEnabled: true,
    onLine: true,
    platform: "Win32",
    pointerEnabled: true,
    product: "Gecko",
    systemLanguage: "zh-CN",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    userLanguage: "zh-CN",
    vendor: "",
    vendorSub: "",
    webdriver: false
}, window = this, window.navigator = navigator;

//网站自定义的md5函数
! function () {
    "use strict";

    function t(t) {
        t ? (f[0] = f[16] = f[1] = f[2] = f[3] = f[4] = f[5] = f[6] = f[7] = f[8] = f[9] = f[10] = f[11] = f[12] = f[13] =
            f[14] = f[15] = 0, this.blocks = f) : this.blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            this.h0 = 1732584193, this.h1 = 4023233417, this.h2 = 2562383102, this.h3 = 271733878, this.h4 = 3285377520,
            this.block = this.start = this.bytes = this.hBytes = 0, this.finalized = this.hashed = !1, this.first = !0
    }
    // var h = "object" == typeof window ? window : {},
    var h = window,
        //对比发现这里永远都是false
        // s = !h.JS_SHA1_NO_NODE_JS && "object" == typeof process && process.versions && process.versions.node;
        s = false;
    s && (h = global);
    //对比发现这里永远都是false
    // var i = !h.JS_SHA1_NO_COMMON_JS && "object" == typeof module && module.exports,
    var i = false,
        //对比发现这里永远都是false
        // e = "function" == typeof define && define.amd,
        e = false,
        r = "0123456789abcdef".split(""),
        o = [-2147483648, 8388608, 32768, 128],
        n = [24, 16, 8, 0],
        a = ["hex", "array", "digest", "arrayBuffer"],
        f = [],
        u = function (h) {
            return function (s) {
                return new t(!0).update(s)[h]()
            }
        },
        c = function () {
            var h = u("hex");
            s && (h = p(h)), h.create = function () {
                return new t
            }, h.update = function (t) {
                return h.create().update(t)
            };
            for (var i = 0; i < a.length; ++i) {
                var e = a[i];
                h[e] = u(e)
            }
            return h
        },
        p = function (t) {
            // var h = eval("require('crypto')"),
            var h = eval("require('D:/python3爬虫视频/JS逆向例子/luosimao/node_modules/crypto-js/crypto-js.js')"),
                s = eval("require('buffer').Buffer"),
                i = function (i) {
                    if ("string" == typeof i) return h.createHash("sha1").update(i, "utf8").digest("hex");
                    if (i.constructor === ArrayBuffer) i = new Uint8Array(i);
                    else if (void 0 === i.length) return t(i);
                    return h.createHash("sha1").update(new s(i)).digest("hex")
                };
            return i
        };
    t.prototype.update = function (t) {
        if (!this.finalized) {
            var s = "string" != typeof t;
            s && t.constructor === h.ArrayBuffer && (t = new Uint8Array(t));
            for (var i, e, r = 0, o = t.length || 0, a = this.blocks; r < o;) {
                if (this.hashed && (this.hashed = !1, a[0] = this.block, a[16] = a[1] = a[2] = a[3] = a[4] = a[5] =
                    a[6] = a[7] = a[8] = a[9] = a[10] = a[11] = a[12] = a[13] = a[14] = a[15] = 0), s)
                    for (e = this.start; r < o && e < 64; ++r) a[e >> 2] |= t[r] << n[3 & e++];
                else
                    for (e = this.start; r < o && e < 64; ++r)(i = t.charCodeAt(r)) < 128 ? a[e >> 2] |= i << n[3 &
                    e++] : i < 2048 ? (a[e >> 2] |= (192 | i >> 6) << n[3 & e++], a[e >> 2] |= (128 | 63 &
                        i) << n[3 & e++]) : i < 55296 || i >= 57344 ? (a[e >> 2] |= (224 | i >> 12) << n[3 & e++],
                            a[e >> 2] |= (128 | i >> 6 & 63) << n[3 & e++], a[e >> 2] |= (128 | 63 & i) << n[3 & e++]
                    ) : (i = 65536 + ((1023 & i) << 10 | 1023 & t.charCodeAt(++r)), a[e >> 2] |= (240 | i >> 18) <<
                        n[3 & e++], a[e >> 2] |= (128 | i >> 12 & 63) << n[3 & e++], a[e >> 2] |= (128 | i >> 6 &
                        63) << n[3 & e++], a[e >> 2] |= (128 | 63 & i) << n[3 & e++]);
                this.lastByteIndex = e, this.bytes += e - this.start, e >= 64 ? (this.block = a[16], this.start = e -
                    64, this.hash(), this.hashed = !0) : this.start = e
            }
            return this.bytes > 4294967295 && (this.hBytes += this.bytes / 4294967296 << 0, this.bytes = this.bytes %
                4294967296), this
        }
    }, t.prototype.finalize = function () {
        if (!this.finalized) {
            this.finalized = !0;
            var t = this.blocks,
                h = this.lastByteIndex;
            t[16] = this.block, t[h >> 2] |= o[3 & h], this.block = t[16], h >= 56 && (this.hashed || this.hash(),
                t[0] = this.block, t[16] = t[1] = t[2] = t[3] = t[4] = t[5] = t[6] = t[7] = t[8] = t[9] = t[10] =
                t[11] = t[12] = t[13] = t[14] = t[15] = 0), t[14] = this.hBytes << 3 | this.bytes >>> 29, t[15] =
                this.bytes << 3, this.hash()
        }
    }, t.prototype.hash = function () {
        var t, h, s = this.h0,
            i = this.h1,
            e = this.h2,
            r = this.h3,
            o = this.h4,
            n = this.blocks;
        for (t = 16; t < 80; ++t) h = n[t - 3] ^ n[t - 8] ^ n[t - 14] ^ n[t - 16], n[t] = h << 1 | h >>> 31;
        for (t = 0; t < 20; t += 5) s = (h = (i = (h = (e = (h = (r = (h = (o = (h = s << 5 | s >>> 27) + (i & e |
            ~i & r) + o + 1518500249 + n[t] << 0) << 5 | o >>> 27) + (s & (i = i << 30 |
            i >>> 2) | ~s & e) + r + 1518500249 + n[t + 1] << 0) << 5 | r >>> 27) + (o & (s = s <<
            30 | s >>> 2) | ~o & i) + e + 1518500249 + n[t + 2] << 0) << 5 | e >>> 27) + (r & (o = o <<
            30 | o >>> 2) | ~r & s) + i + 1518500249 + n[t + 3] << 0) << 5 | i >>> 27) + (e & (r = r << 30 | r >>>
            2) | ~e & o) + s + 1518500249 + n[t + 4] << 0, e = e << 30 | e >>> 2;
        for (; t < 40; t += 5) s = (h = (i = (h = (e = (h = (r = (h = (o = (h = s << 5 | s >>> 27) + (i ^ e ^ r) +
            o + 1859775393 + n[t] << 0) << 5 | o >>> 27) + (s ^ (i = i << 30 | i >>> 2) ^
            e) + r + 1859775393 + n[t + 1] << 0) << 5 | r >>> 27) + (o ^ (s = s << 30 | s >>>
            2) ^ i) + e + 1859775393 + n[t + 2] << 0) << 5 | e >>> 27) + (r ^ (o = o << 30 | o >>> 2) ^
            s) + i + 1859775393 + n[t + 3] << 0) << 5 | i >>> 27) + (e ^ (r = r << 30 | r >>> 2) ^ o) + s +
            1859775393 + n[t + 4] << 0, e = e << 30 | e >>> 2;
        for (; t < 60; t += 5) s = (h = (i = (h = (e = (h = (r = (h = (o = (h = s << 5 | s >>> 27) + (i & e | i & r |
            e & r) + o - 1894007588 + n[t] << 0) << 5 | o >>> 27) + (s & (i = i << 30 |
            i >>> 2) | s & e | i & e) + r - 1894007588 + n[t + 1] << 0) << 5 | r >>> 27) + (o &
            (s = s << 30 | s >>> 2) | o & i | s & i) + e - 1894007588 + n[t + 2] << 0) << 5 | e >>>
            27) + (r & (o = o << 30 | o >>> 2) | r & s | o & s) + i - 1894007588 + n[t + 3] << 0) << 5 | i >>>
            27) + (e & (r = r << 30 | r >>> 2) | e & o | r & o) + s - 1894007588 + n[t + 4] << 0, e = e << 30 |
            e >>> 2;
        for (; t < 80; t += 5) s = (h = (i = (h = (e = (h = (r = (h = (o = (h = s << 5 | s >>> 27) + (i ^ e ^ r) +
            o - 899497514 + n[t] << 0) << 5 | o >>> 27) + (s ^ (i = i << 30 | i >>> 2) ^
            e) + r - 899497514 + n[t + 1] << 0) << 5 | r >>> 27) + (o ^ (s = s << 30 | s >>> 2) ^
            i) + e - 899497514 + n[t + 2] << 0) << 5 | e >>> 27) + (r ^ (o = o << 30 | o >>> 2) ^ s) +
            i - 899497514 + n[t + 3] << 0) << 5 | i >>> 27) + (e ^ (r = r << 30 | r >>> 2) ^ o) + s - 899497514 +
            n[t + 4] << 0, e = e << 30 | e >>> 2;
        this.h0 = this.h0 + s << 0, this.h1 = this.h1 + i << 0, this.h2 = this.h2 + e << 0, this.h3 = this.h3 + r <<
            0, this.h4 = this.h4 + o << 0
    }, t.prototype.hex = function () {
        this.finalize();
        var t = this.h0,
            h = this.h1,
            s = this.h2,
            i = this.h3,
            e = this.h4;
        return r[t >> 28 & 15] + r[t >> 24 & 15] + r[t >> 20 & 15] + r[t >> 16 & 15] + r[t >> 12 & 15] + r[t >> 8 &
        15] + r[t >> 4 & 15] + r[15 & t] + r[h >> 28 & 15] + r[h >> 24 & 15] + r[h >> 20 & 15] + r[h >> 16 &
        15] + r[h >> 12 & 15] + r[h >> 8 & 15] + r[h >> 4 & 15] + r[15 & h] + r[s >> 28 & 15] + r[s >> 24 &
        15] + r[s >> 20 & 15] + r[s >> 16 & 15] + r[s >> 12 & 15] + r[s >> 8 & 15] + r[s >> 4 & 15] + r[15 &
        s] + r[i >> 28 & 15] + r[i >> 24 & 15] + r[i >> 20 & 15] + r[i >> 16 & 15] + r[i >> 12 & 15] + r[i >>
        8 & 15] + r[i >> 4 & 15] + r[15 & i] + r[e >> 28 & 15] + r[e >> 24 & 15] + r[e >> 20 & 15] + r[e >>
        16 & 15] + r[e >> 12 & 15] + r[e >> 8 & 15] + r[e >> 4 & 15] + r[15 & e]
    }, t.prototype.toString = t.prototype.hex, t.prototype.digest = function () {
        this.finalize();
        var t = this.h0,
            h = this.h1,
            s = this.h2,
            i = this.h3,
            e = this.h4;
        return [t >> 24 & 255, t >> 16 & 255, t >> 8 & 255, 255 & t, h >> 24 & 255, h >> 16 & 255, h >> 8 & 255,
            255 & h, s >> 24 & 255, s >> 16 & 255, s >> 8 & 255, 255 & s, i >> 24 & 255, i >> 16 & 255, i >> 8 &
            255, 255 & i, e >> 24 & 255, e >> 16 & 255, e >> 8 & 255, 255 & e]
    }, t.prototype.array = t.prototype.digest, t.prototype.arrayBuffer = function () {
        this.finalize();
        var t = new ArrayBuffer(20),
            h = new DataView(t);
        return h.setUint32(0, this.h0), h.setUint32(4, this.h1), h.setUint32(8, this.h2), h.setUint32(12, this.h3),
            h.setUint32(16, this.h4), t
    };
    var y = c();
    i ? module.exports = y : (h.md5 = y, e && define(function () {
        return y
    }))
}();

function Base64() {
    // private property
    _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    // public method for encoding
    this.encode = function (input) {
        var output = "";
        var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
        var i = 0;
        input = _utf8_encode(input);
        while (i < input.length) {
            chr1 = input.charCodeAt(i++);
            chr2 = input.charCodeAt(i++);
            chr3 = input.charCodeAt(i++);
            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;
            if (isNaN(chr2)) {
                enc3 = enc4 = 64;
            } else if (isNaN(chr3)) {
                enc4 = 64;
            }
            output = output +
                _keyStr.charAt(enc1) + _keyStr.charAt(enc2) +
                _keyStr.charAt(enc3) + _keyStr.charAt(enc4);
        }
        return output;
    };

    // public method for decoding
    this.decode = function (input) {
        var output = "";
        var chr1, chr2, chr3;
        var enc1, enc2, enc3, enc4;
        var i = 0;
        input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
        while (i < input.length) {
            enc1 = _keyStr.indexOf(input.charAt(i++));
            enc2 = _keyStr.indexOf(input.charAt(i++));
            enc3 = _keyStr.indexOf(input.charAt(i++));
            enc4 = _keyStr.indexOf(input.charAt(i++));
            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;
            output = output + String.fromCharCode(chr1);
            if (enc3 != 64) {
                output = output + String.fromCharCode(chr2);
            }
            if (enc4 != 64) {
                output = output + String.fromCharCode(chr3);
            }
        }
        output = _utf8_decode(output);
        return output;
    };

    // private method for UTF-8 encoding
    _utf8_encode = function (string) {
        var utftext = "";
        for (var n = 0; n < string.length; n++) {
            var c = string.charCodeAt(n);
            if (c < 128) {
                utftext += String.fromCharCode(c);
            } else if((c > 127) && (c < 2048)) {
                utftext += String.fromCharCode((c >> 6) | 192);
                utftext += String.fromCharCode((c & 63) | 128);
            } else {
                utftext += String.fromCharCode((c >> 12) | 224);
                utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                utftext += String.fromCharCode((c & 63) | 128);
            }

        }
        return utftext;
    };

    // private method for UTF-8 decoding
    _utf8_decode = function (utftext) {
        var string = "";
        var i = 0;
        var c = c1 = c2 = 0;
        while ( i < utftext.length ) {
            c = utftext.charCodeAt(i);
            if (c < 128) {
                string += String.fromCharCode(c);
                i++;
            } else if((c > 191) && (c < 224)) {
                c2 = utftext.charCodeAt(i+1);
                string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                i += 2;
            } else {
                c2 = utftext.charCodeAt(i+1);
                c3 = utftext.charCodeAt(i+2);
                string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                i += 3;
            }
        }
        return string;
    };
};

function uuid() {
    var s = [];
    var hexDigits = "0123456789abcdefghijklmnopqrstuvwxyz";
    for (var i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4";
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);
    s[8] = s[13] = s[18] = s[23] = "-";
    var uuid = s.join("");
    return uuid;
}

function getparam() {
    "use strict";
    var base64 = new Base64();
    var key = uuid();
    var time= (Math.floor(( new Date().getTime() + 10010) / 99)).toString();
    //var sign = md5(key + base64.encode(time));
    var sign = window.md5(key + base64.encode(time));
    var param = {
        "key": key,
        "time": time,
        "sign": sign
    };
    return param
};


function getparam_eval() {
    "use strict";
    var base64 = new Base64();
    var key = uuid();
    var time = (Math.floor((new Date().getTime() + 10010) / 99)).toString();
    console.log(key, time);
    //var sign = md5(key + base64.encode(time) + 'xianyucoder11');
    var sign = window.md5(key + base64.encode(time) + 'xianyucoder11');
    var param = {
        "key": key,
        "time": time,
        "sign": sign
    };
    return param
};
"""

ctx = execjs.compile(js_code)
param = ctx.call("getparam")

url = "http://js-crack-course-9-1.crawler-lab.com/list?key={}&time={}&sign={}"
# url = "http://js-crack-course-9-3.crawler-lab.com/list?key={}&time={}&sign={}"
# url = "http://js-crack-course-9-2.crawler-lab.com/list?key={}&time={}&sign={}"

header = {
    "Host": "api.crawler-lab.com",
    "Origin": "http://www.crawler-lab.com/",
    "Referer": "http://www.crawler-lab.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
}


cookie = {
    "__cfduid": "",
    # "crawlerlab_token": "",

}


def login():
    global cookie, header
    login_url = "http://api.crawler-lab.com/v1/login"
    try:
        sess = requests.session()
        _resp1 = sess.options(url=login_url, data=json.dumps(l_data))
        cookie.update(_resp1.cookies.get_dict())
        sess.headers.update(header)
        _resp2 = sess.post(url=login_url, data=json.dumps(l_data))  # , headers=header, allow_redirects=False
        cookie.update({"crawlerlab_token": _resp2.json()["data"]})
        print("自动登录成功")
    except:
        raise ValueError("自动登录失败")


login()

artical_url = "http://js-crack-course-9-1.crawler-lab.com/detail/{}?key={}&time={}&sign={}"
resp = requests.get(url=url.format(param["key"], param["time"], param["sign"]), cookies=cookie)


# 9-1请问：
# 这一页帖子的总阅读量（列表页右侧的数字）是多少？
def read_total_9_1():
    print(resp.text)
    total = 0
    average = 0
    for one in resp.json()["data"]:
        total += one["read_count"]

    item = {
        "total": total,
        "average": total // len(resp.json()["data"])
    }
    print("总阅读量和平均阅读量:{}".format(item))


# 9-2请问：
# 第7个帖子（以1为起始）的HTML中id为content的部分中一共有多少个img标签？  0个
def count_img():
    resp2 = requests.get(
        url=artical_url.format(resp.json()["data"][6]["id"], param["key"], param["time"], param["sign"]),
        cookies=cookie)
    print("计算“br”:{}".format(resp2.json()["data"]["content"].count("br")))


# 请问：
# 第5个帖子（以1为起始）的HTML中id为content的部分中一共有多少个数字2？ 0
def count_num_2():
    resp3 = requests.get(
        url=artical_url.format(resp.json()["data"][4]["id"], param["key"], param["time"], param["sign"]),
        cookies=cookie)
    print("计算“数字2”:{}".format(resp3.json()["data"]["content"].count("2")))


# 请问：
# 这一页的所有帖子的内容中（不含列表页）一共提到了多少次“夜幕团队”？475
def count_yemu():
    count_yemu = 0
    for i in resp.json()["data"]:
        resp4 = requests.get(
            url=artical_url.format(i["id"], param["key"], param["time"], param["sign"]),
            cookies=cookie)
        count_yemu += resp4.json()["data"]["content"].count("夜幕团队")
    print("计算“夜幕团队”:{}".format(count_yemu))


# 9-5请问：  eval func
# 这一页帖子的总阅读量（列表页右侧的数字）是多少？
def read_total_9_5():
    artical_url = "http://js-crack-course-9-4.crawler-lab.com/list?key={}&time={}&sign={}"
    total = 0
    param = ctx.call("getparam_eval")
    print(param)
    resp5 = requests.get(url=artical_url.format(param["key"], param["time"], param["sign"]), cookies=cookie)
    print(resp5.text)
    for i in resp5.json()["data"]:
        total += i["read_count"]
    print("计算“总阅读量”:{}".format(total))


def crack_12():
    """desc: 反爬思路：服务器通过检测是否为模拟器等，不是的话设置cookie，
    然后通过返回一个中间人链接，再看看这个返回的状态是否成功，而判断得出的，

    考点：这里当你在浏览器中进行debugger的时候，时间戳已经失效了，所以服务器会认为有人在搞事情，所以返回的status=0
    """
    global cookie
    list_url = "http://js-crack-course-12-1.crawler-lab.com/list"
    _resp = requests.get(url=list_url, cookies=cookie)
    print(_resp.text)  # {"status":0,"anti_spider":"/medium?ts=1584978741536"}
    pass


if __name__ == '__main__':
    # read_total_9_5()
    crack_12()
    pass

"""
function anonymous() {
    var nt0 = '772f34c7919c588750e0188f591d44a0';
    var nt1 = '77ea177fdb1cbcaca6861746f0f32c30';
    var nt2 = 'b0f462c457fe8dd37c6fb4919cc32235';
    var nt3 = '664f34cc0aa75122be2c003b028f360d';
    var nt4 = 'a0ffccd6ec25f3b1ccf96e1a119c98cf';
    var nt5 = '379e1da9968a60857292d40751000fdb';
    var nt6 = '6a959aace276a614bf2738f7ef4b25ac';
    var nt7 = '0d074dc231efeb5418612e34f1ae5017';
    var nt8 = 'f927cd5d68cd35c2f9ffd48a53ba78bc';
    var nt9 = 'b73777942209e27cad55f92eaeedc82f';
    (function () {
        document.cookie = 'NIGHTTEAM=31353834393731343739323738';
        document.cookie = 'NIGHTTEAM_ID=e5d1ef4adb72d22a618d9aa329919619';
        document.cookie = 'NIGHTTEAM_SIGN=cc77e4c3b2b73822850511f0a9e4a468';
        document.cookie = 'NIGHTTEAM_TOKEN=018ff92d599720fead773589ffdc0984';
        if (window.atob) {
            document.cookie = 'NIGHTTEAM_WINDOW=' + nt2
        }
        if ("undefined" != typeof screen && screen.width && screen.height) {
            document.cookie = 'NIGHTTEAM_UNIT=' + nt5
        }
        var switch_flag = true;

        function get_range_value(s) {
            var new_str = s.substring(20, 32) + "nightteam" + s.substring(0, 16) +
                "abcdefghijklmnopqrstuvwxyz0123456789";
            return new_str.substr(0, 32);
        }
        if ("undefined" == typeof navigator || navigator.userAgent === void 0 || navigator.userAgent.match(
                "HeadlessChrome") || navigator.userAgent.match("PhantomJS")) {
            switch_flag = false;
        }
        if (switch_flag) {
            document.cookie = 'NIGHTTEAM_SWITCH=' + get_range_value(nt4);
        }
    })();
    window.location.href = document.referrer;
}
"""