# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from io import StringIO
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import re,string,os
import os.path,sys,urllib,shutil,subprocess,pickle

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EnxavEQud9V68UhjMjyf.bTRBJ5l0hDXvNhmJN8y7NW.KE6KaGmAvkIm2mFu3uf5RVOiUc77c84TNM+axjlo/2Y=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="EnBH8iMQ1wBiSq6o7oCe.UJOQGba5Hxr9T2XzkAdOJG.kegCG4+fyYuommkT7WSTHYfvTNFbv/Qx5/zSq7tr0js=")
kk.loginResult()

ks = LINETCR.LINE()
ks.login(token="En7ye6xqksCfqwN3rxC9.zpO5Uq6Y6/yRRffssL2Swq.MSStspIW0RpoCsiMVKId7GnyQozMFjJVIk2KjdHbW8w=")
ks.loginResult()

kc = LINETCR.LINE()
kc.login(token="EnKsIrraiKMQNQNauXvc.nEAe5Ok20iJn2g9t413upa.ouv9zD0+byPhrxGYblJcKC0VE4+sFU4OVKVLvQKC7Ng=")
kc.loginResult()

ka = LINETCR.LINE()
ka.login(token="Enj9A11zchQ8UUgjeQU3.dpJoajM2Uk+80n6QZbxpmW.6PgbdpAccnkT+l5AIy+aszEM2D67Pwj44BlzVQfMpuI=")
ka.loginResult()

cl

with open('profileSave.pkl') as f:
    save1 = pickle.load(f)

print "loginわるいしずか"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""─┅═✥«わるいしずか»✥═┅─
[☆☆☆ঝ่ণধদู้  थ∅थथণ☆☆☆]
━━━━━━━━━━━━━━━━━━━━
❦✥COMMAND ADMIN✥❦
━━━━━━━━━━━━━━━━━━━━
➫[Id]
➧[Mid]
➫[All mid]
➧[Me]
➫[Me @]
➧[Mybot]
➫[Name Bot: (Text)]
➧[MeName:]
➫[BotStt:]
➧[MeStt:]
➫[ClearRoom]
➧[K1/K2/K3/]
➫[K1/K2/K3-]
➧[K1/K2/K3 gift
➫[Allgift]
➧[Group Id]
➫[TL:"Text"]
➧[Clock:]
➫[Up clock]
➧[Name:'text']
➫[Mic]:"mid"]
➧[ดึง @]
➫[Massage add:"text"]
➧[Add confirmasi]
➫[Comment set:"Text"]
➧[Comment check]
➫[Clock: on]
➧[Clock: off]
➫[Ban]:
➧[Unban]:
➫[Conban]
➧[Banlist]:
➫[Allgiftt]
➧[Test]
➫[Copy @]
➧[Save]
➫[Load]
➧[Spam on (Number) (Text)
➫[Spam off (Number) (Text)
➧[Gcreator]
➫[Covergroup]
➧[Tagall]
➫[Kicker]
➧[เงียบ]
➫[กริบ]
➧[Youtube]
➫[Helpv10]
━━━━━━━━━━━━━━━━━━━━
❦✥COMMAND SET✥❦
━━━━━━━━━━━━━━━━━━━━
➧[Contact: on/off]
➫[Auto join: on/off]
➧[Cancel Invite: 1 on/off]
➫[Auto share: on/off]
➧[Auto leave: on/off]
➫[Comment: on/off]
➧[Auto add: on/off]
➫[Auto like: on/off]║
━━━━━━━━━━━━━━━━━━━━
❦✥COMMAND GROUP✥❦
━━━━━━━━━━━━━━━━━━━━
➧[รี]
➫[Bot Run]
➧[Me Run]
➫[P1 @]
➧[AutoMG:Text]
➫[Pond]
➧[Wc]
➫[รายงาน]
➧[Speed]
➫[.sp]
➧[Ban"@Tag]
➫[Unban"@Tag]
➧[Urlon]:
➫[Urloff]:
➧[Url]:
➫[Ginfo]:
➧[In~"mid"]
➫[Say:"Text"]:
➧[Cancel]:
➫[Gn:"name"]:
➧[NK @tag]:
➫[Dead]
━━━━━━━━━━━━━━━━━━━━
"""
helpMessage2 ="""─┅═✥«わるいしずか»✥═┅─
═══════════════════════
❂➣[PROTECT: ON/OFF]:
❂➣[BLOCK URL: ON/OFF]:
❂➣[NAMELOCK: ON/OFF]:
❂➣[BLOCKINVITE: ON/OFF]:
═══════════════════════
"""
KAC = [cl,ki,kk,ks,kc,ka]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
kimid = kk.getProfile().mid
ki2mid = ks.getProfile().mid
Cmid = kc.getProfile().mid
Emid = ka.getProfile().mid
admin = ["u9ead3fb91359d0f9c1adaadd30647973"]
me = cl.getProfile().mid
bot1 = cl.getProfile().mid
main = cl.getProfile().mid
kicker1 = ki.getProfile().mid
bots = me + kicker1
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []

admins = ["u9ead3fb91359d0f9c1adaadd30647973"]
Rx5 = ["u9ead3fb91359d0f9c1adaadd30647973"]
Rx4 = ["u9ead3fb91359d0f9c1adaadd30647973"]
Rx3 = ["u9ead3fb91359d0f9c1adaadd30647973"]
Rx2 = ["u9ead3fb91359d0f9c1adaadd30647973"]
Rx1 = ["u9ead3fb91359d0f9c1adaadd30647973"]
Administrator = admins + Rx5 + Rx4 + Rx3 + Rx2 + Rx1
AS = Rx2 + Rx1 + Rx3 + Rx4 + Rx5
adminsA = admins + Rx3 + Rx5

omikuzi = ["大吉","中吉","小吉","末吉","大凶","凄1�7"]

wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""
  ╔════♪•●♥●•♪════╗
─┅═✥«わるいしずか»✥═┅─
  ╚════♪•●♥●•♪════╝
""",
    "lang":"JP",
    "comment":"Auto like By.http://line.me/ti/p/~300760.",
    "likeOn":False,
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "dblacklist":False
}

wait2 = {
	'readMember':{},
	'readPoint':{},
	'ROM':{},
	'setTime':{}
    }

setTime = {}
setTime = wait2["setTime"]

res = {
    'num':{},
    'us':{},
    'au':{},
}

save1 = {
    "Saved":False,
    "displayName":"",
    "statusMessage":"",
    "pictureStatus":""
}

def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    kk.cancelGroupInvitation(op.param1, matched_list)
                    ks.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 17:
            if mid in op.param3:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user flushing is complete")

        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = ks.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki.getGroup(op.param1)
				    except:
					try:
                                            G = kc.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    ks.updateGroup(G)
                                except:
                                    try:
                                        kc.updateGroup(G)
                                    except:
                                        try:
                                            ka.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            koutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group name lock")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wekawekaweka 􀜁􀅔Har Har􏿿")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
		if op.type == 17:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 32:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 32:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 25:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 25:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.param3 == "4":
            if op.param1 in protecturl:
				group = cl.getGroup(op.param1)
				if group.preventJoinByTicket == False:
					group.preventJoinByTicket = True
					cl.updateGroup(group)
					cl.sendText(op.param1,"URL can not be changed")
					ki.kickoutFromGroup(op.param1,[op.param2])
					time.sleep(0.01)
					kk.kickoutFromGroup(op.param1,[op.param2])
					time.sleep(0.01)
					ks.kickoutFromGroup(op.param1,[op.param2])
					time.sleep(0.01)
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
				else:
					pass
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u7c6053763344625bb1159355020c5c27":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ki.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kk.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ks.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X = ki.getGroup(list_[1])
                            X = kk.getGroup(list_[1])
                            X = ks.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                            ki.updateGroup(X)
                            kk.updateGroup(X)
                            ks.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1002)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"It's included in a blacklist already〄1�7")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"I decided not to make a comment〄1�7")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"It was eliminated from a blacklist〄1�7")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It isn't included in a blacklist〄1�7")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"It's included in a blacklist already.〄1�7")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"It was added to the blacklist.〄1�7")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"It was eliminated from a blacklist〄1�7")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It isn't included in a blacklist〄1�7")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["help","Help","HELP"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Help2","Key","KEY"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage2)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn:"in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("ki1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("ki1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("ki2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("ki2 gn ","")
                    ki2.updateGroup(X)
                else:
                    ki2.sendText(msg.to,"It can't be used besides the group.")
            elif "kick:" in msg.text:
                midd = msg.text.replace("kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif msg.text in ["Invite"]:
                if msg.from_ in admin:
                 wait["wblack"] = True
                 cl.sendText(msg.to,"send contact")
            elif "เชิญ " in msg.text:
                midd = msg.text.replace("เชิญ ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "In~" in msg.text:
                midd = msg.text.replace("In~","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "In1~" in msg.text:
                midd = msg.text.replace("In1~","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "In2~" in msg.text:
                midd = msg.text.replace("In2~","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "In3~" in msg.text:
                midd = msg.text.replace("In3~","")
                ks.findAndAddContactsByMid(midd)
                ks.inviteIntoGroup(msg.to,[midd])
            elif "In4~" in msg.text:
                midd = msg.text.replace("In4~","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif "In5~" in msg.text:
                midd = msg.text.replace("In5~","")
                ka.findAndAddContactsByMid(midd)
                ka.inviteIntoGroup(msg.to,[midd])
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "K1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif "K2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                kk.sendMessage(msg)
            elif "K3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ks.sendMessage(msg)
            elif "K4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
            elif "K5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
            elif "Mybot" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Cmid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Emid}
                cl.sendMessage(msg)
            elif msg.text in ["เมีย"]:
                msg.contentType = 13
                cl.sendText(msg.to, "นี่เมียมึงจำไวไอ้ดรีม")
                msg.contentMetadata = {'mid': 'u3fc94807030884893bd7004d674087d6'}
                cl.sendMessage(msg)
            elif msg.text in ["ผัว"]:
                msg.contentType = 13
                cl.sendText(msg.to, "นี่ผัวมึงจำไวไอ้ดรีม")
                msg.contentMetadata = {'mid': 'uec20f72318dfbe36f1f1f6381af8ad8f'}
                cl.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ks.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["愛のプレゼンツ1�7","K5 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ka.sendMessage(msg)
            elif msg.text in ["Allgift","All Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                ks.sendMessage(msg)
                kc.sendMessage(msg)
                ka.sendMessage(msg)

            elif msg.text in ["ยกเริก","Cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"There isn't an invited person〄1�7")
                        else:
                            cl.sendText(msg.to,"you Sato face-like person absence〄1�7")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group〄1�7")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")

            elif msg.text in ["K1 cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"There isn't an invited person〄1�7")
                        else:
                            ki.sendText(msg.to,"you Sato face-like person absence〄1�7")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group〄1�7")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")

            elif "Comment set:" in msg.text:
                c = msg.text.replace("Comment set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Error")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"It was changed。\n\n" + c)
            elif msg.text in ["Comment check"]:
                cl.sendText(msg.to,"An automatic comment is established as follows at present。\n\n" + str(wait["comment"]))
            elif msg.text in ["コメント:オン","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done〄1�7")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already〄1�7")
            elif msg.text in ["コメント:オフ","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done〄1�7")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already〄1�7")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Block url:on"]:
                protecturl.append(msg.to)
                cl.sendText(msg.to,"ƊƠƝЄ")
            elif msg.text in ["Block url:off"]:
                if msg.from_ in Administrator:
                    protecturl.remove(msg.to)
                    cl.sendText(msg.to,"ƛԼԼƠƜЄƊ")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ")
            elif msg.text in ["Urlon"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƲƦԼ ƠƝ ƛԼƦЄƛƊƳ〄1�7")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƲƦԼ。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif msg.text in ["Urloff"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƲƦԼ ƇԼƠƧЄƊ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƲƦԼ。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif msg.text in ["กลุ่ม","Ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "ปิดอยู่"
                        else:
                            u = "เปิดอยู่"
                        cl.sendText(msg.to,"[􀜁􀆍Detective􏿿กลุ่ม􀜁􀆍Detective􏿿]\n" + str(ginfo.name) + "\n\n[􀬁􀆃lollipop􏿿ไอดีกลุ่ม􀬁􀆃lollipop􏿿]\n" + msg.to + "\n\n[􀄃􀈡face with flower􏿿ผู้สร้างกลุ่ม􀄃􀈡face with flower􏿿]\n" + gCreator + "\n\n[􀬁􀆐maple leaf􏿿รูปโปรไฟล์กลุ่ม􀬁􀆐maple leaf􏿿]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nสมาชิก:" + str(len(ginfo.members)) + " ท่าน\nเชิญ:" + sinvitee + " ท่าน\nURL:" + u + "")
                    else:
                        cl.sendText(msg.to,"[名字]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[小组的作成者]\n" + gCreator + "\n[小组图标]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mid" == msg. text:
                cl.sendText(msg.to,mid)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,kimid)
                ks.sendText(msg.to,ki2mid)
                kc.sendText(msg.to,Cmid)
                ka.sendText(msg.to,Emid)
            elif "5555" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "ควย" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "105",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "ดีครับ" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                ks.sendMessage(msg)
                kc.sendMessage(msg)
                ka.sendMessage(msg)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "MeName:" in msg.text:
                string = msg.text.replace("MeName:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。")
            elif "Name Bot:" in msg.text:
                string = msg.text.replace("Name Bot:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    kk.updateProfile(profile)
                    ks.updateProfile(profile)
                    kc.updateProfile(profile)
                    ka.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + "。")
#---------------------------------------------------------
            elif "K1 name " in msg.text:
                string = msg.text.replace("K1 name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"The name " + string + "。")
#--------------------------------------------------------
            elif "K2 name " in msg.text:
                string = msg.text.replace("K2 name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"The name " + string + "。")
#--------------------------------------------------------
            elif "K3 name " in msg.text:
                string = msg.text.replace("K3 name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"The name " + string + "。")
#--------------------------------------------------------
            elif "K4 name " in msg.text:
                string = msg.text.replace("K4 name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"The name " + string + "。")
#--------------------------------------------------------
            elif "K5 name " in msg.text:
                string = msg.text.replace("K5 name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ka.updateProfile(profile)
                    ka.sendText(msg.to,"The name " + string + "。")
#--------------------------------------------------------
            elif "BotStt:" in msg.text:
                string = msg.text.replace("BotStt:","")
                if len(string.decode('utf-8')) <= 500:
                    profile_B = ki.getProfile()
                    profile_B.statusMessage = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"statusMessage::" + string + "。")
                    profile_C = kk.getProfile()
                    profile_C.statusMessage = string
                    kk.updateProfile(profile_C)
                    kk.sendText(msg.to,"statusMessage::" + string + "。")
                    profile_C = ks.getProfile()
                    profile_C.statusMessage = string
                    ks.updateProfile(profile_C)
                    ks.sendText(msg.to,"statusMessage::" + string + "。")
                    profile_C = kc.getProfile()
                    profile_C.statusMessage = string
                    kc.updateProfile(profile_C)
                    kc.sendText(msg.to,"statusMessage::" + string + "。")
                    profile_C = ka.getProfile()
                    profile_C.statusMessage = string
                    ka.updateProfile(profile_C)
                    ka.sendText(msg.to,"statusMessage::" + string + "。")
#--------------------------------------------------------
            elif "MeStt:" in msg.text:
                string = msg.text.replace("MeStt:","")
                if len(string.decode('utf-8')) <= 500:
                    profile_B = cl.getProfile()
                    profile_B.statusMessage = string
                    cl.updateProfile(profile_B)
                    cl.sendText(msg.to,"statusMessage::" + string + "。")
#--------------------------------------------------------
            elif "Mic:" in msg.text:
                mmid = msg.text.replace("Mic:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Contact:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƇƠƝƬƛƇƬ ƠƝ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ。")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƝ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ。")
            elif msg.text in ["Contact:off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƇƠƝƬƛƇƬ ƠƑƑ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ。")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƑƑ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ。")
            elif msg.text in ["Auto join:on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʆƠƖƝ ƠƝ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ。")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƝ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ。")
            elif msg.text in ["Auto join:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʆƠƖƝ ƠƑƑ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ。")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƑƑ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ。")
            elif "Cancel invite:" in msg.text:
                try:
                    strnum = msg.text.replace("Cancel invite:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refusal was turned off。\non, please designate and send the number of people.")
                        else:
                            cl.sendText(msg.to,"number of people")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"ปฏิเสทคำเชิญที่มีสมาชิกต่ำกว่า􀄃􀉘pointing right􏿿"+ strnum +"คน􀜁􀄊Shut Up􏿿")
                        else:
                            cl.sendText(msg.to,strnum + "Self- you for below shinin-like small.")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"The price is wrong。")
                    else:
                        cl.sendText(msg.to,"key is wrong。")
            elif msg.text in ["Auto leave:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ԼЄƛƔЄ ƠƝ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ。")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƝ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ。")
            elif msg.text in ["Auto leave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ԼЄƛƔЄ ƠƑƑ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ。")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƜƛƧ ƬƲƦƝЄƊ ƠƑƑ。")
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ。")
            elif msg.text in ["共有:オン","共有：オン","Auto share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["共有:オフ","共有：オフ","Auto share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Already。")
            elif "Set" == msg.text:
                md = ""
                if wait["contact"] == True: md+="✔ Contact → on \n"
                else: md+="✖ Contact → off \n"
                if wait["autoJoin"] == True: md+="✔  Auto join → on \n"
                else: md +="✖ Auto join → off \n"
                if wait["autoCancel"]["on"] == True:md+="✔ Cancel Invite → " + str(wait["autoCancel"]["members"]) + " \n"
                else: md+= "✖ Cancel Invite → off \n"
                if wait["leaveRoom"] == True: md+="✔ Auto leave → on \n"
                else: md+="✖ Auto leave → off \n"
                if wait["timeline"] == True: md+="✔ Auto Share → on \n"
                else:md+="✖ Auto Share → off \n"
                if wait["commentOn"] == True: md+="✔ Comment → on \n"
                else:md+="✖ Comment → off \n"
                if wait["autoAdd"] == True: md+="✔ Auto add → on \n"
                else:md+="✖ Auto add → off \n"
                if wait["likeOn"] == True: md+="✔ Auto like → on \n"
                else:md+="✖ Auto like → off \n"
                cl.sendText(msg.to,md)
            elif msg.text in ["Group id","group id"]:
                gid = cl.getGroupIdsJoined()
                g = ""
                for i in gid:
                    g += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,g)
            elif msg.text in ["ClearRoom","ลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Completion.")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Completion.")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Auto like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")

            elif msg.text in ["Auto add:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It's on already。")
                    else:
                        cl.sendText(msg.to,"on already。")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It was turned on。")
                    else:
                        cl.sendText(msg.to,"Turned on。")
            elif msg.text in ["Auto add:off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It's off already。")
                    else:
                        cl.sendText(msg.to,"off already。")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It was turned off。")
                    else:
                        cl.sendText(msg.to,"Turned off。")
            elif "Massage add:" in msg.text:
                wait["message"] = msg.text.replace("Massage add:","")
                cl.sendText(msg.to,"The message was changed。")
            elif "Auto addition→" in msg.text:
                wait["message"] = msg.text.replace("Auto addition→","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"The message was changed。")
                else:
                    cl.sendText(msg.to,"was change already。")
            elif msg.text in ["Add confirmasi","自動追加問候語確認"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,".automatic message is established as follows。\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"One  of weeds on the surface below the self- additional breath image。\n\n" + wait["message"])
            elif msg.text in ["CHANGE","言語變更"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"ƇƠƲƝƬƦƳ ԼƛƝƓƲƛƓЄ ƊƲƦƖƝƓ ƛ ƇHƛƝƓЄ。")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,". The language was made English。")
            elif msg.text in ["Url"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƇƛƝ'Ƭ ƁЄ ƲƧЄƊ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ.。")
                    else:
                        cl.sendText(msg.to,"ƖMƤƠƧƧƖƁԼЄ ƲƧЄ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ. ")
            elif "gurl:" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl:","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ƖƬ ƇƛƝ'Ƭ ƁЄ ƲƧЄƊ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ。")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = ki.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƇƛƝ ƝƠƬ ƁЄ ƲƧЄƊ ƠƲƬƧƖƊЄ ƬHЄ ƓƦƠƲƤ")
                    else:
                        cl.sendText(msg.to,"ƝƠƬ ƑƠƦ ƲƧЄ ԼЄƧƧ ƬHƛƝ ƓƦƠƲƤ")
            elif msg.text in ["cb"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send the phone number of the person who adds it to the blacklist.")
            elif msg.text in ["cbd"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send the phone number of the person who adds it to the blacklist.")
            elif msg.text in ["cbc"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"There isn't a person made a blacklist。")
                else:
                    cl.sendText(msg.to,"Below is a blacklist。")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Clock:on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"It's on already。")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was turned on")
            elif msg.text in ["Clock:off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"It's off already.。")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"It was tuned off。")
            elif "Clock:" in msg.text:
                n = msg.text.replace("Clock:","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"Last name clock。")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"It was renewed\n\n" + n)
            elif msg.text in ["Up clock"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was renewed。")
                else:
                    cl.sendText(msg.to,"Please turn on a name clock.。")
            elif "Tagall" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)
            elif msg.text in ["Pond"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            elif msg.text in ["K1 join"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["K2 join"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["K3 join"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ks.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(msg.to)

            elif msg.text in ["Bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					ki.leaveGroup(msg.to)
					kk.leaveGroup(msg.to)
					ks.leaveGroup(msg.to)
					kc.leaveGroup(msg.to)
					ka.leaveGroup(msg.to)
                except:
                     pass
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kc.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kc.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    gs.preventJoinByTicket = True
                                    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                                    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif msg.text.lower() == 'รายงาน':
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName
                kk.sendText(msg.to, text)
                profile = ks.getProfile()
                text = profile.displayName
                ks.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName
                kc.sendText(msg.to, text)
                profile = ka.getProfile()
                text = profile.displayName
                ka.sendText(msg.to, text)
#-----------------------------------------------------------
            elif "Kick" in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                           cl.kickoutFromGroup(msg.to,[target])
                    else:
                        pass
            elif "K1-" in msg.text:
				OWN = "u9fee8ed8e746cc6134346e37f672cbb3"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K1-","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ki.kickoutFromGroup(msg.to, [target])
							except:
									ki.kickoutFromGroup(msg.to, [target])
									pass
            elif "K2-" in msg.text:
				OWN = "u49e3ce7e546c60d2f5a38afe264fd1e9"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K2-","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									kk.kickoutFromGroup(msg.to, [target])
							except:
									kk.kickoutFromGroup(msg.to, [target])
									pass

            elif "K3 fuck" in msg.text:
				OWN = "uc903012b76390e088c772b21062a3b20"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("K3 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ks.kickoutFromGroup(msg.to, [target])
							except:
									ks.kickoutFromGroup(msg.to, [target])
									pass
            elif "Ban " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                       ban0 = msg.text.replace("Ban ","")
                       ban1 = ban0.lstrip()
                       ban2 = ban1.replace("@","")
                       ban3 = ban2.rstrip()
                       _name = ban3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
                           pass
                       else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")
                                except:
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")
#-----------------------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#-----------------------------------------------------------
            elif "Unban " in msg.text:
               if msg.toType == 2:
                  if msg.from_ in admin:
                       unb0 = msg.text.replace("Unban ","")
                       unb1 = unb0.lstrip()
                       unb2 = unb1.replace("@","")
                       unb3 = unb2.rstrip()
                       x_name = unb3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if x_name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"ƲƧЄƦ ƊƠЄƧ ƝƠƬ ЄҲƖƧƬ")
                           pass
                       else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")
                                except:
                                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ ƧƲƇƇЄƧƧ")

#-----------------------------------------------------------
            elif "Protect:on" == msg.text:
				if msg.to in protection:
					cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
				else:
					wait["pnharfbot"][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pnharfbot.json','w','utf-8')
					json.dump(wait["pnharfbot"], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ")
            elif "Protect:off" == msg.text:
				try:
					if msg.from_ in Administrator:
						protection.remove(msg.to)
						cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ")
					else:
						cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
				except:
					pass
            elif "Namelock:on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")

            elif "Blockinvite:on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƝ")
            elif "Blockinvite:off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƑƑ")
				except:
					pass
#-----------------------------------------------------------
            elif "Helpv10" in msg.text:
                cl.sendText(msg.to,"""
✔คำสั่ง เช็คตั๋ว
Siriv10:tickets
Siriv10:招待回数
✔คำสั่ง ตั้งค่าดูคนอ่าน
SetLastPoint
既読ポイント設定
✔คำสั่ง เช็คจำนวนคนอ่าน
ViewLastseen
友情破壊
✔คำสั่ง ล็อครูป
Set:iconlock:on
設定:アイコンロック:オン
✔คำสั่ง ล็อคชื่อกลุ่ม
Set:changenamelock:on
設定:グループ名ロック:オン
✔คำสั่ง ล็อคหัวห้อง(แอดมิน)
Set:ownerlock:on
設定:作成者ロック:オン
✔คำสั่ง เชิญบอทออก
Siriv10:bye
✔คำสั่ง เรียกบอทกลับ
Siriv10:reinvite
siriv10:再招待
✔คำสั่ง เปิดการทำงานบอท
Siriv10:on
siriv10:オン
✔คำสั่ง ปิดการทำงานบอท
Siriv10:off
siriv10:オフ
✔คำสั่ง เปิดเชิญ
設定:招待拒否:オフ
✔คำสั่ง ปิดเชิญ
設定:招待拒否:オン
✔คำสั่ง เปิดลิ้ง
siriv10: Inviteurl
Siriv10:招待URL生成
✔คำสั่ง ปิดลิ้ง
 siriv10: DenyInviteURL
Siriv10:招待URL拒否
✔คำสั่ง ยกเลิกค้างเชิญ (สั่ง 2 ครั้ง)
Siriv10:cancellnvite
Siriv10:招待キャンセル
✔คำสั่ง สร้างห้องสำรอง
Siriv10:login
✔คำสั่ง บันทึกห้อง
Siriv10:backup
✔คำสั่ง เช็คบันชี
set:deletelist
✔คำสั่ง คัดลอกบันชี
set:copyownlist
✔คำสั่ง เช็คดารตั้งค่า
set:status
設定:確認
Set:confirmation
✔คำสั่ง ปลดล็อคหัวห้องว่าง
Siriv10:forcerelease
✔คำสั่ง ขอแอดมิน คนใหม่
set:changeowner
siriv10:強制解除
✔คำสั่ง คิกเกอ มาเตะ (คำสั่ง+ข้อมูล)
設定:ブラック追加
✔คำสั่ง เรียกคิกเกอ มาเตะ
Siriv10:追い出し
✔คำสั่ง เพิ่มบันชีดำ
set:addblacklist
✔คำสั่ง เพิ่มบันชีขาว
set:addwhitelist
✔คำสั่ง เพิ่มแอดสำรอง (คำสั่ง+ข้อมูล)
設定:予備作
✔คำสั่ง สลับแอด ให้สำรอง เป็นตัวจริง
設定:作者交換
✔คำสั่ง เช็คแอดมินหลัก
Siriv10:groupcreator
Siriv10:グル作成者
✔คำสั่ง ป้องกันคนรันสติ๋กเกอร์
Set: StampLimitatio:on
➖➖➖➖➖➖➖➖➖➖
✔คำสั่ง ชุดล็อคห้อง
設定:らっこさん:on
設定:スタンプ規制:on
Siriv10:招待URL拒否
Set:changenamelock:on
Set:ownerlock:on
Set:blockinvite:on
Set:iconlock:on
Siriv10:groupcreator
➖➖➖➖➖➖➖➖➖➖
✔คำสั่ง ขอ คท บอท v10
Siriv9:contact
✔คำสั่ง ขอ คท บอทเสริม
Siriv10:追加アカウント
✔คำสั่ง ขอบอท L
Ralu:contact
✔คำสั่ง ขอบท นก
Pen:contact
""")
#-----------------------------------------------------------
            elif "Spam @" in msg.text:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Spam Start")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค���าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop����")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สว���สดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ����􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่า���บบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop����")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ki.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kk.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       ks.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")
                       kc.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop����")
                       ka.sendText(g.mid,"สวัสดีค่าบบบ􀬁􀆃lollipop􏿿")

                       cl.sendText(msg.to, "Ok success")
                       print "Done spam"
#----------------------------------------------------------
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
#----------------------------------------------------------
            elif msg.text in ["Test"]:
                ki.sendText(msg.to,"●")
                ki.sendText(msg.to,"●●")
                ki.sendText(msg.to,"●●●")
                ki.sendText(msg.to,"●●●●")
                ki.sendText(msg.to,"●●●●●")
                ki.sendText(msg.to,"●●●●●●")
                kk.sendText(msg.to,"●●●●●●●")
                kk.sendText(msg.to,"●●●●●●●●")
                kk.sendText(msg.to,"●●●●●●●●●")
                kk.sendText(msg.to,"●●●●●●●●●●")
                kk.sendText(msg.to,"●●●●●●●●●●●")
                kk.sendText(msg.to,"●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●●●●●")
                ks.sendText(msg.to,"●●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●")
                kc.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●●")
                ka.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●●●")
                ka.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●●●●")
                ka.sendText(msg.to,"●Bot «わるいしずか»●")
                cl.sendText(msg.to,"●( ^^)人(^^ )●")
#----------------------------------------------------------
            elif msg.text == "เงียบ":
              if msg.from_ in admin:
                cl.sendText(msg.to, ".......")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text == "กริบ":
              if msg.from_ in admin:
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                print rom
	                chiya += rom[1] + "\n"

	            cl.sendText(msg.to, " %s\n\n\nคนแอบอ่านขี้หี􀜁􀆍Detective􏿿\n(๑و•̀ω•́)و\n%s\n\nเวลาตั้งจุดอ่านล่าสุด􀬁􀆀hourglass 1􏿿\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
	          else:
	            cl.sendText(msg.to, "Sider ga bisa di read cek setpoint dulu bego tinggal ketik\nSetlastpoint\nkalo mau liat sider ketik\nViewlastseen")
#-----------------------------------------------------------speed
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"ƤԼЄƛƧЄ ƧЄƝƊ ƬHЄ ƛƇƇƠƲƝƬ ƦЄƓƖƧƬЄƦЄƊ ƜƖƬH ƛ ƁԼƛƇƘԼƖƧƬ。")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"ƤԼЄƛƧЄ ƧЄƝƊ ƬHЄ ƛƇƇƠƲƝƬ ƦЄƓƖƧƬЄƦЄƊ ƜƖƬH ƛ ƁԼƛƇƘԼƖƧƬ。")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"ƬHЄƦЄ ƖƧƝ'Ƭ ƛ ƤЄƦƧƠƝ MƛƊЄ ƛ ƁԼƛƇƘԼƖƧƬ.。")
                else:
                    cl.sendText(msg.to,"ƁЄԼƠƜ ƖƧ ƛ ƁԼƛƇƘԼƖƧƬ。")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Blist"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "・" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "But it's a blacklist.。")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"There wasn't a blacklist user。")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,ks,kc,ka]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif msg.text in ["ลั่น"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"อุ้ยไปหมดเลย")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = '•─ ͜͡ᴛᴇᴀᴍ ᴛᴇsᴛ ʙᴏᴛ͜͡ ─•'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"ЄƦƦƠƦ")
            elif "Album making" in msg.text:
                try:
                    albumtags = msg.text.replace("Album making","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "An album was made。")
                except:
                    cl.sendText(msg.to,"ЄƦƦƠƦ")
#-----------------------------------------------
            elif msg.text in ["Cb","Clearban"]:
                                wait["blacklist"] = {}
                                cl.sendText(msg.to,"ล้างบัญชีดำ")
#-----------------------------------------------
            elif "vdo:" in msg.text.lower():
                if msg.toType == 2:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
#-----------------------------------------------
            elif msg.text.lower() == 'รี':
                if msg.toType == 2:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        ki.sendText(msg.to,"STAETING...")
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ka.sendText(msg.to,"BOOT...")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "REBOOT"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

#-----------------------------------------------
            elif "Me @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Me @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass
#-----------------------------------------------
            elif "Say " in msg.text:
                string = msg.text.replace("Say ","")
                if len(string.decode('utf-8')) <= 50:
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
#-----------------------------------------------
            elif msg.text in ["Group creator","Gc","Gcreator","gCreator"]:
                ginfo = cl.getGroup(msg.to)
                gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"""Creator Group""")

            elif msg.text in ["Gcreator:inv","เชิญเเอทมิน"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kc.kickuotFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kc.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    gs.preventJoinByTicket = True
                                    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                                    cl.updateGroup(gs)
#-----------------------------------------------
            elif 'Youtube:' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube:', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
#-----------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                text = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (text+"\n")
                if txt[1] == "on":
                    if jmlh <= 1000:
                        for x in range(jmlh):
                            cl.sendText(msg.to, text)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
#-----------------------------------------------
            elif "Steal dp @" in msg.text:
                nama = msg.text.replace("Steal dp @","")
                target = nama.rstrip(' ')
                van = cl.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        midddd = cl.getContact(linedev.mid)
                        PATH = "http://dl.profile.line-cdn.net/" + midddd.pictureStatus
                    cl.sendImageWithURL(msg.to,path)
#-----------------------------------------------
            elif "Steal home @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to,path)
                        except:
                            pass
                print "[Command]dp executed"
#-----------------------------------------------
            elif msg.text in ["Protect all:on","Ext all on","Satan on#"]:
                        cl.sendText(msg.to,"ป้องกันทุกรูปแบบ􀜁􀄊Shut Up􏿿")
                        cl.sendText(msg.to,"Block url:on")
                        cl.sendText(msg.to,"Protect:on")
                        cl.sendText(msg.to,"Namelock:on")
                        cl.sendText(msg.to,"Blockinvite:on")


            elif msg.text in ["Protect all:off","Ext all off","Satan off#"]:
                        cl.sendText(msg.to,"ปิดการป้องกันทั้งหมด")
                        cl.sendText(msg.to,"Block url:off")
                        cl.sendText(msg.to,"Protect:off")
                        cl.sendText(msg.to,"Namelock:off")
                        cl.sendText(msg.to,"Blockinvite:off")
#-----------------------------------------------
            elif msg.text.lower() == 'wc':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#-----------------------------------------------
            elif "P1 " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[profilePicture]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[homePicture]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[homePicture]\n" + str(cu))
#-----------------------------------------------
            elif "AutoMG:" in msg.text:
                bctxt = msg.text.replace("AutoMG:", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
#-----------------------------------------------
            elif "ดึง " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"In~" + key1)
            elif "Mc: " in msg.text:
                mmid = msg.text.replace("Mc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kk.sendMessage(msg)
                ks.sendMessage(msg)
                ks.sendMessage(msg)
                kc.sendMessage(msg)
                kc.sendMessage(msg)
                ka.sendMessage(msg)
                ka.sendMessage(msg)
            elif msg.text in [".sp"]:
                start = time.time()
                cl.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s<==Tamii Server" % (elapsed_time))
#-----------------------------------------------
            elif msg.text in ["Sp","sp"]:
                cl.sendText(msg.to, "Progress.......")
                start = time.time()
                time.sleep(0.01)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                print "[Command]Speed palsu executed"
            elif msg.text in ["Speed"]:
                cl.sendText(msg.to, "Progress.......")
                start = time.time()
                time.sleep(0.01)
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                kk.sendText(msg.to, "%sseconds" % (elapsed_time))
                ks.sendText(msg.to, "%sseconds" % (elapsed_time))
                kc.sendText(msg.to, "%sseconds" % (elapsed_time))
                ka.sendText(msg.to, "%sseconds" % (elapsed_time))
                print "[Command]Speed palsu executed"
#-----------------------------------------------
            elif msg.text == "Save":
                me = cl.getProfile()
                save1["displayName"] = me.displayName
                save1["statusMessage"] = me.statusMessage
                save1["pictureStatus"] = me.pictureStatus
                save1["Saved"] = True
                cl.sendText(msg.to,"บันทึกสถานะบัญชีเรียบร้อยแล้ว")
            elif msg.text == "Load":
                if save1["Saved"]:
                    me = cl.getProfile()
                    me.displayName = save1["displayName"]
                    me.statusMessage = save1["statusMessage"]
                    me.pictureStatus = save1["pictureStatus"]
                    cl.updateDisplayPicture(me.pictureStatus)
                    cl.updateProfile(me)
                    cl.sendText(msg.to,"คืนค่าสถานะแล้ว")
                else:
                    cl.sendText(msg.to,"ก่อนหน้านี้ยังไม่ได้มีการบันทึกสถานะบัญชี")
            elif "Copy " in msg.text:
                if msg.toType == 2:
                    red = re.compile(re.escape('Copy '),re.IGNORECASE)
                    tname = red.sub('',msg.text)
                    tname = tname.lstrip()
                    tname = tname.replace(" @","$spliter$")
                    tname = tname.rstrip()
                    tname = tname.split("$spliter$")
                    tname = tname[0]
                    tname = tname[1:]
                    clist = {
                        "Founded":False,
                        "displayName":"",
                        "statusMessage":"",
                        "pictureStatus":""
                    }
                    mems = cl.getGroup(msg.to).members
                    for targ in mems:
                        if targ.displayName == tname:
                            clist["displayName"] = targ.displayName
                            clist["statusMessage"] = targ.statusMessage
                            clist["pictureStatus"] = targ.pictureStatus
                            clist["Founded"] = True
                    if clist["Founded"]:
                        me = cl.getProfile()
                        me.displayName = clist["displayName"]
                        me.statusMessage = clist["statusMessage"]
                        me.pictureStatus = clist["pictureStatus"]
                        cl.updateDisplayPicture(me.pictureStatus)
                        cl.updateProfile(me)
                        cl.sendText(msg.to,"Copyสำเร็จ")
#-----------------------------------------------
            elif "Bot Run" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                ki.createGroup("Bot Run", mi_d)
                ki.sendText(msg.to,"Success recover")
                kk.createGroup("Bot Run", mi_d)
                kk.sendText(msg.to,"Success recover")
                ks.createGroup("Bot Run", mi_d)
                ks.sendText(msg.to,"Success recover")
                kc.createGroup("Bot Run", mi_d)
                kc.sendText(msg.to,"Success recover")
                ka.createGroup("Bot Run", mi_d)
                ka.sendText(msg.to,"Success recover")

            elif "Me Run" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.createGroup("TestBot Runֆჩ❂†わäD", mi_d)
                cl.createGroup("TestBot Runֆჩ❂†わäD", mi_d)
                cl.createGroup("TestBot Runֆჩ❂†わäD", mi_d)
                cl.createGroup("TestBot Runֆჩ❂†わäD", mi_d)
                cl.sendText(msg.to,"OK Run")
#-----------------------------------------------
            elif msg.text in ["บอทลบรัน"]:
                if msg.toType == 2:
                    klist=[ki1,ki2,ki3,ki4]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kicker.sendText(msg.to,"No one is inviting")
                        else:
                            kicker.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kicker.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kicker.sendText(msg.to,"Not for use less than group")
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False

                elif op.param3 in op.param3:
                    if op.param1 in protection:
                        OWN = "u2144f4eca089e5888899ad5d0551c085","u406133ad4d3fbe50a2f4d51ea081d050","ua51ba06b0dd18c0bfe2cc6caa3458202","u34a9af3a18784280147fc413a68a77fd"
                    if op.param2 in OWN:
                        kicker1 = [cl,ki,kk,ks,kc,ka,km,kn,ko]
                        G = random.choice(kicker1).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)
                    else:
                        G = random.choice(kicker1).getGroup(op.param1)

                        random.choice(kicker1).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        Ticket = random.choice(kicker1).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

                elif op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)


                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass

        if op.type == 19:
            try:
                if op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)


                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)


                elif op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)


                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass

        if op.type == 19:
            try:
                if op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)


                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)


                elif op.param3 in Amid:
                    if op.param2 in kimid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass

        if op.type == 19:
            try:
                if op.param3 in ki2mid:
                    if op.param2 in kimid:
                        if op.param4 in Cmid:
                            if op.param5 in Emid:
                                G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)


                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)


                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)


                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass

        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)


                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)

                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

                elif op.param3 in ki2mid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
                pass

        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass

        if op.type == 32:
			OWN = "ua7fc5964d31f45ac75128fc2b8deb842","u406133ad4d3fbe50a2f4d51ea081d050","ua51ba06b0dd18c0bfe2cc6caa3458202","uc7f32bb28dc009916d40af87c9910ddc"
			if op.param2 in OWN:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				ka.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#------------------------------------------------------------------------------------
#===========================================
#        if op.type == 55:
#            try:
#				if op.param1 in wait2['readPoint']:
#					Name = cl.getContact(op.param2).displayName
#					if Name in wait2['readMember'][op.param1]:
#						pass
#					else:
#						wait2['readMember'][op.param1] += "\n╠" + Name
#						wait2['ROM'][op.param1][op.param2] = "╠" + Name
#				else:
#					cl.sendText
#            except:
#                pass
#
#
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n☑" + Name
                        wait2['ROM'][op.param1][op.param2] = "☑" + Name
                else:
                    cl.sendText
            except:
                  pass

#-----------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
#----------------------------------------

#-------------------------------
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

try:
    while True:
        try:
            Ops = cl.fetchOps(cl.Poll.rev, 5)
        except EOFError:
            raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

        for Op in Ops:
            if (Op.type != OpType.END_OF_OPERATION):
                cl.Poll.rev = max(cl.Poll.rev, Op.revision)
                bot(Op)
except Exception as e:
    print e
    with open('profileSave.pkl', 'w') as f:
        pickle.dump([save1], f)

