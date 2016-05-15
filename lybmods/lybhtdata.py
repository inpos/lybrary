# -*- coding: utf-8 -*-
'''Здесь описываются различные переменные'''
from base64 import b64decode
html = '''\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>{title}</title>
<link rel="stylesheet" href="{style}" type="text/css" />
</head>
<body>
{body}
</body>
</html>'''
style = '''\
body {
    font: 13px Arial, Verdana, Helvetica, sans-serif;
    text-align: center;
}

@media screen {
    body {
        padding: 1em 1em 1em 21em;
        font-family: "Trebuchet MS", Trebuchet, Verdana, Arial, Helvetica, sans-serif;    
        font-size: 76%;    
    }

    div.document, div.footer {
        width: 45em;
        background-color: white;
    }
}

@media print {
    div.document, div.footer {
        width: auto;
        padding-left: 0px;
    }

    div.sidemenu {
        display: none;
    }
    input {
        display: none;
    };
}

input {
    border: 1px solid #003399; 
    padding: 0 2px;; 
    margin-bottom: 0.3em;
    font-size: 85%;
}

select    {
    font-size: 10px ;
    margin-left:0.5em;
    font-family: "Trebuchet MS", Trebuchet, Verdana, Arial, Helvetica, sans-serif;    
    font-size: 90%; 
}

option {
    background:#C5D9FF; 
    color:#003399;
}

div.document, div.footer, td {
    margin: 1em auto 1em auto;
    color: #222;
}

div.document, td {
    text-align: left;
}

div.footer {
    text-align: center;
    font-size: 70%;
}

/*** TOC ***/

div.contents.topic ul {
    margin-top: 0px;
}

div.contents.topic ul > li {
    text-decoration: none;
    line-height: 1.2em;
}

div.contents.topic > p > a {
    text-decoration: none;
}

/*** side menu ***/

div.sidemenu {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 24em;
    font-size: 10px;
    text-align: left;
    border-right: groove gray;
    border-bottom: groove gray;
    padding-right: 1ex;
    background: #FFFAFA url(/menu_img) no-repeat top right;
}

html > body div.sidemenu {
    /* ignored by IE -> everyone else knows 'fixed', right?  */
    position: fixed;
}

div.sidemenu span.section.title {
    line-height: 1.2em;
    font-size: 130%;
}

div.sidemenu ul.menu.current li {
    color: #CC0000;
}

div.sidemenu ul.menu.current > li > a {
    color: #CC0000;
}

div.sidemenu ul.menu.current ul.submenu {
    display: block;
}

div.sidemenu ul.menu.foreign ul.submenu li {
    padding-top: 2px;
    padding-bottom: 2px;
}

div.sidemenu ul.menu.foreign li.menu:hover ul.submenu {
    display: block;
    position: absolute;
    border: groove #990000;
    padding: 1ex 1ex 1ex 3ex;
    margin-top: 0px;
    margin-left: 4em;
    margin-right: -20em;
    color: #990000;
    background-color: white;
}

div.sidemenu ul.submenu {
    display: none;
}

div.sidemenu ul {
    line-height: 1em;
    margin: 1ex;
    padding-left: 1em;
}

/*** headings ***/

h1.title {
    background: url(title_img.png) no-repeat;
    padding: 20px 0 0 180px;
    height: 60px;
    font-size: 200%;
}

h1.title, h1 a, h2 a, h3 a {
    color: #666;
    font-weight: bold;
    font-family: Helvetica, sans-serif;
}

@media screen {
    div.section > h1:before {
        margin-left: -2ex;
        color: #CC0000;
        content: "\00BB" " ";
    }
}

h1 {
    font-size: 150%;
}

h2 {
    font-size: 130%;
}

h3 {
    font-size: 110%;
}

/*** content ***/

a, a:visited {
    background-color: transparent;
/***    font-weight: bold; ***/
    color: Black;
    text-decoration: none;
}

p a:active, ul a:active, td a:active{
    color: Red;
}

p a:hover, ul a:hover, td a:hover {
    text-decoration: underline;
}

p, table, tr, td {
    /*margin: 0.5em 0em 1em 0em;*/
    text-align: justify;
    line-height: 1.5em;
    margin: 0.5em 0em 0em 0em;
}

div.document td {
     font-size: 13px ;
}
td {
     font-size: 13px ;
}

th.docinfo-name {
    padding-left: 3ex;
    text-align: right;
    font-weight: bold;
}

hr {
    clear: both;
    height: 1px;
    color: #8CACBB;
    background-color: transparent;
}

dt {
    line-height: 1.5em;
    margin-left: 1em;
}

dt:before {
    content: "\00BB" " ";
}

ul {
    line-height: 1.5em;
    margin-left: 1em;
}

ol {
    line-height: 1.5em;
    margin-left: 0em;
}

blockquote {
    font-family: Times, "Times New Roman", serif;
    font-style: italic;
}

div.eyecatcher, p.eyecatcher {
    font-family: Times, "Times New Roman", serif;
    text-align: center;
    font-size: 140%;
    line-height: 1.2em;
    margin-left: 9em;
    margin-right: 9em;
}

div.pagequote {
    position: absolute;
    top: 0px;
    right: 0px;
    padding: 10px 10px 0 0;
    text-align: right;
    font-size: 80%;
    color: #990000;
}

div.pagequote .reference {
    font-size: 140%;
}

html > .pagequote {
    /* ignored by IE -> everyone else knows 'fixed', right?  */
    position: fixed;
}

code {
    color: Black;
    background-color: #f0f0f0;
    font-family: "Courier New", Courier, monospace;
}

pre {
    padding: 0.5em;
    border: 1px solid #8cacbb;
    color: Black;
    background-color: #f0f0f0;
    font-family: "Courier New", Courier, monospace;
}
'''
m_img = '''\
iVBORw0KGgoAAAANSUhEUgAAAEgAAABCCAYAAAD0dpAhAAAABmJLR0QA/wD/AP+gvaeTAAAACXBI
WXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3gwdEAgerZOhpwAAABl0RVh0Q29tbWVudABDcmVhdGVk
IHdpdGggR0lNUFeBDhcAACAASURBVHjaPLvnk6Xped73e/N535PzOd2n8/RMd0+e2Z2wGVjkxYKk
ABIkZdIEBZbBEmW6RFIqmXRpLKkUSqqSP9CySzJNFmW6BBEQwy6IxQZsDrM7O3mmZ3o69zl9co5v
9odl+V946rru57mv53cJ/+2H3/fv379JLBpCJIwt6DiOxWjQI51JUSztU69V0AIiQT1Ms9Fg9cRJ
Nu7f5Vf+7ncx9CCaLvHuOz9mbn6JwaDH6tE1Pnz/Lc6cf4xyucT87CqePcZHBlUmEgixVTygXq8Q
ik/j+hqJdIGHe3Xq1QOi2Qw/+ON/zdaDTwgbSUoHu4zHFqqqEjB0vvbiC7iChTXuYU1spqemyOZT
yIrE4WEZIxBjc/s+czNTlCsVAlqCxaVTLB1bQxJUOr0+lcNN8tNpdjYOeOFr38CyTVzXRJQE9rbv
YztjfEFC+vYv/OqVoyuncFwZPZKi3u4QDKj4rk+z1SKVTBGPJ1mYW2Y8GhEOhxmZPUq7j8ilYygB
les3PqDV2WI87BIKyqzfu4Moa3SbByTjBluP1hEEj1J5l1vX36HWrNMbmCwcOUlnItPoWViOzXA8
4PTJ0zzaK9HvN+k1y1RLNSzbIqBpSKKENbHY3dlhdXUeazJheiqD6/W49vEtAopMNBJnPOwSCSsg
aIiiz+FBmcX5HMXiPbY377I0P8Otu7cIanB89RjmxGQyGnDxwgWa9TbhcJR6vcZkNED6zq/9+pXb
dx9S6wxotdvIokujViadShIKBhF9j2g0wnhskkgmMEIxtu7f4qtf+SKTSQNrMuLEqafQlTCxWITx
uE0hN08iHaRV3aPd7rC1cYvt3S2OnjzP+++9zdzsLMHoFBNBZ7fYYHpmgU63ycxUkr1Kk/1SCWSX
yaDNzoN7yKKKKEnEEjFcz2XUG1Kt1hA8iXw+z8rxy4SMAMlEBE0LU6tV8dwB0WiMZDJFOBJkff0B
PiO6ozY3rn/KjWufEo0GuXnzNu1Om9FkwGjU5/LFZwgEQuSyBQw9gPT1n/2VK3okyVwhhyjY9DoN
ApqIa1noAYVbt25QqR6wMD9HKGywsf4pgmkSCku4OGxtXeP+3fewvB6XL30dWfAo1+7hTQROP3aS
Wq3O7t4+xVqDcr1ENpMnm59DDWewpRDBcIJOp0YhP82/+ue/z3e++z129ot0O11uvf8msmAxntj4
vo8sy+hGCFnVObZygm/8zLf54V+8xM3rt9nZ3uXypcvs7e9TLXf4H777W1SqNUbjCa4HCD6XLz9P
OJrHHAgUZrIclsqkkjl8XyESy5LJTlOvHVKt1piaytFsdpBOPP7MlXp5h0q1TCIWQ1c1uu0OAVVk
c/MBT1y8zLFjx5kMJ3x09R3sUYMnL59hc+s+586/QDYVZ3l+nmgky/bWHTxJZSpdYNCrUdwpEtRV
mrZDrT7AcWx8V2T3YIP01DGaPYmAEaHeaKIGIyiyQ6ncY2BPaFSKlLZugQeSrGKEgvi+gOu6PHbh
AnJAJhAKs7K2yr3bt9nf2+NHf/MTGo0mJ0+fJT+zzMKRk6RSU8hCiKeeepZGo0cmXeDEieO89NJL
fOtb32LvYItCYYr8VJ7t7R0qtUOWFo/wyk++z7Gjq0iPP/H5K6loFEMLMJkMcD2HSCRGo1ljtjDF
cNDHstuomoLtjokHJMqVPWKRAEPLRBQVmpUKIcNGlX2siU88fYS33n2Z+WmDw3afm3cfMRpbmKZD
NB4BXyU7c4JG38WyxmRys1RK21x64jE8WaXWs2kW99jbvkd+ZpZnv/ACC0dXSSTTrN+8znjcIxaL
4rk23U6XU+fOcVgs0et2sUY2xf0DPrj6PqWDHcaTMaqucOzoeULBCFtbD5mZmWHQH7O3v8ncbI6r
H39Eq1Gl1SzjuxbJ1AJT04t8/MnbSL/92//oyngyIBIK4tg2qiJzcLBHzJBIxYI0+zUM0eL2+jr1
8h6ua7K9t8sLX3kWz5ZRAyJT+QXKpXUq9R6u57NXOmRx8SiOBcHUDDdu38Ac+0iSwmhkMrF8Tp3/
PIoRRdXC1Jpt5gspth7dojtR6HbHvPH9/52pdJxAOMHlZ58jFo/RbNS59ek1ovEo4+GI0mGJ9fvr
dDodHFegUFigN+gQiUc5ffI8xeIB1z75hHffeYdWo83Fi5c5vnaOjUcbpFJpfFyMoIHrutSrTU6e
PIOqGdj2gHA4QTyWR/rZn/3FK5Y5JhQMkMtkEQWBE8eX+fD9Nzi6toLngi+KrN+/w0w2TjIeImQ4
3L/1Cf3RiPT0LLfurmO6OhtbB3S6XV5//VWyqRh71S5Xr95kcWaWcMSg2WyQy2ZJpmeQ4wVa9Q7B
aJphr02+MMUrP/4hyfwSn7zzKvt3P0QPGSyfOIEia6ytnUUJGrzz+mtEQzp6JIURCPNLv/irrK4c
ZW5uim/+0q9x4Zmv8OE7b/DO22/xzJe+xTPPfZXlpSP8y3/5v/LKq3+JhMBzz3+VeDzFq6+8zIm1
M6iKwKNHD1i/v04+n+Lu/Rv49mfukJ584sSV4yuzHOw9ZGvzFpNJj8NSES0g0elZeL6E5bgEDZVI
WEeVJaYzeaZmTnLs5DPs7FUZjU3u3X9AQA9iWy75qRz5XI7+2MY0bQ4OGxzsFzEnLo4NoHDy7GVy
+WkqzTay5PLGay/zhWee4fe/9/MookcgIBMK6SwvLTOcDAAJXY/xzusvE9QV1o4/xvGjS/z45R+w
9eABS/ko3/17v85g0OfsqeMcP36G0dDG9jXyhSN873u/xeFBkVdff4kPP3qDxaVFXn31LWKxJEtH
jyFLCrmpPKZpogcjhEIGkmQiPfPcxSu37t3kgw/eJRoJUasVmZlJ0m7WCIc0XGeMboRYPX6aB+t3
KZfKBNMn2CmPGUxMIrEoB8UDXM9H9EROnlphv9Kh1OhTqzWp1pqMJjb44DoupXIVRQlw7uKzeJKC
agS5d/8hvufzZ//p34M1YNjvoCmQSsQRRImr77/NhfPnefONN4nHwoyHAxqVPfb3t4jGoyQTES6d
XGbQLHHq8adIJNMkEnFUVadS2mMwHOAj89xzX+H8+cukUhm2dop88+d/gZf+6gc898yXeOqZb7C2
cpYnLjzL6bVzxMJx+oM60ulLz15p1mvMzhZoNrqUK3UerN+jXq8wtmx83+PgoEi708c0TVzPp1Rr
cWxtjd29ffZ2dxElFc/z6Pe7FA/LJJJpbty5hx6QkWSByWSIrgfwPA8Bn8LcEUwxzOZBDT2gYfoB
ookMd9//EY16jVQ6TSQaptFsYlsOp86e4b/82Z9x4fHz3L59B9+ziEVjKKqK60yYLxQoFUt02h0C
kQzvv/cBDx7c5sjSNCFD4MTaMXLpOJOJTSIW48jicVLpAoOhyblzp/i93/1tHr/wGKPRhHwuT6VR
RtV1fC+M9Lu/+wdXwqEAmw8fIooukYiEpspYlsBhucGN63dQAgaj8ZhoNEM8nUYUFbq9Ab7vYxgG
juOQSqep1A6p1lqYjoOs6bSbdeq1Brbj0G638T2fYChC3/I58+QLPNwqYk8GeJ6FO2xw/d0foakq
J06fRQtFCAZDzM/Ns7+7i+1MeHjvDpqi4fsu49GI8XhAMGjg2SbtkUln7PD8577AB9euUzwssXdY
5f0PfkrlsMio3+XY0XkS8TBGMEA8nkRTFbRglHwuw3e/8yvsHTzio08/Ynn5JAE9hqyKSMF45Mqr
r75M9bDM3u4+9+9tMexP2Dk4pNs1scYOni+iqjLpTIqt7S0EScW0BVx7TD6Xw/E8xhOPVquJ41r0
ehM0Pcio38e2HczRZwPPNG3MicU3f/HvcmezyfFTJ9ja3yOiady7/g4Pb10jGDUIxVIk87MMJw7z
87Ps7xdJZWdIpJJUSkVGoz6aohEJhwjqGqVKA80IkM/PYtoeucIMr7/5Dp//4tdJpbLIWohOr8/B
wT71Wo1Gs0qv36AwPcVHn15n/cEjvvj5p/n46sd02zVe/Zu/4uW//nNef/0N5F6jzgtfepHR2MJy
HLLZFA/u3eW1116jUi4BcFCuod1X+OjDG0xNZZCVbVwXXN/hwfptzpx/jI3NIv3hALM3JJHMYFo2
jucjyQqO5OC5HnpAxzItrn1yi4sv/CYB3SGZmkJRJCrFHTLZNJ7gUy/uYo9HKIE0mfwSF5+K0BkM
2d/aRFRDyJ6Foioosoge0Dh5fJUTx49jIjFxLLqHFUKqylQqw2g8RECgUJim1W6wvfGQ+cUs/+T3
/2dS6RmOrJ6kVFxHmSrwvd/6HerFPfqjMf1ej1gshCRLXAnqGlP5aY6fOYeqGiRSeXxvxL/9V39A
Nj/NyTOnECWRaCSEbTs0601+5oWv8eLP/QzHVs9w6+4GSAaZbJpGtcZ4bFMqlpFlAU8Q0DUD8LEs
G9exiWUyFFaeQFMUNne2SUdVXvrPf8gzX/0G5y99nVA2Tyo/gzVpsru7RTaVYjRw+OCdvwTTRA8G
cF0XRRGZjEecP3Oaj65e5csv/gKC5NGs1fF9h3a7hqx4qKrIxsN13njzR7SaFf6vP/pj9vZ2WT62
RigYRPYtzp27hCdHUGSJiWVx5vwF9koHSJ/73KUr1eIO4aDArU/f59b1D3nswnkajRp/+qd/zHgy
5uTqMr1ul6efvkw+n6Veq3Hy7BoIIvfuXOfJy+c5c/I8e7s1Th1f5szpVarlGsgBXNthPOqjqAqS
pKBqOkfXTpHMrbK3c5uIrvHJT19mb/MuTz3/Ik9+7llUPU63UUGVRM6ePkOz20UQReyxSeWwyGRi
4ng2ISPI8dVVNvbKiIEo1699zI0bd7l69Sq/+fd/i/m5I/R6Axr1Ko+du8iwbzI3d4x4PMFXv/w1
rPGIWqVOrdli4ox5+S9/SC4fJxw0iMWizEzNIWUykSu9bp+gESRVmEcMBNnZ2UWRRNLpLEtLywwG
bURRwPN9ZFlhNBwRiYTI5fJoRpDr1z4hGg2DZHHv1sdsbKxz/rHzHD/zJRwUDF1gfX0dH5Gja2cI
ZWYIxQtkEhLrN2/w1o//nHAoyMLSIqIjMrahkMty9YP36NT3GY367O08YtTp0Om0ESRIx+OsLB/h
y195gRe/9R3OPv4Uqqrx7HPPI/oef/BP/hH1poWuR1A0g05ngiBLqKrG4uJRapVDvvb1F7h0+WmS
yQQzMxkUPYo5NGk3axQPdpBFAenokdkrs3OzFEuHHBar5HMFLl56go1HG6iayvKxVSRNpVyuUD7Y
QxBdHjt7nuc//yybm49YWTnJw61tigdFZufnwRMxwhE80aVdP2T2yEni+aO0qjvs7e7w3AvfJJmf
QTXCiNg0S5t89PZrhCNRFEEikQhy5uR5bm8dYk5GhEMGk9GIZvUzu1TKNQbDIf/TP/gujWaD5ZVT
WFKI3YMS+C7vvP0auw/vM1UooOkJer0+vWGP/mhIJpPG91U6vSZHlxbRNZV6/ZCxNUKRx6wtnWeC
x7kzpwkGw5w7fQYRSaU76BFP51k6uopluoS0CAuFZXKpeZYXjrO7UebIkSWee/oimViIuUKcN974
G1rtGs1mha998UvMz88y6E3Y3t/iyLEjuK6D4w7QDZGxFGJvv8rpEyc42N7g+3/yR4z6fQ73d/m/
//DfEQyGURQYjQ/58L3XeOm//QeCYgtDtYiFA3iew9mzp0in0mSyKZ575gleffUdookEnmgx7HdY
mJ1lMuwz7rcoHh6Qz4YJB0VCQZWTx5Y5t7bCTDrFzv4m6dQUg14f1YhSbnVYPrLK+r0NAoEhupDg
zp0H9HpjuiMTaXa2cGUqM4Uuy8wvrzI1NcVHH/2UlWOLzC7k+fijt/niF77EX730QyamTbnaoLi/
jySrZHMzbG1t8eDuPc5fuIBl24QSSdYf3WLcHZMsrCFpUdRQAbPXYnfjFpXyPromkJ5Z4kff/1P6
zTLRWJygESCdmSJkyPTaVUq7m1RLe6iqRDweo1ErUalUGQ0HTKXj+JJEfzRh89EOi0fX6HTaDLpN
zHGf+dkCoYhKMpGi1W0i+iNEPCTZ49bN10jEMzx27jx75S7zC7OIroNrj+i3y5w6fZrsdA5RFJgM
W4i3bt7mjTffoFgpUjl8hOeOCYbCvPzXf81HV6+RmsrzX//8v/J7//B/YWK5WLaDZXscVjtoaoDB
aMRTTz2Oj0XXHOMIKguFNY7MLxJULLLZPNFoBFmRmYwt+p0+1mRCrbhB+/AAUdHQNYVYNIztTojF
Y8TjCQKahO+5tJt1+o0KhUwMSfTQ9QD90YBQOESt0SGdmmIqP8NgOKDZaVI6LHPs6AKymuGja++x
MLvA22+9SyKRoFTdYTAuU9z+gEq9hu91mc5naTWr9HpN8Ptsb13l0YM77O7t8sGHbyMuLC+hKgG2
Nvf4i794mVde+REnz5zl6vUbPPfEZeZmlzi6NMew1+Pzn/syz33hq0TTaURZQjMMhoMht+/cQtcV
Tp54HG/cYTptsLX7iEDAo1ra5cGtdxgM26QLRwjFp2g2q+w/uMlw2CccChFJxMhOZwlpMrbtMBqP
qdfrPP+F55BkkWarxczMNHv7RYKGgWWCZ1n86re/xTd/4ZdplotkEkmMYJRqtcF4bHLh8YuY5pg/
+ZP/jRdf/DtowRC3722yv71DvVHnlR//F1Ixg7uffsT3f/AfsT2Hxy58jU7PJhFWiOoiX/rCV5G+
/Yu/fCUciTGyTbrtHoeHZUrFEr/x3f+et9/5CaX9PU6emOHll37AhXOPoYeCGAGVmzeucunxi8wv
LHH/zg2yuRkebGyQS+vcuvOAXG6KxeWLHDn1OX7ykzfRAiJGMsPP/vy32Xt4j9vXruH5DsvHlknE
42SyWUQBuv0O07kpFEnj46sfs7KyzPLyIq12h0+v3aUwPcXYMpHw+LX/7pe4ducRB8V9pqemOdjZ
ptOpMp1NohlhtvebDEdl0pkU46HC6uoK8YTBO2+9yZkTSxTmF9jb28f0bAr5LGa/ymjQIZlNUauX
ESUV6Ymnn7iSy+WJxuMYRphOu0OrUePtt96l2x3RanV478OP6fRH3Lx1E1nxKe7tMT83R7Vep9Np
cvrc4zSbA5ZWz6ApCkePLbK6vEi7M2Z9p4kniVijNqNGkVQ2z82P38Y2HZaOLhEwAtRrTSrlCrFE
HGvk4Po2kVCQRCLNaNhjOBiwtXmA7XikUgkGwxEiEuNJmWgkiagbCJJKcX+D9957i8X5ec6cOcPj
jz/NxNa4+sk1SuVDUsk4k0mbhcUFbl6/hqzqnD79FO9/+A5aQEQVHQ4Pq+yX6zSbdYbDHtKZcxeu
GEGNn7zyYxTV4IUXX0TVZAQRNFWj1WkxGph0On1a7R47Owfs7B3y6fV1VFlm89EDyvslzp9c4aNP
rjPstJjPTYNkUB2qNHtDZEXE7Dd4+MnrZHIzbG8+Ih6Lc+z4GmfPnSMSDpFOpfj0k5vk8xnq9RbF
gyI+Hs1mg1arS/GgQmF2ikQixmTikJvKsr11gCqO8HzA99jZfsDBfoXRqEUuGaJ4WAEkzp45ybvv
vs5sYY7C9Bx7pSKKJNAfDBhPPGr1Ngf7Fe7e2aDeblIqVlEkiXA4ivD3fvM3fdsacvr0Jf7oP/4h
kXiCYb+LKilksjGMoIYvgG25iEjs7R5QqzVot9vYjoUR0BAEEQQBRZNYXJzl2SefpNIYcPzJX+Lh
3j5BQ6NZfMRHr/+ATGGW21evcubxM4TCcc6dPUOrXSMeDZFJZPnd3/nHhII6qVSKfD4LeJSKhziu
wHQhy2gwZDieILoSsiowN1dgbmGeH7/yCkYoSDySQDd8bMdC1UIYhoGiqgDogRSeaFM93KJSrpJK
JzBNECSNTCpGo9rE47PDlxGIJ+NIzz//hSuFQp52Z8DnvvAig4lDPBLBCGicPnuCU6eOE9A0QsEQ
u3ubBHSFeDzC0ZUjLC8tEjR0IpEwS0cW+eIXn6JUOuTe3UfUGx0WV07Qag9JxQwO9nbQZJFuq4Fl
jTh56jiry3PY4yHBYJB+v897773Jc888zZNPXmY0GrK1tYUgCHieQL8/QhRcfB8CAZ1QSOaLnzvD
0HSo1jssLC2g6yEkUWJubgbXk0gmp1hcPMETlz6HqsbwRIFq9RDf8RFQ6HcHLC4uEAwGiMWCBHSV
TnuI7XgcXV5iODSRfvU3/scrsqaTS0W5dv0Gv/6d7yDKCjvb99na2mJvexfHtXB8m0aziyJryLJK
PBan3mihBQyS6RSyIpNK5am3OvS7I6qHVfK5ON1uH8exGQ965KdzfPz2m5w4c5z52Tyi20UPaDTb
fZYW5tne3EYNBKhVSwxGJoYRIhaL4joW9WYDw9CZmsoznph8+bnnSWem6EwEZEllYpqMzSGiKFMs
FfnWt34JURSJRAPMTBXYOyihGga+Z2HoGpIiIggizWaNTCbJ6soKjXqD0XDEytFjtDodgoEw0s99
6xeuGIbBeOKwsDzPv/jn/5REegpJChEMhWh3OoRDCRrtPoIg4rk+oiCQTKfR1ACyqlEsVjm+ehbL
FvElg4Cm8OjBA2q1EsGwwbDbQQ4EGLQrPLxzk5nZKXRlwPm1Jba2H1LIplidjXFvYwPTlhj0h7Tb
TfRAAEUVGfYHWBOX+cU5Uskksqxy69ZtZpfWGFgejz32BKbpEgqFODjYZWl+hkGnwdGlee7cv8vx
Y6sgBWj3B9iTCYfFQ4LBCL4PjuvS7fbZ2txDQCaXn2I87HNsaZHzZ1eR5paWrpw8eRrTEWkPfRYX
j6IbIVK5OKVyhYsXL/L1r38ZyxXI57NEQgZPPnWJWqXF6VPn6Q9NEskcR5aOcPz4ESQ9TDqb4ca1
q+D6dLptjh6Z4v2fvsTMdJyRbeJZHrl4mIf3dsnMzlLaq2EOqjS7JpdWsuyXKzz91JMMuh1+7ue+
zqfXbuAjo2kylmkhiCIiNj/7jW8wGX8WyEVCIR47f5EbN97DFzza/SYPNh9wZOkEnXaT7PQ8H167
gabp2J7HqZNnGI7HIIiEwmEW5haIRj5TvKoKhFWRYa+J9H/8n//pyk/feAVFdMnFUgwHbS49fpxG
rcORpUUUd8xb776JKkOn18V3HLK5abZ271ErbXL82DGCgRGzhTn+6uWX6LerjAZj6pV9Gp0e5mjM
xvoDsuksjXqDQi6PJPu0mi2WTx5DmIyIRTVEPU6jPabWGyIgI3qghSQ2HxWxbItIOI7jWIRDKtlk
lLlslCNzKo7sYU16KIZA8WCLTz+9iSg6BCQNZ2JRr25j2Q6XLj5H8bDB008+RziVpdlqEo+F0VWD
ymEJ3dAIx0PYgy7j4ZB2p8VMuofouC5KQGZ78zZGYMiTF9b49//2XxMPiext32VleRbR9YiFVAxJ
RJYFHty/x0xuET0UoV7bIBSe4j//xV+yu/OQ3d1NPr12lcL8MrIgMB6PGI8tNja2GA5NctkEnusQ
iSeoVeqUGx0ED3JRgcdOLHL/3ha9wQRZlZidLSB4Hr7vYgQDZHIZhkOTZrNLNpUlGIyQiurcun2d
Tz/+gEr5ANOcMBqM6fcGOI6HIGuUD/dxrR6xoE63VWY+l8I1bUzL5u76faam8wi4OOMJojDEHndI
xQ2aA5Dm56avXLrwHDv7m1jmkPffv0Y05LG7e5cnL1/i3/ybf0q92kRRHBTNRxagVtvlxo271JpN
HB+MxBRjEyQU6rUa83MzxJJJKoe7mBMHEAkZAZqtDrMzebrdNrFohHq9ztz0FIfVBlOxAHe2D5EC
MU4cO8Lt+1tYlktmKk+t3kQgQLm0hyrJiKIMqkLpcJ+fvP4RWjCIZZnIgky7XkOUVAZDi4lpM+xP
CBga6/ducXJlld5wSDKdI5vK0G42cF2XSEjn5s1P0RWYyqfoTxzqtRYBzUDS9PGVUmmH/NQM+/sb
7O6VeOqpy3x87SNuXr/N3EKB8bhLJhPk/oM9GrUKMzNT3Lu3wdGVVSRJwAjGsBwda2wRDoUpV2tY
jkOv1WTQn6DIMo7rMz2dwXZG1OsDDMPg2NEVqpUy/YnLYiGPaQlMTAtVEjh1ao1Wu8e9+xs8fLBD
OGxQKGTo9waoqkSrPeboiVVs1yGTyzEaDtna3EPWVHwfRFFEVVWMoMFk7KKrEktzOT64+gnZqRyW
7TAcjRAFGc+xyeVSWGaX+dk06VQYXbOxHAtpZW32imf3KMxM8f/+P3/J3/8Hv8e7H3zI3/n5b/LG
668xPztHMKSSSBi02i0UVUZTAxjBEN1+j36/ix4I0hgAjBn0+xw7fgbTmtA4LGGNLURRIBI1SMSj
zC8uoAYUer0+09N59raL1Do9CtMzSAEF0/HZL7e4ef0mAT2CLMHBwQGBQOBvaTEdyxmjG0HWH24C
As1mEwGRYrGKJKsgiHiOg2k6TKXCPH/5HJcvzCJ5Np2BSbX8EMlziEaDhMM6W1vr1BtlfH+COR5T
qpSRFYF2b4T0tRefv9Lv9qnXyoSDEVwmpFMJ8tk8t++tM1eYpVJv0esPCOg6qqrQbPbo9kZYpkUy
ESWZiKPoUerVCjgekioRiRrcvnYNH4lEOkY6HWNuboZmo41pTkgmE+hqgM8/c5FiuYxlOyTjMTRJ
QZZlUukkGw+26Ha6SIrI0tI0g26f5YVZXMfE0GX6Y5twMEJAk6nX21RKdYajIZ4v4+HhOhZfemaN
SDTN3v46EhaqbNKplpnPunTbJSSxTlAbMJmYBBSNfC6D67kgyrQ7Q6Rnn3/iiu3KdFo9gqrMYxfP
U9wrMxoNGQwdbnx6C3wfSRTpdLoUpmfodS3Kh01CIQNRlNENhc2H6ySSWSYTk2BYxR6NuHvnPpFw
hEBQI5tJU64cksnkcGyX8ciiMJXHl0QKhWl8QEAiGdMI60GmsinSqQjXr68TNAJ85QunsVyDcqVE
o9PH0A3Wjh1hY2uPoB7g9q11FFlhppAjGgoSDwf40rOnyeSy3H9wC92zCasTgjqEEkk2Dg+YmCKa
MMKc9KjWukgDXwAAFxhJREFU+iSiCUJByGST7B+UcGwZOR4Jo8gGnWqdtVNH2d7Zp1gs0u5/ls5p
AQEt4BIIqEhKhO3dCo5lYwRVZFmiNxgg1RQU0UMWeswUwughgz/6D98nHA7i47G0OMP+QYmgEcS0
hujBAAHPRwvr3Hu4ja5phHSdzf27xC5eJJmK0O70cHyHwkyGfreHhsJ8csyFlbOMh0M+urPF5vYe
+WyEg9IBk7GFlgywdmIZwZrwxc9foNHusnJkic3t+/h6jOv7dZaWEmzvlmm3PZbmJHxBYDB2EVEw
LY+NrQqiWESWtc/grfm52JVAQEXVPttus7kCe7s7GEYAcDCCGtZkiKEHECWdfm9Cq9VBVbTPsDhF
pV5rUq+3aTc7RKNhesM+G+ubhMMhArrG0WNzlMsVVE1nPBkgCjK2beE5DoelCrlcguFghKEbLMwt
8eDBQ2xX4P7DHSKhIM8/fZZmrUwkkqV2cBfb7DA1n6LVHJNJp2i3+5SKNRTVQJBkjHCcW3evE0/m
6HTbIMqUD3bxNB3LFalUOqytzGGZA2zbwbY8nImAEdIQXYF2b4zrCqiyhHT67MyVymGJUDSGiE+1
WmVuJo+HTafTIpmMMxz0UGQJnwDt1gBrbON6NlpARtU0mo0emmYgKxKebxGJxlm/+5BEIkEkFGJ2
PkFAD5DLTtHt9hkOTFzHRVYULMsCyUMSA1QqTRTJp9zocbC/xae31vnCc5do9Ru4KEycCRsHbU6f
OAmCQESWyOUzZKfSDEYW9WqLmdkZBEmi2W0QieYYD7rsFw84qI/wPJl2y2VteYZur4braYzGE0zL
I5vO4lktcHpMXJFmd4Qi6oixcJRIPIxjOfgI7Gxv4QvQ649ottoEdAPXDTCxRarlOo5toQY0fB8E
X6DTaXHk6CytToWIEaS4U+Xtn7xLNBxFVSW+/sKThIIRzLHFeNIlHNKIhCVisQiT4YDjK4uMeiM0
Fb78pcs0q1V+41d+hv1Kk29/9SuMJ/uMTYWNnX2OLi3zO9/7Nf7qR29y7W6VeC5OMujx5SfP8/hj
SwwnA0bmGNsec+70Be6ur9MZjCmXB8wXZvBdkIQhoi6jGDlUFUKhEIaikgw76KpAKBrBFycokobj
TJBOnV69Eo/F6XS6pKbibG3tIckKoXAIQRBoNbqU9huARDwRRVM1er0BnusSCgZQFJlisYqARK/X
p93pYJo2kViI42sLdPpNsukkW1tFQqEonu2zunaMWqNGKBhk/f4meiCM7bq0Byb5qMzOYRXBhVBM
oj906Q8d0tk8o1Ef1xny+Nochekk7UYTD5mZbIRSpcJH1x5RKdYoHVZBlBGxCYWCbG7uMhjYPHbh
NLNzGQ4rbYrFGvPTBSaDCaLvMJWNMzRNWgMHx1UQfQ/fs5FFSaXTHTEzM0s6nSQUDpHNZugNJoyH
Fr7vEgwbSLKA51j4OMiKgi94WK6H6zhMJhZ6QKdebWBOXLKZBK7ssLyQpW+O2N7aZGoqjh5Q6PVM
7tx/gGNDrVJktpAhGApTrlR4/ukz3Pn0BnFVIZOOc3B4yMzMIkYIRhMH37FwPJFKe4CmwjNPPcb1
G7d5tFuk2bXQNJ1sNgG47G1v4QEHB1WGgzGuJ9Nqdblz+xbhUAJR8BEknZCuomLTMS32qhNCkSBZ
TaQj93AdA+npp89eEQSBXq8HvkAkEuPg4JD+cES/O0QQbBzLRpFU8Gw832M0sRAFiX5viO+LWJaN
bdsMBiMsx0GQ4Z/941/hwcNt+sMJqhIkEQvhmC6KKhAORxgMJiiqRqfTRZFFjEiYfrvD088/zWuv
XWNi98kkw3S6XarNHtZ4yIWzJ3jr7XdR3Qkn1+awLQEjMGY5m6NjTvj0To2AJnLq1Fn63R5GUCGR
COP7Lq1Wl929EjMzc+ztlUklM8gy6IrAxNeod8eMBg0iioFrTUilosiqgHhseYF+r0+l0qLRHHH9
2l363SGu4yAIoEgK6USIXC6MruvEYjEy6TSSJCHJAWzbI5GMYdufKSmfTfHsk2doNKssL0xjRAIc
Vsp0W22azRrDToN2rYakCIiygCgHcF0fgEZvyD/8nX9Bs9UhEUuzWMhz6fJFbMvi+Ooin1y7ycrR
OeaXF+l2RuweVHAnQRzP4nCnhWWOME2TJ59+Asu3WF07Rb8/JpPJkM7E6HUHfPDedebn51hdO0Iy
JtBoFrnxcJN2a8jjJy+wOJ8lFItwUKnSaPaQTp9ZudLtWyhqkGKxhK7rSJKM69sEDRXPExkMJggy
7O8fks2k0TSNQDCG53ooqkI8HuLWjXUMw2BuJsXp49MUq3UGpsNkYqNrGuFIlEq1QTSWpDA9Q38w
RFc1QrpKKBggmUwwGvQ5cfwsQUPA0CUOqk129soMewNEQUSTRQw9REBW6PQtZN+kkE9jRFRe+3AL
0xEIhQO8+uqrTOXypDJZ0rkMh/sVgmEdw1Bpt/sMBmNce4wg+ETieWzLBUXh5r377B50aHRHWKZH
IhZC3i/3GY1dRsMxgYBOt9shFosjqyLxcBDflekobXxfRvRB9G18CRJRBUWOIEkw6rTxfJ98PsPJ
k9N4zogjM7Pc2d7FdTx0TaLf72EYQUzbptmqE49HaTfb6JpMNhUnEAojTLrMLmTZflRHNWTubFZZ
XljmxS+t4U7G2J5JIp6g1+pxdCrM4kya7VKFn3zQZLPYRlYlJEkgk0rR7/R4cP8+mq6hh4KsrczS
6bUxLZOdzTKjQZ94/BK1zV2yuSS2aXPm5FEER8DzXAbjPnpIRcyk4siKx+kzq3R6Q6YKeWx7zLg9
YNQ1P2u/RGOUS3UCwQBDc8TO1g6iKKCpLorocvXDu0SjCWZmoyxOpxibJvFoENH30TUVX5TpTwZ4
eGRTOSYTG9caEYkYxBNpEokwe/vbJHJzfPj+x6wcX6HV7PMbv/x1dja3ePOD2xwcHiL7Jq5lM13I
05lIvH2nzI+vl/jJO5u4lkM0EsL3RGTFwHHA800atQaDYZft7X3a7Q6FQo5gOMBwPOGv/+an3Lpb
5OFGBVkJUKv1CcXCOJ5NKpUC10W6/OS5K74H9+89IBQJUzzYZ9idMBlYtFtNjh6doddq0B+M8X2F
dmdErdKi1zG5eeM+t248JJ5KcWS5wNpCjma3zplTp7l24waqHmU6n2Vnr0QunUP0PDzPx3Y9VlZW
6Y8muBMTVfZJ5qb58Stv8fknztDtVbEFmfv37nHm5Gk6rRqm7ZOMRUmm8+RiQcr1Eq12E0SRw1qf
8dgiHAkSi4WZTIZk85/Bpol4hGq1gu9p5PIJEvEUw2Gfeq2DKIj0+kO63S5nTiyyND/H/kGRwlSK
bqdDIhxGWj66fOVgv4xl+VQOy8iCx3g4JF/IEzB0BgOTYqlGvd7GMl1ajR6WbVOrNhiNLKZnpzh7
dpFMOkouFWZi2VSaA0KBAMFIiEa9Rm9g0+6O0A2DWCIGgsDYtEjFEhiayN5hg3t3t+n0hxybTZNI
GVSqDUYTlUjIIaAEEEWXWDBKMpPmxv2bbFeb9CYClifS6Y2wLJvpXJZY1EBWRCLROD420ZDB0tIU
jXqZdmfAeDxBVqBW7RIORhAFn5FpUq40CYck8pks/YlLb2DjiwrSoD++oqoy1z65wbkzp0hlE0Rj
USRJpd/vc/v2Brbj4rk+o4HJxJygaSq+7+H7HstLCyws5nD8Ia4Jkuximj7T01l6nR7tbo9kJk2n
O0ZRNUzTRwtoGEaQ/b0DjJCB5XjU6g22Nvf5Z7//Xa5ev8PItijk0hwc1lElmXBAoT4c02q3sbwR
jaGDLKmYpkWrPUKWZBzPxnU9fEHC932ikTDtbhtRhGw2zsQ0qVVbDIcOuiHjeT7RSIhIJICIyN1H
+1gjC1XTSKZi7O4cILXb3SvFgxKe67K7W6TbHrHxcJv79zeoVbrIksJoNGYymuB6DoGAiizLAHie
h+cLqJpOIGCgaBKW44DjIuJTqjU5urKGZU54tFkkGg3heQ7hUITtrQMymSQ7OzvohsaD+1usLa9y
4liKwfhvdzVRotEaE41FMG2L5dk8qihhBIM83KkwPx0H16dS7aCqGrIkoygaekBHlD7LiGQ5SL/f
RRAEDCOA57lUK11mC1PMFuJEYjqxWAhVkxn3TXb262zvFmm2+6iaiiQIwhVJUghHIuD7DPo9BFEg
Fo8xGIxQVBFZFpmYExRZBDxs22IysRElCdsxObayTK/fpz+w2N+v8fj505SL+1iCxN076xi6gRrQ
UVWVUDDKwf4Blu1RKVcZDR0OiiUSiQTnzs4z6lRBgnrXpjV0cW0PWRJJpeP4no0jBVCwyWanaLeq
tNtjKvUuhqGD4BAyNBzfIRozsEyT0WSEa3sM+xMk2cVzXY6tzTJodzGCBo7voSgBLMuiMJXGFz2G
vSHNepd6vYMky1wJhTQ8z8N1XS5cfJxEIkJhYYbRoMdoOALfRVMVZFkiEglRmE2iqiqVwybJVJJQ
WMO2RzRrPaLROBubW6hGhFa7jxYwCOghBv0+mXSKBw826PXHOI6FpqrUG036fZPpqRz7+4fMT0+T
z4SRAirVShdNj5KI6njuGGSD/tgmFgnT7XdwHId2Z0C7M0TTAmgBhYAs4PkCruUwGds4jkUyEcKz
HXRDQVUELHOIrGmMJja6rnH/zhauL2HZDotLMwxGY7SAiutYSJ97/qkrjz1+Fk1TOXv2LJ7vEotH
mJnLc/vWOo7tEArqGEYIXddJp2PEExEiUR1F0eh2RyiKTL83ptsZIQgeg96E/XIDXJFuZ0yj0WRt
dZVut0Oz0cM0PYJBncGgz2RsEomEMYIyKyvzTGyYmD0qbZNsNs/cTI7ReEwsFeXwsImNx/hvy7z9
XhtEhWZziO/7CDiEYzFm8hmscZ92f4isSAi4eJ4PfPawNS2RmekIg16bZCKMFhDxPOh0+pjWmFwu
je97nDh+DGllbf5KrVbB8xxKpUMebWxTqzW5c+c+iqKQTCRQVJF4IoEakFldXaLdbILgkp2KIgnQ
aPT/f+s16i1M+zMSZDzqY45NVFmlWqnRrHeIRaPYrkW92mA0nNDv91lZXcB3IRaPsL9fZLqQQ9Yi
ZBMGvXGf+w/3kAWHetckYmgk4iHee+9DLNtjd/cQ15MQBJAlBUnwSUUVcukI7WEfAZV+fwCIn135
jSK2Y7JQSJBIJDBHNtFwkIAuoesGtuXTbHXJ5TJ0B5/NYCLRKKoSoFa9T6/XR7NMVFX7TLaqwcra
cRLJANVame2dPRTBx3NFwhEF7UiMgCEhSSKalMJ1RbSgwP5+jWFPxnFcDqsNTNMkHk1QqTYBl2Ao
xKA/ZuXYKuFIkEgwRkCVGZuQTxXoj5uUm3UULcTS0gytRp1wSCEQltnc3eTxS0+zu7eFHhoxbpif
tYmw0RSDkWPTb4tEogbNxhBRFPARcCyPIwsZNCOAa4IrWGi6jPS331KyaJNMqJSKDjvbB4TCQaRQ
OHglk8qx8WCX0mGFhaUCTz59iicvLeJ6Nq7nUq20Gfx/LZxZjyNnFYafqq9221Xe7XbbPe6enpl0
opB0iIIURVwjhESu4ALEDX+k/xhCQkhEIMFFRlGGmczSm9vtrTbXvnBh/sG5Oe95jt73nDCgrkvy
XDroyWhETUWdFziOja5XCFng7gIUQ2A7GkJodLsdDNOgM+giNKgriTCMGI5GfPrZC6bjPmURk2Qp
RZZyc3NHUsgkWYGkq6zWj6iySppHKEKw3vh02x1W7o48TqiKijDMMXQdVSggxRiaxNZNUFUdRSmQ
aw1ZEuR5xqjv4Ad7nI5NwzIo0pi2Y5IXCWWeo+sSjYZFs2WwXKwQJyfHV3//278wTJ0//fE3fPLx
DE3N8V2XRqvF+fM5rhuyWu1I4wqn1WJ+Oufp+Rk/vXmDogjWjy7T2RDPi7DtNkUBuq5RFYLtzmUf
JmRFTlXmSFXJdD7lZDrlxekRy9UjQsjUksIuDHl+Omd+Nucvf/2Ou/sVg8GE3Tri/Pkxnuezjyrq
skbWNc7P5ng7j50bI1QFy1BRVIO2PeTmdkmWJhz1bbwwo5Jk7KZJr6NgaBJxFCHLEkUJWZ4xGvYo
KygVg81qiyRBt+sgNZtmPRyOmM6GNEyTh+WCJ/MJZZUBEqoGYZjh7TKSKKc/6LDbbZAlg3ZXpSYj
DkvafQ3PlSmLFCRI4gJF0VmvNgihEYcBv//dr5DkmqWbHHQsi3n67CkyOde3j6zWez46GyE0iaTQ
2W42NJptbm5v0VSJ2UkXL0xRZY2TJycsH27I0oKX379HCJnhuEXgR8RRzvFRBy+IUFWZs/kTdrt7
HNtkPDB5WK5oNW38MEKzGsRRjqWp+ElEkUCUZmRpAYC4+Pj5VbfbYTByuLm7p9vvUFIh1RW2bZMl
OZeXF+i6YDCwmU27XFw849//eUnTbqGpBq2WTbyvWW88dq5HWR48rihKSJOUfZhwejYjzVO224Bw
n1GWBaZl8PrVG9Io5clszLff/pZ2p8Xrt28Igj1ffvkp7z68JYoTup0x241PXuRIEoSeT54l3N0+
EoQJmq6hqgJVlXDsJqpW47l7hGLiu1ualsLxuAm1QoWMaZkYegtNKFRliqqqyLLO4n6D0A2KvKam
Rkwmo6uT+QjfdxmO+7jeBl1VOT17wu3NNUI2WdzfoQiZbqdNHPkgZ4x7bfZRhe+nZFmEomr0+w5x
lCBLEoZhHYLjfgR1xc8uL1ivAzTdAnJMU6MucrqdLpZpsd3seHd9A5XMFz+/RJbh+5c/kKQFhqEj
y5CkGWUh8f7dgjwvGA7H/PjqHaqm/n+cc6BioybeZ5hmk7KKscwGmqpAVbDzfdotizhKyWuV7W7F
sGsSBSGa1sAPY4a9DmmyB9FEXFw8uzKtmtFoQlXW1KXAdX3Wjw8YhoW7i7j87Avevn2P7/pIUoFU
NziZGGyDw0eX5cPjoQitZh+m1FKFrlqkSYTve3zzyy95eNji+y6DYYc0zQ5X1HaDOEnpdVvEUYDZ
0Hm8v+cf3/0Ty7Q5OzvDdWNmJ8ccH48I9wea7w86vP7vexYPKzTVwHYs6rrAMBWCMKSuatK4omlr
2G0Dp23SaJa07Ta1ZJCVFXazSZUHnJ6e0mqa9LsdjiZDtu6KdkNjcuQQ7beIX3z1yVVRw+31NZqp
kqc+42MHXVdomipxXhCEezRF0Ot1ieOMs3kX3wu5W2xQZYNGQ9DvDXn58g2WYWGaBlG4R5YFVQFZ
npDnOVmWE3g+VVFSZBl+4NM/6iPqA1aoVcVg5NBotrhd7Ehjj8vLT/np7TUPjztkIVCEQllXmMZh
md4HAVVZkCcFeV6jCo0kPmStJaVEU2oMTWbU6bByfSpq4iRju/L47KNz/N0jSAdr3d88MJ9OMHQV
qUhRhIT4+uvPr/bhnmfnA4J9RpGVIKkISUKWU2TFRNcEpqHz7v0N56czoiwjS2VqqSYMcvI8Q1Pg
xbMZfhhjNSzqGoJwj2WaXJzPOH32hMnRCE0zuHgxpSwrhKwhFSWbXcBq6yNXFVEW47kxJ9MRi+Wa
bscBJMxmCz8IUYVGWcJ41Dswm6GzWXtk+SGHFMcJinJoScdpMeg0GPcdwjhD6DqGotKyDBRV5/2H
NceTHkISPJ0c0W3omGXEZucjhKCgQszmo6siiXF6XV798I4//+HX/Pj6gTSLeH425WHjMxn3aZoS
33x1QV7GrLZ7bu42LJcBk8kYS1M4Om6zWHg4js1i8UhVVWiGRqvR4MX5Cbsowdu5DI86fPhwSxSn
zOdHVFlCu9vDth2cdof+6AjLanBzveBo2GO9dPn88jmmYXA8m3J9+wFFlpGqBN8POZmdoukwHHbx
vABF0UiTFFnWUISKpjZZbz10Q0eRCyRJJokryrxgOh7QsiTkOqYsK9aeR5Fn5GXO0vVYbvf8D+E9
mWBb8hAIAAAAAElFTkSuQmCC'''
body = '''\
<div class="sidemenu">
{menu}
</div>
{document}'''
menu_container = '''\
<ul id="lyb-section">
{menu}
</ul>'''
menu = '''\
<li>
<span class="section title">{name}</span>
<ul class="menu foreign" id="index-menu">
{submenu}
</ul>
</li>'''
submenu = '''\
<li class="menu title">
<a href="{url}">{name}</a>
{submenuitem}
</li>    
'''
submenuitem_container = '''\
<ul class="submenu">
{submenuitem}
</ul>'''
submenuitem = '''\
<li class="menu item">
<a href="{url}">{name}</a>
</li>'''
form_minisearch = '''\
<ul id="lyb-section">
<li>
<span class="section title">Поиск</span>
<ul class="menu foreign" id="index-menu">
<li class="menu title">
<form action="/poisk" method="post">
<p><input type="text" name="search">
<input type="submit" value="Поиск"></p>
</form>
</li>
</ul>
</li>
</ul>'''
form_auth = '''\
<ul id="lyb-section">
<li>
<span class="section title">Авторизация</span>
<ul class="menu foreign" id="index-menu">
<li class="menu title">
<form action="/auth/login" method="post">
<input type="hidden" name="from_page" value="{from_page}">
<p><input type="text" name="username"></p>
</li>
<li class="menu title">
<p><input type="password" name="password"></p>
<p><input type="submit" value="Войти"></p>
</form>
</li>
</ul>
</li>
</ul>'''
form_user = '''\
<ul id="lyb-section">
<li>
<span class="section title">Пользователь</span>
<ul class="menu foreign" id="index-menu">
<li class="menu title">
<form action="/auth/logout" method="post">
<p><a href="/ctl/user">{username}</a>
<input type="submit" value="Выйти"></p>
</form>
</li>
</ul>
</li>
</ul>'''
login_body = '''<div class="document"><h2>В графе "Авторизация" введите имя пользовотеля и пароль.</h2></div>'''
user_body = '''\
<div align="left">
<table>
{groups}
</table>
</div>
<div align="right"><a href="/ctl/users"><i>&larr; Обратно в список пользователей</i></a></div>'''
group_body = '''\
<div align="left">
<table>
{groups}
</table>
</div>
<div align="right"><a href="/ctl/groups"><i>&larr; Обратно в список групп</i></a></div>'''
logged_on_boddy = '''<div class="document"><h2>Вы уже вошли в систему под пользователем [{username}].</h2></div>'''
access_denied_body = '''<div class="document"><h2>Не хватает прав доступа.</h2></div>'''
form_upload = '''\
<form action="/edit/upload" enctype="multipart/form-data" method="post">
<input type="hidden" name="catid" value={catid}>
<p>Путь для загрузки в раздел "{catname}".<input type="text" size="50" name="filein">
<input type="submit" value="Загрузить"></p>
</form>'''
back_href = '<a href="javascript: history.go(-1)">Назад</a>'
index_html = '''<div class="document"><h2>Добро пожаловать в архив.</h2></div>'''
nicedit_html1 = '''\
<script src="/edit/nejs" type="text/javascript"></script>
<script type="text/javascript">
bkLib.onDomLoaded(function() {
    new nicEditor({fullPanel : false, 
                    maxHeight : 450,
                    iconsPath : '/edit/negif',
                    buttonList : ['xhtml','bold','italic','underline',
                                    'left','center','right','justify',
                                    'ol','ul','subscript','superscript',
                                    'strikethrough','removeformat','indent',
                                    'outdent','hr','image','forecolor',
                                    'bgcolor','link','unlink','fontSize',
                                    'fontFamily','fontFormat']
                }).panelInstance('nicedit-js-area');
});
</script>'''
nicedit_html2 = '''\
<form action="/edit/insert_doc" enctype="multipart/form-data" method="post">
<input type="hidden" name="url" value="{url}">
{modify_doc}
<input type="hidden" name="catid" value={catid}>
{textarea}
<p><b>Имя документа:</b><input type="text" name="doc_name" size=60 value="{docname}">
<input type="submit" value="Готово"></p>
</form>
<div align="right">
<a href="/category?catid={catid}">
<i>&larr; Обратно в раздел "{catname}"</i>
</a>
</div>'''
nicedit_textarea = '''<textarea name="html" style="width: 100%;" id="nicedit-js-area">{input_html}</textarea>'''
nicedit_js = r'''\
LyogTmljRWRpdCAtIE1pY3JvIElubGluZSBXWVNJV1lHCiAqIENvcHlyaWdodCAyMDA3LTIwMDgg
QnJpYW4gS2lyY2hvZmYKICoKICogTmljRWRpdCBpcyBkaXN0cmlidXRlZCB1bmRlciB0aGUgdGVy
bXMgb2YgdGhlIE1JVCBsaWNlbnNlCiAqIEZvciBtb3JlIGluZm9ybWF0aW9uIHZpc2l0IGh0dHA6
Ly9uaWNlZGl0LmNvbS8KICogRG8gbm90IHJlbW92ZSB0aGlzIGNvcHlyaWdodCBtZXNzYWdlCiAq
Lwp2YXIgYmtFeHRlbmQgPSBmdW5jdGlvbigpewoJdmFyIGFyZ3MgPSBhcmd1bWVudHM7CglpZiAo
YXJncy5sZW5ndGggPT0gMSkgYXJncyA9IFt0aGlzLCBhcmdzWzBdXTsKCWZvciAodmFyIHByb3Ag
aW4gYXJnc1sxXSkgYXJnc1swXVtwcm9wXSA9IGFyZ3NbMV1bcHJvcF07CglyZXR1cm4gYXJnc1sw
XTsKfTsKZnVuY3Rpb24gYmtDbGFzcygpIHsgfQpia0NsYXNzLnByb3RvdHlwZS5jb25zdHJ1Y3Qg
PSBmdW5jdGlvbigpIHt9Owpia0NsYXNzLmV4dGVuZCA9IGZ1bmN0aW9uKGRlZikgewogIHZhciBj
bGFzc0RlZiA9IGZ1bmN0aW9uKCkgewogICAgICBpZiAoYXJndW1lbnRzWzBdICE9PSBia0NsYXNz
KSB7IHJldHVybiB0aGlzLmNvbnN0cnVjdC5hcHBseSh0aGlzLCBhcmd1bWVudHMpOyB9CiAgfTsK
ICB2YXIgcHJvdG8gPSBuZXcgdGhpcyhia0NsYXNzKTsKICBia0V4dGVuZChwcm90byxkZWYpOwog
IGNsYXNzRGVmLnByb3RvdHlwZSA9IHByb3RvOwogIGNsYXNzRGVmLmV4dGVuZCA9IHRoaXMuZXh0
ZW5kOwogIHJldHVybiBjbGFzc0RlZjsKfTsKCnZhciBia0VsZW1lbnQgPSBia0NsYXNzLmV4dGVu
ZCh7Cgljb25zdHJ1Y3QgOiBmdW5jdGlvbihlbG0sZCkgewoJCWlmKHR5cGVvZihlbG0pID09ICJz
dHJpbmciKSB7CgkJCWVsbSA9IChkIHx8IGRvY3VtZW50KS5jcmVhdGVFbGVtZW50KGVsbSk7CgkJ
fQoJCWVsbSA9ICRCSyhlbG0pOwoJCXJldHVybiBlbG07Cgl9LAoKCWFwcGVuZFRvIDogZnVuY3Rp
b24oZWxtKSB7CgkJZWxtLmFwcGVuZENoaWxkKHRoaXMpOwoJCXJldHVybiB0aGlzOwoJfSwKCglh
cHBlbmRCZWZvcmUgOiBmdW5jdGlvbihlbG0pIHsKCQllbG0ucGFyZW50Tm9kZS5pbnNlcnRCZWZv
cmUodGhpcyxlbG0pOwoJCXJldHVybiB0aGlzOwoJfSwKCglhZGRFdmVudCA6IGZ1bmN0aW9uKHR5
cGUsIGZuKSB7CgkJYmtMaWIuYWRkRXZlbnQodGhpcyx0eXBlLGZuKTsKCQlyZXR1cm4gdGhpczsK
CX0sCgoJc2V0Q29udGVudCA6IGZ1bmN0aW9uKGMpIHsKCQl0aGlzLmlubmVySFRNTCA9IGM7CgkJ
cmV0dXJuIHRoaXM7Cgl9LAoKCXBvcyA6IGZ1bmN0aW9uKCkgewoJCXZhciBjdXJsZWZ0ID0gY3Vy
dG9wID0gMDsKCQl2YXIgbyA9IG9iaiA9IHRoaXM7CgkJaWYgKG9iai5vZmZzZXRQYXJlbnQpIHsK
CQkJZG8gewoJCQkJY3VybGVmdCArPSBvYmoub2Zmc2V0TGVmdDsKCQkJCWN1cnRvcCArPSBvYmou
b2Zmc2V0VG9wOwoJCQl9IHdoaWxlIChvYmogPSBvYmoub2Zmc2V0UGFyZW50KTsKCQl9CgkJdmFy
IGIgPSAoIXdpbmRvdy5vcGVyYSkgPyBwYXJzZUludCh0aGlzLmdldFN0eWxlKCdib3JkZXItd2lk
dGgnKSB8fCB0aGlzLnN0eWxlLmJvcmRlcikgfHwgMCA6IDA7CgkJcmV0dXJuIFtjdXJsZWZ0K2Is
Y3VydG9wK2IrdGhpcy5vZmZzZXRIZWlnaHRdOwoJfSwKCglub1NlbGVjdCA6IGZ1bmN0aW9uKCkg
ewoJCWJrTGliLm5vU2VsZWN0KHRoaXMpOwoJCXJldHVybiB0aGlzOwoJfSwKCglwYXJlbnRUYWcg
OiBmdW5jdGlvbih0KSB7CgkJdmFyIGVsbSA9IHRoaXM7CgkJIGRvIHsKCQkJaWYoZWxtICYmIGVs
bS5ub2RlTmFtZSAmJiBlbG0ubm9kZU5hbWUudG9VcHBlckNhc2UoKSA9PSB0KSB7CgkJCQlyZXR1
cm4gZWxtOwoJCQl9CgkJCWVsbSA9IGVsbS5wYXJlbnROb2RlOwoJCX0gd2hpbGUoZWxtKTsKCQly
ZXR1cm4gZmFsc2U7Cgl9LAoKCWhhc0NsYXNzIDogZnVuY3Rpb24oY2xzKSB7CgkJcmV0dXJuIHRo
aXMuY2xhc3NOYW1lLm1hdGNoKG5ldyBSZWdFeHAoJyhcXHN8XiluaWNFZGl0LScrY2xzKycoXFxz
fCQpJykpOwoJfSwKCglhZGRDbGFzcyA6IGZ1bmN0aW9uKGNscykgewoJCWlmICghdGhpcy5oYXND
bGFzcyhjbHMpKSB7IHRoaXMuY2xhc3NOYW1lICs9ICIgbmljRWRpdC0iK2NscyB9OwoJCXJldHVy
biB0aGlzOwoJfSwKCglyZW1vdmVDbGFzcyA6IGZ1bmN0aW9uKGNscykgewoJCWlmICh0aGlzLmhh
c0NsYXNzKGNscykpIHsKCQkJdGhpcy5jbGFzc05hbWUgPSB0aGlzLmNsYXNzTmFtZS5yZXBsYWNl
KG5ldyBSZWdFeHAoJyhcXHN8XiluaWNFZGl0LScrY2xzKycoXFxzfCQpJyksJyAnKTsKCQl9CgkJ
cmV0dXJuIHRoaXM7Cgl9LAoKCXNldFN0eWxlIDogZnVuY3Rpb24oc3QpIHsKCQl2YXIgZWxtU3R5
bGUgPSB0aGlzLnN0eWxlOwoJCWZvcih2YXIgaXRtIGluIHN0KSB7CgkJCXN3aXRjaChpdG0pIHsK
CQkJCWNhc2UgJ2Zsb2F0JzoKCQkJCQllbG1TdHlsZVsnY3NzRmxvYXQnXSA9IGVsbVN0eWxlWydz
dHlsZUZsb2F0J10gPSBzdFtpdG1dOwoJCQkJCWJyZWFrOwoJCQkJY2FzZSAnb3BhY2l0eSc6CgkJ
CQkJZWxtU3R5bGUub3BhY2l0eSA9IHN0W2l0bV07CgkJCQkJZWxtU3R5bGUuZmlsdGVyID0gImFs
cGhhKG9wYWNpdHk9IiArIE1hdGgucm91bmQoc3RbaXRtXSoxMDApICsgIikiOwoJCQkJCWJyZWFr
OwoJCQkJY2FzZSAnY2xhc3NOYW1lJzoKCQkJCQl0aGlzLmNsYXNzTmFtZSA9IHN0W2l0bV07CgkJ
CQkJYnJlYWs7CgkJCQlkZWZhdWx0OgoJCQkJCS8vaWYoZG9jdW1lbnQuY29tcGF0TW9kZSB8fCBp
dG0gIT0gImN1cnNvciIpIHsgLy8gTmFzdHkgV29ya2Fyb3VuZCBmb3IgSUUgNS41CgkJCQkJCWVs
bVN0eWxlW2l0bV0gPSBzdFtpdG1dOwoJCQkJCS8vfQoJCQl9CgkJfQoJCXJldHVybiB0aGlzOwoJ
fSwKCglnZXRTdHlsZSA6IGZ1bmN0aW9uKCBjc3NSdWxlLCBkICkgewoJCXZhciBkb2MgPSAoIWQp
ID8gZG9jdW1lbnQuZGVmYXVsdFZpZXcgOiBkOwoJCWlmKHRoaXMubm9kZVR5cGUgPT0gMSkKCQly
ZXR1cm4gKGRvYyAmJiBkb2MuZ2V0Q29tcHV0ZWRTdHlsZSkgPyBkb2MuZ2V0Q29tcHV0ZWRTdHls
ZSggdGhpcywgbnVsbCApLmdldFByb3BlcnR5VmFsdWUoY3NzUnVsZSkgOiB0aGlzLmN1cnJlbnRT
dHlsZVsgYmtMaWIuY2FtZWxpemUoY3NzUnVsZSkgXTsKCX0sCgoJcmVtb3ZlIDogZnVuY3Rpb24o
KSB7CgkJdGhpcy5wYXJlbnROb2RlLnJlbW92ZUNoaWxkKHRoaXMpOwoJCXJldHVybiB0aGlzOwoJ
fSwKCglzZXRBdHRyaWJ1dGVzIDogZnVuY3Rpb24oYXQpIHsKCQlmb3IodmFyIGl0bSBpbiBhdCkg
ewoJCQl0aGlzW2l0bV0gPSBhdFtpdG1dOwoJCX0KCQlyZXR1cm4gdGhpczsKCX0KfSk7Cgp2YXIg
YmtMaWIgPSB7Cglpc01TSUUgOiAobmF2aWdhdG9yLmFwcFZlcnNpb24uaW5kZXhPZigiTVNJRSIp
ICE9IC0xKSwKCglhZGRFdmVudCA6IGZ1bmN0aW9uKG9iaiwgdHlwZSwgZm4pIHsKCQkob2JqLmFk
ZEV2ZW50TGlzdGVuZXIpID8gb2JqLmFkZEV2ZW50TGlzdGVuZXIoIHR5cGUsIGZuLCBmYWxzZSAp
IDogb2JqLmF0dGFjaEV2ZW50KCJvbiIrdHlwZSwgZm4pOwoJfSwKCgl0b0FycmF5IDogZnVuY3Rp
b24oaXRlcmFibGUpIHsKCQl2YXIgbGVuZ3RoID0gaXRlcmFibGUubGVuZ3RoLCByZXN1bHRzID0g
bmV3IEFycmF5KGxlbmd0aCk7CiAgICAJd2hpbGUgKGxlbmd0aC0tKSB7IHJlc3VsdHNbbGVuZ3Ro
XSA9IGl0ZXJhYmxlW2xlbmd0aF0gfTsKICAgIAlyZXR1cm4gcmVzdWx0czsKCX0sCgoJbm9TZWxl
Y3QgOiBmdW5jdGlvbihlbGVtZW50KSB7CgkJaWYoZWxlbWVudC5zZXRBdHRyaWJ1dGUgJiYgZWxl
bWVudC5ub2RlTmFtZS50b0xvd2VyQ2FzZSgpICE9ICdpbnB1dCcgJiYgZWxlbWVudC5ub2RlTmFt
ZS50b0xvd2VyQ2FzZSgpICE9ICd0ZXh0YXJlYScpIHsKCQkJZWxlbWVudC5zZXRBdHRyaWJ1dGUo
J3Vuc2VsZWN0YWJsZScsJ29uJyk7CgkJfQoJCWZvcih2YXIgaT0wO2k8ZWxlbWVudC5jaGlsZE5v
ZGVzLmxlbmd0aDtpKyspIHsKCQkJYmtMaWIubm9TZWxlY3QoZWxlbWVudC5jaGlsZE5vZGVzW2ld
KTsKCQl9Cgl9LAoJY2FtZWxpemUgOiBmdW5jdGlvbihzKSB7CgkJcmV0dXJuIHMucmVwbGFjZSgv
XC0oLikvZywgZnVuY3Rpb24obSwgbCl7cmV0dXJuIGwudG9VcHBlckNhc2UoKX0pOwoJfSwKCWlu
QXJyYXkgOiBmdW5jdGlvbihhcnIsaXRlbSkgewoJICAgIHJldHVybiAoYmtMaWIuc2VhcmNoKGFy
cixpdGVtKSAhPSBudWxsKTsKCX0sCglzZWFyY2ggOiBmdW5jdGlvbihhcnIsaXRtKSB7CgkJZm9y
KHZhciBpPTA7IGkgPCBhcnIubGVuZ3RoOyBpKyspIHsKCQkJaWYoYXJyW2ldID09IGl0bSkKCQkJ
CXJldHVybiBpOwoJCX0KCQlyZXR1cm4gbnVsbDsKCX0sCgljYW5jZWxFdmVudCA6IGZ1bmN0aW9u
KGUpIHsKCQllID0gZSB8fCB3aW5kb3cuZXZlbnQ7CgkJaWYoZS5wcmV2ZW50RGVmYXVsdCAmJiBl
LnN0b3BQcm9wYWdhdGlvbikgewoJCQllLnByZXZlbnREZWZhdWx0KCk7CgkJCWUuc3RvcFByb3Bh
Z2F0aW9uKCk7CgkJfQoJCXJldHVybiBmYWxzZTsKCX0sCglkb21Mb2FkIDogW10sCglkb21Mb2Fk
ZWQgOiBmdW5jdGlvbigpIHsKCQlpZiAoYXJndW1lbnRzLmNhbGxlZS5kb25lKSByZXR1cm47CgkJ
YXJndW1lbnRzLmNhbGxlZS5kb25lID0gdHJ1ZTsKCQlmb3IgKGkgPSAwO2kgPCBia0xpYi5kb21M
b2FkLmxlbmd0aDtpKyspIGJrTGliLmRvbUxvYWRbaV0oKTsKCX0sCglvbkRvbUxvYWRlZCA6IGZ1
bmN0aW9uKGZpcmVUaGlzKSB7CgkJdGhpcy5kb21Mb2FkLnB1c2goZmlyZVRoaXMpOwoJCWlmIChk
b2N1bWVudC5hZGRFdmVudExpc3RlbmVyKSB7CgkJCWRvY3VtZW50LmFkZEV2ZW50TGlzdGVuZXIo
IkRPTUNvbnRlbnRMb2FkZWQiLCBia0xpYi5kb21Mb2FkZWQsIG51bGwpOwoJCX0gZWxzZSBpZihi
a0xpYi5pc01TSUUpIHsKCQkJZG9jdW1lbnQud3JpdGUoIjxzdHlsZT4ubmljRWRpdC1tYWluIHAg
eyBtYXJnaW46IDA7IH08L3N0eWxlPjxzY3IiKyJpcHQgaWQ9X19pZV9vbmxvYWQgZGVmZXIgIiAr
ICgobG9jYXRpb24ucHJvdG9jb2wgPT0gImh0dHBzOiIpID8gInNyYz0namF2YXNjcmlwdDp2b2lk
KDApJyIgOiAic3JjPS8vMCIpICsgIj48XC9zY3IiKyJpcHQ+Iik7CgkJCSRCSygiX19pZV9vbmxv
YWQiKS5vbnJlYWR5c3RhdGVjaGFuZ2UgPSBmdW5jdGlvbigpIHsKCQkJICAgIGlmICh0aGlzLnJl
YWR5U3RhdGUgPT0gImNvbXBsZXRlIil7YmtMaWIuZG9tTG9hZGVkKCk7fQoJCQl9OwoJCX0KCSAg
ICB3aW5kb3cub25sb2FkID0gYmtMaWIuZG9tTG9hZGVkOwoJfQp9OwoKZnVuY3Rpb24gJEJLKGVs
bSkgewoJaWYodHlwZW9mKGVsbSkgPT0gInN0cmluZyIpIHsKCQllbG0gPSBkb2N1bWVudC5nZXRF
bGVtZW50QnlJZChlbG0pOwoJfQoJcmV0dXJuIChlbG0gJiYgIWVsbS5hcHBlbmRUbykgPyBia0V4
dGVuZChlbG0sYmtFbGVtZW50LnByb3RvdHlwZSkgOiBlbG07Cn0KCnZhciBia0V2ZW50ID0gewoJ
YWRkRXZlbnQgOiBmdW5jdGlvbihldlR5cGUsIGV2RnVuYykgewoJCWlmKGV2RnVuYykgewoJCQl0
aGlzLmV2ZW50TGlzdCA9IHRoaXMuZXZlbnRMaXN0IHx8IHt9OwoJCQl0aGlzLmV2ZW50TGlzdFtl
dlR5cGVdID0gdGhpcy5ldmVudExpc3RbZXZUeXBlXSB8fCBbXTsKCQkJdGhpcy5ldmVudExpc3Rb
ZXZUeXBlXS5wdXNoKGV2RnVuYyk7CgkJfQoJCXJldHVybiB0aGlzOwoJfSwKCWZpcmVFdmVudCA6
IGZ1bmN0aW9uKCkgewoJCXZhciBhcmdzID0gYmtMaWIudG9BcnJheShhcmd1bWVudHMpLCBldlR5
cGUgPSBhcmdzLnNoaWZ0KCk7CgkJaWYodGhpcy5ldmVudExpc3QgJiYgdGhpcy5ldmVudExpc3Rb
ZXZUeXBlXSkgewoJCQlmb3IodmFyIGk9MDtpPHRoaXMuZXZlbnRMaXN0W2V2VHlwZV0ubGVuZ3Ro
O2krKykgewoJCQkJdGhpcy5ldmVudExpc3RbZXZUeXBlXVtpXS5hcHBseSh0aGlzLGFyZ3MpOwoJ
CQl9CgkJfQoJfQp9OwoKZnVuY3Rpb24gX18ocykgewoJcmV0dXJuIHM7Cn0KCkZ1bmN0aW9uLnBy
b3RvdHlwZS5jbG9zdXJlID0gZnVuY3Rpb24oKSB7CiAgdmFyIF9fbWV0aG9kID0gdGhpcywgYXJn
cyA9IGJrTGliLnRvQXJyYXkoYXJndW1lbnRzKSwgb2JqID0gYXJncy5zaGlmdCgpOwogIHJldHVy
biBmdW5jdGlvbigpIHsgaWYodHlwZW9mKGJrTGliKSAhPSAndW5kZWZpbmVkJykgeyByZXR1cm4g
X19tZXRob2QuYXBwbHkob2JqLGFyZ3MuY29uY2F0KGJrTGliLnRvQXJyYXkoYXJndW1lbnRzKSkp
OyB9IH07Cn0KCkZ1bmN0aW9uLnByb3RvdHlwZS5jbG9zdXJlTGlzdGVuZXIgPSBmdW5jdGlvbigp
IHsKICAJdmFyIF9fbWV0aG9kID0gdGhpcywgYXJncyA9IGJrTGliLnRvQXJyYXkoYXJndW1lbnRz
KSwgb2JqZWN0ID0gYXJncy5zaGlmdCgpOwogIAlyZXR1cm4gZnVuY3Rpb24oZSkgewogIAllID0g
ZSB8fCB3aW5kb3cuZXZlbnQ7CiAgCWlmKGUudGFyZ2V0KSB7IHZhciB0YXJnZXQgPSBlLnRhcmdl
dDsgfSBlbHNlIHsgdmFyIHRhcmdldCA9ICBlLnNyY0VsZW1lbnQgfTsKCSAgCXJldHVybiBfX21l
dGhvZC5hcHBseShvYmplY3QsIFtlLHRhcmdldF0uY29uY2F0KGFyZ3MpICk7Cgl9Owp9CgoKLyog
U1RBUlQgQ09ORklHICovCgp2YXIgbmljRWRpdG9yQ29uZmlnID0gYmtDbGFzcy5leHRlbmQoewoJ
YnV0dG9ucyA6IHsKCQknYm9sZCcgOiB7bmFtZSA6IF9fKCdDbGljayB0byBCb2xkJyksIGNvbW1h
bmQgOiAnQm9sZCcsIHRhZ3MgOiBbJ0InLCdTVFJPTkcnXSwgY3NzIDogeydmb250LXdlaWdodCcg
OiAnYm9sZCd9LCBrZXkgOiAnYid9LAoJCSdpdGFsaWMnIDoge25hbWUgOiBfXygnQ2xpY2sgdG8g
SXRhbGljJyksIGNvbW1hbmQgOiAnSXRhbGljJywgdGFncyA6IFsnRU0nLCdJJ10sIGNzcyA6IHsn
Zm9udC1zdHlsZScgOiAnaXRhbGljJ30sIGtleSA6ICdpJ30sCgkJJ3VuZGVybGluZScgOiB7bmFt
ZSA6IF9fKCdDbGljayB0byBVbmRlcmxpbmUnKSwgY29tbWFuZCA6ICdVbmRlcmxpbmUnLCB0YWdz
IDogWydVJ10sIGNzcyA6IHsndGV4dC1kZWNvcmF0aW9uJyA6ICd1bmRlcmxpbmUnfSwga2V5IDog
J3UnfSwKCQknbGVmdCcgOiB7bmFtZSA6IF9fKCdMZWZ0IEFsaWduJyksIGNvbW1hbmQgOiAnanVz
dGlmeWxlZnQnLCBub0FjdGl2ZSA6IHRydWV9LAoJCSdjZW50ZXInIDoge25hbWUgOiBfXygnQ2Vu
dGVyIEFsaWduJyksIGNvbW1hbmQgOiAnanVzdGlmeWNlbnRlcicsIG5vQWN0aXZlIDogdHJ1ZX0s
CgkJJ3JpZ2h0JyA6IHtuYW1lIDogX18oJ1JpZ2h0IEFsaWduJyksIGNvbW1hbmQgOiAnanVzdGlm
eXJpZ2h0Jywgbm9BY3RpdmUgOiB0cnVlfSwKCQknanVzdGlmeScgOiB7bmFtZSA6IF9fKCdKdXN0
aWZ5IEFsaWduJyksIGNvbW1hbmQgOiAnanVzdGlmeWZ1bGwnLCBub0FjdGl2ZSA6IHRydWV9LAoJ
CSdvbCcgOiB7bmFtZSA6IF9fKCdJbnNlcnQgT3JkZXJlZCBMaXN0JyksIGNvbW1hbmQgOiAnaW5z
ZXJ0b3JkZXJlZGxpc3QnLCB0YWdzIDogWydPTCddfSwKCQkndWwnIDogCXtuYW1lIDogX18oJ0lu
c2VydCBVbm9yZGVyZWQgTGlzdCcpLCBjb21tYW5kIDogJ2luc2VydHVub3JkZXJlZGxpc3QnLCB0
YWdzIDogWydVTCddfSwKCQknc3Vic2NyaXB0JyA6IHtuYW1lIDogX18oJ0NsaWNrIHRvIFN1YnNj
cmlwdCcpLCBjb21tYW5kIDogJ3N1YnNjcmlwdCcsIHRhZ3MgOiBbJ1NVQiddfSwKCQknc3VwZXJz
Y3JpcHQnIDoge25hbWUgOiBfXygnQ2xpY2sgdG8gU3VwZXJzY3JpcHQnKSwgY29tbWFuZCA6ICdz
dXBlcnNjcmlwdCcsIHRhZ3MgOiBbJ1NVUCddfSwKCQknc3RyaWtldGhyb3VnaCcgOiB7bmFtZSA6
IF9fKCdDbGljayB0byBTdHJpa2UgVGhyb3VnaCcpLCBjb21tYW5kIDogJ3N0cmlrZVRocm91Z2gn
LCBjc3MgOiB7J3RleHQtZGVjb3JhdGlvbicgOiAnbGluZS10aHJvdWdoJ319LAoJCSdyZW1vdmVm
b3JtYXQnIDoge25hbWUgOiBfXygnUmVtb3ZlIEZvcm1hdHRpbmcnKSwgY29tbWFuZCA6ICdyZW1v
dmVmb3JtYXQnLCBub0FjdGl2ZSA6IHRydWV9LAoJCSdpbmRlbnQnIDoge25hbWUgOiBfXygnSW5k
ZW50IFRleHQnKSwgY29tbWFuZCA6ICdpbmRlbnQnLCBub0FjdGl2ZSA6IHRydWV9LAoJCSdvdXRk
ZW50JyA6IHtuYW1lIDogX18oJ1JlbW92ZSBJbmRlbnQnKSwgY29tbWFuZCA6ICdvdXRkZW50Jywg
bm9BY3RpdmUgOiB0cnVlfSwKCQknaHInIDoge25hbWUgOiBfXygnSG9yaXpvbnRhbCBSdWxlJyks
IGNvbW1hbmQgOiAnaW5zZXJ0SG9yaXpvbnRhbFJ1bGUnLCBub0FjdGl2ZSA6IHRydWV9Cgl9LAoJ
aWNvbnNQYXRoIDogJy4uL25pY0VkaXRvckljb25zLmdpZicsCglidXR0b25MaXN0IDogWydzYXZl
JywnYm9sZCcsJ2l0YWxpYycsJ3VuZGVybGluZScsJ2xlZnQnLCdjZW50ZXInLCdyaWdodCcsJ2p1
c3RpZnknLCdvbCcsJ3VsJywnZm9udFNpemUnLCdmb250RmFtaWx5JywnZm9udEZvcm1hdCcsJ2lu
ZGVudCcsJ291dGRlbnQnLCdpbWFnZScsJ3VwbG9hZCcsJ2xpbmsnLCd1bmxpbmsnLCdmb3JlY29s
b3InLCdiZ2NvbG9yJ10sCglpY29uTGlzdCA6IHsieGh0bWwiOjEsImJnY29sb3IiOjIsImZvcmVj
b2xvciI6MywiYm9sZCI6NCwiY2VudGVyIjo1LCJociI6NiwiaW5kZW50Ijo3LCJpdGFsaWMiOjgs
Imp1c3RpZnkiOjksImxlZnQiOjEwLCJvbCI6MTEsIm91dGRlbnQiOjEyLCJyZW1vdmVmb3JtYXQi
OjEzLCJyaWdodCI6MTQsInNhdmUiOjI1LCJzdHJpa2V0aHJvdWdoIjoxNiwic3Vic2NyaXB0Ijox
Nywic3VwZXJzY3JpcHQiOjE4LCJ1bCI6MTksInVuZGVybGluZSI6MjAsImltYWdlIjoyMSwibGlu
ayI6MjIsInVubGluayI6MjMsImNsb3NlIjoyNCwiYXJyb3ciOjI2LCJ1cGxvYWQiOjI3fSwKCWlu
aXRXaXRoTGluZUJyZWFrOiB0cnVlCn0pOwovKiBFTkQgQ09ORklHICovCgoKdmFyIG5pY0VkaXRv
cnMgPSB7CgluaWNQbHVnaW5zIDogW10sCgllZGl0b3JzIDogW10sCgoJcmVnaXN0ZXJQbHVnaW4g
OiBmdW5jdGlvbihwbHVnaW4sb3B0aW9ucykgewoJCXRoaXMubmljUGx1Z2lucy5wdXNoKHtwIDog
cGx1Z2luLCBvIDogb3B0aW9uc30pOwoJfSwKCglhbGxUZXh0QXJlYXMgOiBmdW5jdGlvbihuaWNP
cHRpb25zKSB7CgkJdmFyIHRleHRhcmVhcyA9IGRvY3VtZW50LmdldEVsZW1lbnRzQnlUYWdOYW1l
KCJ0ZXh0YXJlYSIpOwoJCWZvcih2YXIgaT0wO2k8dGV4dGFyZWFzLmxlbmd0aDtpKyspIHsKCQkJ
bmljRWRpdG9ycy5lZGl0b3JzLnB1c2gobmV3IG5pY0VkaXRvcihuaWNPcHRpb25zKS5wYW5lbElu
c3RhbmNlKHRleHRhcmVhc1tpXSkpOwoJCX0KCQlyZXR1cm4gbmljRWRpdG9ycy5lZGl0b3JzOwoJ
fSwKCglmaW5kRWRpdG9yIDogZnVuY3Rpb24oZSkgewoJCXZhciBlZGl0b3JzID0gbmljRWRpdG9y
cy5lZGl0b3JzOwoJCWZvcih2YXIgaT0wO2k8ZWRpdG9ycy5sZW5ndGg7aSsrKSB7CgkJCWlmKGVk
aXRvcnNbaV0uaW5zdGFuY2VCeUlkKGUpKSB7CgkJCQlyZXR1cm4gZWRpdG9yc1tpXTsgLy8gciBp
cyBhbiBpbnN0YW5jZSBvZiBuaWNFZGl0b3JJbnN0YW5jZSB0aGVyZWZvcmUgaXQgZG9lcyBub3Qg
aGF2ZSByZW1vdmVJbnN0YW5jZSBvciByZW1vdmVQYW5lbCBtZXRob2RzCgkJCX0KCQl9Cgl9Cn07
CgoKdmFyIG5pY0VkaXRvciA9IGJrQ2xhc3MuZXh0ZW5kKHsKCWNvbnN0cnVjdCA6IGZ1bmN0aW9u
KG8pIHsKCQl0aGlzLm9wdGlvbnMgPSBuZXcgbmljRWRpdG9yQ29uZmlnKCk7CgkJYmtFeHRlbmQo
dGhpcy5vcHRpb25zLG8pOwoJCXRoaXMubmljSW5zdGFuY2VzID0gbmV3IEFycmF5KCk7CgkJdGhp
cy5sb2FkZWRQbHVnaW5zID0gbmV3IEFycmF5KCk7CgoJCXZhciBwbHVnaW5zID0gbmljRWRpdG9y
cy5uaWNQbHVnaW5zOwoJCWZvcih2YXIgaT0wO2k8cGx1Z2lucy5sZW5ndGg7aSsrKSB7CgkJCXRo
aXMubG9hZGVkUGx1Z2lucy5wdXNoKG5ldyBwbHVnaW5zW2ldLnAodGhpcyxwbHVnaW5zW2ldLm8p
KTsKCQl9CgkJbmljRWRpdG9ycy5lZGl0b3JzLnB1c2godGhpcyk7CgkJYmtMaWIuYWRkRXZlbnQo
ZG9jdW1lbnQuYm9keSwnbW91c2Vkb3duJywgdGhpcy5zZWxlY3RDaGVjay5jbG9zdXJlTGlzdGVu
ZXIodGhpcykgKTsKCX0sCgoJcGFuZWxJbnN0YW5jZSA6IGZ1bmN0aW9uKGUsbykgewoJCWUgPSB0
aGlzLmNoZWNrUmVwbGFjZSgkQksoZSkpOwoJCXZhciBwYW5lbEVsbSA9IG5ldyBia0VsZW1lbnQo
J0RJVicpLnNldFN0eWxlKHt3aWR0aCA6IChwYXJzZUludChlLmdldFN0eWxlKCd3aWR0aCcpKSB8
fCBlLmNsaWVudFdpZHRoKSsncHgnfSkuYXBwZW5kQmVmb3JlKGUpOwoJCXRoaXMuc2V0UGFuZWwo
cGFuZWxFbG0pOwoJCXJldHVybiB0aGlzLmFkZEluc3RhbmNlKGUsbyk7Cgl9LAoKCWNoZWNrUmVw
bGFjZSA6IGZ1bmN0aW9uKGUpIHsKCQl2YXIgciA9IG5pY0VkaXRvcnMuZmluZEVkaXRvcihlKTsK
CQlpZihyKSB7CgkJCXIucmVtb3ZlSW5zdGFuY2UoZSk7CgkJCXIucmVtb3ZlUGFuZWwoKTsKCQl9
CgkJcmV0dXJuIGU7Cgl9LAoKCWFkZEluc3RhbmNlIDogZnVuY3Rpb24oZSxvKSB7CgkJZSA9IHRo
aXMuY2hlY2tSZXBsYWNlKCRCSyhlKSk7CgkJaWYoIGUuY29udGVudEVkaXRhYmxlIHx8ICEhd2lu
ZG93Lm9wZXJhICkgewoJCQl2YXIgbmV3SW5zdGFuY2UgPSBuZXcgbmljRWRpdG9ySW5zdGFuY2Uo
ZSxvLHRoaXMpOwoJCX0gZWxzZSB7CgkJCXZhciBuZXdJbnN0YW5jZSA9IG5ldyBuaWNFZGl0b3JJ
RnJhbWVJbnN0YW5jZShlLG8sdGhpcyk7CgkJfQoJCXRoaXMubmljSW5zdGFuY2VzLnB1c2gobmV3
SW5zdGFuY2UpOwoJCXJldHVybiB0aGlzOwoJfSwKCglyZW1vdmVJbnN0YW5jZSA6IGZ1bmN0aW9u
KGUpIHsKCQllID0gJEJLKGUpOwoJCXZhciBpbnN0YW5jZXMgPSB0aGlzLm5pY0luc3RhbmNlczsK
CQlmb3IodmFyIGk9MDtpPGluc3RhbmNlcy5sZW5ndGg7aSsrKSB7CgkJCWlmKGluc3RhbmNlc1tp
XS5lID09IGUpIHsKCQkJCWluc3RhbmNlc1tpXS5yZW1vdmUoKTsKCQkJCXRoaXMubmljSW5zdGFu
Y2VzLnNwbGljZShpLDEpOwoJCQl9CgkJfQoJfSwKCglyZW1vdmVQYW5lbCA6IGZ1bmN0aW9uKGUp
IHsKCQlpZih0aGlzLm5pY1BhbmVsKSB7CgkJCXRoaXMubmljUGFuZWwucmVtb3ZlKCk7CgkJCXRo
aXMubmljUGFuZWwgPSBudWxsOwoJCX0KCX0sCgoJaW5zdGFuY2VCeUlkIDogZnVuY3Rpb24oZSkg
ewoJCWUgPSAkQksoZSk7CgkJdmFyIGluc3RhbmNlcyA9IHRoaXMubmljSW5zdGFuY2VzOwoJCWZv
cih2YXIgaT0wO2k8aW5zdGFuY2VzLmxlbmd0aDtpKyspIHsKCQkJaWYoaW5zdGFuY2VzW2ldLmUg
PT0gZSkgewoJCQkJcmV0dXJuIGluc3RhbmNlc1tpXTsKCQkJfQoJCX0KCX0sCgoJc2V0UGFuZWwg
OiBmdW5jdGlvbihlKSB7CgkJdGhpcy5uaWNQYW5lbCA9IG5ldyBuaWNFZGl0b3JQYW5lbCgkQkso
ZSksdGhpcy5vcHRpb25zLHRoaXMpOwoJCXRoaXMuZmlyZUV2ZW50KCdwYW5lbCcsdGhpcy5uaWNQ
YW5lbCk7CgkJcmV0dXJuIHRoaXM7Cgl9LAoKCW5pY0NvbW1hbmQgOiBmdW5jdGlvbihjbWQsYXJn
cykgewoJCWlmKHRoaXMuc2VsZWN0ZWRJbnN0YW5jZSkgewoJCQl0aGlzLnNlbGVjdGVkSW5zdGFu
Y2UubmljQ29tbWFuZChjbWQsYXJncyk7CgkJfQoJfSwKCglnZXRJY29uIDogZnVuY3Rpb24oaWNv
bk5hbWUsb3B0aW9ucykgewoJCXZhciBpY29uID0gdGhpcy5vcHRpb25zLmljb25MaXN0W2ljb25O
YW1lXTsKCQl2YXIgZmlsZSA9IChvcHRpb25zLmljb25GaWxlcykgPyBvcHRpb25zLmljb25GaWxl
c1tpY29uTmFtZV0gOiAnJzsKCQlyZXR1cm4ge2JhY2tncm91bmRJbWFnZSA6ICJ1cmwoJyIrKChp
Y29uKSA/IHRoaXMub3B0aW9ucy5pY29uc1BhdGggOiBmaWxlKSsiJykiLCBiYWNrZ3JvdW5kUG9z
aXRpb24gOiAoKGljb24pID8gKChpY29uLTEpKi0xOCkgOiAwKSsncHggMHB4J307Cgl9LAoKCXNl
bGVjdENoZWNrIDogZnVuY3Rpb24oZSx0KSB7CgkJdmFyIGZvdW5kID0gZmFsc2U7CgkJZG97CgkJ
CWlmKHQuY2xhc3NOYW1lICYmIHQuY2xhc3NOYW1lLmluZGV4T2YoJ25pY0VkaXQnKSAhPSAtMSkg
ewoJCQkJcmV0dXJuIGZhbHNlOwoJCQl9CgkJfSB3aGlsZSh0ID0gdC5wYXJlbnROb2RlKTsKCQl0
aGlzLmZpcmVFdmVudCgnYmx1cicsdGhpcy5zZWxlY3RlZEluc3RhbmNlLHQpOwoJCXRoaXMubGFz
dFNlbGVjdGVkSW5zdGFuY2UgPSB0aGlzLnNlbGVjdGVkSW5zdGFuY2U7CgkJdGhpcy5zZWxlY3Rl
ZEluc3RhbmNlID0gbnVsbDsKCQlyZXR1cm4gZmFsc2U7Cgl9Cgp9KTsKbmljRWRpdG9yID0gbmlj
RWRpdG9yLmV4dGVuZChia0V2ZW50KTsKCgp2YXIgbmljRWRpdG9ySW5zdGFuY2UgPSBia0NsYXNz
LmV4dGVuZCh7Cglpc1NlbGVjdGVkIDogZmFsc2UsCgoJY29uc3RydWN0IDogZnVuY3Rpb24oZSxv
cHRpb25zLG5pY0VkaXRvcikgewoJCXRoaXMubmUgPSBuaWNFZGl0b3I7CgkJdGhpcy5lbG0gPSB0
aGlzLmUgPSBlOwoJCXRoaXMub3B0aW9ucyA9IG9wdGlvbnMgfHwge307CgoJCW5ld1ggPSBwYXJz
ZUludChlLmdldFN0eWxlKCd3aWR0aCcpKSB8fCBlLmNsaWVudFdpZHRoOwoJCW5ld1kgPSBwYXJz
ZUludChlLmdldFN0eWxlKCdoZWlnaHQnKSkgfHwgZS5jbGllbnRIZWlnaHQ7CgkJdGhpcy5pbml0
aWFsSGVpZ2h0ID0gbmV3WS04OwoKCQl2YXIgaXNUZXh0YXJlYSA9IChlLm5vZGVOYW1lLnRvTG93
ZXJDYXNlKCkgPT0gInRleHRhcmVhIik7CgkJaWYoaXNUZXh0YXJlYSB8fCB0aGlzLm9wdGlvbnMu
aGFzUGFuZWwpIHsKCQkJdmFyIGllN3MgPSAoYmtMaWIuaXNNU0lFICYmICEoKHR5cGVvZiBkb2N1
bWVudC5ib2R5LnN0eWxlLm1heEhlaWdodCAhPSAidW5kZWZpbmVkIikgJiYgZG9jdW1lbnQuY29t
cGF0TW9kZSA9PSAiQ1NTMUNvbXBhdCIpKQoJCQl2YXIgcyA9IHt3aWR0aDogbmV3WCsncHgnLCBi
b3JkZXIgOiAnMXB4IHNvbGlkICNjY2MnLCBib3JkZXJUb3AgOiAwLCBvdmVyZmxvd1kgOiAnYXV0
bycsIG92ZXJmbG93WDogJ2hpZGRlbicgfTsKCQkJc1soaWU3cykgPyAnaGVpZ2h0JyA6ICdtYXhI
ZWlnaHQnXSA9ICh0aGlzLm5lLm9wdGlvbnMubWF4SGVpZ2h0KSA/IHRoaXMubmUub3B0aW9ucy5t
YXhIZWlnaHQrJ3B4JyA6IG51bGw7CgkJCXRoaXMuZWRpdG9yQ29udGFpbiA9IG5ldyBia0VsZW1l
bnQoJ0RJVicpLnNldFN0eWxlKHMpLmFwcGVuZEJlZm9yZShlKTsKCQkJdmFyIGVkaXRvckVsbSA9
IG5ldyBia0VsZW1lbnQoJ0RJVicpLnNldFN0eWxlKHt3aWR0aCA6IChuZXdYLTgpKydweCcsIG1h
cmdpbjogJzRweCcsIG1pbkhlaWdodCA6IG5ld1krJ3B4J30pLmFkZENsYXNzKCdtYWluJykuYXBw
ZW5kVG8odGhpcy5lZGl0b3JDb250YWluKTsKCgkJCWUuc2V0U3R5bGUoe2Rpc3BsYXkgOiAnbm9u
ZSd9KTsKCgkJCWVkaXRvckVsbS5pbm5lckhUTUwgPSBlLmlubmVySFRNTDsKCQkJaWYoaXNUZXh0
YXJlYSkgewoJCQkJZWRpdG9yRWxtLnNldENvbnRlbnQoZS52YWx1ZSk7CgkJCQl0aGlzLmNvcHlF
bG0gPSBlOwoJCQkJdmFyIGYgPSBlLnBhcmVudFRhZygnRk9STScpOwoJCQkJaWYoZikgeyBia0xp
Yi5hZGRFdmVudCggZiwgJ3N1Ym1pdCcsIHRoaXMuc2F2ZUNvbnRlbnQuY2xvc3VyZSh0aGlzKSk7
IH0KCQkJfQoJCQllZGl0b3JFbG0uc2V0U3R5bGUoKGllN3MpID8ge2hlaWdodCA6IG5ld1krJ3B4
J30gOiB7b3ZlcmZsb3c6ICdoaWRkZW4nfSk7CgkJCXRoaXMuZWxtID0gZWRpdG9yRWxtOwoJCX0K
CQl0aGlzLm5lLmFkZEV2ZW50KCdibHVyJyx0aGlzLmJsdXIuY2xvc3VyZSh0aGlzKSk7CgoJCXRo
aXMuaW5pdCgpOwoJCXRoaXMuYmx1cigpOwoJfSwKCglpbml0IDogZnVuY3Rpb24oKSB7CgkJdGhp
cy5lbG0uc2V0QXR0cmlidXRlKCdjb250ZW50RWRpdGFibGUnLCd0cnVlJyk7CgkJaWYodGhpcy5n
ZXRDb250ZW50KCkgPT0gIiIgJiYgdGhpcy5vcHRpb25zLmluaXRXaXRoTGluZUJyZWFrKSB7CgkJ
CXRoaXMuc2V0Q29udGVudCgnPGJyIC8+Jyk7CgkJfQoJCXRoaXMuaW5zdGFuY2VEb2MgPSBkb2N1
bWVudC5kZWZhdWx0VmlldzsKCQl0aGlzLmVsbS5hZGRFdmVudCgnbW91c2Vkb3duJyx0aGlzLnNl
bGVjdGVkLmNsb3N1cmVMaXN0ZW5lcih0aGlzKSkuYWRkRXZlbnQoJ2tleXByZXNzJyx0aGlzLmtl
eURvd24uY2xvc3VyZUxpc3RlbmVyKHRoaXMpKS5hZGRFdmVudCgnZm9jdXMnLHRoaXMuc2VsZWN0
ZWQuY2xvc3VyZSh0aGlzKSkuYWRkRXZlbnQoJ2JsdXInLHRoaXMuYmx1ci5jbG9zdXJlKHRoaXMp
KS5hZGRFdmVudCgna2V5dXAnLHRoaXMuc2VsZWN0ZWQuY2xvc3VyZSh0aGlzKSk7CgkJdGhpcy5u
ZS5maXJlRXZlbnQoJ2FkZCcsdGhpcyk7Cgl9LAoKCXJlbW92ZSA6IGZ1bmN0aW9uKCkgewoJCXRo
aXMuc2F2ZUNvbnRlbnQoKTsKCQlpZih0aGlzLmNvcHlFbG0gfHwgdGhpcy5vcHRpb25zLmhhc1Bh
bmVsKSB7CgkJCXRoaXMuZWRpdG9yQ29udGFpbi5yZW1vdmUoKTsKCQkJdGhpcy5lLnNldFN0eWxl
KHsnZGlzcGxheScgOiAnYmxvY2snfSk7CgkJCXRoaXMubmUucmVtb3ZlUGFuZWwoKTsKCQl9CgkJ
dGhpcy5kaXNhYmxlKCk7CgkJdGhpcy5uZS5maXJlRXZlbnQoJ3JlbW92ZScsdGhpcyk7Cgl9LAoK
CWRpc2FibGUgOiBmdW5jdGlvbigpIHsKCQl0aGlzLmVsbS5zZXRBdHRyaWJ1dGUoJ2NvbnRlbnRF
ZGl0YWJsZScsJ2ZhbHNlJyk7Cgl9LAoKCWdldFNlbCA6IGZ1bmN0aW9uKCkgewoJCXJldHVybiAo
d2luZG93LmdldFNlbGVjdGlvbikgPyB3aW5kb3cuZ2V0U2VsZWN0aW9uKCkgOiBkb2N1bWVudC5z
ZWxlY3Rpb247Cgl9LAoKCWdldFJuZyA6IGZ1bmN0aW9uKCkgewoJCXZhciBzID0gdGhpcy5nZXRT
ZWwoKTsKCQlpZighcykgeyByZXR1cm4gbnVsbDsgfQoJCXJldHVybiAocy5yYW5nZUNvdW50ID4g
MCkgPyBzLmdldFJhbmdlQXQoMCkgOgoJCXMuY3JlYXRlUmFuZ2UgJiYgcy5jcmVhdGVSYW5nZSgp
IHx8IGRvY3VtZW50LmNyZWF0ZVJhbmdlKCk7Cgl9LAoKCXNlbFJuZyA6IGZ1bmN0aW9uKHJuZyxz
KSB7CgkJaWYod2luZG93LmdldFNlbGVjdGlvbikgewoJCQlzLnJlbW92ZUFsbFJhbmdlcygpOwoJ
CQlzLmFkZFJhbmdlKHJuZyk7CgkJfSBlbHNlIHsKCQkJcm5nLnNlbGVjdCgpOwoJCX0KCX0sCgoJ
c2VsRWxtIDogZnVuY3Rpb24oKSB7CgkJdmFyIHIgPSB0aGlzLmdldFJuZygpOwoJCWlmKHIuc3Rh
cnRDb250YWluZXIpIHsKCQkJdmFyIGNvbnRhaW4gPSByLnN0YXJ0Q29udGFpbmVyOwoJCQlpZihy
LmNsb25lQ29udGVudHMoKS5jaGlsZE5vZGVzLmxlbmd0aCA9PSAxKSB7CgkJCQlmb3IodmFyIGk9
MDtpPGNvbnRhaW4uY2hpbGROb2Rlcy5sZW5ndGg7aSsrKSB7CgkJCQkJdmFyIHJuZyA9IGNvbnRh
aW4uY2hpbGROb2Rlc1tpXS5vd25lckRvY3VtZW50LmNyZWF0ZVJhbmdlKCk7CgkJCQkJcm5nLnNl
bGVjdE5vZGUoY29udGFpbi5jaGlsZE5vZGVzW2ldKTsKCQkJCQlpZihyLmNvbXBhcmVCb3VuZGFy
eVBvaW50cyhSYW5nZS5TVEFSVF9UT19TVEFSVCxybmcpICE9IDEgJiYKCQkJCQkJci5jb21wYXJl
Qm91bmRhcnlQb2ludHMoUmFuZ2UuRU5EX1RPX0VORCxybmcpICE9IC0xKSB7CgkJCQkJCXJldHVy
biAkQksoY29udGFpbi5jaGlsZE5vZGVzW2ldKTsKCQkJCQl9CgkJCQl9CgkJCX0KCQkJcmV0dXJu
ICRCSyhjb250YWluKTsKCQl9IGVsc2UgewoJCQlyZXR1cm4gJEJLKCh0aGlzLmdldFNlbCgpLnR5
cGUgPT0gIkNvbnRyb2wiKSA/IHIuaXRlbSgwKSA6IHIucGFyZW50RWxlbWVudCgpKTsKCQl9Cgl9
LAoKCXNhdmVSbmcgOiBmdW5jdGlvbigpIHsKCQl0aGlzLnNhdmVkUmFuZ2UgPSB0aGlzLmdldFJu
ZygpOwoJCXRoaXMuc2F2ZWRTZWwgPSB0aGlzLmdldFNlbCgpOwoJfSwKCglyZXN0b3JlUm5nIDog
ZnVuY3Rpb24oKSB7CgkJaWYodGhpcy5zYXZlZFJhbmdlKSB7CgkJCXRoaXMuc2VsUm5nKHRoaXMu
c2F2ZWRSYW5nZSx0aGlzLnNhdmVkU2VsKTsKCQl9Cgl9LAoKCWtleURvd24gOiBmdW5jdGlvbihl
LHQpIHsKCQl0aGlzLm5lLmZpcmVFdmVudCgna2V5RG93bicsdGhpcyxlKTsKCgkJaWYoZS5jdHJs
S2V5KSB7CgkJCXRoaXMubmUuZmlyZUV2ZW50KCdrZXknLHRoaXMsZSk7CgkJfQoJfSwKCglzZWxl
Y3RlZCA6IGZ1bmN0aW9uKGUsdCkgewoJCWlmKCF0KSB7dCA9IHRoaXMuc2VsRWxtKCl9CgkJaWYo
IWUuY3RybEtleSkgewoJCQl2YXIgc2VsSW5zdGFuY2UgPSB0aGlzLm5lLnNlbGVjdGVkSW5zdGFu
Y2U7CgkJCWlmKHNlbEluc3RhbmNlICE9IHRoaXMpIHsKCQkJCWlmKHNlbEluc3RhbmNlKSB7CgkJ
CQkJdGhpcy5uZS5maXJlRXZlbnQoJ2JsdXInLHNlbEluc3RhbmNlLHQpOwoJCQkJfQoJCQkJdGhp
cy5uZS5zZWxlY3RlZEluc3RhbmNlID0gdGhpczsKCQkJCXRoaXMubmUuZmlyZUV2ZW50KCdmb2N1
cycsc2VsSW5zdGFuY2UsdCk7CgkJCX0KCQkJdGhpcy5uZS5maXJlRXZlbnQoJ3NlbGVjdGVkJyxz
ZWxJbnN0YW5jZSx0KTsKCQkJdGhpcy5pc0ZvY3VzZWQgPSB0cnVlOwoJCQl0aGlzLmVsbS5hZGRD
bGFzcygnc2VsZWN0ZWQnKTsKCQl9CgkJcmV0dXJuIGZhbHNlOwoJfSwKCglibHVyIDogZnVuY3Rp
b24oKSB7CgkJdGhpcy5pc0ZvY3VzZWQgPSBmYWxzZTsKCQl0aGlzLmVsbS5yZW1vdmVDbGFzcygn
c2VsZWN0ZWQnKTsKCX0sCgoJc2F2ZUNvbnRlbnQgOiBmdW5jdGlvbigpIHsKCQlpZih0aGlzLmNv
cHlFbG0gfHwgdGhpcy5vcHRpb25zLmhhc1BhbmVsKSB7CgkJCXRoaXMubmUuZmlyZUV2ZW50KCdz
YXZlJyx0aGlzKTsKCQkJKHRoaXMuY29weUVsbSkgPyB0aGlzLmNvcHlFbG0udmFsdWUgPSB0aGlz
LmdldENvbnRlbnQoKSA6IHRoaXMuZS5pbm5lckhUTUwgPSB0aGlzLmdldENvbnRlbnQoKTsKCQl9
Cgl9LAoKCWdldEVsbSA6IGZ1bmN0aW9uKCkgewoJCXJldHVybiB0aGlzLmVsbTsKCX0sCgoJZ2V0
Q29udGVudCA6IGZ1bmN0aW9uKCkgewoJCXRoaXMuY29udGVudCA9IHRoaXMuZ2V0RWxtKCkuaW5u
ZXJIVE1MOwoJCXRoaXMubmUuZmlyZUV2ZW50KCdnZXQnLHRoaXMpOwoJCXJldHVybiB0aGlzLmNv
bnRlbnQ7Cgl9LAoKCXNldENvbnRlbnQgOiBmdW5jdGlvbihlKSB7CgkJdGhpcy5jb250ZW50ID0g
ZTsKCQl0aGlzLm5lLmZpcmVFdmVudCgnc2V0Jyx0aGlzKTsKCQl0aGlzLmVsbS5pbm5lckhUTUwg
PSB0aGlzLmNvbnRlbnQ7Cgl9LAoKCW5pY0NvbW1hbmQgOiBmdW5jdGlvbihjbWQsYXJncykgewoJ
CWRvY3VtZW50LmV4ZWNDb21tYW5kKGNtZCxmYWxzZSxhcmdzKTsKCX0KfSk7Cgp2YXIgbmljRWRp
dG9ySUZyYW1lSW5zdGFuY2UgPSBuaWNFZGl0b3JJbnN0YW5jZS5leHRlbmQoewoJc2F2ZWRTdHls
ZXMgOiBbXSwKCglpbml0IDogZnVuY3Rpb24oKSB7CgkJdmFyIGMgPSB0aGlzLmVsbS5pbm5lckhU
TUwucmVwbGFjZSgvXlxzK3xccyskL2csICcnKTsKCQl0aGlzLmVsbS5pbm5lckhUTUwgPSAnJzsK
CQkoIWMpID8gYyA9ICI8YnIgLz4iIDogYzsKCQl0aGlzLmluaXRpYWxDb250ZW50ID0gYzsKCgkJ
dGhpcy5lbG1GcmFtZSA9IG5ldyBia0VsZW1lbnQoJ2lmcmFtZScpLnNldEF0dHJpYnV0ZXMoeydz
cmMnIDogJ2phdmFzY3JpcHQ6OycsICdmcmFtZUJvcmRlcicgOiAwLCAnYWxsb3dUcmFuc3BhcmVu
Y3knIDogJ3RydWUnLCAnc2Nyb2xsaW5nJyA6ICdubyd9KS5zZXRTdHlsZSh7aGVpZ2h0OiAnMTAw
cHgnLCB3aWR0aDogJzEwMCUnfSkuYWRkQ2xhc3MoJ2ZyYW1lJykuYXBwZW5kVG8odGhpcy5lbG0p
OwoKCQlpZih0aGlzLmNvcHlFbG0pIHsgdGhpcy5lbG1GcmFtZS5zZXRTdHlsZSh7d2lkdGggOiAo
dGhpcy5lbG0ub2Zmc2V0V2lkdGgtNCkrJ3B4J30pOyB9CgoJCXZhciBzdHlsZUxpc3QgPSBbJ2Zv
bnQtc2l6ZScsJ2ZvbnQtZmFtaWx5JywnZm9udC13ZWlnaHQnLCdjb2xvciddOwoJCWZvcihpdG0g
aW4gc3R5bGVMaXN0KSB7CgkJCXRoaXMuc2F2ZWRTdHlsZXNbYmtMaWIuY2FtZWxpemUoaXRtKV0g
PSB0aGlzLmVsbS5nZXRTdHlsZShpdG0pOwoJCX0KCgkJc2V0VGltZW91dCh0aGlzLmluaXRGcmFt
ZS5jbG9zdXJlKHRoaXMpLDUwKTsKCX0sCgoJZGlzYWJsZSA6IGZ1bmN0aW9uKCkgewoJCXRoaXMu
ZWxtLmlubmVySFRNTCA9IHRoaXMuZ2V0Q29udGVudCgpOwoJfSwKCglpbml0RnJhbWUgOiBmdW5j
dGlvbigpIHsKCQl2YXIgZmQgPSAkQksodGhpcy5lbG1GcmFtZS5jb250ZW50V2luZG93LmRvY3Vt
ZW50KTsKCQlmZC5kZXNpZ25Nb2RlID0gIm9uIjsKCQlmZC5vcGVuKCk7CgkJdmFyIGNzcyA9IHRo
aXMubmUub3B0aW9ucy5leHRlcm5hbENTUzsKCQlmZC53cml0ZSgnPGh0bWw+PGhlYWQ+JysoKGNz
cykgPyAnPGxpbmsgaHJlZj0iJytjc3MrJyIgcmVsPSJzdHlsZXNoZWV0IiB0eXBlPSJ0ZXh0L2Nz
cyIgLz4nIDogJycpKyc8L2hlYWQ+PGJvZHkgaWQ9Im5pY0VkaXRDb250ZW50IiBzdHlsZT0ibWFy
Z2luOiAwICFpbXBvcnRhbnQ7IGJhY2tncm91bmQtY29sb3I6IHRyYW5zcGFyZW50ICFpbXBvcnRh
bnQ7Ij4nK3RoaXMuaW5pdGlhbENvbnRlbnQrJzwvYm9keT48L2h0bWw+Jyk7CgkJZmQuY2xvc2Uo
KTsKCQl0aGlzLmZyYW1lRG9jID0gZmQ7CgoJCXRoaXMuZnJhbWVXaW4gPSAkQksodGhpcy5lbG1G
cmFtZS5jb250ZW50V2luZG93KTsKCQl0aGlzLmZyYW1lQ29udGVudCA9ICRCSyh0aGlzLmZyYW1l
V2luLmRvY3VtZW50LmJvZHkpLnNldFN0eWxlKHRoaXMuc2F2ZWRTdHlsZXMpOwoJCXRoaXMuaW5z
dGFuY2VEb2MgPSB0aGlzLmZyYW1lV2luLmRvY3VtZW50LmRlZmF1bHRWaWV3OwoKCQl0aGlzLmhl
aWdodFVwZGF0ZSgpOwoJCXRoaXMuZnJhbWVEb2MuYWRkRXZlbnQoJ21vdXNlZG93bicsIHRoaXMu
c2VsZWN0ZWQuY2xvc3VyZUxpc3RlbmVyKHRoaXMpKS5hZGRFdmVudCgna2V5dXAnLHRoaXMuaGVp
Z2h0VXBkYXRlLmNsb3N1cmVMaXN0ZW5lcih0aGlzKSkuYWRkRXZlbnQoJ2tleWRvd24nLHRoaXMu
a2V5RG93bi5jbG9zdXJlTGlzdGVuZXIodGhpcykpLmFkZEV2ZW50KCdrZXl1cCcsdGhpcy5zZWxl
Y3RlZC5jbG9zdXJlKHRoaXMpKTsKCQl0aGlzLm5lLmZpcmVFdmVudCgnYWRkJyx0aGlzKTsKCX0s
CgoJZ2V0RWxtIDogZnVuY3Rpb24oKSB7CgkJcmV0dXJuIHRoaXMuZnJhbWVDb250ZW50OwoJfSwK
CglzZXRDb250ZW50IDogZnVuY3Rpb24oYykgewoJCXRoaXMuY29udGVudCA9IGM7CgkJdGhpcy5u
ZS5maXJlRXZlbnQoJ3NldCcsdGhpcyk7CgkJdGhpcy5mcmFtZUNvbnRlbnQuaW5uZXJIVE1MID0g
dGhpcy5jb250ZW50OwoJCXRoaXMuaGVpZ2h0VXBkYXRlKCk7Cgl9LAoKCWdldFNlbCA6IGZ1bmN0
aW9uKCkgewoJCXJldHVybiAodGhpcy5mcmFtZVdpbikgPyB0aGlzLmZyYW1lV2luLmdldFNlbGVj
dGlvbigpIDogdGhpcy5mcmFtZURvYy5zZWxlY3Rpb247Cgl9LAoKCWhlaWdodFVwZGF0ZSA6IGZ1
bmN0aW9uKCkgewoJCXRoaXMuZWxtRnJhbWUuc3R5bGUuaGVpZ2h0ID0gTWF0aC5tYXgodGhpcy5m
cmFtZUNvbnRlbnQub2Zmc2V0SGVpZ2h0LHRoaXMuaW5pdGlhbEhlaWdodCkrJ3B4JzsKCX0sCgoJ
bmljQ29tbWFuZCA6IGZ1bmN0aW9uKGNtZCxhcmdzKSB7CgkJdGhpcy5mcmFtZURvYy5leGVjQ29t
bWFuZChjbWQsZmFsc2UsYXJncyk7CgkJc2V0VGltZW91dCh0aGlzLmhlaWdodFVwZGF0ZS5jbG9z
dXJlKHRoaXMpLDEwMCk7Cgl9CgoKfSk7CnZhciBuaWNFZGl0b3JQYW5lbCA9IGJrQ2xhc3MuZXh0
ZW5kKHsKCWNvbnN0cnVjdCA6IGZ1bmN0aW9uKGUsb3B0aW9ucyxuaWNFZGl0b3IpIHsKCQl0aGlz
LmVsbSA9IGU7CgkJdGhpcy5vcHRpb25zID0gb3B0aW9uczsKCQl0aGlzLm5lID0gbmljRWRpdG9y
OwoJCXRoaXMucGFuZWxCdXR0b25zID0gbmV3IEFycmF5KCk7CgkJdGhpcy5idXR0b25MaXN0ID0g
YmtFeHRlbmQoW10sdGhpcy5uZS5vcHRpb25zLmJ1dHRvbkxpc3QpOwoKCQl0aGlzLnBhbmVsQ29u
dGFpbiA9IG5ldyBia0VsZW1lbnQoJ0RJVicpLnNldFN0eWxlKHtvdmVyZmxvdyA6ICdoaWRkZW4n
LCB3aWR0aCA6ICcxMDAlJywgYm9yZGVyIDogJzFweCBzb2xpZCAjY2NjY2NjJywgYmFja2dyb3Vu
ZENvbG9yIDogJyNlZmVmZWYnfSkuYWRkQ2xhc3MoJ3BhbmVsQ29udGFpbicpOwoJCXRoaXMucGFu
ZWxFbG0gPSBuZXcgYmtFbGVtZW50KCdESVYnKS5zZXRTdHlsZSh7bWFyZ2luIDogJzJweCcsIG1h
cmdpblRvcCA6ICcwcHgnLCB6b29tIDogMSwgb3ZlcmZsb3cgOiAnaGlkZGVuJ30pLmFkZENsYXNz
KCdwYW5lbCcpLmFwcGVuZFRvKHRoaXMucGFuZWxDb250YWluKTsKCQl0aGlzLnBhbmVsQ29udGFp
bi5hcHBlbmRUbyhlKTsKCgkJdmFyIG9wdCA9IHRoaXMubmUub3B0aW9uczsKCQl2YXIgYnV0dG9u
cyA9IG9wdC5idXR0b25zOwoJCWZvcihidXR0b24gaW4gYnV0dG9ucykgewoJCQkJdGhpcy5hZGRC
dXR0b24oYnV0dG9uLG9wdCx0cnVlKTsKCQl9CgkJdGhpcy5yZW9yZGVyKCk7CgkJZS5ub1NlbGVj
dCgpOwoJfSwKCglhZGRCdXR0b24gOiBmdW5jdGlvbihidXR0b25OYW1lLG9wdGlvbnMsbm9PcmRl
cikgewoJCXZhciBidXR0b24gPSBvcHRpb25zLmJ1dHRvbnNbYnV0dG9uTmFtZV07CgkJdmFyIHR5
cGUgPSAoYnV0dG9uWyd0eXBlJ10pID8gZXZhbCgnKHR5cGVvZignK2J1dHRvblsndHlwZSddKycp
ID09ICJ1bmRlZmluZWQiKSA/IG51bGwgOiAnK2J1dHRvblsndHlwZSddKyc7JykgOiBuaWNFZGl0
b3JCdXR0b247CgkJdmFyIGhhc0J1dHRvbiA9IGJrTGliLmluQXJyYXkodGhpcy5idXR0b25MaXN0
LGJ1dHRvbk5hbWUpOwoJCWlmKHR5cGUgJiYgKGhhc0J1dHRvbiB8fCB0aGlzLm5lLm9wdGlvbnMu
ZnVsbFBhbmVsKSkgewoJCQl0aGlzLnBhbmVsQnV0dG9ucy5wdXNoKG5ldyB0eXBlKHRoaXMucGFu
ZWxFbG0sYnV0dG9uTmFtZSxvcHRpb25zLHRoaXMubmUpKTsKCQkJaWYoIWhhc0J1dHRvbikgewoJ
CQkJdGhpcy5idXR0b25MaXN0LnB1c2goYnV0dG9uTmFtZSk7CgkJCX0KCQl9Cgl9LAoKCWZpbmRC
dXR0b24gOiBmdW5jdGlvbihpdG0pIHsKCQlmb3IodmFyIGk9MDtpPHRoaXMucGFuZWxCdXR0b25z
Lmxlbmd0aDtpKyspIHsKCQkJaWYodGhpcy5wYW5lbEJ1dHRvbnNbaV0ubmFtZSA9PSBpdG0pCgkJ
CQlyZXR1cm4gdGhpcy5wYW5lbEJ1dHRvbnNbaV07CgkJfQoJfSwKCglyZW9yZGVyIDogZnVuY3Rp
b24oKSB7CgkJdmFyIGJsID0gdGhpcy5idXR0b25MaXN0OwoJCWZvcih2YXIgaT0wO2k8YmwubGVu
Z3RoO2krKykgewoJCQl2YXIgYnV0dG9uID0gdGhpcy5maW5kQnV0dG9uKGJsW2ldKTsKCQkJaWYo
YnV0dG9uKSB7CgkJCQl0aGlzLnBhbmVsRWxtLmFwcGVuZENoaWxkKGJ1dHRvbi5tYXJnaW4pOwoJ
CQl9CgkJfQoJfSwKCglyZW1vdmUgOiBmdW5jdGlvbigpIHsKCQl0aGlzLmVsbS5yZW1vdmUoKTsK
CX0KfSk7CnZhciBuaWNFZGl0b3JCdXR0b24gPSBia0NsYXNzLmV4dGVuZCh7CgoJY29uc3RydWN0
IDogZnVuY3Rpb24oZSxidXR0b25OYW1lLG9wdGlvbnMsbmljRWRpdG9yKSB7CgkJdGhpcy5vcHRp
b25zID0gb3B0aW9ucy5idXR0b25zW2J1dHRvbk5hbWVdOwoJCXRoaXMubmFtZSA9IGJ1dHRvbk5h
bWU7CgkJdGhpcy5uZSA9IG5pY0VkaXRvcjsKCQl0aGlzLmVsbSA9IGU7CgoJCXRoaXMubWFyZ2lu
ID0gbmV3IGJrRWxlbWVudCgnRElWJykuc2V0U3R5bGUoeydmbG9hdCcgOiAnbGVmdCcsIG1hcmdp
blRvcCA6ICcycHgnfSkuYXBwZW5kVG8oZSk7CgkJdGhpcy5jb250YWluID0gbmV3IGJrRWxlbWVu
dCgnRElWJykuc2V0U3R5bGUoe3dpZHRoIDogJzIwcHgnLCBoZWlnaHQgOiAnMjBweCd9KS5hZGRD
bGFzcygnYnV0dG9uQ29udGFpbicpLmFwcGVuZFRvKHRoaXMubWFyZ2luKTsKCQl0aGlzLmJvcmRl
ciA9IG5ldyBia0VsZW1lbnQoJ0RJVicpLnNldFN0eWxlKHtiYWNrZ3JvdW5kQ29sb3IgOiAnI2Vm
ZWZlZicsIGJvcmRlciA6ICcxcHggc29saWQgI2VmZWZlZid9KS5hcHBlbmRUbyh0aGlzLmNvbnRh
aW4pOwoJCXRoaXMuYnV0dG9uID0gbmV3IGJrRWxlbWVudCgnRElWJykuc2V0U3R5bGUoe3dpZHRo
IDogJzE4cHgnLCBoZWlnaHQgOiAnMThweCcsIG92ZXJmbG93IDogJ2hpZGRlbicsIHpvb20gOiAx
LCBjdXJzb3IgOiAncG9pbnRlcid9KS5hZGRDbGFzcygnYnV0dG9uJykuc2V0U3R5bGUodGhpcy5u
ZS5nZXRJY29uKGJ1dHRvbk5hbWUsb3B0aW9ucykpLmFwcGVuZFRvKHRoaXMuYm9yZGVyKTsKCQl0
aGlzLmJ1dHRvbi5hZGRFdmVudCgnbW91c2VvdmVyJywgdGhpcy5ob3Zlck9uLmNsb3N1cmUodGhp
cykpLmFkZEV2ZW50KCdtb3VzZW91dCcsdGhpcy5ob3Zlck9mZi5jbG9zdXJlKHRoaXMpKS5hZGRF
dmVudCgnbW91c2Vkb3duJyx0aGlzLm1vdXNlQ2xpY2suY2xvc3VyZSh0aGlzKSkubm9TZWxlY3Qo
KTsKCgkJaWYoIXdpbmRvdy5vcGVyYSkgewoJCQl0aGlzLmJ1dHRvbi5vbm1vdXNlZG93biA9IHRo
aXMuYnV0dG9uLm9uY2xpY2sgPSBia0xpYi5jYW5jZWxFdmVudDsKCQl9CgoJCW5pY0VkaXRvci5h
ZGRFdmVudCgnc2VsZWN0ZWQnLCB0aGlzLmVuYWJsZS5jbG9zdXJlKHRoaXMpKS5hZGRFdmVudCgn
Ymx1cicsIHRoaXMuZGlzYWJsZS5jbG9zdXJlKHRoaXMpKS5hZGRFdmVudCgna2V5Jyx0aGlzLmtl
eS5jbG9zdXJlKHRoaXMpKTsKCgkJdGhpcy5kaXNhYmxlKCk7CgkJdGhpcy5pbml0KCk7Cgl9LAoK
CWluaXQgOiBmdW5jdGlvbigpIHsgIH0sCgoJaGlkZSA6IGZ1bmN0aW9uKCkgewoJCXRoaXMuY29u
dGFpbi5zZXRTdHlsZSh7ZGlzcGxheSA6ICdub25lJ30pOwoJfSwKCgl1cGRhdGVTdGF0ZSA6IGZ1
bmN0aW9uKCkgewoJCWlmKHRoaXMuaXNEaXNhYmxlZCkgeyB0aGlzLnNldEJnKCk7IH0KCQllbHNl
IGlmKHRoaXMuaXNIb3ZlcikgeyB0aGlzLnNldEJnKCdob3ZlcicpOyB9CgkJZWxzZSBpZih0aGlz
LmlzQWN0aXZlKSB7IHRoaXMuc2V0QmcoJ2FjdGl2ZScpOyB9CgkJZWxzZSB7IHRoaXMuc2V0Qmco
KTsgfQoJfSwKCglzZXRCZyA6IGZ1bmN0aW9uKHN0YXRlKSB7CgkJc3dpdGNoKHN0YXRlKSB7CgkJ
CWNhc2UgJ2hvdmVyJzoKCQkJCXZhciBzdGF0ZVN0eWxlID0ge2JvcmRlciA6ICcxcHggc29saWQg
IzY2NicsIGJhY2tncm91bmRDb2xvciA6ICcjZGRkJ307CgkJCQlicmVhazsKCQkJY2FzZSAnYWN0
aXZlJzoKCQkJCXZhciBzdGF0ZVN0eWxlID0ge2JvcmRlciA6ICcxcHggc29saWQgIzY2NicsIGJh
Y2tncm91bmRDb2xvciA6ICcjY2NjJ307CgkJCQlicmVhazsKCQkJZGVmYXVsdDoKCQkJCXZhciBz
dGF0ZVN0eWxlID0ge2JvcmRlciA6ICcxcHggc29saWQgI2VmZWZlZicsIGJhY2tncm91bmRDb2xv
ciA6ICcjZWZlZmVmJ307CgkJfQoJCXRoaXMuYm9yZGVyLnNldFN0eWxlKHN0YXRlU3R5bGUpLmFk
ZENsYXNzKCdidXR0b24tJytzdGF0ZSk7Cgl9LAoKCWNoZWNrTm9kZXMgOiBmdW5jdGlvbihlKSB7
CgkJdmFyIGVsbSA9IGU7CgkJZG8gewoJCQlpZih0aGlzLm9wdGlvbnMudGFncyAmJiBia0xpYi5p
bkFycmF5KHRoaXMub3B0aW9ucy50YWdzLGVsbS5ub2RlTmFtZSkpIHsKCQkJCXRoaXMuYWN0aXZh
dGUoKTsKCQkJCXJldHVybiB0cnVlOwoJCQl9CgkJfSB3aGlsZSgoZWxtID0gZWxtLnBhcmVudE5v
ZGUpICYmIGVsbS5jbGFzc05hbWUgIT0gIm5pY0VkaXQiKTsKCQllbG0gPSAkQksoZSk7CgkJd2hp
bGUoZWxtLm5vZGVUeXBlID09IDMpIHsKCQkJZWxtID0gJEJLKGVsbS5wYXJlbnROb2RlKTsKCQl9
CgkJaWYodGhpcy5vcHRpb25zLmNzcykgewoJCQlmb3IoaXRtIGluIHRoaXMub3B0aW9ucy5jc3Mp
IHsKCQkJCWlmKGVsbS5nZXRTdHlsZShpdG0sdGhpcy5uZS5zZWxlY3RlZEluc3RhbmNlLmluc3Rh
bmNlRG9jKSA9PSB0aGlzLm9wdGlvbnMuY3NzW2l0bV0pIHsKCQkJCQl0aGlzLmFjdGl2YXRlKCk7
CgkJCQkJcmV0dXJuIHRydWU7CgkJCQl9CgkJCX0KCQl9CgkJdGhpcy5kZWFjdGl2YXRlKCk7CgkJ
cmV0dXJuIGZhbHNlOwoJfSwKCglhY3RpdmF0ZSA6IGZ1bmN0aW9uKCkgewoJCWlmKCF0aGlzLmlz
RGlzYWJsZWQpIHsKCQkJdGhpcy5pc0FjdGl2ZSA9IHRydWU7CgkJCXRoaXMudXBkYXRlU3RhdGUo
KTsKCQkJdGhpcy5uZS5maXJlRXZlbnQoJ2J1dHRvbkFjdGl2YXRlJyx0aGlzKTsKCQl9Cgl9LAoK
CWRlYWN0aXZhdGUgOiBmdW5jdGlvbigpIHsKCQl0aGlzLmlzQWN0aXZlID0gZmFsc2U7CgkJdGhp
cy51cGRhdGVTdGF0ZSgpOwoJCWlmKCF0aGlzLmlzRGlzYWJsZWQpIHsKCQkJdGhpcy5uZS5maXJl
RXZlbnQoJ2J1dHRvbkRlYWN0aXZhdGUnLHRoaXMpOwoJCX0KCX0sCgoJZW5hYmxlIDogZnVuY3Rp
b24oaW5zLHQpIHsKCQl0aGlzLmlzRGlzYWJsZWQgPSBmYWxzZTsKCQl0aGlzLmNvbnRhaW4uc2V0
U3R5bGUoeydvcGFjaXR5JyA6IDF9KS5hZGRDbGFzcygnYnV0dG9uRW5hYmxlZCcpOwoJCXRoaXMu
dXBkYXRlU3RhdGUoKTsKCQlpZiAodCAhPT0gZG9jdW1lbnQpIHsKCQkJdGhpcy5jaGVja05vZGVz
KHQpOwoJCX0KCX0sCgoJZGlzYWJsZSA6IGZ1bmN0aW9uKGlucyx0KSB7CgkJdGhpcy5pc0Rpc2Fi
bGVkID0gdHJ1ZTsKCQl0aGlzLmNvbnRhaW4uc2V0U3R5bGUoeydvcGFjaXR5JyA6IDAuNn0pLnJl
bW92ZUNsYXNzKCdidXR0b25FbmFibGVkJyk7CgkJdGhpcy51cGRhdGVTdGF0ZSgpOwoJfSwKCgl0
b2dnbGVBY3RpdmUgOiBmdW5jdGlvbigpIHsKCQkodGhpcy5pc0FjdGl2ZSkgPyB0aGlzLmRlYWN0
aXZhdGUoKSA6IHRoaXMuYWN0aXZhdGUoKTsKCX0sCgoJaG92ZXJPbiA6IGZ1bmN0aW9uKCkgewoJ
CWlmKCF0aGlzLmlzRGlzYWJsZWQpIHsKCQkJdGhpcy5pc0hvdmVyID0gdHJ1ZTsKCQkJdGhpcy51
cGRhdGVTdGF0ZSgpOwoJCQl0aGlzLm5lLmZpcmVFdmVudCgiYnV0dG9uT3ZlciIsdGhpcyk7CgkJ
fQoJfSwKCglob3Zlck9mZiA6IGZ1bmN0aW9uKCkgewoJCXRoaXMuaXNIb3ZlciA9IGZhbHNlOwoJ
CXRoaXMudXBkYXRlU3RhdGUoKTsKCQl0aGlzLm5lLmZpcmVFdmVudCgiYnV0dG9uT3V0Iix0aGlz
KTsKCX0sCgoJbW91c2VDbGljayA6IGZ1bmN0aW9uKCkgewoJCWlmKHRoaXMub3B0aW9ucy5jb21t
YW5kKSB7CgkJCXRoaXMubmUubmljQ29tbWFuZCh0aGlzLm9wdGlvbnMuY29tbWFuZCx0aGlzLm9w
dGlvbnMuY29tbWFuZEFyZ3MpOwoJCQlpZighdGhpcy5vcHRpb25zLm5vQWN0aXZlKSB7CgkJCQl0
aGlzLnRvZ2dsZUFjdGl2ZSgpOwoJCQl9CgkJfQoJCXRoaXMubmUuZmlyZUV2ZW50KCJidXR0b25D
bGljayIsdGhpcyk7Cgl9LAoKCWtleSA6IGZ1bmN0aW9uKG5pY0luc3RhbmNlLGUpIHsKCQlpZih0
aGlzLm9wdGlvbnMua2V5ICYmIGUuY3RybEtleSAmJiBTdHJpbmcuZnJvbUNoYXJDb2RlKGUua2V5
Q29kZSB8fCBlLmNoYXJDb2RlKS50b0xvd2VyQ2FzZSgpID09IHRoaXMub3B0aW9ucy5rZXkpIHsK
CQkJdGhpcy5tb3VzZUNsaWNrKCk7CgkJCWlmKGUucHJldmVudERlZmF1bHQpIGUucHJldmVudERl
ZmF1bHQoKTsKCQl9Cgl9Cgp9KTsKCgp2YXIgbmljUGx1Z2luID0gYmtDbGFzcy5leHRlbmQoewoK
CWNvbnN0cnVjdCA6IGZ1bmN0aW9uKG5pY0VkaXRvcixvcHRpb25zKSB7CgkJdGhpcy5vcHRpb25z
ID0gb3B0aW9uczsKCQl0aGlzLm5lID0gbmljRWRpdG9yOwoJCXRoaXMubmUuYWRkRXZlbnQoJ3Bh
bmVsJyx0aGlzLmxvYWRQYW5lbC5jbG9zdXJlKHRoaXMpKTsKCgkJdGhpcy5pbml0KCk7Cgl9LAoK
CWxvYWRQYW5lbCA6IGZ1bmN0aW9uKG5wKSB7CgkJdmFyIGJ1dHRvbnMgPSB0aGlzLm9wdGlvbnMu
YnV0dG9uczsKCQlmb3IodmFyIGJ1dHRvbiBpbiBidXR0b25zKSB7CgkJCW5wLmFkZEJ1dHRvbihi
dXR0b24sdGhpcy5vcHRpb25zKTsKCQl9CgkJbnAucmVvcmRlcigpOwoJfSwKCglpbml0IDogZnVu
Y3Rpb24oKSB7ICB9Cn0pOwoKCgoKIC8qIFNUQVJUIENPTkZJRyAqLwp2YXIgbmljUGFuZU9wdGlv
bnMgPSB7IH07Ci8qIEVORCBDT05GSUcgKi8KCnZhciBuaWNFZGl0b3JQYW5lID0gYmtDbGFzcy5l
eHRlbmQoewoJY29uc3RydWN0IDogZnVuY3Rpb24oZWxtLG5pY0VkaXRvcixvcHRpb25zLG9wZW5C
dXR0b24pIHsKCQl0aGlzLm5lID0gbmljRWRpdG9yOwoJCXRoaXMuZWxtID0gZWxtOwoJCXRoaXMu
cG9zID0gZWxtLnBvcygpOwoKCQl0aGlzLmNvbnRhaW4gPSBuZXcgYmtFbGVtZW50KCdkaXYnKS5z
ZXRTdHlsZSh7ekluZGV4IDogJzk5OTk5Jywgb3ZlcmZsb3cgOiAnaGlkZGVuJywgcG9zaXRpb24g
OiAnYWJzb2x1dGUnLCBsZWZ0IDogdGhpcy5wb3NbMF0rJ3B4JywgdG9wIDogdGhpcy5wb3NbMV0r
J3B4J30pCgkJdGhpcy5wYW5lID0gbmV3IGJrRWxlbWVudCgnZGl2Jykuc2V0U3R5bGUoe2ZvbnRT
aXplIDogJzEycHgnLCBib3JkZXIgOiAnMXB4IHNvbGlkICNjY2MnLCAnb3ZlcmZsb3cnOiAnaGlk
ZGVuJywgcGFkZGluZyA6ICc0cHgnLCB0ZXh0QWxpZ246ICdsZWZ0JywgYmFja2dyb3VuZENvbG9y
IDogJyNmZmZmYzknfSkuYWRkQ2xhc3MoJ3BhbmUnKS5zZXRTdHlsZShvcHRpb25zKS5hcHBlbmRU
byh0aGlzLmNvbnRhaW4pOwoKCQlpZihvcGVuQnV0dG9uICYmICFvcGVuQnV0dG9uLm9wdGlvbnMu
bm9DbG9zZSkgewoJCQl0aGlzLmNsb3NlID0gbmV3IGJrRWxlbWVudCgnZGl2Jykuc2V0U3R5bGUo
eydmbG9hdCcgOiAncmlnaHQnLCBoZWlnaHQ6ICcxNnB4Jywgd2lkdGggOiAnMTZweCcsIGN1cnNv
ciA6ICdwb2ludGVyJ30pLnNldFN0eWxlKHRoaXMubmUuZ2V0SWNvbignY2xvc2UnLG5pY1BhbmVP
cHRpb25zKSkuYWRkRXZlbnQoJ21vdXNlZG93bicsb3BlbkJ1dHRvbi5yZW1vdmVQYW5lLmNsb3N1
cmUodGhpcykpLmFwcGVuZFRvKHRoaXMucGFuZSk7CgkJfQoKCQl0aGlzLmNvbnRhaW4ubm9TZWxl
Y3QoKS5hcHBlbmRUbyhkb2N1bWVudC5ib2R5KTsKCgkJdGhpcy5wb3NpdGlvbigpOwoJCXRoaXMu
aW5pdCgpOwoJfSwKCglpbml0IDogZnVuY3Rpb24oKSB7IH0sCgoJcG9zaXRpb24gOiBmdW5jdGlv
bigpIHsKCQlpZih0aGlzLm5lLm5pY1BhbmVsKSB7CgkJCXZhciBwYW5lbEVsbSA9IHRoaXMubmUu
bmljUGFuZWwuZWxtOwoJCQl2YXIgcGFuZWxQb3MgPSBwYW5lbEVsbS5wb3MoKTsKCQkJdmFyIG5l
d0xlZnQgPSBwYW5lbFBvc1swXStwYXJzZUludChwYW5lbEVsbS5nZXRTdHlsZSgnd2lkdGgnKSkt
KHBhcnNlSW50KHRoaXMucGFuZS5nZXRTdHlsZSgnd2lkdGgnKSkrOCk7CgkJCWlmKG5ld0xlZnQg
PCB0aGlzLnBvc1swXSkgewoJCQkJdGhpcy5jb250YWluLnNldFN0eWxlKHtsZWZ0IDogbmV3TGVm
dCsncHgnfSk7CgkJCX0KCQl9Cgl9LAoKCXRvZ2dsZSA6IGZ1bmN0aW9uKCkgewoJCXRoaXMuaXNW
aXNpYmxlID0gIXRoaXMuaXNWaXNpYmxlOwoJCXRoaXMuY29udGFpbi5zZXRTdHlsZSh7ZGlzcGxh
eSA6ICgodGhpcy5pc1Zpc2libGUpID8gJ2Jsb2NrJyA6ICdub25lJyl9KTsKCX0sCgoJcmVtb3Zl
IDogZnVuY3Rpb24oKSB7CgkJaWYodGhpcy5jb250YWluKSB7CgkJCXRoaXMuY29udGFpbi5yZW1v
dmUoKTsKCQkJdGhpcy5jb250YWluID0gbnVsbDsKCQl9Cgl9LAoKCWFwcGVuZCA6IGZ1bmN0aW9u
KGMpIHsKCQljLmFwcGVuZFRvKHRoaXMucGFuZSk7Cgl9LAoKCXNldENvbnRlbnQgOiBmdW5jdGlv
bihjKSB7CgkJdGhpcy5wYW5lLnNldENvbnRlbnQoYyk7Cgl9Cgp9KTsKCgoKdmFyIG5pY0VkaXRv
ckFkdmFuY2VkQnV0dG9uID0gbmljRWRpdG9yQnV0dG9uLmV4dGVuZCh7CgoJaW5pdCA6IGZ1bmN0
aW9uKCkgewoJCXRoaXMubmUuYWRkRXZlbnQoJ3NlbGVjdGVkJyx0aGlzLnJlbW92ZVBhbmUuY2xv
c3VyZSh0aGlzKSkuYWRkRXZlbnQoJ2JsdXInLHRoaXMucmVtb3ZlUGFuZS5jbG9zdXJlKHRoaXMp
KTsKCX0sCgoJbW91c2VDbGljayA6IGZ1bmN0aW9uKCkgewoJCWlmKCF0aGlzLmlzRGlzYWJsZWQp
IHsKCQkJaWYodGhpcy5wYW5lICYmIHRoaXMucGFuZS5wYW5lKSB7CgkJCQl0aGlzLnJlbW92ZVBh
bmUoKTsKCQkJfSBlbHNlIHsKCQkJCXRoaXMucGFuZSA9IG5ldyBuaWNFZGl0b3JQYW5lKHRoaXMu
Y29udGFpbix0aGlzLm5lLHt3aWR0aCA6ICh0aGlzLndpZHRoIHx8ICcyNzBweCcpLCBiYWNrZ3Jv
dW5kQ29sb3IgOiAnI2ZmZid9LHRoaXMpOwoJCQkJdGhpcy5hZGRQYW5lKCk7CgkJCQl0aGlzLm5l
LnNlbGVjdGVkSW5zdGFuY2Uuc2F2ZVJuZygpOwoJCQl9CgkJfQoJfSwKCglhZGRGb3JtIDogZnVu
Y3Rpb24oZixlbG0pIHsKCQl0aGlzLmZvcm0gPSBuZXcgYmtFbGVtZW50KCdmb3JtJykuYWRkRXZl
bnQoJ3N1Ym1pdCcsdGhpcy5zdWJtaXQuY2xvc3VyZUxpc3RlbmVyKHRoaXMpKTsKCQl0aGlzLnBh
bmUuYXBwZW5kKHRoaXMuZm9ybSk7CgkJdGhpcy5pbnB1dHMgPSB7fTsKCgkJZm9yKGl0bSBpbiBm
KSB7CgkJCXZhciBmaWVsZCA9IGZbaXRtXTsKCQkJdmFyIHZhbCA9ICcnOwoJCQlpZihlbG0pIHsK
CQkJCXZhbCA9IGVsbS5nZXRBdHRyaWJ1dGUoaXRtKTsKCQkJfQoJCQlpZighdmFsKSB7CgkJCQl2
YWwgPSBmaWVsZFsndmFsdWUnXSB8fCAnJzsKCQkJfQoJCQl2YXIgdHlwZSA9IGZbaXRtXS50eXBl
OwoKCQkJaWYodHlwZSA9PSAndGl0bGUnKSB7CgkJCQkJbmV3IGJrRWxlbWVudCgnZGl2Jykuc2V0
Q29udGVudChmaWVsZC50eHQpLnNldFN0eWxlKHtmb250U2l6ZSA6ICcxNHB4JywgZm9udFdlaWdo
dDogJ2JvbGQnLCBwYWRkaW5nIDogJzBweCcsIG1hcmdpbiA6ICcycHggMCd9KS5hcHBlbmRUbyh0
aGlzLmZvcm0pOwoJCQl9IGVsc2UgewoJCQkJdmFyIGNvbnRhaW4gPSBuZXcgYmtFbGVtZW50KCdk
aXYnKS5zZXRTdHlsZSh7b3ZlcmZsb3cgOiAnaGlkZGVuJywgY2xlYXIgOiAnYm90aCd9KS5hcHBl
bmRUbyh0aGlzLmZvcm0pOwoJCQkJaWYoZmllbGQudHh0KSB7CgkJCQkJbmV3IGJrRWxlbWVudCgn
bGFiZWwnKS5zZXRBdHRyaWJ1dGVzKHsnZm9yJyA6IGl0bX0pLnNldENvbnRlbnQoZmllbGQudHh0
KS5zZXRTdHlsZSh7bWFyZ2luIDogJzJweCA0cHgnLCBmb250U2l6ZSA6ICcxM3B4Jywgd2lkdGg6
ICc1MHB4JywgbGluZUhlaWdodCA6ICcyMHB4JywgdGV4dEFsaWduIDogJ3JpZ2h0JywgJ2Zsb2F0
JyA6ICdsZWZ0J30pLmFwcGVuZFRvKGNvbnRhaW4pOwoJCQkJfQoKCQkJCXN3aXRjaCh0eXBlKSB7
CgkJCQkJY2FzZSAndGV4dCc6CgkJCQkJCXRoaXMuaW5wdXRzW2l0bV0gPSBuZXcgYmtFbGVtZW50
KCdpbnB1dCcpLnNldEF0dHJpYnV0ZXMoe2lkIDogaXRtLCAndmFsdWUnIDogdmFsLCAndHlwZScg
OiAndGV4dCd9KS5zZXRTdHlsZSh7bWFyZ2luIDogJzJweCAwJywgZm9udFNpemUgOiAnMTNweCcs
ICdmbG9hdCcgOiAnbGVmdCcsIGhlaWdodCA6ICcyMHB4JywgYm9yZGVyIDogJzFweCBzb2xpZCAj
Y2NjJywgb3ZlcmZsb3cgOiAnaGlkZGVuJ30pLnNldFN0eWxlKGZpZWxkLnN0eWxlKS5hcHBlbmRU
byhjb250YWluKTsKCQkJCQkJYnJlYWs7CgkJCQkJY2FzZSAnc2VsZWN0JzoKCQkJCQkJdGhpcy5p
bnB1dHNbaXRtXSA9IG5ldyBia0VsZW1lbnQoJ3NlbGVjdCcpLnNldEF0dHJpYnV0ZXMoe2lkIDog
aXRtfSkuc2V0U3R5bGUoe2JvcmRlciA6ICcxcHggc29saWQgI2NjYycsICdmbG9hdCcgOiAnbGVm
dCcsIG1hcmdpbiA6ICcycHggMCd9KS5hcHBlbmRUbyhjb250YWluKTsKCQkJCQkJZm9yKG9wdCBp
biBmaWVsZC5vcHRpb25zKSB7CgkJCQkJCQl2YXIgbyA9IG5ldyBia0VsZW1lbnQoJ29wdGlvbicp
LnNldEF0dHJpYnV0ZXMoe3ZhbHVlIDogb3B0LCBzZWxlY3RlZCA6IChvcHQgPT0gdmFsKSA/ICdz
ZWxlY3RlZCcgOiAnJ30pLnNldENvbnRlbnQoZmllbGQub3B0aW9uc1tvcHRdKS5hcHBlbmRUbyh0
aGlzLmlucHV0c1tpdG1dKTsKCQkJCQkJfQoJCQkJCQlicmVhazsKCQkJCQljYXNlICdjb250ZW50
JzoKCQkJCQkJdGhpcy5pbnB1dHNbaXRtXSA9IG5ldyBia0VsZW1lbnQoJ3RleHRhcmVhJykuc2V0
QXR0cmlidXRlcyh7aWQgOiBpdG19KS5zZXRTdHlsZSh7Ym9yZGVyIDogJzFweCBzb2xpZCAjY2Nj
JywgJ2Zsb2F0JyA6ICdsZWZ0J30pLnNldFN0eWxlKGZpZWxkLnN0eWxlKS5hcHBlbmRUbyhjb250
YWluKTsKCQkJCQkJdGhpcy5pbnB1dHNbaXRtXS52YWx1ZSA9IHZhbDsKCQkJCX0KCQkJfQoJCX0K
CQluZXcgYmtFbGVtZW50KCdpbnB1dCcpLnNldEF0dHJpYnV0ZXMoeyd0eXBlJyA6ICdzdWJtaXQn
fSkuc2V0U3R5bGUoe2JhY2tncm91bmRDb2xvciA6ICcjZWZlZmVmJyxib3JkZXIgOiAnMXB4IHNv
bGlkICNjY2MnLCBtYXJnaW4gOiAnM3B4IDAnLCAnZmxvYXQnIDogJ2xlZnQnLCAnY2xlYXInIDog
J2JvdGgnfSkuYXBwZW5kVG8odGhpcy5mb3JtKTsKCQl0aGlzLmZvcm0ub25zdWJtaXQgPSBia0xp
Yi5jYW5jZWxFdmVudDsKCX0sCgoJc3VibWl0IDogZnVuY3Rpb24oKSB7IH0sCgoJZmluZEVsbSA6
IGZ1bmN0aW9uKHRhZyxhdHRyLHZhbCkgewoJCXZhciBsaXN0ID0gdGhpcy5uZS5zZWxlY3RlZElu
c3RhbmNlLmdldEVsbSgpLmdldEVsZW1lbnRzQnlUYWdOYW1lKHRhZyk7CgkJZm9yKHZhciBpPTA7
aTxsaXN0Lmxlbmd0aDtpKyspIHsKCQkJaWYobGlzdFtpXS5nZXRBdHRyaWJ1dGUoYXR0cikgPT0g
dmFsKSB7CgkJCQlyZXR1cm4gJEJLKGxpc3RbaV0pOwoJCQl9CgkJfQoJfSwKCglyZW1vdmVQYW5l
IDogZnVuY3Rpb24oKSB7CgkJaWYodGhpcy5wYW5lKSB7CgkJCXRoaXMucGFuZS5yZW1vdmUoKTsK
CQkJdGhpcy5wYW5lID0gbnVsbDsKCQkJdGhpcy5uZS5zZWxlY3RlZEluc3RhbmNlLnJlc3RvcmVS
bmcoKTsKCQl9Cgl9Cn0pOwoKCnZhciBuaWNCdXR0b25UaXBzID0gYmtDbGFzcy5leHRlbmQoewoJ
Y29uc3RydWN0IDogZnVuY3Rpb24obmljRWRpdG9yKSB7CgkJdGhpcy5uZSA9IG5pY0VkaXRvcjsK
CQluaWNFZGl0b3IuYWRkRXZlbnQoJ2J1dHRvbk92ZXInLHRoaXMuc2hvdy5jbG9zdXJlKHRoaXMp
KS5hZGRFdmVudCgnYnV0dG9uT3V0Jyx0aGlzLmhpZGUuY2xvc3VyZSh0aGlzKSk7CgoJfSwKCglz
aG93IDogZnVuY3Rpb24oYnV0dG9uKSB7CgkJdGhpcy50aW1lciA9IHNldFRpbWVvdXQodGhpcy5j
cmVhdGUuY2xvc3VyZSh0aGlzLGJ1dHRvbiksNDAwKTsKCX0sCgoJY3JlYXRlIDogZnVuY3Rpb24o
YnV0dG9uKSB7CgkJdGhpcy50aW1lciA9IG51bGw7CgkJaWYoIXRoaXMucGFuZSkgewoJCQl0aGlz
LnBhbmUgPSBuZXcgbmljRWRpdG9yUGFuZShidXR0b24uYnV0dG9uLHRoaXMubmUse2ZvbnRTaXpl
IDogJzEycHgnLCBtYXJnaW5Ub3AgOiAnNXB4J30pOwoJCQl0aGlzLnBhbmUuc2V0Q29udGVudChi
dXR0b24ub3B0aW9ucy5uYW1lKTsKCQl9Cgl9LAoKCWhpZGUgOiBmdW5jdGlvbihidXR0b24pIHsK
CQlpZih0aGlzLnRpbWVyKSB7CgkJCWNsZWFyVGltZW91dCh0aGlzLnRpbWVyKTsKCQl9CgkJaWYo
dGhpcy5wYW5lKSB7CgkJCXRoaXMucGFuZSA9IHRoaXMucGFuZS5yZW1vdmUoKTsKCQl9Cgl9Cn0p
OwpuaWNFZGl0b3JzLnJlZ2lzdGVyUGx1Z2luKG5pY0J1dHRvblRpcHMpOwoKCgogLyogU1RBUlQg
Q09ORklHICovCnZhciBuaWNTZWxlY3RPcHRpb25zID0gewoJYnV0dG9ucyA6IHsKCQknZm9udFNp
emUnIDoge25hbWUgOiBfXygnU2VsZWN0IEZvbnQgU2l6ZScpLCB0eXBlIDogJ25pY0VkaXRvckZv
bnRTaXplU2VsZWN0JywgY29tbWFuZCA6ICdmb250c2l6ZSd9LAoJCSdmb250RmFtaWx5JyA6IHtu
YW1lIDogX18oJ1NlbGVjdCBGb250IEZhbWlseScpLCB0eXBlIDogJ25pY0VkaXRvckZvbnRGYW1p
bHlTZWxlY3QnLCBjb21tYW5kIDogJ2ZvbnRuYW1lJ30sCgkJJ2ZvbnRGb3JtYXQnIDoge25hbWUg
OiBfXygnU2VsZWN0IEZvbnQgRm9ybWF0JyksIHR5cGUgOiAnbmljRWRpdG9yRm9udEZvcm1hdFNl
bGVjdCcsIGNvbW1hbmQgOiAnZm9ybWF0QmxvY2snfQoJfQp9OwovKiBFTkQgQ09ORklHICovCnZh
ciBuaWNFZGl0b3JTZWxlY3QgPSBia0NsYXNzLmV4dGVuZCh7CgoJY29uc3RydWN0IDogZnVuY3Rp
b24oZSxidXR0b25OYW1lLG9wdGlvbnMsbmljRWRpdG9yKSB7CgkJdGhpcy5vcHRpb25zID0gb3B0
aW9ucy5idXR0b25zW2J1dHRvbk5hbWVdOwoJCXRoaXMuZWxtID0gZTsKCQl0aGlzLm5lID0gbmlj
RWRpdG9yOwoJCXRoaXMubmFtZSA9IGJ1dHRvbk5hbWU7CgkJdGhpcy5zZWxPcHRpb25zID0gbmV3
IEFycmF5KCk7CgoJCXRoaXMubWFyZ2luID0gbmV3IGJrRWxlbWVudCgnZGl2Jykuc2V0U3R5bGUo
eydmbG9hdCcgOiAnbGVmdCcsIG1hcmdpbiA6ICcycHggMXB4IDAgMXB4J30pLmFwcGVuZFRvKHRo
aXMuZWxtKTsKCQl0aGlzLmNvbnRhaW4gPSBuZXcgYmtFbGVtZW50KCdkaXYnKS5zZXRTdHlsZSh7
d2lkdGg6ICc5MHB4JywgaGVpZ2h0IDogJzIwcHgnLCBjdXJzb3IgOiAncG9pbnRlcicsIG92ZXJm
bG93OiAnaGlkZGVuJ30pLmFkZENsYXNzKCdzZWxlY3RDb250YWluJykuYWRkRXZlbnQoJ2NsaWNr
Jyx0aGlzLnRvZ2dsZS5jbG9zdXJlKHRoaXMpKS5hcHBlbmRUbyh0aGlzLm1hcmdpbik7CgkJdGhp
cy5pdGVtcyA9IG5ldyBia0VsZW1lbnQoJ2RpdicpLnNldFN0eWxlKHtvdmVyZmxvdyA6ICdoaWRk
ZW4nLCB6b29tIDogMSwgYm9yZGVyOiAnMXB4IHNvbGlkICNjY2MnLCBwYWRkaW5nTGVmdCA6ICcz
cHgnLCBiYWNrZ3JvdW5kQ29sb3IgOiAnI2ZmZid9KS5hcHBlbmRUbyh0aGlzLmNvbnRhaW4pOwoJ
CXRoaXMuY29udHJvbCA9IG5ldyBia0VsZW1lbnQoJ2RpdicpLnNldFN0eWxlKHtvdmVyZmxvdyA6
ICdoaWRkZW4nLCAnZmxvYXQnIDogJ3JpZ2h0JywgaGVpZ2h0OiAnMThweCcsIHdpZHRoIDogJzE2
cHgnfSkuYWRkQ2xhc3MoJ3NlbGVjdENvbnRyb2wnKS5zZXRTdHlsZSh0aGlzLm5lLmdldEljb24o
J2Fycm93JyxvcHRpb25zKSkuYXBwZW5kVG8odGhpcy5pdGVtcyk7CgkJdGhpcy50eHQgPSBuZXcg
YmtFbGVtZW50KCdkaXYnKS5zZXRTdHlsZSh7b3ZlcmZsb3cgOiAnaGlkZGVuJywgJ2Zsb2F0JyA6
ICdsZWZ0Jywgd2lkdGggOiAnNjZweCcsIGhlaWdodCA6ICcxNHB4JywgbWFyZ2luVG9wIDogJzFw
eCcsIGZvbnRGYW1pbHkgOiAnc2Fucy1zZXJpZicsIHRleHRBbGlnbiA6ICdjZW50ZXInLCBmb250
U2l6ZSA6ICcxMnB4J30pLmFkZENsYXNzKCdzZWxlY3RUeHQnKS5hcHBlbmRUbyh0aGlzLml0ZW1z
KTsKCgkJaWYoIXdpbmRvdy5vcGVyYSkgewoJCQl0aGlzLmNvbnRhaW4ub25tb3VzZWRvd24gPSB0
aGlzLmNvbnRyb2wub25tb3VzZWRvd24gPSB0aGlzLnR4dC5vbm1vdXNlZG93biA9IGJrTGliLmNh
bmNlbEV2ZW50OwoJCX0KCgkJdGhpcy5tYXJnaW4ubm9TZWxlY3QoKTsKCgkJdGhpcy5uZS5hZGRF
dmVudCgnc2VsZWN0ZWQnLCB0aGlzLmVuYWJsZS5jbG9zdXJlKHRoaXMpKS5hZGRFdmVudCgnYmx1
cicsIHRoaXMuZGlzYWJsZS5jbG9zdXJlKHRoaXMpKTsKCgkJdGhpcy5kaXNhYmxlKCk7CgkJdGhp
cy5pbml0KCk7Cgl9LAoKCWRpc2FibGUgOiBmdW5jdGlvbigpIHsKCQl0aGlzLmlzRGlzYWJsZWQg
PSB0cnVlOwoJCXRoaXMuY2xvc2UoKTsKCQl0aGlzLmNvbnRhaW4uc2V0U3R5bGUoe29wYWNpdHkg
OiAwLjZ9KTsKCX0sCgoJZW5hYmxlIDogZnVuY3Rpb24odCkgewoJCXRoaXMuaXNEaXNhYmxlZCA9
IGZhbHNlOwoJCXRoaXMuY2xvc2UoKTsKCQl0aGlzLmNvbnRhaW4uc2V0U3R5bGUoe29wYWNpdHkg
OiAxfSk7Cgl9LAoKCXNldERpc3BsYXkgOiBmdW5jdGlvbih0eHQpIHsKCQl0aGlzLnR4dC5zZXRD
b250ZW50KHR4dCk7Cgl9LAoKCXRvZ2dsZSA6IGZ1bmN0aW9uKCkgewoJCWlmKCF0aGlzLmlzRGlz
YWJsZWQpIHsKCQkJKHRoaXMucGFuZSkgPyB0aGlzLmNsb3NlKCkgOiB0aGlzLm9wZW4oKTsKCQl9
Cgl9LAoKCW9wZW4gOiBmdW5jdGlvbigpIHsKCQl0aGlzLnBhbmUgPSBuZXcgbmljRWRpdG9yUGFu
ZSh0aGlzLml0ZW1zLHRoaXMubmUse3dpZHRoIDogJzg4cHgnLCBwYWRkaW5nOiAnMHB4JywgYm9y
ZGVyVG9wIDogMCwgYm9yZGVyTGVmdCA6ICcxcHggc29saWQgI2NjYycsIGJvcmRlclJpZ2h0IDog
JzFweCBzb2xpZCAjY2NjJywgYm9yZGVyQm90dG9tIDogJzBweCcsIGJhY2tncm91bmRDb2xvciA6
ICcjZmZmJ30pOwoKCQlmb3IodmFyIGk9MDtpPHRoaXMuc2VsT3B0aW9ucy5sZW5ndGg7aSsrKSB7
CgkJCXZhciBvcHQgPSB0aGlzLnNlbE9wdGlvbnNbaV07CgkJCXZhciBpdG1Db250YWluID0gbmV3
IGJrRWxlbWVudCgnZGl2Jykuc2V0U3R5bGUoe292ZXJmbG93IDogJ2hpZGRlbicsIGJvcmRlckJv
dHRvbSA6ICcxcHggc29saWQgI2NjYycsIHdpZHRoOiAnODhweCcsIHRleHRBbGlnbiA6ICdsZWZ0
Jywgb3ZlcmZsb3cgOiAnaGlkZGVuJywgY3Vyc29yIDogJ3BvaW50ZXInfSk7CgkJCXZhciBpdG0g
PSBuZXcgYmtFbGVtZW50KCdkaXYnKS5zZXRTdHlsZSh7cGFkZGluZyA6ICcwcHggNHB4J30pLnNl
dENvbnRlbnQob3B0WzFdKS5hcHBlbmRUbyhpdG1Db250YWluKS5ub1NlbGVjdCgpOwoJCQlpdG0u
YWRkRXZlbnQoJ2NsaWNrJyx0aGlzLnVwZGF0ZS5jbG9zdXJlKHRoaXMsb3B0WzBdKSkuYWRkRXZl
bnQoJ21vdXNlb3ZlcicsdGhpcy5vdmVyLmNsb3N1cmUodGhpcyxpdG0pKS5hZGRFdmVudCgnbW91
c2VvdXQnLHRoaXMub3V0LmNsb3N1cmUodGhpcyxpdG0pKS5zZXRBdHRyaWJ1dGVzKCdpZCcsb3B0
WzBdKTsKCQkJdGhpcy5wYW5lLmFwcGVuZChpdG1Db250YWluKTsKCQkJaWYoIXdpbmRvdy5vcGVy
YSkgewoJCQkJaXRtLm9ubW91c2Vkb3duID0gYmtMaWIuY2FuY2VsRXZlbnQ7CgkJCX0KCQl9Cgl9
LAoKCWNsb3NlIDogZnVuY3Rpb24oKSB7CgkJaWYodGhpcy5wYW5lKSB7CgkJCXRoaXMucGFuZSA9
IHRoaXMucGFuZS5yZW1vdmUoKTsKCQl9Cgl9LAoKCW92ZXIgOiBmdW5jdGlvbihvcHQpIHsKCQlv
cHQuc2V0U3R5bGUoe2JhY2tncm91bmRDb2xvciA6ICcjY2NjJ30pOwoJfSwKCglvdXQgOiBmdW5j
dGlvbihvcHQpIHsKCQlvcHQuc2V0U3R5bGUoe2JhY2tncm91bmRDb2xvciA6ICcjZmZmJ30pOwoJ
fSwKCgoJYWRkIDogZnVuY3Rpb24oayx2KSB7CgkJdGhpcy5zZWxPcHRpb25zLnB1c2gobmV3IEFy
cmF5KGssdikpOwoJfSwKCgl1cGRhdGUgOiBmdW5jdGlvbihlbG0pIHsKCQl0aGlzLm5lLm5pY0Nv
bW1hbmQodGhpcy5vcHRpb25zLmNvbW1hbmQsZWxtKTsKCQl0aGlzLmNsb3NlKCk7Cgl9Cn0pOwoK
dmFyIG5pY0VkaXRvckZvbnRTaXplU2VsZWN0ID0gbmljRWRpdG9yU2VsZWN0LmV4dGVuZCh7Cglz
ZWwgOiB7MSA6ICcxJm5ic3A7KDhwdCknLCAyIDogJzImbmJzcDsoMTBwdCknLCAzIDogJzMmbmJz
cDsoMTJwdCknLCA0IDogJzQmbmJzcDsoMTRwdCknLCA1IDogJzUmbmJzcDsoMThwdCknLCA2IDog
JzYmbmJzcDsoMjRwdCknfSwKCWluaXQgOiBmdW5jdGlvbigpIHsKCQl0aGlzLnNldERpc3BsYXko
J0ZvbnQmbmJzcDtTaXplLi4uJyk7CgkJZm9yKGl0bSBpbiB0aGlzLnNlbCkgewoJCQl0aGlzLmFk
ZChpdG0sJzxmb250IHNpemU9IicraXRtKyciPicrdGhpcy5zZWxbaXRtXSsnPC9mb250PicpOwoJ
CX0KCX0KfSk7Cgp2YXIgbmljRWRpdG9yRm9udEZhbWlseVNlbGVjdCA9IG5pY0VkaXRvclNlbGVj
dC5leHRlbmQoewoJc2VsIDogeydhcmlhbCcgOiAnQXJpYWwnLCdjb21pYyBzYW5zIG1zJyA6ICdD
b21pYyBTYW5zJywnY291cmllciBuZXcnIDogJ0NvdXJpZXIgTmV3JywnZ2VvcmdpYScgOiAnR2Vv
cmdpYScsICdoZWx2ZXRpY2EnIDogJ0hlbHZldGljYScsICdpbXBhY3QnIDogJ0ltcGFjdCcsICd0
aW1lcyBuZXcgcm9tYW4nIDogJ1RpbWVzJywgJ3RyZWJ1Y2hldCBtcycgOiAnVHJlYnVjaGV0Jywg
J3ZlcmRhbmEnIDogJ1ZlcmRhbmEnfSwKCglpbml0IDogZnVuY3Rpb24oKSB7CgkJdGhpcy5zZXRE
aXNwbGF5KCdGb250Jm5ic3A7RmFtaWx5Li4uJyk7CgkJZm9yKGl0bSBpbiB0aGlzLnNlbCkgewoJ
CQl0aGlzLmFkZChpdG0sJzxmb250IGZhY2U9IicraXRtKyciPicrdGhpcy5zZWxbaXRtXSsnPC9m
b250PicpOwoJCX0KCX0KfSk7Cgp2YXIgbmljRWRpdG9yRm9udEZvcm1hdFNlbGVjdCA9IG5pY0Vk
aXRvclNlbGVjdC5leHRlbmQoewoJCXNlbCA6IHsncCcgOiAnUGFyYWdyYXBoJywgJ3ByZScgOiAn
UHJlJywgJ2g2JyA6ICdIZWFkaW5nJm5ic3A7NicsICdoNScgOiAnSGVhZGluZyZuYnNwOzUnLCAn
aDQnIDogJ0hlYWRpbmcmbmJzcDs0JywgJ2gzJyA6ICdIZWFkaW5nJm5ic3A7MycsICdoMicgOiAn
SGVhZGluZyZuYnNwOzInLCAnaDEnIDogJ0hlYWRpbmcmbmJzcDsxJ30sCgoJaW5pdCA6IGZ1bmN0
aW9uKCkgewoJCXRoaXMuc2V0RGlzcGxheSgnRm9udCZuYnNwO0Zvcm1hdC4uLicpOwoJCWZvcihp
dG0gaW4gdGhpcy5zZWwpIHsKCQkJdmFyIHRhZyA9IGl0bS50b1VwcGVyQ2FzZSgpOwoJCQl0aGlz
LmFkZCgnPCcrdGFnKyc+JywnPCcraXRtKycgc3R5bGU9InBhZGRpbmc6IDBweDsgbWFyZ2luOiAw
cHg7Ij4nK3RoaXMuc2VsW2l0bV0rJzwvJyt0YWcrJz4nKTsKCQl9Cgl9Cn0pOwoKbmljRWRpdG9y
cy5yZWdpc3RlclBsdWdpbihuaWNQbHVnaW4sbmljU2VsZWN0T3B0aW9ucyk7CgoKCi8qIFNUQVJU
IENPTkZJRyAqLwp2YXIgbmljTGlua09wdGlvbnMgPSB7CglidXR0b25zIDogewoJCSdsaW5rJyA6
IHtuYW1lIDogJ0FkZCBMaW5rJywgdHlwZSA6ICduaWNMaW5rQnV0dG9uJywgdGFncyA6IFsnQSdd
fSwKCQkndW5saW5rJyA6IHtuYW1lIDogJ1JlbW92ZSBMaW5rJywgIGNvbW1hbmQgOiAndW5saW5r
Jywgbm9BY3RpdmUgOiB0cnVlfQoJfQp9OwovKiBFTkQgQ09ORklHICovCgp2YXIgbmljTGlua0J1
dHRvbiA9IG5pY0VkaXRvckFkdmFuY2VkQnV0dG9uLmV4dGVuZCh7CglhZGRQYW5lIDogZnVuY3Rp
b24oKSB7CgkJdGhpcy5sbiA9IHRoaXMubmUuc2VsZWN0ZWRJbnN0YW5jZS5zZWxFbG0oKS5wYXJl
bnRUYWcoJ0EnKTsKCQl0aGlzLmFkZEZvcm0oewoJCQknJyA6IHt0eXBlIDogJ3RpdGxlJywgdHh0
IDogJ0FkZC9FZGl0IExpbmsnfSwKCQkJJ2hyZWYnIDoge3R5cGUgOiAndGV4dCcsIHR4dCA6ICdV
UkwnLCB2YWx1ZSA6ICdodHRwOi8vJywgc3R5bGUgOiB7d2lkdGg6ICcxNTBweCd9fSwKCQkJJ3Rp
dGxlJyA6IHt0eXBlIDogJ3RleHQnLCB0eHQgOiAnVGl0bGUnfSwKCQkJJ3RhcmdldCcgOiB7dHlw
ZSA6ICdzZWxlY3QnLCB0eHQgOiAnT3BlbiBJbicsIG9wdGlvbnMgOiB7JycgOiAnQ3VycmVudCBX
aW5kb3cnLCAnX2JsYW5rJyA6ICdOZXcgV2luZG93J30sc3R5bGUgOiB7d2lkdGggOiAnMTAwcHgn
fX0KCQl9LHRoaXMubG4pOwoJfSwKCglzdWJtaXQgOiBmdW5jdGlvbihlKSB7CgkJdmFyIHVybCA9
IHRoaXMuaW5wdXRzWydocmVmJ10udmFsdWU7CgkJaWYodXJsID09ICJodHRwOi8vIiB8fCB1cmwg
PT0gIiIpIHsKCQkJYWxlcnQoIllvdSBtdXN0IGVudGVyIGEgVVJMIHRvIENyZWF0ZSBhIExpbmsi
KTsKCQkJcmV0dXJuIGZhbHNlOwoJCX0KCQl0aGlzLnJlbW92ZVBhbmUoKTsKCgkJaWYoIXRoaXMu
bG4pIHsKCQkJdmFyIHRtcCA9ICdqYXZhc2NyaXB0Om5pY1RlbXAoKTsnOwoJCQl0aGlzLm5lLm5p
Y0NvbW1hbmQoImNyZWF0ZWxpbmsiLHRtcCk7CgkJCXRoaXMubG4gPSB0aGlzLmZpbmRFbG0oJ0En
LCdocmVmJyx0bXApOwoJCQkvLyBzZXQgdGhlIGxpbmsgdGV4dCB0byB0aGUgdGl0bGUgb3IgdGhl
IHVybCBpZiB0aGVyZSBpcyBubyB0ZXh0IHNlbGVjdGVkCgkJCWlmICh0aGlzLmxuLmlubmVySFRN
TCA9PSB0bXApIHsKCQkJCXRoaXMubG4uaW5uZXJIVE1MID0gdGhpcy5pbnB1dHNbJ3RpdGxlJ10u
dmFsdWUgfHwgdXJsOwoJCQl9OwoJCX0KCQlpZih0aGlzLmxuKSB7CgkJCXZhciBvbGRUaXRsZSA9
IHRoaXMubG4udGl0bGU7CgkJCXRoaXMubG4uc2V0QXR0cmlidXRlcyh7CgkJCQlocmVmIDogdGhp
cy5pbnB1dHNbJ2hyZWYnXS52YWx1ZSwKCQkJCXRpdGxlIDogdGhpcy5pbnB1dHNbJ3RpdGxlJ10u
dmFsdWUsCgkJCQl0YXJnZXQgOiB0aGlzLmlucHV0c1sndGFyZ2V0J10ub3B0aW9uc1t0aGlzLmlu
cHV0c1sndGFyZ2V0J10uc2VsZWN0ZWRJbmRleF0udmFsdWUKCQkJfSk7CgkJCS8vIHNldCB0aGUg
bGluayB0ZXh0IHRvIHRoZSB0aXRsZSBvciB0aGUgdXJsIGlmIHRoZSBvbGQgdGV4dCB3YXMgdGhl
IG9sZCB0aXRsZQoJCQlpZiAodGhpcy5sbi5pbm5lckhUTUwgPT0gb2xkVGl0bGUpIHsKCQkJCXRo
aXMubG4uaW5uZXJIVE1MID0gdGhpcy5pbnB1dHNbJ3RpdGxlJ10udmFsdWUgfHwgdGhpcy5pbnB1
dHNbJ2hyZWYnXS52YWx1ZTsKCQkJfTsKCQl9Cgl9Cn0pOwoKbmljRWRpdG9ycy5yZWdpc3RlclBs
dWdpbihuaWNQbHVnaW4sbmljTGlua09wdGlvbnMpOwoKCgovKiBTVEFSVCBDT05GSUcgKi8KdmFy
IG5pY0NvbG9yT3B0aW9ucyA9IHsKCWJ1dHRvbnMgOiB7CgkJJ2ZvcmVjb2xvcicgOiB7bmFtZSA6
IF9fKCdDaGFuZ2UgVGV4dCBDb2xvcicpLCB0eXBlIDogJ25pY0VkaXRvckNvbG9yQnV0dG9uJywg
bm9DbG9zZSA6IHRydWV9LAoJCSdiZ2NvbG9yJyA6IHtuYW1lIDogX18oJ0NoYW5nZSBCYWNrZ3Jv
dW5kIENvbG9yJyksIHR5cGUgOiAnbmljRWRpdG9yQmdDb2xvckJ1dHRvbicsIG5vQ2xvc2UgOiB0
cnVlfQoJfQp9OwovKiBFTkQgQ09ORklHICovCgp2YXIgbmljRWRpdG9yQ29sb3JCdXR0b24gPSBu
aWNFZGl0b3JBZHZhbmNlZEJ1dHRvbi5leHRlbmQoewoJYWRkUGFuZSA6IGZ1bmN0aW9uKCkgewoJ
CQl2YXIgY29sb3JMaXN0ID0gezAgOiAnMDAnLDEgOiAnMzMnLDIgOiAnNjYnLDMgOic5OScsNCA6
ICdDQycsNSA6ICdGRid9OwoJCQl2YXIgY29sb3JJdGVtcyA9IG5ldyBia0VsZW1lbnQoJ0RJVicp
LnNldFN0eWxlKHt3aWR0aDogJzI3MHB4J30pOwoKCQkJZm9yKHZhciByIGluIGNvbG9yTGlzdCkg
ewoJCQkJZm9yKHZhciBiIGluIGNvbG9yTGlzdCkgewoJCQkJCWZvcih2YXIgZyBpbiBjb2xvckxp
c3QpIHsKCQkJCQkJdmFyIGNvbG9yQ29kZSA9ICcjJytjb2xvckxpc3Rbcl0rY29sb3JMaXN0W2dd
K2NvbG9yTGlzdFtiXTsKCgkJCQkJCXZhciBjb2xvclNxdWFyZSA9IG5ldyBia0VsZW1lbnQoJ0RJ
VicpLnNldFN0eWxlKHsnY3Vyc29yJyA6ICdwb2ludGVyJywgJ2hlaWdodCcgOiAnMTVweCcsICdm
bG9hdCcgOiAnbGVmdCd9KS5hcHBlbmRUbyhjb2xvckl0ZW1zKTsKCQkJCQkJdmFyIGNvbG9yQm9y
ZGVyID0gbmV3IGJrRWxlbWVudCgnRElWJykuc2V0U3R5bGUoe2JvcmRlcjogJzJweCBzb2xpZCAn
K2NvbG9yQ29kZX0pLmFwcGVuZFRvKGNvbG9yU3F1YXJlKTsKCQkJCQkJdmFyIGNvbG9ySW5uZXIg
PSBuZXcgYmtFbGVtZW50KCdESVYnKS5zZXRTdHlsZSh7YmFja2dyb3VuZENvbG9yIDogY29sb3JD
b2RlLCBvdmVyZmxvdyA6ICdoaWRkZW4nLCB3aWR0aCA6ICcxMXB4JywgaGVpZ2h0IDogJzExcHgn
fSkuYWRkRXZlbnQoJ2NsaWNrJyx0aGlzLmNvbG9yU2VsZWN0LmNsb3N1cmUodGhpcyxjb2xvckNv
ZGUpKS5hZGRFdmVudCgnbW91c2VvdmVyJyx0aGlzLm9uLmNsb3N1cmUodGhpcyxjb2xvckJvcmRl
cikpLmFkZEV2ZW50KCdtb3VzZW91dCcsdGhpcy5vZmYuY2xvc3VyZSh0aGlzLGNvbG9yQm9yZGVy
LGNvbG9yQ29kZSkpLmFwcGVuZFRvKGNvbG9yQm9yZGVyKTsKCgkJCQkJCWlmKCF3aW5kb3cub3Bl
cmEpIHsKCQkJCQkJCWNvbG9yU3F1YXJlLm9ubW91c2Vkb3duID0gY29sb3JJbm5lci5vbm1vdXNl
ZG93biA9IGJrTGliLmNhbmNlbEV2ZW50OwoJCQkJCQl9CgoJCQkJCX0KCQkJCX0KCQkJfQoJCQl0
aGlzLnBhbmUuYXBwZW5kKGNvbG9ySXRlbXMubm9TZWxlY3QoKSk7Cgl9LAoKCWNvbG9yU2VsZWN0
IDogZnVuY3Rpb24oYykgewoJCXRoaXMubmUubmljQ29tbWFuZCgnZm9yZUNvbG9yJyxjKTsKCQl0
aGlzLnJlbW92ZVBhbmUoKTsKCX0sCgoJb24gOiBmdW5jdGlvbihjb2xvckJvcmRlcikgewoJCWNv
bG9yQm9yZGVyLnNldFN0eWxlKHtib3JkZXIgOiAnMnB4IHNvbGlkICMwMDAnfSk7Cgl9LAoKCW9m
ZiA6IGZ1bmN0aW9uKGNvbG9yQm9yZGVyLGNvbG9yQ29kZSkgewoJCWNvbG9yQm9yZGVyLnNldFN0
eWxlKHtib3JkZXIgOiAnMnB4IHNvbGlkICcrY29sb3JDb2RlfSk7Cgl9Cn0pOwoKdmFyIG5pY0Vk
aXRvckJnQ29sb3JCdXR0b24gPSBuaWNFZGl0b3JDb2xvckJ1dHRvbi5leHRlbmQoewoJY29sb3JT
ZWxlY3QgOiBmdW5jdGlvbihjKSB7CgkJdGhpcy5uZS5uaWNDb21tYW5kKCdoaWxpdGVDb2xvcics
Yyk7CgkJdGhpcy5yZW1vdmVQYW5lKCk7Cgl9Cn0pOwoKbmljRWRpdG9ycy5yZWdpc3RlclBsdWdp
bihuaWNQbHVnaW4sbmljQ29sb3JPcHRpb25zKTsKCgoKLyogU1RBUlQgQ09ORklHICovCnZhciBu
aWNJbWFnZU9wdGlvbnMgPSB7CglidXR0b25zIDogewoJCSdpbWFnZScgOiB7bmFtZSA6ICdBZGQg
SW1hZ2UnLCB0eXBlIDogJ25pY0ltYWdlQnV0dG9uJywgdGFncyA6IFsnSU1HJ119Cgl9Cgp9Owov
KiBFTkQgQ09ORklHICovCgp2YXIgbmljSW1hZ2VCdXR0b24gPSBuaWNFZGl0b3JBZHZhbmNlZEJ1
dHRvbi5leHRlbmQoewoJYWRkUGFuZSA6IGZ1bmN0aW9uKCkgewoJCXRoaXMuaW0gPSB0aGlzLm5l
LnNlbGVjdGVkSW5zdGFuY2Uuc2VsRWxtKCkucGFyZW50VGFnKCdJTUcnKTsKCQl0aGlzLmFkZEZv
cm0oewoJCQknJyA6IHt0eXBlIDogJ3RpdGxlJywgdHh0IDogJ0FkZC9FZGl0IEltYWdlJ30sCgkJ
CSdzcmMnIDoge3R5cGUgOiAndGV4dCcsIHR4dCA6ICdVUkwnLCAndmFsdWUnIDogJ2h0dHA6Ly8n
LCBzdHlsZSA6IHt3aWR0aDogJzE1MHB4J319LAoJCQknYWx0JyA6IHt0eXBlIDogJ3RleHQnLCB0
eHQgOiAnQWx0IFRleHQnLCBzdHlsZSA6IHt3aWR0aDogJzEwMHB4J319LAoJCQknYWxpZ24nIDog
e3R5cGUgOiAnc2VsZWN0JywgdHh0IDogJ0FsaWduJywgb3B0aW9ucyA6IHtub25lIDogJ0RlZmF1
bHQnLCdsZWZ0JyA6ICdMZWZ0JywgJ3JpZ2h0JyA6ICdSaWdodCd9fQoJCX0sdGhpcy5pbSk7Cgl9
LAoKCXN1Ym1pdCA6IGZ1bmN0aW9uKGUpIHsKCQl2YXIgc3JjID0gdGhpcy5pbnB1dHNbJ3NyYydd
LnZhbHVlOwoJCWlmKHNyYyA9PSAiIiB8fCBzcmMgPT0gImh0dHA6Ly8iKSB7CgkJCWFsZXJ0KCJZ
b3UgbXVzdCBlbnRlciBhIEltYWdlIFVSTCB0byBpbnNlcnQiKTsKCQkJcmV0dXJuIGZhbHNlOwoJ
CX0KCQl0aGlzLnJlbW92ZVBhbmUoKTsKCgkJaWYoIXRoaXMuaW0pIHsKCQkJdmFyIHRtcCA9ICdq
YXZhc2NyaXB0Om5pY0ltVGVtcCgpOyc7CgkJCXRoaXMubmUubmljQ29tbWFuZCgiaW5zZXJ0SW1h
Z2UiLHRtcCk7CgkJCXRoaXMuaW0gPSB0aGlzLmZpbmRFbG0oJ0lNRycsJ3NyYycsdG1wKTsKCQl9
CgkJaWYodGhpcy5pbSkgewoJCQl0aGlzLmltLnNldEF0dHJpYnV0ZXMoewoJCQkJc3JjIDogdGhp
cy5pbnB1dHNbJ3NyYyddLnZhbHVlLAoJCQkJYWx0IDogdGhpcy5pbnB1dHNbJ2FsdCddLnZhbHVl
LAoJCQkJYWxpZ24gOiB0aGlzLmlucHV0c1snYWxpZ24nXS52YWx1ZQoJCQl9KTsKCQl9Cgl9Cn0p
OwoKbmljRWRpdG9ycy5yZWdpc3RlclBsdWdpbihuaWNQbHVnaW4sbmljSW1hZ2VPcHRpb25zKTsK
CgoKCi8qIFNUQVJUIENPTkZJRyAqLwp2YXIgbmljU2F2ZU9wdGlvbnMgPSB7CglidXR0b25zIDog
ewoJCSdzYXZlJyA6IHtuYW1lIDogX18oJ1NhdmUgdGhpcyBjb250ZW50JyksIHR5cGUgOiAnbmlj
RWRpdG9yU2F2ZUJ1dHRvbid9Cgl9Cn07Ci8qIEVORCBDT05GSUcgKi8KCnZhciBuaWNFZGl0b3JT
YXZlQnV0dG9uID0gbmljRWRpdG9yQnV0dG9uLmV4dGVuZCh7Cglpbml0IDogZnVuY3Rpb24oKSB7
CgkJaWYoIXRoaXMubmUub3B0aW9ucy5vblNhdmUpIHsKCQkJdGhpcy5tYXJnaW4uc2V0U3R5bGUo
eydkaXNwbGF5JyA6ICdub25lJ30pOwoJCX0KCX0sCgltb3VzZUNsaWNrIDogZnVuY3Rpb24oKSB7
CgkJdmFyIG9uU2F2ZSA9IHRoaXMubmUub3B0aW9ucy5vblNhdmU7CgkJdmFyIHNlbGVjdGVkSW5z
dGFuY2UgPSB0aGlzLm5lLnNlbGVjdGVkSW5zdGFuY2U7CgkJb25TYXZlKHNlbGVjdGVkSW5zdGFu
Y2UuZ2V0Q29udGVudCgpLCBzZWxlY3RlZEluc3RhbmNlLmVsbS5pZCwgc2VsZWN0ZWRJbnN0YW5j
ZSk7Cgl9Cn0pOwoKbmljRWRpdG9ycy5yZWdpc3RlclBsdWdpbihuaWNQbHVnaW4sbmljU2F2ZU9w
dGlvbnMpOwoKCgovKiBTVEFSVCBDT05GSUcgKi8KdmFyIG5pY1VwbG9hZE9wdGlvbnMgPSB7Cgli
dXR0b25zIDogewoJCSd1cGxvYWQnIDoge25hbWUgOiAnVXBsb2FkIEltYWdlJywgdHlwZSA6ICdu
aWNVcGxvYWRCdXR0b24nfQoJfQoKfTsKLyogRU5EIENPTkZJRyAqLwoKdmFyIG5pY1VwbG9hZEJ1
dHRvbiA9IG5pY0VkaXRvckFkdmFuY2VkQnV0dG9uLmV4dGVuZCh7CgluaWNVUkkgOiAnaHR0cDov
L2ZpbGVzLm5pY2VkaXQuY29tLycsCgoJYWRkUGFuZSA6IGZ1bmN0aW9uKCkgewoJCXRoaXMuaW0g
PSB0aGlzLm5lLnNlbGVjdGVkSW5zdGFuY2Uuc2VsRWxtKCkucGFyZW50VGFnKCdJTUcnKTsKCQl0
aGlzLm15SUQgPSBNYXRoLnJvdW5kKE1hdGgucmFuZG9tKCkqTWF0aC5wb3coMTAsMTUpKTsKCQl0
aGlzLnJlcXVlc3RJbnRlcnZhbCA9IDEwMDA7CgkJdGhpcy51cmkgPSB0aGlzLm5lLm9wdGlvbnMu
dXBsb2FkVVJJIHx8IHRoaXMubmljVVJJOwoJCW5pY1VwbG9hZEJ1dHRvbi5sYXN0UGx1Z2luID0g
dGhpczsKCgkJdGhpcy5teUZyYW1lID0gbmV3IGJrRWxlbWVudCgnaWZyYW1lJykuc2V0QXR0cmli
dXRlcyh7IHdpZHRoIDogJzEwMCUnLCBoZWlnaHQgOiAnMTAwcHgnLCBmcmFtZUJvcmRlciA6IDAs
IHNjcm9sbGluZyA6ICdubycgfSkuc2V0U3R5bGUoe2JvcmRlciA6IDB9KS5hcHBlbmRUbyh0aGlz
LnBhbmUucGFuZSk7CgkJdGhpcy5wcm9ncmVzc1dyYXBwZXIgPSBuZXcgYmtFbGVtZW50KCdkaXYn
KS5zZXRTdHlsZSh7ZGlzcGxheTogJ25vbmUnLCB3aWR0aDogJzEwMCUnLCBoZWlnaHQ6ICcyMHB4
JywgYm9yZGVyIDogJzFweCBzb2xpZCAjY2NjJ30pLmFwcGVuZFRvKHRoaXMucGFuZS5wYW5lKTsK
CQl0aGlzLnByb2dyZXNzID0gbmV3IGJrRWxlbWVudCgnZGl2Jykuc2V0U3R5bGUoe3dpZHRoOiAn
MCUnLCBoZWlnaHQ6ICcyMHB4JywgYmFja2dyb3VuZENvbG9yIDogJyNjY2MnfSkuc2V0Q29udGVu
dCgnJm5ic3AnKS5hcHBlbmRUbyh0aGlzLnByb2dyZXNzV3JhcHBlcik7CgoJCXNldFRpbWVvdXQo
dGhpcy5hZGRGb3JtLmNsb3N1cmUodGhpcyksNTApOwoJfSwKCglhZGRGb3JtIDogZnVuY3Rpb24o
KSB7CgkJdmFyIG15RG9jID0gdGhpcy5teURvYyA9IHRoaXMubXlGcmFtZS5jb250ZW50V2luZG93
LmRvY3VtZW50OwoJCW15RG9jLm9wZW4oKTsKCQlteURvYy53cml0ZSgiPGh0bWw+PGJvZHk+Iik7
CgkJbXlEb2Mud3JpdGUoJzxmb3JtIG1ldGhvZD0icG9zdCIgYWN0aW9uPSInK3RoaXMudXJpKyc/
aWQ9Jyt0aGlzLm15SUQrJyIgZW5jdHlwZT0ibXVsdGlwYXJ0L2Zvcm0tZGF0YSI+Jyk7CgkJbXlE
b2Mud3JpdGUoJzxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9IkFQQ19VUExPQURfUFJPR1JFU1Mi
IHZhbHVlPSInK3RoaXMubXlJRCsnIiAvPicpOwoJCWlmKHRoaXMudXJpID09IHRoaXMubmljVVJJ
KSB7CgkJCW15RG9jLndyaXRlKCc8ZGl2IHN0eWxlPSJwb3NpdGlvbjogYWJzb2x1dGU7IG1hcmdp
bi1sZWZ0OiAxNjBweDsiPjxpbWcgc3JjPSJodHRwOi8vaW1hZ2VzaGFjay51cy9pbWcvaW1hZ2Vz
aGFjay5wbmciIHdpZHRoPSIzMCIgc3R5bGU9ImZsb2F0OiBsZWZ0OyIgLz48ZGl2IHN0eWxlPSJm
bG9hdDogbGVmdDsgbWFyZ2luLWxlZnQ6IDVweDsgZm9udC1zaXplOiAxMHB4OyI+SG9zdGVkIGJ5
PGJyIC8+PGEgaHJlZj0iaHR0cDovL3d3dy5pbWFnZXNoYWNrLnVzLyIgdGFyZ2V0PSJfYmxhbmsi
PkltYWdlU2hhY2s8L2E+PC9kaXY+PC9kaXY+Jyk7CgkJfQoJCW15RG9jLndyaXRlKCc8ZGl2IHN0
eWxlPSJmb250LXNpemU6IDE0cHg7IGZvbnQtd2VpZ2h0OiBib2xkOyBwYWRkaW5nLXRvcDogNXB4
OyI+SW5zZXJ0IGFuIEltYWdlPC9kaXY+Jyk7CgkJbXlEb2Mud3JpdGUoJzxpbnB1dCBuYW1lPSJu
aWNJbWFnZSIgdHlwZT0iZmlsZSIgc3R5bGU9Im1hcmdpbi10b3A6IDEwcHg7IiAvPicpOwoJCW15
RG9jLndyaXRlKCc8L2Zvcm0+Jyk7CgkJbXlEb2Mud3JpdGUoIjwvYm9keT48L2h0bWw+Iik7CgkJ
bXlEb2MuY2xvc2UoKTsKCgkJdGhpcy5teUJvZHkgPSBteURvYy5ib2R5OwoKCQl0aGlzLm15Rm9y
bSA9ICRCSyh0aGlzLm15Qm9keS5nZXRFbGVtZW50c0J5VGFnTmFtZSgnZm9ybScpWzBdKTsKCQl0
aGlzLm15SW5wdXQgPSAkQksodGhpcy5teUJvZHkuZ2V0RWxlbWVudHNCeVRhZ05hbWUoJ2lucHV0
JylbMV0pLmFkZEV2ZW50KCdjaGFuZ2UnLCB0aGlzLnN0YXJ0VXBsb2FkLmNsb3N1cmUodGhpcykp
OwoJCXRoaXMubXlTdGF0dXMgPSBuZXcgYmtFbGVtZW50KCdkaXYnLHRoaXMubXlEb2MpLnNldFN0
eWxlKHt0ZXh0QWxpZ24gOiAnY2VudGVyJywgZm9udFNpemUgOiAnMTRweCd9KS5hcHBlbmRUbyh0
aGlzLm15Qm9keSk7Cgl9LAoKCXN0YXJ0VXBsb2FkIDogZnVuY3Rpb24oKSB7CgkJdGhpcy5teUZv
cm0uc2V0U3R5bGUoe2Rpc3BsYXkgOiAnbm9uZSd9KTsKCQl0aGlzLm15U3RhdHVzLnNldENvbnRl
bnQoJzxpbWcgc3JjPSJodHRwOi8vZmlsZXMubmljZWRpdC5jb20vYWpheC1sb2FkZXIuZ2lmIiBz
dHlsZT0iZmxvYXQ6IHJpZ2h0OyBtYXJnaW4tcmlnaHQ6IDQwcHg7IiAvPjxzdHJvbmc+VXBsb2Fk
aW5nLi4uPC9zdHJvbmc+PGJyIC8+UGxlYXNlIHdhaXQnKTsKCQl0aGlzLm15Rm9ybS5zdWJtaXQo
KTsKCQlzZXRUaW1lb3V0KHRoaXMubWFrZVJlcXVlc3QuY2xvc3VyZSh0aGlzKSx0aGlzLnJlcXVl
c3RJbnRlcnZhbCk7Cgl9LAoKCW1ha2VSZXF1ZXN0IDogZnVuY3Rpb24oKSB7CgkJaWYodGhpcy5w
YW5lICYmIHRoaXMucGFuZS5wYW5lKSB7CgkJCW5pY1VwbG9hZEJ1dHRvbi5sYXN0UGx1Z2luID0g
dGhpczsKCQkJdmFyIHMgPSBuZXcgYmtFbGVtZW50KCdzY3JpcHQnKS5zZXRBdHRyaWJ1dGVzKHsg
dHlwZSA6ICd0ZXh0L2phdmFzY3JpcHQnLCBzcmMgOiB0aGlzLnVyaSsnP2NoZWNrPScrdGhpcy5t
eUlEKycmcmFuZD0nK01hdGgucm91bmQoTWF0aC5yYW5kb20oKSpNYXRoLnBvdygxMCwxNSkpfSku
YWRkRXZlbnQoJ2xvYWQnLCBmdW5jdGlvbigpIHsKCQkJCXMucGFyZW50Tm9kZS5yZW1vdmVDaGls
ZChzKTsKCQkJfSkuYXBwZW5kVG8oZG9jdW1lbnQuZ2V0RWxlbWVudHNCeVRhZ05hbWUoJ2hlYWQn
KVswXSk7CgkJCWlmKHRoaXMucmVxdWVzdEludGVydmFsKSB7CgkJCQlzZXRUaW1lb3V0KHRoaXMu
bWFrZVJlcXVlc3QuY2xvc3VyZSh0aGlzKSwgdGhpcy5yZXF1ZXN0SW50ZXJ2YWwpOwoJCQl9CgkJ
fQoJfSwKCglzZXRQcm9ncmVzcyA6IGZ1bmN0aW9uKHBlcmNlbnQpIHsKCQl0aGlzLnByb2dyZXNz
V3JhcHBlci5zZXRTdHlsZSh7ZGlzcGxheTogJ2Jsb2NrJ30pOwoJCXRoaXMucHJvZ3Jlc3Muc2V0
U3R5bGUoe3dpZHRoIDogcGVyY2VudCsnJSd9KTsKCX0sCgoJdXBkYXRlIDogZnVuY3Rpb24obykg
ewoJCWlmKG8gPT0gZmFsc2UpIHsKCQkJdGhpcy5wcm9ncmVzc1dyYXBwZXIuc2V0U3R5bGUoe2Rp
c3BsYXkgOiAnbm9uZSd9KTsKCQl9IGVsc2UgaWYoby51cmwpIHsKCQkJdGhpcy5zZXRQcm9ncmVz
cygxMDApOwoJCQl0aGlzLnJlcXVlc3RJbnRlcnZhbCA9IGZhbHNlOwoKCQkJaWYoIXRoaXMuaW0p
IHsKCQkJCXRoaXMubmUuc2VsZWN0ZWRJbnN0YW5jZS5yZXN0b3JlUm5nKCk7CgkJCQl2YXIgdG1w
ID0gJ2phdmFzY3JpcHQ6bmljSW1UZW1wKCk7JzsKCQkJCXRoaXMubmUubmljQ29tbWFuZCgiaW5z
ZXJ0SW1hZ2UiLHRtcCk7CgkJCQl0aGlzLmltID0gdGhpcy5maW5kRWxtKCdJTUcnLCdzcmMnLHRt
cCk7CgkJCX0KCQkJdmFyIHcgPSBwYXJzZUludCh0aGlzLm5lLnNlbGVjdGVkSW5zdGFuY2UuZWxt
LmdldFN0eWxlKCd3aWR0aCcpKTsKCQkJaWYodGhpcy5pbSkgewoJCQkJdGhpcy5pbS5zZXRBdHRy
aWJ1dGVzKHsKCQkJCQlzcmMgOiBvLnVybCwKCQkJCQl3aWR0aCA6ICh3ICYmIG8ud2lkdGgpID8g
TWF0aC5taW4odyxvLndpZHRoKSA6ICcnCgkJCQl9KTsKCQkJfQoKCQkJdGhpcy5yZW1vdmVQYW5l
KCk7CgkJfSBlbHNlIGlmKG8uZXJyb3IpIHsKCQkJdGhpcy5yZXF1ZXN0SW50ZXJ2YWwgPSBmYWxz
ZTsKCQkJdGhpcy5zZXRQcm9ncmVzcygxMDApOwoJCQlhbGVydCgiVGhlcmUgd2FzIGFuIGVycm9y
IHVwbG9hZGluZyB5b3VyIGltYWdlICgiK28uZXJyb3IrIikuIik7CgkJCXRoaXMucmVtb3ZlUGFu
ZSgpOwoJCX0gZWxzZSBpZihvLm5vcHJvZ3Jlc3MpIHsKCQkJdGhpcy5wcm9ncmVzc1dyYXBwZXIu
c2V0U3R5bGUoe2Rpc3BsYXkgOiAnbm9uZSd9KTsKCQkJaWYodGhpcy51cmkuaW5kZXhPZignaHR0
cDonKSA9PSAtMSB8fCB0aGlzLnVyaS5pbmRleE9mKHdpbmRvdy5sb2NhdGlvbi5ob3N0KSAhPSAt
MSkgewoJCQkJdGhpcy5yZXF1ZXN0SW50ZXJ2YWwgPSBmYWxzZTsKCQkJfQoJCX0gZWxzZSB7CgkJ
CXRoaXMuc2V0UHJvZ3Jlc3MoIE1hdGgucm91bmQoIChvLmN1cnJlbnQvby50b3RhbCkgKiA3NSkg
KTsKCQkJaWYoby5pbnRlcnZhbCkgewoJCQkJdGhpcy5yZXF1ZXN0SW50ZXJ2YWwgPSBvLmludGVy
dmFsOwoJCQl9CgkJfQoJfQoKfSk7CgpuaWNVcGxvYWRCdXR0b24uc3RhdHVzQ2IgPSBmdW5jdGlv
bihvKSB7CgluaWNVcGxvYWRCdXR0b24ubGFzdFBsdWdpbi51cGRhdGUobyk7Cn0KCm5pY0VkaXRv
cnMucmVnaXN0ZXJQbHVnaW4obmljUGx1Z2luLG5pY1VwbG9hZE9wdGlvbnMpOwoKCgp2YXIgbmlj
WEhUTUwgPSBia0NsYXNzLmV4dGVuZCh7CglzdHJpcEF0dHJpYnV0ZXMgOiBbJ19tb3pfZGlydHkn
LCdfbW96X3Jlc2l6aW5nJywnX2V4dGVuZGVkJ10sCglub1Nob3J0IDogWydzdHlsZScsJ3RpdGxl
Jywnc2NyaXB0JywndGV4dGFyZWEnLCdhJ10sCgljc3NSZXBsYWNlIDogeydmb250LXdlaWdodDpi
b2xkOycgOiAnc3Ryb25nJywgJ2ZvbnQtc3R5bGU6aXRhbGljOycgOiAnZW0nfSwKCXNpemVzIDog
ezEgOiAneHgtc21hbGwnLCAyIDogJ3gtc21hbGwnLCAzIDogJ3NtYWxsJywgNCA6ICdtZWRpdW0n
LCA1IDogJ2xhcmdlJywgNiA6ICd4LWxhcmdlJ30sCgoJY29uc3RydWN0IDogZnVuY3Rpb24obmlj
RWRpdG9yKSB7CgkJdGhpcy5uZSA9IG5pY0VkaXRvcjsKCQlpZih0aGlzLm5lLm9wdGlvbnMueGh0
bWwpIHsKCQkJbmljRWRpdG9yLmFkZEV2ZW50KCdnZXQnLHRoaXMuY2xlYW51cC5jbG9zdXJlKHRo
aXMpKTsKCQl9Cgl9LAoKCWNsZWFudXAgOiBmdW5jdGlvbihuaSkgewoJCXZhciBub2RlID0gbmku
Z2V0RWxtKCk7CgkJdmFyIHhodG1sID0gdGhpcy50b1hIVE1MKG5vZGUpOwoJCW5pLmNvbnRlbnQg
PSB4aHRtbDsKCX0sCgoJdG9YSFRNTCA6IGZ1bmN0aW9uKG4scixkKSB7CgkJdmFyIHR4dCA9ICcn
OwoJCXZhciBhdHRyVHh0ID0gJyc7CgkJdmFyIGNzc1R4dCA9ICcnOwoJCXZhciBuVHlwZSA9IG4u
bm9kZVR5cGU7CgkJdmFyIG5OYW1lID0gbi5ub2RlTmFtZS50b0xvd2VyQ2FzZSgpOwoJCXZhciBu
Q2hpbGQgPSBuLmhhc0NoaWxkTm9kZXMgJiYgbi5oYXNDaGlsZE5vZGVzKCk7CgkJdmFyIGV4dHJh
Tm9kZXMgPSBuZXcgQXJyYXkoKTsKCgkJc3dpdGNoKG5UeXBlKSB7CgkJCWNhc2UgMToKCQkJCXZh
ciBuQXR0cmlidXRlcyA9IG4uYXR0cmlidXRlczsKCgkJCQlzd2l0Y2gobk5hbWUpIHsKCQkJCQlj
YXNlICdiJzoKCQkJCQkJbk5hbWUgPSAnc3Ryb25nJzsKCQkJCQkJYnJlYWs7CgkJCQkJY2FzZSAn
aSc6CgkJCQkJCW5OYW1lID0gJ2VtJzsKCQkJCQkJYnJlYWs7CgkJCQkJY2FzZSAnZm9udCc6CgkJ
CQkJCW5OYW1lID0gJ3NwYW4nOwoJCQkJCQlicmVhazsKCQkJCX0KCgkJCQlpZihyKSB7CgkJCQkJ
Zm9yKHZhciBpPTA7aTxuQXR0cmlidXRlcy5sZW5ndGg7aSsrKSB7CgkJCQkJCXZhciBhdHRyID0g
bkF0dHJpYnV0ZXNbaV07CgoJCQkJCQl2YXIgYXR0cmlidXRlTmFtZSA9IGF0dHIubm9kZU5hbWUu
dG9Mb3dlckNhc2UoKTsKCQkJCQkJdmFyIGF0dHJpYnV0ZVZhbHVlID0gYXR0ci5ub2RlVmFsdWU7
CgoJCQkJCQlpZighYXR0ci5zcGVjaWZpZWQgfHwgIWF0dHJpYnV0ZVZhbHVlIHx8IGJrTGliLmlu
QXJyYXkodGhpcy5zdHJpcEF0dHJpYnV0ZXMsYXR0cmlidXRlTmFtZSkgfHwgdHlwZW9mKGF0dHJp
YnV0ZVZhbHVlKSA9PSAiZnVuY3Rpb24iKSB7CgkJCQkJCQljb250aW51ZTsKCQkJCQkJfQoKCQkJ
CQkJc3dpdGNoKGF0dHJpYnV0ZU5hbWUpIHsKCQkJCQkJCWNhc2UgJ3N0eWxlJzoKCQkJCQkJCQl2
YXIgY3NzID0gYXR0cmlidXRlVmFsdWUucmVwbGFjZSgvIC9nLCIiKTsKCQkJCQkJCQlmb3IoaXRt
IGluIHRoaXMuY3NzUmVwbGFjZSkgewoJCQkJCQkJCQlpZihjc3MuaW5kZXhPZihpdG0pICE9IC0x
KSB7CgkJCQkJCQkJCQlleHRyYU5vZGVzLnB1c2godGhpcy5jc3NSZXBsYWNlW2l0bV0pOwoJCQkJ
CQkJCQkJY3NzID0gY3NzLnJlcGxhY2UoaXRtLCcnKTsKCQkJCQkJCQkJfQoJCQkJCQkJCX0KCQkJ
CQkJCQljc3NUeHQgKz0gY3NzOwoJCQkJCQkJCWF0dHJpYnV0ZVZhbHVlID0gIiI7CgkJCQkJCQli
cmVhazsKCQkJCQkJCWNhc2UgJ2NsYXNzJzoKCQkJCQkJCQlhdHRyaWJ1dGVWYWx1ZSA9IGF0dHJp
YnV0ZVZhbHVlLnJlcGxhY2UoIkFwcGxlLXN0eWxlLXNwYW4iLCIiKTsKCQkJCQkJCWJyZWFrOwoJ
CQkJCQkJY2FzZSAnc2l6ZSc6CgkJCQkJCQkJY3NzVHh0ICs9ICJmb250LXNpemU6Iit0aGlzLnNp
emVzW2F0dHJpYnV0ZVZhbHVlXSsnOyc7CgkJCQkJCQkJYXR0cmlidXRlVmFsdWUgPSAiIjsKCQkJ
CQkJCWJyZWFrOwoJCQkJCQl9CgoJCQkJCQlpZihhdHRyaWJ1dGVWYWx1ZSkgewoJCQkJCQkJYXR0
clR4dCArPSAnICcrYXR0cmlidXRlTmFtZSsnPSInK2F0dHJpYnV0ZVZhbHVlKyciJzsKCQkJCQkJ
fQoJCQkJCX0KCgkJCQkJaWYoY3NzVHh0KSB7CgkJCQkJCWF0dHJUeHQgKz0gJyBzdHlsZT0iJytj
c3NUeHQrJyInOwoJCQkJCX0KCgkJCQkJZm9yKHZhciBpPTA7aTxleHRyYU5vZGVzLmxlbmd0aDtp
KyspIHsKCQkJCQkJdHh0ICs9ICc8JytleHRyYU5vZGVzW2ldKyc+JzsKCQkJCQl9CgoJCQkJCWlm
KGF0dHJUeHQgPT0gIiIgJiYgbk5hbWUgPT0gInNwYW4iKSB7CgkJCQkJCXIgPSBmYWxzZTsKCQkJ
CQl9CgkJCQkJaWYocikgewoJCQkJCQl0eHQgKz0gJzwnK25OYW1lOwoJCQkJCQlpZihuTmFtZSAh
PSAnYnInKSB7CgkJCQkJCQl0eHQgKz0gYXR0clR4dDsKCQkJCQkJfQoJCQkJCX0KCQkJCX0KCgoK
CQkJCWlmKCFuQ2hpbGQgJiYgIWJrTGliLmluQXJyYXkodGhpcy5ub1Nob3J0LGF0dHJpYnV0ZU5h
bWUpKSB7CgkJCQkJaWYocikgewoJCQkJCQl0eHQgKz0gJyAvPic7CgkJCQkJfQoJCQkJfSBlbHNl
IHsKCQkJCQlpZihyKSB7CgkJCQkJCXR4dCArPSAnPic7CgkJCQkJfQoKCQkJCQlmb3IodmFyIGk9
MDtpPG4uY2hpbGROb2Rlcy5sZW5ndGg7aSsrKSB7CgkJCQkJCXZhciByZXN1bHRzID0gdGhpcy50
b1hIVE1MKG4uY2hpbGROb2Rlc1tpXSx0cnVlLHRydWUpOwoJCQkJCQlpZihyZXN1bHRzKSB7CgkJ
CQkJCQl0eHQgKz0gcmVzdWx0czsKCQkJCQkJfQoJCQkJCX0KCQkJCX0KCgkJCQlpZihyICYmIG5D
aGlsZCkgewoJCQkJCXR4dCArPSAnPC8nK25OYW1lKyc+JzsKCQkJCX0KCgkJCQlmb3IodmFyIGk9
MDtpPGV4dHJhTm9kZXMubGVuZ3RoO2krKykgewoJCQkJCXR4dCArPSAnPC8nK2V4dHJhTm9kZXNb
aV0rJz4nOwoJCQkJfQoKCQkJCWJyZWFrOwoJCQljYXNlIDM6CgkJCQkvL2lmKG4ubm9kZVZhbHVl
ICE9ICdcbicpIHsKCQkJCQl0eHQgKz0gbi5ub2RlVmFsdWU7CgkJCQkvL30KCQkJCWJyZWFrOwoJ
CX0KCgkJcmV0dXJuIHR4dDsKCX0KfSk7Cm5pY0VkaXRvcnMucmVnaXN0ZXJQbHVnaW4obmljWEhU
TUwpOwoKCgp2YXIgbmljQkJDb2RlID0gYmtDbGFzcy5leHRlbmQoewoJY29uc3RydWN0IDogZnVu
Y3Rpb24obmljRWRpdG9yKSB7CgkJdGhpcy5uZSA9IG5pY0VkaXRvcjsKCQlpZih0aGlzLm5lLm9w
dGlvbnMuYmJDb2RlKSB7CgkJCW5pY0VkaXRvci5hZGRFdmVudCgnZ2V0Jyx0aGlzLmJiR2V0LmNs
b3N1cmUodGhpcykpOwoJCQluaWNFZGl0b3IuYWRkRXZlbnQoJ3NldCcsdGhpcy5iYlNldC5jbG9z
dXJlKHRoaXMpKTsKCgkJCXZhciBsb2FkZWRQbHVnaW5zID0gdGhpcy5uZS5sb2FkZWRQbHVnaW5z
OwoJCQlmb3IoaXRtIGluIGxvYWRlZFBsdWdpbnMpIHsKCQkJCWlmKGxvYWRlZFBsdWdpbnNbaXRt
XS50b1hIVE1MKSB7CgkJCQkJdGhpcy54aHRtbCA9IGxvYWRlZFBsdWdpbnNbaXRtXTsKCQkJCX0K
CQkJfQoJCX0KCX0sCgoJYmJHZXQgOiBmdW5jdGlvbihuaSkgewoJCXZhciB4aHRtbCA9IHRoaXMu
eGh0bWwudG9YSFRNTChuaS5nZXRFbG0oKSk7CgkJbmkuY29udGVudCA9IHRoaXMudG9CQkNvZGUo
eGh0bWwpOwoJfSwKCgliYlNldCA6IGZ1bmN0aW9uKG5pKSB7CgkJbmkuY29udGVudCA9IHRoaXMu
ZnJvbUJCQ29kZShuaS5jb250ZW50KTsKCX0sCgoJdG9CQkNvZGUgOiBmdW5jdGlvbih4aHRtbCkg
ewoJCWZ1bmN0aW9uIHJwKHIsbSkgewoJCQl4aHRtbCA9IHhodG1sLnJlcGxhY2UocixtKTsKCQl9
CgoJCXJwKC9cbi9naSwiIik7CgkJcnAoLzxzdHJvbmc+KC4qPyk8XC9zdHJvbmc+L2dpLCJbYl0k
MVsvYl0iKTsKCQlycCgvPGVtPiguKj8pPFwvZW0+L2dpLCJbaV0kMVsvaV0iKTsKCQlycCgvPHNw
YW4uKj9zdHlsZT0idGV4dC1kZWNvcmF0aW9uOnVuZGVybGluZTsiPiguKj8pPFwvc3Bhbj4vZ2ks
Ilt1XSQxWy91XSIpOwoJCXJwKC88dWw+KC4qPyk8XC91bD4vZ2ksIltsaXN0XSQxWy9saXN0XSIp
OwoJCXJwKC88bGk+KC4qPyk8XC9saT4vZ2ksIlsqXSQxWy8qXSIpOwoJCXJwKC88b2w+KC4qPyk8
XC9vbD4vZ2ksIltsaXN0PTFdJDFbL2xpc3RdIik7CgkJcnAoLzxpbWcuKj9zcmM9IiguKj8pIi4q
Pz4vZ2ksIltpbWddJDFbL2ltZ10iKTsKCQlycCgvPGEuKj9ocmVmPSIoLio/KSIuKj8+KC4qPyk8
XC9hPi9naSwiW3VybD0kMV0kMlsvdXJsXSIpOwoJCXJwKC88YnIuKj8+L2dpLCJcbiIpOwoJCXJw
KC88Lio/Pi4qPzxcLy4qPz4vZ2ksIiIpOwoKCQlyZXR1cm4geGh0bWw7Cgl9LAoKCWZyb21CQkNv
ZGUgOiBmdW5jdGlvbihiYkNvZGUpIHsKCQlmdW5jdGlvbiBycChyLG0pIHsKCQkJYmJDb2RlID0g
YmJDb2RlLnJlcGxhY2UocixtKTsKCQl9CgoJCXJwKC9cW2JcXSguKj8pXFtcL2JcXS9naSwiPHN0
cm9uZz4kMTwvc3Ryb25nPiIpOwoJCXJwKC9cW2lcXSguKj8pXFtcL2lcXS9naSwiPGVtPiQxPC9l
bT4iKTsKCQlycCgvXFt1XF0oLio/KVxbXC91XF0vZ2ksIjxzcGFuIHN0eWxlPVwidGV4dC1kZWNv
cmF0aW9uOnVuZGVybGluZTtcIj4kMTwvc3Bhbj4iKTsKCQlycCgvXFtsaXN0XF0oLio/KVxbXC9s
aXN0XF0vZ2ksIjx1bD4kMTwvdWw+Iik7CgkJcnAoL1xbbGlzdD0xXF0oLio/KVxbXC9saXN0XF0v
Z2ksIjxvbD4kMTwvb2w+Iik7CgkJcnAoL1xbXCpcXSguKj8pXFtcL1wqXF0vZ2ksIjxsaT4kMTwv
bGk+Iik7CgkJcnAoL1xbaW1nXF0oLio/KVxbXC9pbWdcXS9naSwiPGltZyBzcmM9XCIkMVwiIC8+
Iik7CgkJcnAoL1xbdXJsPSguKj8pXF0oLio/KVxbXC91cmxcXS9naSwiPGEgaHJlZj1cIiQxXCI+
JDI8L2E+Iik7CgkJcnAoL1xuL2dpLCI8YnIgLz4iKTsKCQkvL3JwKC9cWy4qP1xdKC4qPylcW1wv
Lio/XF0vZ2ksIiQxIik7CgoJCXJldHVybiBiYkNvZGU7Cgl9CgoKfSk7Cm5pY0VkaXRvcnMucmVn
aXN0ZXJQbHVnaW4obmljQkJDb2RlKTsKCgoKbmljRWRpdG9yID0gbmljRWRpdG9yLmV4dGVuZCh7
CiAgICAgICAgZmxvYXRpbmdQYW5lbCA6IGZ1bmN0aW9uKCkgewogICAgICAgICAgICAgICAgdGhp
cy5mbG9hdGluZyA9IG5ldyBia0VsZW1lbnQoJ0RJVicpLnNldFN0eWxlKHtwb3NpdGlvbjogJ2Fi
c29sdXRlJywgdG9wIDogJy0xMDAwcHgnfSkuYXBwZW5kVG8oZG9jdW1lbnQuYm9keSk7CiAgICAg
ICAgICAgICAgICB0aGlzLmFkZEV2ZW50KCdmb2N1cycsIHRoaXMucmVwb3NpdGlvbi5jbG9zdXJl
KHRoaXMpKS5hZGRFdmVudCgnYmx1cicsIHRoaXMuaGlkZS5jbG9zdXJlKHRoaXMpKTsKICAgICAg
ICAgICAgICAgIHRoaXMuc2V0UGFuZWwodGhpcy5mbG9hdGluZyk7CiAgICAgICAgfSwKCiAgICAg
ICAgcmVwb3NpdGlvbiA6IGZ1bmN0aW9uKCkgewogICAgICAgICAgICAgICAgdmFyIGUgPSB0aGlz
LnNlbGVjdGVkSW5zdGFuY2UuZTsKICAgICAgICAgICAgICAgIHRoaXMuZmxvYXRpbmcuc2V0U3R5
bGUoeyB3aWR0aCA6IChwYXJzZUludChlLmdldFN0eWxlKCd3aWR0aCcpKSB8fCBlLmNsaWVudFdp
ZHRoKSsncHgnIH0pOwogICAgICAgICAgICAgICAgdmFyIHRvcCA9IGUub2Zmc2V0VG9wLXRoaXMu
ZmxvYXRpbmcub2Zmc2V0SGVpZ2h0OwogICAgICAgICAgICAgICAgaWYodG9wIDwgMCkgewogICAg
ICAgICAgICAgICAgICAgICAgICB0b3AgPSBlLm9mZnNldFRvcCtlLm9mZnNldEhlaWdodDsKICAg
ICAgICAgICAgICAgIH0KCiAgICAgICAgICAgICAgICB0aGlzLmZsb2F0aW5nLnNldFN0eWxlKHsg
dG9wIDogdG9wKydweCcsIGxlZnQgOiBlLm9mZnNldExlZnQrJ3B4JywgZGlzcGxheSA6ICdibG9j
aycgfSk7CiAgICAgICAgfSwKCiAgICAgICAgaGlkZSA6IGZ1bmN0aW9uKCkgewogICAgICAgICAg
ICAgICAgdGhpcy5mbG9hdGluZy5zZXRTdHlsZSh7IHRvcCA6ICctMTAwMHB4J30pOwogICAgICAg
IH0KfSk7CgoKCi8qIFNUQVJUIENPTkZJRyAqLwp2YXIgbmljQ29kZU9wdGlvbnMgPSB7CglidXR0
b25zIDogewoJCSd4aHRtbCcgOiB7bmFtZSA6ICdFZGl0IEhUTUwnLCB0eXBlIDogJ25pY0NvZGVC
dXR0b24nfQoJfQoKfTsKLyogRU5EIENPTkZJRyAqLwoKdmFyIG5pY0NvZGVCdXR0b24gPSBuaWNF
ZGl0b3JBZHZhbmNlZEJ1dHRvbi5leHRlbmQoewoJd2lkdGggOiAnMzUwcHgnLAoKCWFkZFBhbmUg
OiBmdW5jdGlvbigpIHsKCQl0aGlzLmFkZEZvcm0oewoJCQknJyA6IHt0eXBlIDogJ3RpdGxlJywg
dHh0IDogJ0VkaXQgSFRNTCd9LAoJCQknY29kZScgOiB7dHlwZSA6ICdjb250ZW50JywgJ3ZhbHVl
JyA6IHRoaXMubmUuc2VsZWN0ZWRJbnN0YW5jZS5nZXRDb250ZW50KCksIHN0eWxlIDoge3dpZHRo
OiAnMzQwcHgnLCBoZWlnaHQgOiAnMjAwcHgnfX0KCQl9KTsKCX0sCgoJc3VibWl0IDogZnVuY3Rp
b24oZSkgewoJCXZhciBjb2RlID0gdGhpcy5pbnB1dHNbJ2NvZGUnXS52YWx1ZTsKCQl0aGlzLm5l
LnNlbGVjdGVkSW5zdGFuY2Uuc2V0Q29udGVudChjb2RlKTsKCQl0aGlzLnJlbW92ZVBhbmUoKTsK
CX0KfSk7CgpuaWNFZGl0b3JzLnJlZ2lzdGVyUGx1Z2luKG5pY1BsdWdpbixuaWNDb2RlT3B0aW9u
cyk7CgoK'''
nicedit_img = r'''\
R0lGODlh5gESAPcAAAAAABERESIiIjMzMzNmIndVIkR3IkRERFVVVWZmZnd3d90iIu4zM7tEEbtV
Iqp3M91mAO53EcxmM7t3RIhmd+5ERO5EVe5VVf9VVf9mZv9md+53d/93dzOIEUSIEVWIIlWZImaZ
M1WIRGaIVWaqRHe7RHeqVWaIZneqd7uIM7uZM/+qM//MM4iIRKqIVYi7RIiqVYi7VZm7VbuqVZmZ
d4i7ZsyZVd2ZVe6ZVcyqRMyZZt2ZZt2qZsyqd92qd8y7d+67ZpnMZt3MVe7MZu7dZv/dZu7MdxEz
uxFEuxFVuzNmqjNmuzN3u0R3uyJmzDN3zER3zJl3iP93iGaZmUSZqlWIu2aIqlWIzESI3VWI3VWZ
3WaIzGaZzHeZzGaI3WaZ3XeZ3VWq3Waq3Xeq3VWq7maq7neq7ma7/4iIiJmZmZmqiJm7iLuqmYiq
qoi7qqqqqru7u/+IiN2qiMy7iN27iMy7md27me6qiO6qme67mf+7u5nMiKrMiLvMmbvdu93MiO7M
iMzMqt3Mqu7Mqv/Mu+7du8zuu//uqoiZ3YiqzJmqzIiq3Zm73aq73Yiq7oi77pm77qq77rvM3YjM
7pnd/6rM7rvM7rvd7szMzMzM3czd3d3d3f/MzO7dzO7d3f/d3d3u3f//zO7u3f/u3czd7szd/93d
/93u7t3u/+7u7v/u7u7u/+7//////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAK4ALAAAAADmARIA
AAj+AF0JHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePCSWN4XKFJMmSiVoxFJWnR488
okDKnEmzpqtWkx5NyvkIVcZGi7Y0WUK0KNEmWyzZXCoxUyNFUKNKVZSJaUOVBIEKNWoUqVKKTqeK
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
l3RZl3bpEAEBADs='''
def ne_js():
    return b64decode(nicedit_js.encode('utf-8'))
def ne_gif():
    return b64decode(nicedit_img.encode('utf-8'))
def m_i():
    return b64decode(m_img.encode('utf-8'))